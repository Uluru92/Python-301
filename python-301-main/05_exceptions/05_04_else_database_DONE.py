# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

# For this exercise, I am using Exercise_01 (databases) from Python-201.
# Instead of passing the user name from .env, I am asking the user to input the user name
# If the username is wrong, I am catching the error.


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DATABASE_EXERCISES")

while True:
    try:
        DB_USER = input(f"Please input your user: ") # For this case the correct user is: root

        # Build database URL
        DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        # Create the engine
        engine = create_engine(DATABASE_URL)

        # Reflect the existing database... so we don't need to define all existing tables
        metadata = MetaData()
        metadata.reflect(bind=engine)

        # Access the 'film' and 'category' tables
        film_table = metadata.tables['film']
        category_table = metadata.tables['category']

        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Print some info from each table
        with engine.connect() as conn:
            print("Films:")
            result = conn.execute(film_table.select()).fetchall()
            for row in result:
                print(row.title + ": "+row.description)

            print("\nCategories:")
            result = conn.execute(category_table.select()).fetchall()
            for row in result:
                last_update = row.last_update.strftime("%Y-%m-%d %H:%M:%S")
                print(f"{row.category_id}: {row.name} - Last updated on {last_update}")
            break

    except Exception as e:
        print("❌ Something went wrong:")
        print(f"   Type: {type(e).__name__}")
        print(f"   Details: {e}")
        print("Please try again...\n")