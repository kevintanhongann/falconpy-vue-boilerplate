
import falcon

class HelloResource:
    def on_get(self, req, resp):
        resp.media = {"message": "Hello, World!"}

app = falcon.App()
app.add_route("/", HelloResource())

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    with make_server("", 8000, app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
