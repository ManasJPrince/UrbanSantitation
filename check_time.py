from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./urban_sanitation.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

print(f"Python Local Time: {datetime.now()}")
print(f"Python UTC Time:   {datetime.utcnow()}")

try:
    result = db.execute(text("SELECT id, timestamp, zone_id FROM incidents ORDER BY id DESC LIMIT 5")).fetchall()
    print("\nRecent Incidents in DB:")
    for row in result:
        print(f"ID: {row[0]}, Time: {row[1]}, Zone: {row[2]}")
except Exception as e:
    print(e)
