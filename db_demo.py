import psycopg2

'''Solution for FATAL Connection Error'''
''' https://stackabuse.com/working-with-postgresql-in-python/ '''
con = psycopg2.connect(
    host = "127.0.0.1",
    database =  "postgres",
    user = "postgres",
    password = "postgres",
    port = "5432")
print("Database opened successfully")

# Create a cursor
cur = con.cursor()

#execute query
cur.execute('''CREATE TABLE STUDENT(
    ADMISSION INT PRIMARY KEY   NOT NULL,
    NAME    TEXT    NOT NULL,
    AGE     INT     NOT NULL,
    COURSE  CHAR(50));''')
print("Table created successfully")

#cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')")

#rows = cur.fetchall()

#for r in rows:
#    print(f"id {r[10]} name {r[1]}")

# Close the cursor
cur.close()

# Close the connection
con.commit()
print("Record inserted successfully")
con.close()