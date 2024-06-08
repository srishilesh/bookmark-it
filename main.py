from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__, template_folder="templates")

urls = []

@app.route('/', methods=["POST", "GET"])d
def home():
    if request.method == "POST":
        url = request.form['url']
        urls.append(url)
    return render_template("home.html")

    
@app.route("/display", methods=["GET"])
def display():
    if request.method == "GET":
        return urls

if __name__ == '__main__':
    app.run(debug=True)