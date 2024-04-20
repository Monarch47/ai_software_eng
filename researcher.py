"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="Your_api_key")

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


context = "Given a new software project, start by researching the existing solutions and their limitations in depth. Evaluate the preferred or specified technology stack; if none is provided, recommend the most suitable technologies based on the project requirements, including programming languages, frameworks, and databases. Design the UI/UX to align with the project’s functionality and user demands, or suggest the best options if no specific designs are requested. Analyze the project's functionality and features to formulate a detailed development strategy. This should include defining dependencies, outlining the workflow, and naming all necessary modules. Base your recommendations and strategy on best practices and the most effective solutions for the given requirements,be mindful you have to write the code structure it in a manner you have an ease. Software aimed at "
language_preference = """For Web development: MERN stack
Programming language: Python,html,css,javascript
if specific language is asked in prompt then use that only"""

def research(prompt):
    convo.send_message(f"context: {context}, language:{language_preference}, prompt: {prompt}")
    response = convo.last.text
    return response
