import json
from flask import request, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'nsndvd.eu.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'nsndvd-ucs-api'
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def get_token_auth_header():
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        raise AuthError({
            'code': 'auth_header_missing',
            'description': 'Authorization header missing.'
        }, 401)

    if auth_header.split()[0].lower() != 'bearer' or len(auth_header.split()) != 2:
        raise AuthError({
            'code': 'invalid_auth_header',
            'description': 'Authorization header must be in "bearer" token format.'
        }, 401)

    return auth_header.split()[1]

def check_permissions(permission, payload):
    if not payload['permissions']:
        raise AuthError({
            'code': 'no_permissions_in_payoload',
            'description': 'Authorization token doesn\'t contain permissions payload'
        }, 401)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'user_not_allowed',
            'description': 'The user doesn\'t have the required permission'
        }, 403)
    
    return True

def verify_decode_jwt(token):
    our_key = {}
    well_known_jwks_url = urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
    jwks = json.loads(well_known_jwks_url.read())

    header = jwt.get_unverified_header(token)
    if 'kid' not in header:
        raise AuthError({
            'code': 'invalid_authentication_header',
            'description': 'Missing kid in token.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == header['kid']:
            our_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    
    if not our_key:
        raise AuthError({
                'code': 'invalid_header',
                'description': 'Couldn\'t find a key with the right key id.'
            }, 400)
    try:
        decoded_payload = jwt.decode(
            token,
            our_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer='https://' + AUTH0_DOMAIN + '/'
        )

        return decoded_payload

    except jwt.ExpiredSignatureError:
        raise AuthError({
            'code': 'token_expired',
            'description': 'Token expired.'
        }, 401)
    except jwt.JWTClaimsError:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Incorrect claims. Please, check the audience and issuer.'
        }, 401)
    except Exception:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Unable to parse authentication token.'
        }, 400)
    
def requires_auth(permission=None):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token = get_token_auth_header()
                payload = verify_decode_jwt(token)
                if (permission):
                    check_permissions(permission, payload)
            except AuthError as err:
                print(err)
                abort(err.status_code, err.error['description'])
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator

# Given a token, return the associated SID
def get_sub(payload):
    return payload['sub']
