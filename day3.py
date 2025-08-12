'''
Day 3 — First API Call (GitHub API)

    Goal: Learn to fetch JSON data from an API.

    Tasks:

        Read GitHub API docs: GitHub REST API

        Fetch data for any GitHub username

        Parse JSON & print specific fields
'''

import requests

username = 'maninderjeet-singh-vo'
url = f'https://api.github.com/users/{username}'
response = requests.get(url)
data = response.json()

# # print(data)

# # for key, value in data.items():
# #     print(f"{key}: {value}")

print(f"Name: {data['name']}")
print(f"Public Repos: {data['public_repos']}")
print(f"Followers: {data['followers']}")

# Now, let’s try to get a webpage. For this example, let’s get GitHub’s public timeline:

# response = requests.post('https://jsonplaceholder.typicode.com/posts')
# posts = response.json()

# print( type(posts))

# for post in posts:
#     print(f"{post['title']}")

# response = requests.post('https://jsonplaceholder.typicode.com/posts',data={'title':'Maninderjeet Singh','body':'This is a test post','userId':1})
# data = response.json()

# print( data)

# # for post in posts:
# #     print(f"{post['title']}")