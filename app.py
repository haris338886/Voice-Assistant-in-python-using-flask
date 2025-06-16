from flask import Flask, render_template, request, jsonify
import datetime
import random
import re
import os
import webbrowser
import pyjokes

app = Flask(__name__)

def process_command(command):
    command = command.lower()

    # TIME & DATE
    if "time" in command:
        return "The current time is " + datetime.datetime.now().strftime("%I:%M %p")
    elif "date" in command:
        return "Today's date is " + datetime.datetime.now().strftime("%A, %B %d, %Y")

    # GREETINGS
    elif "hello" in command or "hi" in command:
        return "Hello! How can I assist you today?"
    elif "bye" in command or "goodbye" in command:
        return "Goodbye! Have a great day!"

    # WEBSITES
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."
    elif "github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub..."

    # CALCULATIONS
    elif "calculate" in command:
        try:
            expression = re.findall(r'calculate (.*)', command)[0]
            result = eval(expression)
            return f"The result is {result}"
        except Exception:
            return "Sorry, I couldn't calculate that."

    # JOKES
    elif "joke" in command:
        return pyjokes.get_joke()

    # DEFAULT
    else:
        return "Sorry, I did not understand that. Try saying 'time', 'date', or 'tell me a joke'."

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    command = data.get('command', '')
    response = process_command(command)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
