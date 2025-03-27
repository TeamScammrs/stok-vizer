import os
import json
import textwrap
import google.generativeai as genai
from pathlib import Path

class GeminiChatbot:
    def __init__(self, 
                 model_name: str = "gemini-1.5-pro", 
                 history_file: str = "chat_history.json"):
        """
        Initialize the Gemini Chatbot with persistent global chat history
        
        Args:
            model_name (str): Name of the Gemini model to use
            history_file (str): Global file to store all chat history
        """
        # API Key Configuration
        #bring api key as GEMINI_API_KEY from env file
        GEMINI_API_KEY = "your_api_key"
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Ensure history directory exists
        Path(history_file).parent.mkdir(parents=True, exist_ok=True)
        
        # Generation Configuration
        self.generation_config = {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
        
        # Safety Settings
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
        
        # Model and Chat Session Setup
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            system_instruction="""You are a smart Finance & Investment Chatbot that helps users solve investment problems, simplify financial jargon, and provide real-time market insights with personalized feedback.

Core Capabilities:
🔹 Investment Assistance – Answer queries, break down jargon, and provide educational insights.
🔹 Personalized Feedback – Analyze user portfolios, suggest improvements, and assess risk.
🔹 Report Generation – Create reports on portfolio performance, asset valuation, tax efficiency, and market trends.
🔹 Graph Analysis – Interpret charts (candlesticks, moving averages, RSI, MACD) and summarize key takeaways.
🔹 Real-Time Market Data – Display live stock/crypto prices, news, and alerts on a personalized dashboard.
🔹 Advanced Tools – Scenario analysis, backtesting, AI-driven financial planning, and sector rotation insights.

User Experience:

Adapt responses based on expertise (beginner to advanced).

Offer actionable insights, not just data.

Use interactive visuals and reports for clarity.

Make sure that you are NOT using ** or any such characters for Bold, etc. Don't include any font styling please. Also make sure you answer in coherent terms"""
        )
        
        # Chat History Management
        self.history_file = history_file
        self.chat_session = self.model.start_chat(history=self._load_global_history())
    
    def _load_global_history(self):
        """Load the global chat history from file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading global history: {e}")
            return []
    
    def _save_global_history(self):
        """Save the current history to the global file"""
        try:
            with open(self.history_file, 'w') as f:
                # Convert the chat history to a serializable format
                serializable_history = []
                for message in self.chat_session.history:
                    serializable_history.append({
                        'role': message.role,
                        'parts': [{'text': part.text} for part in message.parts]
                    })
                json.dump(serializable_history, f, indent=2)
        except Exception as e:
            print(f"Error saving global history: {e}")
    
    def chat(self, user_input):
        """Process user input and maintain global history"""
        try:
            if not user_input.strip():
                return "Please enter a valid message"
            
            # Get response and update history
            response = self.chat_session.send_message(user_input)
            self._save_global_history()  # Persist after each message
            
            # Extract and return response text
            if response.candidates and response.candidates[0].content.parts:
                return str(response.candidates[0].content.parts[0].text)
            return "No response generated"
            
        except Exception as e:
            print(f"Chat error: {e}")
            return f"An error occurred: {str(e)}"

# Example usage:
if __name__ == "__main__":
    chatbot = GeminiChatbot()
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        response = chatbot.chat(user_input)
        print("Bot:", response)