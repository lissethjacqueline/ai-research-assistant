"""Goal: make a simple and interactive call to the OpenAI Chat API."""

# Import the OpenAI client to connect to the API
from openai import OpenAI

# Import dotenv to load API keys from a .env file
from dotenv import load_dotenv

# Import os to access env variables from the operating system
import os

# Import sys so we can read command-line arguments from the terminal
import sys

# Load the .env file so the API KEY are available
load_dotenv()

# Initialize the OpenAI client with your API key from the environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question(question: str) -> str:
      """Send a user question to the OpenAI Chat API and return the response.

    Args:
        question (str): The question the user wants to ask the model.

    Returns:
        str: The assistant's answer.
    """

    # Send the user’s question to the Chat Completions API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}, # assistant
            {"role": "user", "content": question} # The actual user question
        ]
    )
    return response.choices[0].message.content #returns the API response

if __name__ == "__main__":
    # If the user typed a question in the terminal, use that.
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:]) #combine all words into 1 string
    else:
        #Otherwise ask the user to type a ? 
        question = input("Ask me anything: ")

    answer = ask_question(question)
    print(answer)
