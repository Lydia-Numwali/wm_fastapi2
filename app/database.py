from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:myPassword!!!@localhost:3306/waste_db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)




# SessionLocal will be used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_db_connection():
    try:
        # Test the connection
        with engine.connect() as connection:
            # Wrap the query using text()
            query = text("SELECT 1")
            result = connection.execute(query)  # Use execute() with wrapped query
            print(result.fetchone())  # Should print (1,)
    except OperationalError as e:
        print(f"Error connecting to the database: {e}")
