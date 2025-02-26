# app.py
from flask import Flask
import config

app = Flask(__name__)

# config.py에서 설정을 로드
app.config.from_object(config.Config)

@app.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)

