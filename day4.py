'''
Day 4 — Storing API Data in SQLite
Goal: Save API data for later use.

Tasks:

Create SQLite DB & table for GitHub profiles

Insert API data into DB

Query & display stored profiles

'''

import sqlite3

# conn = sqlite3.connect('github_profiles.db')
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS profiles (
#     username TEXT PRIMARY KEY,
#     name TEXT,
#     public_repos INTEGER,
#     followers INTEGER
# )
# """)

# cursor.execute("INSERT OR REPLACE INTO profiles VALUES (?, ?, ?, ?)",
#                ("octocat", "The Octocat", 8, 100))
# conn.commit()

# rows = cursor.execute("SELECT * FROM profiles").fetchall()
# print(rows)
# conn.close()

conn = sqlite3.connect('github_profiles.db')
cursor = conn.cursor()

cursor.execute('''
create table if not exists new_profiles (
    username text primary key,
    name text,
    public_repos integer,
    followers integer
)
''')

cursor.execute("insert or replace into new_profiles values(?, ?, ?, ?)", ('octocat3', 'The Octocat3', 5, 500))

conn.commit()

rows = cursor.execute("select * from new_profiles").fetchall()
print(rows)
conn.close()