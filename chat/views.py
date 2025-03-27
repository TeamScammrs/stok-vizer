from django.shortcuts import render
from . import chatbot
import json
import os

def index(request):
    history_file = "chat_history.json"
    chatbot_instance = chatbot.GeminiChatbot(history_file=history_file)
    
    if request.method == "POST":
        user_input = request.POST.get('input', '').strip()
        if user_input:
            # Get response (this automatically saves to history)
            final = chatbot_instance.chat(user_input)
            
            # Load the updated history (now includes the new message)
            with open(history_file, 'r') as f:
                chat_history = json.load(f)
            
            return render(request, "chat/chat.html", {
                "chat_history": chat_history  # Only pass history, not separate user_input/final
            })
    
    # For GET requests
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            chat_history = json.load(f)
    else:
        chat_history = []
    
    return render(request, "chat/chat.html", {
        "chat_history": chat_history
    })

def stock(request):
    if request.method == "POST":
        history_file = "chat_history.json"
        chatbot_instance = chatbot.GeminiChatbot(history_file=history_file)
        user_input = request.POST.get('input', '').strip()
        if user_input:
            final = chatbot_instance.chat(user_input)
            with open(history_file, 'r') as f:
                chat_history = json.load(f)
            return render(request, "chat/chat.html", {
                "chat_history": chat_history
            })
    return render(request, "chat/stock.html")