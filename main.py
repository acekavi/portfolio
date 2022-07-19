from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<page_name>")
def html_page(page_name):
    return render_template(f'{page_name}.html')