from flask import Flask

app = Flask(__name__)

@app.route("/members", methods=['POST','GET'])
def members():
    print("ORAS LJUDINA")
    return "BAJAGA CIGANE"

if __name__=="__main__":
    app.run(host="0.0.0.0")