# import nltk
# import wikipedia
import os
from nltk.tokenize import sent_tokenize

# Download NLTK data (if not already downloaded)
# nltk.download('punkt')

# Load the saved Wikipedia page
wiki_file = "India.txt"

if os.path.exists(wiki_file):
    with open(wiki_file, "r", encoding="utf-8") as file:
        wikipedia_content = file.read()
else:
    print("Wikipedia page file not found. Please save the Wikipedia page in your project folder.")

# Tokenize the content into sentences
sentences = sent_tokenize(wikipedia_content)


# Function to get a response based on user input
def get_response(user_input1):
    # Simple logic to find a relevant sentence from the Wikipedia content
    user_input1 = user_input1.lower()
    for sentence in sentences:
        if user_input1 in sentence.lower():
            return sentence
    return "I couldn't find information related to your query."


# Main chat loop
print("Chatbot: Hello! I have information from a Wikipedia page. Ask me anything (or type 'exit' to quit).")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
