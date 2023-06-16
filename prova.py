#!/usr/bin/python


from flask import Flask
from sys import stderr
app = Flask(__name__)

@app.route('/')

def root():
    print('Hello world!', file=sys.stderr)
    
            
               
    

    


    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
