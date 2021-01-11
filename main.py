from flask import Flask, request, send_file
import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument("model", help="Model directory")
    parser.add_argument("documents", help="List of text documents to answer the question with", nargs='+')
    args = parser.parse_args()

    res = Loading_Model(args.model, args.documents)
    print("model loaded")
    app.run(host="127.0.0.1",port=8080,debug=True)
    
