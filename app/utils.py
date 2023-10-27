import gpxpy
import os
from flask import current_app

# 추가적인 유틸리티 함수를 여기에 정의하세요.

def parse_gpx(file_path):
    """GPX 파일을 파싱하여 경로 데이터를 반환합니다."""
    absolute_path = os.path.join(current_app.root_path, file_path)
    with open(absolute_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        data = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    data.append((point.latitude, point.longitude))
    return data

def get_first_point_from_gpx(file_path):
    """GPX 파일의 첫 번째 포인트를 반환합니다."""
    absolute_path = os.path.join(current_app.root_path, file_path)
    with open(absolute_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    return (point.latitude, point.longitude)
    return None


def extract_time_from_gpx(file_path):
    absolute_path = os.path.join(current_app.root_path, file_path)
    with open(absolute_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        times = [point.time for track in gpx.tracks for segment in track.segments for point in segment.points]
    return times
