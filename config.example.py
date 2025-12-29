# Flask Configuration Example
# Sao chép file này thành config.py và cập nhật các giá trị

class Config:
    """Base configuration"""
    SECRET_KEY = 'your-secret-key-here-change-in-production'
    DEBUG = False
    TESTING = False
    
    # Session
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    PERMANENT_SESSION_LIFETIME = 86400  # 24 hours


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SECRET_KEY = 'dev-secret-key-not-for-production'
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = 'your-production-secret-key-here'
    # Thay đổi các giá trị này khi deploy
    

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'test-secret-key'


# Chọn config
# config = DevelopmentConfig()  # Cho development
# config = ProductionConfig()   # Cho production
