from flask import Flask, request, send_file

from iTA import Loading_Model

app = Flask(__name__)

@app.route("/")
def home():
    return send_file('home.html')

@app.route('/get')
def index():        
    data = request.args.get('msg')
    data = data.strip()
    print(data)
    if data == "":
        return "Uh oh! You gotta ask something."

    return str(res.get_response(data))

if __name__ == '__main__':
    res = Loading_Model()
    print("model loaded")
    app.run(host="127.0.0.1",port=8080,debug=True)
    
