from flask import Flask
import time, socket

app = Flask(__name__)

@app.route("/")
def home():
    ts = time.time()
    hostname = socket.gethostname()
    #return 'Timestamp: '+str(ts)+'\t'+'Hostname: '+hostname
    return {'timestamp' : ts, 'hostname': hostname}, 200

if __name__ == "__main__":
    app.run(debug=True)