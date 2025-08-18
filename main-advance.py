import sqlite3
import json
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

console.print("=" * 50, style="bold cyan")
console.print("              GitHub Profile Fetcher  ", style="bold yellow")
console.print("=" * 50, style="bold cyan")

def get_db_connection():
    conn = sqlite3.connect('github_automation.db')
    conn.row_factory = sqlite3.Row  
    return conn

def showUserDetail(user):

    table = Table(title=f"GitHub Profile", style="cyan")
    table.add_column("Field", style="bold green")
    table.add_column("Value", style="bold yellow")

    table.add_row("UserName", user['userName'] or "N/A")
    table.add_row("Name", user['name'] or "N/A")
    table.add_row("URL", user['url'])
    table.add_row("Avatar", user['avatar_url'])
    table.add_row("Public Repos", str(user['public_repos']))
    table.add_row("Followers", str(user['followers']))
    table.add_row("Joined At", user['joined_at'])

    console.print(table)

def checkUserInDB(userName): 
    try:
        conn = get_db_connection()
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
            console.print("\n[green]User found from DB successfully[/green]\n")
            result = dict(result)
            name = result['name']
            url = result['url']
            avatar_url = result['avatar_url']
            public_repos = result['public_repos']
            followers = result['followers']
            joined_at = result['joined_at']

            user = {'userName':userName,'name':name,'url':url,'avatar_url':avatar_url,'public_repos':public_repos,'followers':followers,'joined_at':joined_at}
            showUserDetail(user)
            conn.close()
            return user
            
        else:
            console.print('[red]Sorry, We don\'t have details for that username[/red]')
            return False
    except sqlite3.Error as e:
        # Catch database errors
        console.print(f"[red] Database error:[/red] {e}")

    except Exception as e:
        # Catch other errors
        console.print(f"[red] Unexpected error:[/red] {e}")

    finally:
        # Always close connection
        if conn:
            conn.close()
            # console.print("[yellow]Connection closed[/yellow]")


def checkUserOnGitHub(userName):
    with console.status("[bold cyan]Fetching data from GitHub...[/bold cyan]", spinner="dots"):
        try:
            response = requests.get(f'https://api.github.com/users/{userName}', timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            console.print(f"[red] Error fetching data: {e} [/red]")
            return
    if response.status_code == 404:
        print('Username not found on GitHub.')
        return
    result = response.json()

    if result.get('message') == 'Not Found' or result.get('status')  == '404':
        console.print("\n[red]Username not found on GitHub.[/red]\n")
        return
    else:
        console.print("\n[green]Username found on GitHub.[/green]\n")
        name = result.get('name','N/A')
        url = result.get('url','')
        avatar_url = result.get('avatar_url','')
        public_repos = result.get('public_repos',0)
        followers = result.get('followers',0)
        joined_at = result.get('created_at','')

        showUserDetail({'userName':userName,'name':name,'url':url,'avatar_url':avatar_url,'public_repos':public_repos,'followers':followers,'joined_at':joined_at})

        saveInput = console.input("[bold cyan] Do you want to store information in DB for future? yes/no (default: yes): [/bold cyan] ").strip().lower()
        if not saveInput or saveInput == 'yes':
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('insert into profiles values(?,?,?,?,?,?,?)',(userName,name,url,avatar_url,public_repos,followers,joined_at))
                conn.commit()
                conn.close()
                console.print("\n[green] Information stored suceessfully.[/green]\n")
            except sqlite3.Error as e:
                # Catch database errors
                console.print(f"[red] Database error:[/red] {e}")

            except Exception as e:
                # Catch other errors
                console.print(f"[red] Unexpected error:[/red] {e}")

            finally:
                # Always close connection
                if conn:
                    conn.close()
                    # console.print("[yellow]Connection closed[/yellow]")
                else:
                    console.print("\n[red] Information not stored.[/red]\n")

def userFetcher():
    while True:
        userName = console.input("[bold cyan] Enter GitHub username: [/bold cyan] ").strip()
        if not userName:
            console.print("[bold red]Error: [/bold red] [red]Username cannot be empty[/red]", style="yellow")
            continue

        userExist = checkUserInDB(userName)
        if not userExist:
            search = console.input("[bold cyan] Do you want to search from github? (yes/no) (default: no): [/bold cyan] ").strip().lower()
            if(search == 'yes'):
                checkUserOnGitHub(userName)
        break

# while True:
#     userFetcher()
#     again = console.input("[bold cyan] Do you want to search another username? (yes/no, default: no):  [/bold cyan] ").strip().lower()
#     if(again != 'yes'):
#         break
# console.print("\n[green] Thanks for using Github Profile Fetcher Tool..[/green]\n")
    
if __name__ == "__main__":
    while True:
        userFetcher()
        again = console.input("[bold cyan]Do you want to search another username? (yes/no, default: no): [/bold cyan]").strip().lower()
        if again != "yes":
            break
    console.print("\n[green]Thanks for using GitHub Profile Fetcher Tool..[/green]\n")
