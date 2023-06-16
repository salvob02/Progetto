from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
        if request.form:
                print('Form:' + str(request.form))
        if request.data:
                print('Data:' + str(request.data))

        return ''
    
            
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
