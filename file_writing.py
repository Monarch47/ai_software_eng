import os

def write_to_text_file(folder_path, file_name, text_to_write):
    """
    Write text to a specified file within a given folder.

    Args:
    folder_path (str): The path to the folder where the file will be saved.
    file_name (str): The name of the file to write to (including the extension).
    text_to_write (str): The text that will be written to the file.
    """
    # Ensure the directory exists
    os.makedirs(folder_path, exist_ok=True)

    # Create the full file path
    file_path = os.path.join(folder_path, file_name)

    # Writing to the file
    with open(file_path, 'w') as file:
        file.write(text_to_write)

    print(f'File has been written to {file_path}')

def append_to_text_file(folder_path, file_name, text_to_append):
    """
    Append text to a specified file within a given folder. Creates the file if it doesn't exist.

    Args:
    folder_path (str): The path to the folder where the file will be saved.
    file_name (str): The name of the file to append to (including the extension).
    text_to_append (str): The text that will be appended to the file.
    """
    # Ensure the directory exists
    os.makedirs(folder_path, exist_ok=True)

    # Create the full file path
    file_path = os.path.join(folder_path, file_name)

    # Appending to the file
    with open(file_path, 'a') as file:
        file.write(text_to_append)