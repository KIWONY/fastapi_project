from dataclasses import dataclass
from os import environ, path

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass    # 딕셔너리 형태
class Config:
    """
    기본 configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = environ.get("DB_URL","postgresql://test:test@localhost/test")
    DEBUG: bool = True
    TEST_MODE: bool = True

@dataclass
class ProdConfig(Config):
    """
    운영서버 config
    """
    PROJ_RELOAD: bool = False

class TestConfig(Config):
    DB_URL: str = "postgresql://test@localhost/test_db"
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    TEST_MODE: bool = True

def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig, local=LocalConfig, test=TestConfig)
    return config.get(environ.get("API_ENV", "local"))()





