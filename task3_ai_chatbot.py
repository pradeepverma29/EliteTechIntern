
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there, what can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created for the internship task."]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?", "I'm fine, thank you!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No worries.", "Don't mention it."]
    ],
    [
        r"quit",
        ["Bye! Have a great day.", "Goodbye!"]
    ],
]

def start_chat():
    print("Hello! I'm your AI Chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_chat()
