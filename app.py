from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def long_running_request():
    # Simulate a 4-minute delay
    time.sleep(240)
    return "Request completed", 200

if __name__ == "__main__":
    app.run(debug=True)