# __init__.py

# 패키지 초기화 코드를 여기에 작성할 수 있습니다.

# 예를 들어, Flask 앱 객체를 여기에서 생성하고자 한다면:
from flask import Flask, render_template

app = Flask(__name__)

from app import routes