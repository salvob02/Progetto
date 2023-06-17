
from flask import Flask, render_template
  
app = Flask(__name__)
  
# lista 
Linguaggi =["Python", "Javascript", "Java", "C", 
           "C#", "C++", "Php", "Swift", "R"]
  
# definizione funzione home page
@app.route('/')  #path sul quale eseguire
def homepage():
  
# ritorna index.html e lista
# nei parametri passaggio di len e lista al file html
    return render_template("index.html", len = len(Linguaggi), Linguaggi = Linguaggi)
  
   


            
if __name__ == "__main__":
    app.run(use_reloader = True ,debug=True, host="0.0.0.0", port=8081)   #generare il file http in locale alla porta 8081
