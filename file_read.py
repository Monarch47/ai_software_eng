import os

def read_file(folder_path, file_name):
    """
    Reads the contents of a file located in a specified folder.

    Parameters:
        folder_path (str): The path to the folder where the file is located.
        file_name (str): The name of the file to be read.

    Returns:
        str: The content of the file or an error message if an exception occurs.
    """
    # Construct full path to the file
    file_path = os.path.join(folder_path, file_name)

    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "The file does not exist."
    except IOError:
        return "An error occurred while reading the file."
    except Exception as e:
        return f"An error occurred: {e}"
