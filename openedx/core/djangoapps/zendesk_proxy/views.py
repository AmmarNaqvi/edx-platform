"""
Define request handlers used by the zendesk_proxy djangoapp
"""

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt  # TODO: remove this before merge/deploy, it's only here for ease of manual testing during development
@require_POST
def zendesk_passthrough(_request):
    """
    This is just a skeleton for now to make sure I get django routing set up properly.
    """
    return HttpResponse(status=200)
