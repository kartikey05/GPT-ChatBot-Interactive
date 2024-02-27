import os
from openai import OpenAI
from config.config import chatgpt_api_key

# Set the OpenAI API key from the configuration
os.environ["OPENAI_API_KEY"] = chatgpt_api_key

# Initialize the OpenAI client
client = OpenAI()

def generate_response(user_input):
    # Generate response using ChatGPT
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response['choices'][0]['message']['content'].strip()

# Chat loop
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break

        chatbot_response = generate_response(user_input)
        print(f"Chatbot: {chatbot_response}")
