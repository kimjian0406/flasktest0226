# config.py

import os

class Config:
    SECRET_KEY = os.urandom(24)  # 애플리케이션의 보안을 위해 secret key 설정

