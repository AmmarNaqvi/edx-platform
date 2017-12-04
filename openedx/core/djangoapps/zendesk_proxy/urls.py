"""
Map urls to the relevant view handlers
"""

from django.conf.urls import url

from openedx.core.djangoapps.zendesk_proxy.views import ZendeskPassthroughView

urlpatterns = [
    url(r'^$', ZendeskPassthroughView.as_view(), name='zendesk_proxy'),
]
