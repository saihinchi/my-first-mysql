class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'saihinchi308',
      'password': 'Taku0420',
      'host': 'localhost',
      'db_name': 'english'
  })

Config = SystemConfig