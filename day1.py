'''
Day 1 — Python Refresher & Setup
    Goal: Set up tools, refresh syntax, and get familiar with best practices.

    Tasks:

    Install Python 3.12+ → Download

    Install VS Code → Download

    Install Git → Download

    Create GitHub account if you don’t have one → Sign Up

    Create a new folder week1_github_profile_fetcher

    Create & activate virtual environment:

    bash
    Copy
    Edit
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    Install requests + SQLite3 (SQLite is built-in, so no install needed)

    bash
    Copy
    Edit
    pip install requests
'''

name='Maninderjeet Singh'
age = 30
skills = ['HTML','CSS','Bootstrap','JavaScript','jQuery','MySql','PHP','Laravel']

print(f"My name is {name}, age {age} and I know {', '.join(skills)}")