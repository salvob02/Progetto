
from flask import Flask
app = Flask(__name__)


@app.route('/')
def root():
    i=0
    return "Hello World (Python)! %d" % (i)

            
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
