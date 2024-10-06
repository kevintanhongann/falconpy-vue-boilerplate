
import falcon
from falcon.http_status import HTTP_401

class AuthMiddleware:
    def process_request(self, req, resp):
        token = req.get_header('Authorization')

        if token is None:
            raise falcon.HTTPUnauthorized('Auth token required')

        if not self._is_valid_token(token):
            raise falcon.HTTPUnauthorized('Invalid auth token')

    def _is_valid_token(self, token):
        # TODO: Implement token validation logic
        return True  # Placeholder implementation

class RequireJSON:
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.')

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.')

app = falcon.App(middleware=[
    AuthMiddleware(),
    RequireJSON(),
])

# Example protected resource
class ProtectedResource:
    def on_get(self, req, resp):
        resp.media = {'message': 'This is a protected resource'}

app.add_route('/protected', ProtectedResource())
