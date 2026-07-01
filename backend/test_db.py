from app.database.session import engine

try:
    with engine.connect() as connection:
        print("✅ PostgreSQL Connected Successfully!")
except Exception as e:
    print("❌ Database Connection Failed")
    print(e)