import json


# Function to load responses from JSON file
def load_responses_from_json(json_file_1):
    with open(json_file_1, 'r') as file:
        data = json.load(file)
    return data['qa_pairs']


# Function to save responses to JSON file
def save_responses_to_json(json_file_1, responses1):
    data = {"qa_pairs": responses1}
    with open(json_file_1, 'w') as file:
        json.dump(data, file, indent=4)


# Function to get a response
def get_response(question, responses1):
    question = question.lower()
    for (k, v) in responses1.items():
        if question == k.lower():
            return v
    return "I'm sorry, I don't understand that question."


# Main chat loop
if __name__ == "__main__":
    json_file = "responses.json"
    responses = load_responses_from_json(json_file)

    print("Chatbot: Hello! Ask me a question (or type 'exit' to quit).")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            save_responses_to_json(json_file, responses)  # Save responses to JSON before exiting
            break
        response = get_response(user_input, responses)
        print("Chatbot:", response)

        # If the response is not in the JSON, prompt the user to add a new response
        if response == "I'm sorry, I don't understand that question.":
            new_response = input("Chatbot: Please provide a response for this question: ")
            # responses.append({"question": user_input, "response": new_response})
            responses[user_input] = new_response
            save_responses_to_json(json_file, responses)  # Save updated responses to JSON
            print("Chatbot: Response added!")
