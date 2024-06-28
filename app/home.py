from flask import Blueprint, render_template, request


import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()

home = Blueprint('home', __name__)

@home.route('/')
def home_base(): 
    response = chat.send_message("""Hello, You're Kris. You are a expert scholar of Bhagwat Geeta. You shall not reply with "I am an ai chatbot or anything to do with chatting at all. You must talk like a friend, in simple english. When I share a problem or anything concerning you should reply with a shlok from geeta and reply with some helpful advice as a friend. To start with, you can introduce yourself with Namaste. """)

    return render_template('index.html', response=response)

@home.post('/chat')
def chat_req():
    query = request.form.get('query')
    response = chat.send_message(query)
    return render_template('chat.response.html',query=query, response=response)