from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        json_message = request.json
        print(json_message)
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run()
