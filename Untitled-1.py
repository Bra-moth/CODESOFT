import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK data files
nltk.download('punkt')

def chatbot_response(user_input):
    # Convert the user input to lower case for case insensitive matching
    user_input = user_input.lower()
    
    # Tokenize the user input
    tokens = word_tokenize(user_input)

    # Rule-based responses
    if "hello" in tokens or "hi" in tokens:
        return "Hello! How can I help you today?"
    elif "how" in tokens and "you" in tokens:
        return "I'm a chatbot, so I'm always good! How can I assist you?"
    elif "name" in tokens:
        return "I am a simple chatbot created to assist you with basic queries."
    elif "help" in tokens:
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "bye" in tokens or "goodbye" in tokens:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to keep the conversation going
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if "bye" in word_tokenize(user_input.lower()) or "goodbye" in word_tokenize(user_input.lower()):
            break

# Start the chat
chat()
