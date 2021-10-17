#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Listen to a Pitt-Google Pub/Sub stream and save alerts to the database."""
from importlib import import_module
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from stream.models import Alert, Topic

from pittgoogle import Consumer


logger = logging.getLogger(__name__)

PITTGOOGLE_CONSUMER_CONFIGURATION = settings.PITTGOOGLE_CONSUMER_CONFIGURATION
PITTGOOGLE_PARSERS = settings.PITTGOOGLE_PARSERS


def get_parser_classes(topic):
    """."""
    parser_classes = []

    try:
        parsers = PITTGOOGLE_PARSERS[topic]
    except KeyError:
        logger.log(msg=f'PITTGOOGLE_PARSERS not found for topic: {topic}.', level=logging.WARNING)
        return parser_classes

    for parser in parsers:
        mod_name, class_name = parser.rsplit('.', 1)
        try:
            mod = import_module(mod_name)
            clazz = getattr(mod, class_name)
        except (ImportError, AttributeError):
            raise ImportError(f'Unable to import parser {parser}')
        parser_classes.append(clazz)

    return parser_classes


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.consumer = Consumer(PITTGOOGLE_CONSUMER_CONFIGURATION['subscription_name'])

    def handle(self, *args, **options):
        """Pull and process alerts from a Pitt-Google Pub/Sub stream.

        -   Execute a "streaming pull" in a background thread.
            Asyncronously, pull alerts and process them through the callback,
            `parse_and_save`.

        -   Stop when a stoping condition is reached.

        -   Block until the processing is complete and the connection has been closed.
        """
        self.consumer.stream_alerts(
            callback=self.parse_and_save,
            stop_conditions=PITTGOOGLE_CONSUMER_CONFIGURATION['stop_conditions'],
        )

    def parse_and_save(alert, topic_name):
        """Parse the alert and save to the database."""
        topic, _ = Topic.objects.get_or_create(name=topic_name)
        alert = Alert.objects.create(topic=topic, raw_message=alert.data)

        for parser_class in get_parser_classes(topic.name):
            with transaction.atomic():
                # Get the parser class, instantiate it, parse the alert, and save it
                parser = parser_class(alert)
                alert.parsed = parser.parse()
                if alert.parsed is True:
                    alert.save()
                    break
