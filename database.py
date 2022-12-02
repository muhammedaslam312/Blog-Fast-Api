from sqlalchemy import create_engine

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine =create_engine('postgresql://postgres:9961610563@localhost/fast_blog',
    echo =True
)

SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()