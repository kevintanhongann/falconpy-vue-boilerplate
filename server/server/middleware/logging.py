
import falcon
import logging
import time
from uuid import uuid4

class LoggingMiddleware:
    def __init__(self):
        self.logger = logging.getLogger('falcon.request')

    def process_request(self, req, resp):
        req.context['start_time'] = time.time()
        req.context['request_id'] = str(uuid4())

    def process_response(self, req, resp, resource, req_succeeded):
        total_time = time.time() - req.context['start_time']
        status = resp.status if req_succeeded else '500 Internal Server Error'
        
        log_entry = {
            'request_id': req.context['request_id'],
            'method': req.method,
            'path': req.path,
            'status': status,
            'duration': f'{total_time:.4f}s'
        }

        if req_succeeded:
            self.logger.info(f"Request completed: {log_entry}")
        else:
            self.logger.error(f"Request failed: {log_entry}")

def get_logging_middleware():
    return LoggingMiddleware()
