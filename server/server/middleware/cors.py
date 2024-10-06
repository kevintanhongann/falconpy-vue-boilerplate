
import falcon
from falcon.http_status import HTTPStatus

class CORSMiddleware:
    def __init__(self, allowed_origins=None, allowed_methods=None, allowed_headers=None):
        self.allowed_origins = allowed_origins or ['*']
        self.allowed_methods = allowed_methods or ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS']
        self.allowed_headers = allowed_headers or ['*']

    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', ', '.join(self.allowed_origins))
        resp.set_header('Access-Control-Allow-Methods', ', '.join(self.allowed_methods))
        resp.set_header('Access-Control-Allow-Headers', ', '.join(self.allowed_headers))

    def process_response(self, req, resp, resource, req_succeeded):
        if req.method == 'OPTIONS':
            resp.status = falcon.HTTP_200
            resp.set_header('Access-Control-Max-Age', '3600')
            resp.complete = True

def cors_middleware(allowed_origins=None, allowed_methods=None, allowed_headers=None):
    return CORSMiddleware(allowed_origins, allowed_methods, allowed_headers)
