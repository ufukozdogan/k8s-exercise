from flask import Flask
import time, socket

app = Flask(__name__)

@app.route("/")
def home():
    ts = time.time()
    hostname = socket.gethostname()
    return {'timestamp' : ts, 'hostname': hostname}, 200