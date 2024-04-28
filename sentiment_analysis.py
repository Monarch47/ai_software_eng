import google.generativeai as genai

genai.configure(api_key="AIzaSyC6ZIlEOr6X3dqMIPOdMotUiFhoTsfqP54")

# Set up the model
generation_config = {
  "temperature": 0.1,
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


context = """context: "Use sentiment analysis to detect your next move:
Don't give anything else, and do not use markdown
1) if you feel that in chat history now demands in depth research (not for trivial task only for difficult project)
your response : 'research'
2) If you  feel that in the chat history if you feel that everything is done now we just have to code 
your response: "code"
3) And if you feel nothing from the above is happening
Your response: "pass"
"""

def sen_analysis(chat_history):
    convo.send_message(f"context: {context}, prompt:{chat_history}")
    response = convo.last.text
    return response
