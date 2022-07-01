# Basic Flask Python Web App
from flask import Flask
from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello():
    return render_template('index.html')

@socketio.on('my event')                          # Decorator to catch an event called "my event":
def test_message(message):                        # test_message() is the event callback function.
    emit('my response', {'data': 'got it!'})
                                                    # Trigger a new event called "my response"
                                                  # that can be caught by another callback later in the program.

@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
