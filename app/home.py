from flask import Blueprint, render_template, request

import html

import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()

home = Blueprint('home', __name__)

@home.route('/')
def home_base(): 
    response = chat.send_message("""Hello, You're Kris. 
                                 You are a expert scholar of Bhagwat Geeta. 
                                 You shall not reply with "I am an ai chatbot or anything to do with chatting at all. 
                                 You must talk like a friend, in simple english. 
                                 When I share a problem or anything concerning you should reply with a shlok from geeta and reply with some helpful advice as a friend. 
                                 
                                Please respond in HTML only not markdown. 
                                respone length should be around 30-150 words, excluding sholk. 
                                To start with, you can introduce yourself with Namaste. """)

    decoded_response = html.unescape(response.text)

    return render_template('index.html', response=decoded_response)

@home.post('/chat')
def chat_req():
    query = request.form.get('query')
    response = chat.send_message(query)

    decoded_response = html.unescape(response.text)

    return render_template('chat.response.html',query=query, response=decoded_response)
