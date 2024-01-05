from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def get():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "message": "Hello! I am currently running on a Docker Container!",
        "time": time,
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
