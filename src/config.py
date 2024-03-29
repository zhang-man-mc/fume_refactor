

class Config:
    # 爬取参数
    # shop_name = ['吉刻联盟','大成海鲜','大肆撸串','天钥小馆',,'弄堂咪道','杨记齐齐哈','棒约翰','狼来了','缘家','食其家','馨远美食小镇（哈尼美食广场）']
    shop_name = ['吉刻联盟']
    begin_date = '2024-3-22'
    end_date = '2024-3-23'
    page_size = 100
    page_num = 5

    # 请求间隔秒
    delay_start = 1

    # 数据库
    ip = 'localhost'
    user = 'root'
    password = '1234'
    port = 3306
    data_base_name = 're_conganize_fume'

    # 验证码平台
    verification_code_account = '191259'
    verification_code_password = 'zsc654321'

    def __init__(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{Config.user}:{Config.password}@{Config.ip}:{Config.port}/{Config.data_base_name}?charset=utf8"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{Config.user}:{Config.password}@{Config.ip}:{Config.port}/{Config.data_base_name}?charset=utf8"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = None


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}

if __name__ == '__main__':
    print(DevelopmentConfig.SQLALCHEMY_DATABASE_URL)