'''
Day 5 — Automation Mini Task
Goal: Automate fetching & storing profiles.

Tasks:

Write a script that:

Reads usernames from a list

Fetches their GitHub data

Stores them in SQLite
'''
import requests
import sqlite3

username = input('Enter username: ')

response = requests.get(f'https://api.github.com/users/{username}')
data = response.json()

# print(data)
# exit()
# print(f"{data['name']},{data['url']},{data['avatar_url']},{data['public_repos']},{data['followers']},{data['created_at']}")
name = data['name']
url = data['url']
avatar_url = data['avatar_url']
public_repos = data['public_repos']
followers = data['followers']
created_at = data['created_at']

print(f"Name: {name}")
# exit()
conn = sqlite3.connect('github_automation.db')
cursor = conn.cursor()

cursor.execute('''
	create table if not exists profiles(
		name text primary key,
		url text,
		avatar_url text,
		public_repos integer,
		followers integer,
		joined_at text
	)
''')

cursor.execute("insert or replace into profiles values(?,?,?,?,?,?)",(name,url,avatar_url,public_repos,followers,created_at))

rows = cursor.execute("select * from profiles").fetchall()

print(rows)