from sqlalchemy import Table,Column
from config.db import meta

users=Table(
    'users',meta,
    Column('usr_id',Integer,primary_key=True),
    Column('usr_lvl_id',Integer),
    Column('passwd')

)