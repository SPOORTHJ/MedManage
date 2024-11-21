from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://pma:360@localhost/hmdbms")

try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print(result.fetchone())
except Exception as e:
    print("Error connecting to the database:", e)