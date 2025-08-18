# GitHub Profile Fetcher 🐙

A simple Python CLI tool that fetches and stores **GitHub user profile details**.
It first checks a local **SQLite database** for cached profiles and, if not found, fetches from the **GitHub API**.

## 🚀 Features

* Fetch GitHub user details (name, avatar, repos, followers, join date).
* Cache results in **SQLite database** for faster future lookups.
* User-friendly CLI prompts.
* Option to **skip saving** fetched data.
* Prevents empty username input.
* Handles "user not found" errors gracefully.

## 🛠️ Tech Stack

* **Python 3.x**
* **SQLite3** (for local storage)
* **Requests** library (for API calls)

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/github-profile-fetcher.git
   cd github-profile-fetcher
   ```

2. Install dependencies (if not already installed):

   ```bash
   pip install requests
   ```

3. Run the script:

   ```bash
   python github_fetcher.py
   ```

## ⚙️ Usage

1. Enter a GitHub username when prompted.
2. If details are cached → shows instantly.
3. If not cached → asks permission to fetch from GitHub API.
4. Optionally save fetched details for future queries.
5. Repeat until you choose to exit.

### Example Run

```bash
Enter username: torvalds
User found from DB successfully
----------------------------------------------------------------------------------------------------
Username: torvalds
Name: Linus Torvalds
url: https://api.github.com/users/torvalds
avatar_url: https://avatars.githubusercontent.com/u/1024025?v=4
public_repos: 6
followers: 260000
joined_at: 2011-09-03T15:26:22Z
----------------------------------------------------------------------------------------------------
```

## 🗂️ Database Schema

Table: **profiles**

| Column        | Type    | Description            |
| ------------- | ------- | ---------------------- |
| username      | TEXT PK | GitHub username        |
| name          | TEXT    | Full name              |
| url           | TEXT    | GitHub API URL         |
| avatar\_url   | TEXT    | Profile picture        |
| public\_repos | INTEGER | Number of public repos |
| followers     | INTEGER | Number of followers    |
| joined\_at    | TEXT    | Account creation date  |

## 🔑 Notes

* GitHub API has a **rate limit** of 60 requests/hour (for unauthenticated users).
* Consider adding authentication (personal access token) if you plan to scale.

## 📌 Future Improvements

* Add GitHub token authentication (to increase API limits).
* Store repos & bio details.
* Build a simple Flask/Django frontend.
* Export data as CSV/JSON.

---
