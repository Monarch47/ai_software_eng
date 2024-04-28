// Initialize the Showdown converter globally
var converter = new showdown.Converter();
const chatContainer = document.getElementById('chat-container');

function addMessage(message, isSender) {
    chatContainer.classList.remove('hidden');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message-container', isSender ? 'sender' : 'receiver', 'flex', 'items-start', 'mb-4');

    const avatar = document.createElement('div');
    avatar.classList.add('avatar', 'bg-blue-500', 'text-white', 'flex', 'items-center', 'justify-center', 'rounded-full', 'w-10', 'h-10', 'mr-2');
    avatar.textContent = isSender ? 'U' : 'G';
    messageElement.appendChild(avatar);

    const messageBubble = document.createElement('div');
    messageBubble.classList.add('message-bubble', isSender ? 'max-w-md_bg-red-300' : 'bg-[#29293d]', 'rounded-lg', 'p-3', 'w-4/5'); // Changed max-w-3/4 to w-3/4
    messageBubble.textContent = message;
    messageElement.appendChild(messageBubble);

    chatContainer.appendChild(messageElement);
}

function handleUserInput(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function handleFileUpload() {
    const fileInput = document.getElementById('file-upload');
    const files = fileInput.files;

    if (files.length > 0) {
        const file = files[0]; // We will send the first file to the server
        const formData = new FormData();
        formData.append('document', file);

        fetch('http://127.0.0.1:5000/input_m', {
            method: 'POST',
            body: formData
        }).then(response => response.text())
            .then(result => {
                console.log('File upload response:', result);
                addMessage(`Uploaded: ${file.name}`, true);
            })
            .catch(error => console.error('Error:', error));
    }
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') {
    };

    addMessage(userInput, true); // Show user's message on the chat interface

    fetch('http://127.0.0.1:5000/input_t', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok'); // Handling HTTP error statuses
            }
            return response.text();  // Assuming server responds with text
        })
        .then(data => {
            console.log('Server response:', data);
            addMessage(data, false); // Optionally, display the server's response
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage(`Error: ${error.message}`, false); // Display error message in the chat interface
        });

    document.getElementById('user-input').value = ''; // Clear input after sending
}

function fetchString() {
    fetch('http://127.0.0.1:5000/send_string')
        .then(response => response.text())
        .then(data => {
            addMessage(data, false); // Displaying the fetched string from send_string endpoint
        })
        .catch(error => console.error('Error fetching from send_string:', error));
}

function createTerminalContent() {
    const terminalDiv = document.getElementById('terminal');

    // Clear any existing content
    terminalDiv.innerHTML = '';

    // Add terminal output
    const filesRunning = ["npm run start", "Node.js v14.17.0", "Watching for changes..."];
    filesRunning.forEach(file => {
        const p = document.createElement('p');
        p.textContent = file;
        p.classList.add('p-4', 'font-mono', 'text-white');
        terminalDiv.appendChild(p);
    });
}

// Note: Your script had two definitions for initializeChat(). Ensure to only have one.
// This is the one that will be used.
document.addEventListener('DOMContentLoaded', function () {
    createTerminalContent();
    const sendButton = document.getElementById('send-btn');
    const fileUploadInput = document.getElementById('file-upload');
    const userInput = document.getElementById('user-input');

    sendButton.addEventListener('click', sendMessage);
    fileUploadInput.addEventListener('change', handleFileUpload);
    userInput.addEventListener('keypress', handleUserInput);
});
