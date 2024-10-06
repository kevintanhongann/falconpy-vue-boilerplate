# import falcon
# from falcon_cors import CORS

# from .routes import setup_routes

# def create_app():
#     cors = CORS(allow_all_origins=True, allow_all_headers=True, allow_all_methods=True)
#     app = falcon.App(middleware=[cors.middleware])
    
#     setup_routes(app)
    
#     return app
