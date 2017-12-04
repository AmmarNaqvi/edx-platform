"""
Define request handlers used by the zendesk_proxy djangoapp
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

ZENDESK_REQUESTS_PER_HOUR = 15


class ZendeskProxyThrottle(UserRateThrottle):
    """
    Custom throttle rates for this particular endpoint's use case.
    """
    THROTTLE_RATES = {
        'user': '{}/hour'.format(ZENDESK_REQUESTS_PER_HOUR),
    }

class ZendeskPassthroughView(APIView):
    """
    TODO better docstring
    """

    throttle_classes = ZendeskProxyThrottle,

    def post(self, _request):
        """
        TODO real docstring here
        """
        return Response(status=status.HTTP_200_OK)
