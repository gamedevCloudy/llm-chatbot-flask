from flask import Blueprint, render_template



home = Blueprint('home', __name__)

@home.route('/')
def home_base(): 
    return render_template('index.html')

@home.post('/chat')
def chat():
    return "<article>this is the response from server</article>"