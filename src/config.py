class Config:
    SECRET_KEY= 'DESTROYER'


class developmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='tdp'

config={
    'development':developmentConfig
}