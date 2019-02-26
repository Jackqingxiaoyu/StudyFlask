class Config:
    # 表单配置文件
    CSRF_ENABLED = True
    SECRET_KEY = "helloyuxin"

    # 邮件配置文件
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = "25"
    MAIL_USE_TLS = True
    MAIL_USERNAME = "1205211194@qq.com"
    MAIL_PASSWORD = "tnahnheylwpfibfj"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopConfig(Config):
    DEBUG = True
    # 数据库需要
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/devdb"

class TestConfig(Config):
    TEST = True
    # 数据库需要
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/testdb"

class ProductionConfig(Config):
    # 数据库需要
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/informationsystem"

config = {
    "develop":DevelopConfig,
    "test":TestConfig,
    "product":ProductionConfig,
    "default":DevelopConfig,
}