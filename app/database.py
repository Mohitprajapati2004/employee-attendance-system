from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://ems_hans_user:b5y1GqNczQ6I1UcLCFjxhXd6puyPBC5X@dpg-d6l7rfdm5p6s73981n60-a.oregon-postgres.render.com:5432/ems_hans"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()