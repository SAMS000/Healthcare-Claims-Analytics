from sqlalchemy import text

from config.database import engine

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))

    print("\nConnected successfully!\n")

    for row in result:
        print(row[0])