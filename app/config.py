from decouple import config


class Config:
    DB_USER = config("DB_USER", default='postgres')
    DB_PASSWORD = config("DB_PASSWORD", default='postgres')
    DB_HOST = config("DB_HOST", default='database')
    DB_NAME = config("DB_NAME", default='postgres')
    DB_URI = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


settings = Config
