from core.database import Base, engine
from models.model import User, Nanny

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
