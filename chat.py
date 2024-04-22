import google.generativeai as genai
import subprocess
import file_read
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

convo = model.start_chat(history=[
])

guideline = file_read.read_file_from_current_folder("guideline")

def conv(prompt):
    convo.send_message(f"guideline: {guideline} prompt: {prompt}")
    response = convo.last.text
    return response


      
   

