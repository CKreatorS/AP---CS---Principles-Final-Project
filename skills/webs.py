from flask import Flask

def create_app():
    app = Flask(__name__)

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=4247)