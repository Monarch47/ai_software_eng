"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import subprocess

genai.configure(api_key="AIzaSyC6ZIlEOr6X3dqMIPOdMotUiFhoTsfqP54")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])
def parse_after(text, after):
    """
    Extracts and returns the substring that follows a specified text within a given string.

    Args:
    text (str): The full string from which to extract the substring.
    after (str): The text after which the substring should be extracted.

    Returns:
    str: The substring following the specified text, or an empty string if the text is not found.
    """
    # Find the index of the specified text
    index = text.find(after)
    
    # If the text is found, return the substring that follows
    if index != -1:
        return text[index + len(after):]
    else:
        # If the text is not found, return an empty string
        return ""


def run_powershell_command(user_input):
    # Open a PowerShell process
    process = subprocess.Popen(["powershell"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send the user input to PowerShell and close the input to indicate that we're done
    stdout, stderr = process.communicate(input=user_input)

    # Check for errors
    if process.returncode != 0:
        print("Error:", stderr)
    else:
        print("Output:", stdout)


def add_code_with_powershell(code, filename="game.py"):
    # Create or modify the file with the provided code
    with open(filename, 'w') as file:
        file.write(code)

    # Open the file with Vim using PowerShell
    # Note: Assumes PowerShell and Vim are installed and correctly set in PATH
    try:
        # Using PowerShell to open Vim with the created file
        subprocess.run(["powershell", "-Command", f"vim {filename}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")



while True:
    chat = input("Prompt: ")
    convo.send_message(chat)
    response = convo.last.text
    
    add_code_with_powershell(response)
    print(response)
    
      
   

