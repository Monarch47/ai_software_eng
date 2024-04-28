def append_history_to_file(history, file_path='history.chat'):
  with open("file.chat", "ab") as file:
    for a in history:
      file.write(str(a).encode('utf-8'))

def read_file(file_path='history.chat'):
    interactions = []
    current_interaction = {}

    with open(file_path, 'rb') as file:
        for line in file:
            line = line.strip()
            if line.startswith('parts {'):
                # Start collecting parts text
                text = []
                line = next(file).strip()  # Move to the next line
                while not line.startswith('}'):
                    if line.startswith('text:'):
                        # Remove 'text:' and leading/trailing quotes
                        text.append(line.split('text:', 1)[1].strip().strip('"'))
                    line = next(file).strip()
                # Store the collected text
                if 'parts' not in current_interaction:
                    current_interaction['parts'] = []
                current_interaction['parts'].extend(text)
            elif line.startswith('role:'):
                # Extract role
                role = line.split('role:', 1)[1].strip().strip('"')
                current_interaction['role'] = role
            elif line == '' and current_interaction:
                # Empty line might indicate end of one block of interaction
                interactions.append(current_interaction)
                current_interaction = {}  # Reset for next interaction
        
        # Add the last interaction if not already added
        if current_interaction:
            interactions.append(current_interaction)

    return interactions