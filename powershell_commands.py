import subprocess

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

run_powershell_command("pip install keyboard")