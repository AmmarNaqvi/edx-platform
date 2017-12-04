"""
Map urls to the relevant view handlers
"""

from django.conf.urls import url

from openedx.core.djangoapps.zendesk_proxy import views

urlpatterns = [
    url(r'^$', views.zendesk_passthrough, name='zendesk_proxy'),
]
