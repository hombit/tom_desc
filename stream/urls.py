from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from stream import views

app_name = 'stream'

router = DefaultRouter()
router.register(r'targets', views.TargetViewSet)
router.register(r'alerts', views.AlertViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'events', views.EventViewSet)
router.register(f'elasticcdiaobject', views.ElasticcDiaObjectViewSet)
router.register(f'elasticcdiasource', views.ElasticcDiaSourceViewSet)
router.register(f'elasticcdiatruth', views.ElasticcDiaTruthViewSet)

urlpatterns = [
    url('dumprknoptest', views.DumpRknopTest.as_view()),
    url('addelasticcdiaobject', views.MaybeAddElasticcDiaObject.as_view()),
    url('addelasticalert', views.MaybeAddElasticcAlert.as_view()),
    url('addtruth', views.MaybeAddElasticcTruth.as_view()),
    url('runsqlquery', views.RunSQLQuery.as_view()),
    url('', include((router.urls, 'stream'), namespace='stream')),
]
