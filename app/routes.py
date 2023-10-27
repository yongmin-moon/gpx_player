from flask import render_template, jsonify
from app import app
from app.utils import *

@app.route('/')
def index():
    point = get_first_point_from_gpx('static/gpx/VID_20231024_171219_00_002.gpx')
    return render_template('index.html', point=point)


# 추가적인 라우트와 뷰 함수를 여기에 정의하세요.

@app.route('/gpx-data')
def gpx_data():
    """GPX 데이터를 반환하는 API 엔드포인트입니다."""
    data = parse_gpx('static/gpx/VID_20231024_171219_00_002.gpx')
    return jsonify(data)


@app.route('/gpx-time-data')
def gpx_time_data():
    """GPX 파일의 시간 데이터를 반환하는 API 엔드포인트입니다."""
    times = extract_time_from_gpx('static/gpx/VID_20231024_171219_00_002.gpx')
    return jsonify(times)