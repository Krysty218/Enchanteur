import sqlite3

# Step 2: Connect to the SQLite3 database (or create it if it doesn't exist)
conn = sqlite3.connect('myproject/db.sqlite3')  # 'example.db' is the database file

# Step 3: Create a cursor object
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results
tables = cursor.fetchall()

# Print all table names
print("Tables in the database:")
for table in tables:
    print(table[0])

# Rename the table
# Insert a row (1, 'lav', 0) into the users table
insert_query = "INSERT INTO events_user (id, username, typ) VALUES (?, ?, ?)"
cursor.execute(insert_query, (1, 'lav', 0))

# Commit the transaction to save the changes
conn.commit()

# Execute a SELECT statement
cursor.execute('SELECT * FROM events_user')

# Fetch all rows
rows = cursor.fetchall()
# Process the rows
for row in rows:
    print(row)


print("Table created successfully.")

conn.close()