# GitHub Profile Fetcher

A Python command-line tool that allows you to **fetch GitHub user profiles** using the GitHub REST API and store results in a **SQLite database** for offline access. The project uses [Rich](https://github.com/Textualize/rich) for a modern, colorful, and user-friendly terminal experience.

---

## ✨ Features

✅ Fetch GitHub user details (Name, Repos, Followers, Join date, Avatar, etc.)
✅ Store user profiles in a local **SQLite database**
✅ Retrieve details from the database if the user already exists
✅ Graceful error handling with **try/except**
✅ Beautiful CLI output using **Rich** (tables, spinners, colors)
✅ Option to search GitHub again if not found in DB

---

## 🛠️ Technologies Used

* **Python 3.x**
* **SQLite3** (lightweight database)
* **Requests** (for API calls)
* **Rich** (for modern CLI formatting & spinners)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/maninderjeet-singh/gitHub-profile-fetcher.git
cd gitHub-profile-fetcher
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install requests rich
```

---

## ▶️ Usage

Run the script from the terminal:

```bash
python main.py
```

You’ll see a colorful welcome banner, and then you can:

* Enter a **GitHub username** to search.
* If found in **local DB**, details are displayed instantly.
* If not in DB, you’ll be asked whether to fetch from GitHub.
* Optionally, save the details for future use.

---

## 📸 Example Output

```text
==================================================
              GitHub Profile Fetcher  
==================================================

Enter GitHub username: octocat

✅ User found on GitHub.

┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field         ┃ Value                         ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ UserName      │ octocat                       │
│ Name          │ The Octocat                   │
│ URL           │ https://api.github.com/users/ │
│ Avatar        │ https://avatars.githubusercontent.com/u/583231?v=4 │
│ Public Repos  │ 8                             │
│ Followers     │ 9380                          │
│ Joined At     │ 2011-01-25T18:44:36Z          │
└───────────────┴───────────────────────────────┘
```

---

## 🗄️ Database

The script uses **SQLite** (`github_automation.db`) to store user details:

| username | name | url | avatar\_url | public\_repos | followers | joined\_at |
| -------- | ---- | --- | ----------- | ------------- | --------- | ---------- |

This means you don’t need to call the API again for the same user — it fetches from DB.

---

## ⚠️ Error Handling

* **Invalid usernames** → Shown in red
* **Network/API errors** → Properly displayed with error message
* **Database errors** → Caught using `try/except`

---

## 📌 Future Improvements

* Add option to **display avatar image in terminal** (using `PIL` or `rich.image`).
* Implement **caching with expiry**.
* Allow **searching multiple users in batch**.

---

## 👨‍💻 Author

Built with ❤️ in Python by Maninderjeet Singh

---
