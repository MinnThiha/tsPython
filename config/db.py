from sqlalchemy import create_engine, MetaData

engine=create_engine("mysql+pymysql://root'@'localhost:3306/MPU_TEST")
meta=MetaData()
conn=engine.connect()
