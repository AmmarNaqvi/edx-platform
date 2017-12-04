"""Tests for zendesk_proxy views."""

from django.core.urlresolvers import reverse
from openedx.core.lib.api.test_utils import ApiTestCase

class ZendeskProxyTestCase(ApiTestCase):
    """Tests for zendesk_proxy views."""

    def setUp(self):
        self.url = reverse('zendesk_proxy')
        return super(ZendeskProxyTestCase, self).setUp()

    def test_naive_empty_post(self):
        response = self.request_with_auth("post", self.url)
        self.assertHttpOK(response)
