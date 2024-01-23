from flask import Flask, render_template, request, url_for, redirect
import Pyro4

app = Flask(__name__)
chat_server = Pyro4.Proxy("PYRO:obj_7dbbe483ab5d49508a28247eb6693d44@localhost:51072")


@app.route('/')
def index():
    return render_template('chat.html', messages=chat_server.get_messages());


@app.route('/send', methods=['POST'])
def send_message():
    message = request.form['message']
    chat_server.post_message(message)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
