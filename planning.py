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


context = """Develop a complete technical strategy for the software project described. Your strategy should encompass in-depth planning for all aspects of the project to ensure robustness and scalability. Follow these guidelines:

Comprehensive Module Planning:
Module Identification: Identify all necessary modules required for the project's core functionalities. Describe each module in detail, including its purpose, main functions, and interactions with other modules.
Data Handling and Integration: Specify how data will flow between modules, detailing any data processing, storage requirements, and external data integrations.
Detailed Dependency Management:
List of Dependencies: Compile a detailed list of all software libraries, frameworks, and tools that the project will depend on. Include specific versions and their purposes to ensure compatibility and optimal performance.
Dependency Handling: Explain the methods for managing these dependencies, including version control, package management, and updating strategies.
Technical Infrastructure Design:
Infrastructure Requirements: Outline the technical infrastructure needed for hosting, executing, and managing the application, including servers, databases, and cloud services.
Security Architecture: Describe security measures that will be implemented to protect data and ensure privacy, including encryption techniques and compliance with relevant standards.
Development Workflow and Testing Regimen:
Development Methodologies: Recommend a development methodology that suits the project’s needs, detailing the version control system, code review practices, and collaboration tools.
Testing Strategy: Develop a comprehensive testing strategy that includes unit testing, integration testing, system testing, and user acceptance testing. Specify tools and frameworks for implementing these tests.
Feature Development Based on Limitations and Proposed Enhancements:
Identify Limitations: From an analysis of existing solutions, identify key limitations and areas for improvement.
Feature Design: Propose new features or enhancements that address these limitations. Provide a detailed plan for the development of these features, including technical specifications and integration with existing modules.
Documentation and Future Reference:
Technical Documentation: Plan for the creation of detailed documentation covering the architecture, codebase, APIs, and user manuals to facilitate future development and maintenance.
Change Management: Describe a process for handling future changes and updates to the software, ensuring continuity and scalability."""""

def planning(prompt):
    convo.send_message(f"context: {context}, prompt:{prompt}, note: you have to code, so decide everything now only. And make choices such that you can make it")
    response = convo.last.text
    return response
