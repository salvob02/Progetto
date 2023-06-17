
from flask import Flask, render_template
  
# declaring app name
app = Flask(__name__)
  
# making list of languages
Linguaggi =["Python", "Javascript", "Java", "C", 
           "C#", "C++", "Php", "Swift", "R"]
  
# defining home page
@app.route('/')
def homepage():
  
# returning index.html and list
# and length of list to html page
    return render_template("index.html", len = len(Linguaggi), Linguaggi = Linguaggi)
  
   


            
if __name__ == "__main__":
    app.run(use_reloader = True ,debug=True, host="0.0.0.0", port=8081)
