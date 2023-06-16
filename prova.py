#!/usr/bin/python


from flask import Flask
app = Flask(__name__)

@app.route('/')

def root():
    i=0
    while (i<5):
              i=i+1
    
    return "il valore di i e: ",i
            
               
    

    


    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
