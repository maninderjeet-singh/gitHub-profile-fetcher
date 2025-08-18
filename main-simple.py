import sqlite3
import requests

def showUserDetail(user):
    print('-'*100)
    print(f"Username: {user['userName']}")
    print(f"Name: {user['name']}")
    print(f"url: {user['url']}")
    print(f"avatar_url: {user['avatar_url']}")
    print(f"public_repos: {user['public_repos']}")
    print(f"followers: {user['followers']}")
    print(f"joined_at: {user['joined_at']}")
    print('-'*100)

def userFetcher():
    userInputRequired = True
    while(userInputRequired == True):
        userName = input('Enter username: ')
        if userName == '':
            print('Username cannot be empty')
        else:
            userInputRequired = False

    conn = sqlite3.connect('github_automation.db')
    # enables dict-like row acces
    conn.row_factory = sqlite3.Row  

    cursor = conn.cursor()

    cursor.execute('''
        create table if not exists profiles(
            username TEXT PRIMARY KEY,
            name text,
            url text,
            avatar_url text,
            public_repos integer,
            followers integer,
            joined_at text
        )
    ''')

    result = cursor.execute('select * from profiles where username=?',(userName,)).fetchone()

    if(result):
        print('User found from DB successfully')
        result = dict(result)
        name = result['name']
        url = result['url']
        avatar_url = result['avatar_url']
        public_repos = result['public_repos']
        followers = result['followers']
        joined_at = result['joined_at']
        showUserDetail({'userName':userName,'name':name,'url':url,'avatar_url':avatar_url,'public_repos':public_repos,'followers':followers,'joined_at':joined_at})
        
    else:
        print('Sorry, We don\'t have details for that username')
        search = input('Do you want to search from github? (yes/no) (default: no): ')
        search = search.lower()
        if(search == 'yes'):
            print('searching username on github')
            response = requests.get(f'https://api.github.com/users/{userName}')
            if response.status_code == 404:
                print('Username not found on GitHub.')
                return
            result = response.json()

            # if 'status' in  result and result['status'] == '404':
            if result.get('message') == 'Not Found' or result.get('status')  == '404':
                print('Username not found on github.')
                return
            else:
                print('\nGreat!, Username found on github.')
                name = result.get('name','N/A')
                url = result.get('url','')
                avatar_url = result.get('avatar_url','')
                public_repos = result.get('public_repos',0)
                followers = result.get('followers',0)
                joined_at = result.get('created_at','')

                showUserDetail({'userName':userName,'name':name,'url':url,'avatar_url':avatar_url,'public_repos':public_repos,'followers':followers,'joined_at':joined_at})

                saveInput = input('Do you want to store information in DB for future? yes/no (default: yes): ')
                if not saveInput or saveInput.lower() == 'yes':
                    cursor.execute('insert into profiles values(?,?,?,?,?,?,?)',(userName,name,url,avatar_url,public_repos,followers,joined_at))
                    conn.commit()
                else:
                    print('not saved.')
# end of showUserDetail function

while True:
    userFetcher()
    again = input('Do you want to search another username? (yes/no, default: no): ').lower()
    if(again != 'yes'):
        break
    

print('Thanks for using Github Profile Fetcher Tool.')
