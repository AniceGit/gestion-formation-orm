from sqlmodel import create_engine

DATABASE_URL = "sqlite:///db/database.db"
engine = create_engine(DATABASE_URL, echo=True)
