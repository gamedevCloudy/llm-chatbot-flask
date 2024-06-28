from flask import Blueprint, render_template, request



home = Blueprint('home', __name__)

@home.route('/')
def home_base(): 
    return render_template('index.html')

@home.post('/chat')
def chat():
    query = request.form.get('query')
    return f"<article>{query}</article>"