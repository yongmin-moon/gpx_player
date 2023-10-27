# 환경별 설정 정보를 여기에 정의하세요.

class Config:
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite:///example.db'  # 예시

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True
