class Config:
    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        pass
        

class DevelopmentConfig(Config):
    DEBUG = True
    
    
class TestingConfig(Config):
    TESTING = True    
    
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
    }
