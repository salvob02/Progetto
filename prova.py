
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    
    return 'Hello, World!'

def ciclo():
    i=0
    if i==0:
        index()



            
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
