from flask import Flask, Response

def create_application() -> Flask:
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def dummy():
        return Response("This is Somthing?")
    
    return app

if __name__=="__main__":
    app = create_application()
    app.run(host="127.0.0.1", port=5000, debug=True)