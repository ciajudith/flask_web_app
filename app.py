from flask import Flask, render_template, request, url_for, redirect
import Pyro4

app = Flask(__name__)
chat_server = Pyro4.Proxy("PYRO:obj_c957c682bfd4441c8cad30fa5bf45268@localhost:63633")


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
