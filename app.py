from flask import Flask, request, jsonify, render_template
from apiMethod import aiHelper

app = Flask(__name__)

@app.route("/aiResponse", methods=["GET", "POST"])
def aiMaths():
    if request.method == "POST":
        query = request.form.get("query")
        print(f"\n\nUser-Query: {query}")
        data = aiHelper(query)
        print(f"\n\nAI-Response: {data}")
    return render_template("aiResponse.html", data=data)

@app.route("/")
def home():
    return render_template("index.html")
