from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from task_service.infrastructure.settings import settings


DATABASE_URL = f"postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"  # Para PostgreSQL
# DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"  # Para MySQL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.commit()
        db.close()
