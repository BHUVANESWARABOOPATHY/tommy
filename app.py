from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
chat_history = []

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['message']
        chat_history.append(f"You: {user_input}")
        bot_reply = f"Bot: You said '{user_input}'"
        chat_history.append(bot_reply)
    return render_template('index.html', chat_history=chat_history)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
