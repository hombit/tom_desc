#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Listen to a Pitt-Google Pub/Sub stream and save alerts to the database."""
import logging

from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
# from django.db import transaction
from tom_alerts.alerts import get_service_class
from tom_targets.models import Target

# from stream.models import Alert, Topic

from tom_pittgoogle.consumer_stream_python import ConsumerStreamPython as Consumer


logger = logging.getLogger(__name__)

PITTGOOGLE_CONSUMER_CONFIGURATION = settings.PITTGOOGLE_CONSUMER_CONFIGURATION


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        """Pull and process alerts from a Pitt-Google Pub/Sub stream.

        -   Execute a "streaming pull" in a background thread.
            Asyncronously, pull alerts and process them through the callback,
            `parse_and_save`.

        -   Stop when a stoping condition is reached.

        -   Block until the processing is complete and the connection has been closed.
        """
        kwargs = {
                # "desc_group": Group.objects.get(name='DESC'),
                # "broker": get_service_class('Pitt-Google StreamPython')(),
                **PITTGOOGLE_CONSUMER_CONFIGURATION,  # stopping conditions
        }

        consumer = Consumer(PITTGOOGLE_CONSUMER_CONFIGURATION['subscription_name'])
        _ = consumer.stream_alerts(
            user_callback=self.parse_and_save,
            **kwargs
        )

    @staticmethod
    def parse_and_save(alert_dict, **kwargs):
        """Parse the alert and save to the database."""

        # target = kwargs["broker"].to_target(alert_dict)
        target, created = Target.objects.get_or_create(
            name=alert_dict['objectId'],
            type='SIDEREAL',
            ra=alert_dict['ra'],
            dec=alert_dict['dec'],
        )

        if created:
            extra_fields = [item["name"] for item in settings.EXTRA_FIELDS]
            extras = {k: v for k, v in alert_dict.items() if k in extra_fields}

            target.save(extras=extras)
            # assign_perm('tom_targets.view_target', kwargs["desc_group"], target)

        success = True
        return success