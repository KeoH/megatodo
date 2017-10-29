"""
    Utils related with Json Web Token
"""

from .serializers.user import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    '''
        Function to handler the login response with JWTokens
    '''
    return {
        'token' : token,
        'user' : UserSerializer(user, context={'request':request}).data
    }