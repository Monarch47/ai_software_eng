import google.generativeai as genai
import subprocess
import file_read
import file_writing
import os
import json
from sentiment_analysis import sen_analysis
from hist_save import read_file, append_history_to_file
genai.configure(api_key="AIzaSyC6ZIlEOr6X3dqMIPOdMotUiFhoTsfqP54")
# Set up the model
generation_config = {
  "temperature": 1.5,
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



if os.path.exists('history.json'):
  convo = model.start_chat(history= read_file('history.chat'))
else:
  convo = model.start_chat(history = [])
guideline = file_read.read_file_from_current_folder("guideline")

def conv(prompt):
    context = """Your name is Lagrange (from now on)  
                       always give response keeping these pointers in mind:
                        1) Talk in humanly way
                        2) If required or asked for brainstorm ideas (Language: python)
                        3) Help with in error, code debugging, dependency issues and all (in depth)
                        4) If you are asked to make project, then only use python
                        5) Till you don't think development cycle is just about to begin follow the above rules"""
    convo.send_message(f"""context: {context}
                      prompt: {prompt}""")
    response = convo.last.text
    history = convo.history
    append_history_to_file(history=history)
    return response

def researcher(prompt):
    context= """Your name Lagrange
    1) Given a new software project or problem, 
    1)start by researching the existing solutions and if required their limitations.
    2)Evaluate all dependencies whole code going to be in python based on the project requirements, including frameworks, and databases. 
    3) If require Design the UI/UX to align with the project’s functionality, 
    4) Analyze the project's functionality and features to formulate a detailed development strategy.This should include defining dependencies,
    outlining the workflow, and naming all necessary modules. 
    5) Base your recommendations and strategy on best practices and the most effective solutions for the given requirements"""
    convo.send_message(f"context: {context}, prompt: {prompt}")
    response = convo.last.text
    history = convo.history
    append_history_to_file(history=history)

    return response


import os
import subprocess

def initialize_project(structure, base_path="."):
    """
    Initialize the project directories and files according to the specified structure.
    """
    os.makedirs(base_path, exist_ok=True)
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, dict):
            initialize_project(value, path)
        else:
            with open(path, 'w') as f:
                f.write('')  # Create an empty file


def code_generation(prompt):
    """
    This function interacts with a backend to generate code based on the given prompt and specific rules.
    """
    context = """Rules:
    - You should write clean and documented code.
    - The code should work on the first try without any errors or bugs.
    - Choose the library or dependency you know best.
    - Make sure you write the code files such that they can be executed sequentially
    - The extension used for the Markdown code blocks should be accurate.
    - Nested directories should be specified in the Markdown filename, the code structure should be accurate. If it requires to be nested to work, then it should be nested.
    - You need to include required files for the code to run. Like: requirements.txt, Cargo.toml, etc.
    Here is a mandatory template that you have to follow:
      1) Start by giving a one-line info on the code you're about to create and execute
      2) use the following delimiter for python: Starting delimiter -'''python; ending delimiter - python''' 
      3) use the following delimiter for powershell: Starting delimiter -'''shell; ending delimiter - shell'''   
    
    Any response other than this format will be rejected. You should not refuse to complete the task, you should try your absolute best and if there's any implementation detail that's impossible to complete, you should write a comment in the code explaining why it's impossible to complete. The refusal is only a last resort, it should never happen.
    Do not leave any "Note"."""
    # Simulated backend interaction (replace with actual API call or function)
    convo.send_message(f"context:{context}, prompt:{prompt}") # Replace with API interaction logic
    response = convo.last.text
    history = convo.history

    append_history_to_file(history=history)
    return response

model_selection = {
    "research": researcher,
    "code": code_generation,
    "pass": conv
}
def chat(input):
    return model_selection[sen_analysis(input).split(" ")[0]](input)
