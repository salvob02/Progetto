
from flask import Flask

app = Flask(__name__)

lista=["uno","uno","uno","due"]
@app.route('/')
def index():
    
    return 'Hello, World!'

def ciclo():
    for parola in lista:
        if parola=="uno":
        index()



            
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
