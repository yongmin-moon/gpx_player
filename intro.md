초기 가상환경 설정
python3.11 -m venv gpx_player
.\gpx_player\Scripts\activate
python.exe -m pip install --upgrade pip
pip install Flask, gpxpy


/myproject/
|-- /app/
|   |-- /templates/
|   |   |-- index.html
|   |   |-- map.html
|   |-- /static/
|   |   |-- /css/
|   |   |-- /js/
|   |   |-- /images/
|   |-- __init__.py
|   |-- routes.py
|   |-- models.py (데이터베이스 모델이 필요한 경우)
|   |-- utils.py (유틸리티 함수나 GPX 파싱 함수 등)
|-- config.py (환경별 설정 정보)
|-- run.py (Flask 앱을 실행하는 스크립트)
|-- requirements.txt (필요한 파이썬 패키지 목록)
|-- README.md (프로젝트 설명 및 실행 방법)
|-- .gitignore (Git에서 무시할 파일/디렉토리 목록)