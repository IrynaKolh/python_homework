import sqlite3
import os

""" 
Task 1: Create a New SQLite Database
Write code to connect to a new SQLite database, ../db/magazines.db and to close the connection.
Execute the script and confirm the database file is created. Note: All SQL statements should be executed within a try block, 
followed by a corresponing except block, because any SQL statement can cause an exception to be raised.

"""
os.makedirs("../db", exist_ok=True)

def create_connection():
    try:
        conn = sqlite3.connect("../db/magazines.db")
        print("Database created and connected successfully.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return None

def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed.")

# if __name__ == "__main__":
#     conn = create_connection()
#     close_connection(conn)


""" 
Task 2: Define Database Structure
We have publishers that publish magazines.  Each publisher has a unique name, and so does each magazine.  
There is a one-to-many relationship between publishers and magazines.  We also have subscribers, and each subscriber has a name and an address.  
We have a many-to-many association between subscribers and magazines, because a subscriber may subscribe to several magazines, 
and a magazine may have many subscribers.  So, we have a join table called subscriptions.  
The subscriptions table also stores the expiration_date (a string) for the subscription.  
All the names, the address, and the expiration_date must be non-null.
1. Think for a minute.  There is a one-to-many relationship between publishers and magazines.  
Which table has a foreign key? Where does the foreigh key point?  How about the subscriptions table: What foreigh keys does it have?
2. Add SQL statements to sql_intro.py that create the following tables:
    publishers
    magazines
    subscribers
    subscriptions Be sure to include the columns you need in each, with the right data types, with UNIQUE and NOT NULL constraints as needed, 
        and with foreign keys as needed. You can reuse column names if you choose, i.e. you might have a name column for publishers and 
        a name column for magazines. By the way, if you mess up this or the following steps, you can just delete db/magazines.db.
3. Open the db/magazines.db file in VSCode to confirm that the tables are created.

"""

def create_tables(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
            )
        """)

        print("Tables created successfully.")

    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

# if __name__ == "__main__":
#     conn = create_connection()
#     if conn:
#         conn.execute("PRAGMA foreign_keys = 1")
#         create_tables(conn)
#         close_connection(conn)


"""
Task 3: Populate Tables with Data
1. Add the following line to sql_intro.py, right after the statement that connects to the database:
        conn.execute("PRAGMA foreign_keys = 1")
    This line tells SQLite to make sure the foreign keys are valid.
2. Create functions, one for each of the tables, to add entries. Include code to handle exceptions as needed, and to ensure that 
    there is no duplication of information. The subscribers name and address columns don't have unique values -- you might have several subscribers 
    with the same name -- but when creating a subscriber you should check that you don't already have an entry 
    where BOTH the name and the address are the same as for the one you are trying to create.
3. Add code to the main line of your program to populate each of the 4 tables with at least 3 entries. Don't forget the commit!
4. Run the program several times. View the database to ensure that you are creating the right information, without duplication.
"""

def add_publisher(conn, name):
    try:
        conn.execute("INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.Error as e:
        print(f"Error adding publisher: {e}")

def add_magazine(conn, name, publisher_name):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        publisher = cursor.fetchone()
        if publisher:
            conn.execute("INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher[0]))
    except sqlite3.Error as e:
        print(f"Error adding magazine: {e}")

def add_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if not cursor.fetchone():
            conn.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")

def add_subscription(conn, subscriber_name, magazine_name, expiration_date):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
        subscriber = cursor.fetchone()

        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        magazine = cursor.fetchone()

        if subscriber and magazine:
            conn.execute("""
                INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
            """, (subscriber[0], magazine[0], expiration_date))

    except sqlite3.Error as e:
        print(f"Error adding subscription: {e}")

# if __name__ == "__main__":
#     conn = create_connection()
#     if conn:
#         conn.execute("PRAGMA foreign_keys = 1")
#         create_tables(conn)

#         # Populate
#         add_publisher(conn, "TechPress")
#         add_publisher(conn, "HealthWorld")
#         add_publisher(conn, "NatureMedia")

#         add_magazine(conn, "Tech Today", "TechPress")
#         add_magazine(conn, "Healthy Living", "HealthWorld")
#         add_magazine(conn, "Nature Weekly", "NatureMedia")

#         add_subscriber(conn, "Alice Smith", "123 Maple Street")
#         add_subscriber(conn, "Bob Johnson", "456 Oak Avenue")
#         add_subscriber(conn, "Carol Taylor", "789 Pine Road")

#         add_subscription(conn, "Alice Smith", "Tech Today", "2025-12-31")
#         add_subscription(conn, "Bob Johnson", "Nature Weekly", "2025-11-15")
#         add_subscription(conn, "Carol Taylor", "Healthy Living", "2025-10-01")

#         conn.commit()
#         close_connection(conn)

"""
Task 4: Write SQL Queries
Write a query to retrieve all information from the subscribers table.
Write a query to retrieve all magazines sorted by name.
Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
Add these queries to your script. For each, print out all the rows returned by the query.
"""

def show_all_subscribers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers")
    rows = cursor.fetchall()
    print("\nAll subscribers:")
    for row in rows:
        print(row)

def show_all_magazines(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    rows = cursor.fetchall()
    print("\nAll magazines:")
    for row in rows:
        print(row)

def show_magazines_by_publisher(conn, publisher_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.publisher_id
        WHERE p.name = ?
    """, (publisher_name,))
    rows = cursor.fetchall()
    print(f"\nMagazines by {publisher_name}:")
    for row in rows:
        print(row)

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        show_all_subscribers(conn)
        show_all_magazines(conn)
        show_magazines_by_publisher(conn, "TechPress")
        close_connection(conn)
