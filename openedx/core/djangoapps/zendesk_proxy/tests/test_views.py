"""Tests for zendesk_proxy views."""

from django.core.urlresolvers import reverse
from django.test.utils import override_settings

from openedx.core.lib.api.test_utils import ApiTestCase
from openedx.core.djangoapps.zendesk_proxy.views import ZENDESK_REQUESTS_PER_HOUR

class ZendeskProxyTestCase(ApiTestCase):
    """Tests for zendesk_proxy views."""

    def setUp(self):
        self.url = reverse('zendesk_proxy')
        return super(ZendeskProxyTestCase, self).setUp()

    def test_naive_empty_post(self):
        response = self.request_with_auth("post", self.url)
        self.assertHttpOK(response)

    @override_settings(
        CACHES={
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                'LOCATION': 'zendesk_proxy',
            }
        }
    )
    def test_rate_limiting(self):
        """
        Confirm rate limits work as expected. Note that drf's rate limiting makes use of the default cache to enforce
        limits; that's why this test needs a "real" default cache (as opposed to the usual-for-tests DummyCache)
        """
        for _ in range(ZENDESK_REQUESTS_PER_HOUR):
            self.request_with_auth("post", self.url)
        response = self.request_with_auth("post", self.url)
        self.assertEqual(response.status_code, 429)
