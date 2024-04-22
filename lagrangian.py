from file_writing import write_to_text_file
import subprocess
from datetime import datetime
from file_read import read_file
import chat

#Functions

# Time stamp
def current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

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

# Open a PowerShell process
def run_powershell_command(user_input):
    process = subprocess.Popen(["powershell"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send the user input to PowerShell and close the input to indicate that we're done
    stdout, stderr = process.communicate(input=user_input)

    # Check for errors
    if process.returncode != 0:
        print("Error:", stderr)
    else:
        print("Output:", stdout)

#Code function
def add_code_with_powershell(code, filename="example.py"):
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




print("Hey!, Lagrangian this side")

#chat

while True:
    ins = input("Prompts: ")
    print(chat.conv(ins))
    










