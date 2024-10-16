from flask import Flask, request, jsonify, render_template
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

app = Flask(__name__)

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"(hi|hey|hello)",
        ["Hello!", "Hi there!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help you."]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand you."]
    ]
]

chatbot = Chat(pairs, reflections)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
