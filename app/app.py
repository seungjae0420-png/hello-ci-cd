from flask import Flask
def create_app():
    app = Flask(__name__)
    @app.get("/health")
    def health():
        return {"status": "ok"}, 200
    @app.get("/")
    def index():
        return "Hello CI!", 200
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
