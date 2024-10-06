
import falcon
from .auth import AuthMiddleware
from .logging import LoggingMiddleware
from .cors import CORSMiddleware

def create_middleware():
    return [
        AuthMiddleware(),
        LoggingMiddleware(),
        CORSMiddleware(),
    ]

def apply_middleware(app):
    middleware = create_middleware()
    for mw in middleware:
        app.add_middleware(mw)

def init_middleware(app: falcon.App):
    apply_middleware(app)
