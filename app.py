from flask import Flask, render_template, request, url_for, redirect
import Pyro4

app = Flask(__name__)
chat_server = Pyro4.Proxy("PYRO:obj_ba54637e382f4444a4b902240ecd4759@localhost:57381")


@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/send', methods=['POST'])
def send_message():
    message = request.form['message']
    chat_server.post_message(message)
    return redirect(url_for('index'))


@app.route('/messages', methods=['GET'])
def get_messages():
    messages = chat_server.get_messages()
    return render_template('messages.html', messages=messages)


if __name__ == '__main__':
    app.run()
