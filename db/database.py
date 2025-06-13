from sqlmodel import create_engine

DATABASE_URL = "sqlite:///db/gestion-formation.db"
engine = create_engine(DATABASE_URL, echo=True)
