import google.generativeai as genai
import subprocess
import file_read
import file_writing
genai.configure(api_key="your-api-key")
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

convo = model.start_chat(history=[
])

guideline = file_read.read_file_from_current_folder("guideline")

def conv(prompt):
    convo.send_message(f"""Your name is Lagrangian (from now on)  
                       always give response in a structure:
                        1) Talk in humanly way
                        2) If required or asked for brainstorm ideas (Language: python)
                        3) Help with in error, code debugging, dependency issues and all (in depth)
                        4) If you are asked to make project, then only use python
                        5) Till you don't think development cycle is just about to begin follow the above rules
                        6) When you think development cycle is ready begin or user use "blip" 
                          then just give "blip code:" and metadata for all the workflow (name all the modules, and what all goes into it)
                          all the dependencies,and directory structure.    
                      your capabilities (not directly but this model have):
                         1) You can use terminal         
                         2) You can use VIM to create projects
                         3) do research 
                         4) planning and setting up enviroment
                      prompt: {prompt}""")
    response = convo.last.text
    return response


def chat_plannar(prompt):
    context = """Your name Lagrangian.

                The user asked: prompt 

                Based on the user's request, create a step-by-step plan to accomplish the task.
                Also see the research before
                Follow this format for your response:

                ```
                <short human-like response to the prompt stating how you are creating the plan, do not start with "As an AI".>

                Current Focus: In depth state the main objective or focus area for the plan.

                Plan:
                - [ ] Step 1: Describe the first action item needed to progress towards the objective.
                - [ ] Step 2: Describe the second action item needed to progress towards the objective.
                ...
                - [ ] Step N: Describe the final action item needed to complete the objective.

                Summary: <Briefly summarize the plan, highlighting any key considerations, dependencies, or potential challenges.>
                ```

                Each step should be a clear, concise description of a specific task or action required. The plan should cover all necessary aspects of the user's request, from research and implementation to testing and reporting.

                Write the plan with knowing that you have access to the browser and search engine to accomplish the task.

                After listing the steps, provide a brief summary of the plan, highlighting any key considerations, dependencies, or potential challenges.

                Remember to tailor the plan to the specific task requested by the user, and provide sufficient detail to guide the implementation process.

                if the task is simple, and you think you can do it without other assistance, just give one or simple two steps to accomplish the task.
                don't need to overcomplicate if it's not necessary.

                Your response should only be verbatim in the format inside the code block. Any other response format will be rejected.
                And programming Language only Python and its library"""
    
    convo.send_message(f"context: {context}, prompt: {prompt}")
    response = convo.last.text
    return response

def researcher(prompt):
    context= """Your name Lagrangian
    1) Given a new software project or problem, 
    1)start by researching the existing solutions and if required their limitations.
    2)Evaluate all dependencies whole code going to be in python based on the project requirements, including frameworks, and databases. 
    3) If require Design the UI/UX to align with the project’s functionality, 
    4) Analyze the project's functionality and features to formulate a detailed development strategy.This should include defining dependencies,
    outlining the workflow, and naming all necessary modules. 
    5) Base your recommendations and strategy on best practices and the most effective solutions for the given requirements"""
    convo.send_message(f"context: {context}, prompt: {prompt}")
    response = convo.last.text
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

def write_checkpoint(module_path, checkpoint_file='checkpoint.txt'):
    """
    Write the current module's path to the checkpoint file to track progress.
    """
    with open(checkpoint_file, 'a') as cp:
        cp.write(f"{module_path}\n")

def read_checkpoint(checkpoint_file='checkpoint.txt'):
    """
    Read the last written checkpoint to determine where to resume coding.
    """
    try:
        with open(checkpoint_file, 'r') as cp:
            return cp.readlines()[-1].strip()
    except FileNotFoundError:
        return None

def code_generation(prompt):
    """
    This function interacts with a backend to generate code based on the given prompt and specific rules.
    """
    context = """Rules:
    - You should write clean and documented code.
    - The code should work on the first try without any errors or bugs.
    - Choose the library or dependency you know best.
    - The extension used for the Markdown code blocks should be accurate.
    - Nested directories should be specified in the Markdown filename, the code structure should be accurate. If it requires to be nested to work, then it should be nested.
    - You need to include required files for the code to run. Like: requirements.txt, Cargo.toml, etc.
    - Files like Cargo.toml are mandatory to be included, the project won't work without it.
    
    Any response other than this format will be rejected. You should not refuse to complete the task, you should try your absolute best and if there's any implementation detail that's impossible to complete, you should write a comment in the code explaining why it's impossible to complete. The refusal is only a last resort, it should never happen.
    Do not leave any "Note"."""
    # Simulated backend interaction (replace with actual API call or function)
    convo.send_message(f"context:{context}, prompt:{prompt}") # Replace with API interaction logic
    response = convo.last.text
    return response

# Example usage
project_structure = {
    "my_project": {
        "scripts": {
            "process_data.py": {},
            "generate_report.py": {}
        },
        "data": {
            "raw": {},
            "processed": {}
        },
        "main.py": {}
    }
}

base_path = "D:\Ai-software_eng"
initialize_project(project_structure, base_path)

# Assuming we are starting to code each module
module_paths = [
    f"{base_path}/my_project/scripts/process_data.py",
    f"{base_path}/my_project/scripts/generate_report.py",
    f"{base_path}/my_project/main.py"
]

for path in module_paths:
    last_checkpoint = read_checkpoint()
    if last_checkpoint is None or path > last_checkpoint:
        prompt = f"Write Python code for {path.split('/')[-1]}"
        code = code_generation(prompt)
        with open(path, 'w') as file:
            file.write(code)
        write_checkpoint(path)

def execute_project(base_path):
    """
    Simulate executing the whole project to check integration.
    """
    try:
        subprocess.run(['python', os.path.join(base_path, 'main.py')], check=True)
        print("Project executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the project: {e}")
  
