from tyk.decorators import *
from gateway import TykGateway as tyk

from webhook import trigger_webhook

@Hook
def WebhookMiddleware(request, session, spec):
    payload = {
        'api_id': spec['APIID'],
        'user_agent': request.get_header('User-Agent')
    }
    trigger_webhook(payload)
    return request, session
