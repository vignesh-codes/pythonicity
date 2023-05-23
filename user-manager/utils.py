from calendar import timegm
from datetime import datetime
from core.settings import JWT_SETTINGS


def jwt_payload(user, context=None):
    username = user.get_username()
    user_id = str(user.id)

    if hasattr(username, 'pk'):
        username = username.pk

    payload = {
        user.USERNAME_FIELD: username,
        'sub': user_id,
        'exp': datetime.utcnow(),
    }

    payload['origIat'] = timegm(datetime.utcnow().utctimetuple())

    payload['aud'] = "JWT_SETTINGS.JWT_AUDIENCE"

    payload['iss'] = "IN"

    return payload