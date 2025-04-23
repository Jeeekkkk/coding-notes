# Setting Up a New Project with GitHub

## 1. Create the Repository (GitHub)
- Create a new repository in GitHub UI
- Leave **"Initialize with README"** unchecked (you'll create it locally)
- Do not add `.gitignore` or license — manage these from the local repo

## 2. Prepare Local Project Folder
Create the project directory locally and move into it:

`mkdir project-name`  
`cd project-name`

Create a virtual environment:

`python -m venv venv`

Activate it (PowerShell):

`.\venv\Scripts\Activate.ps1`

Activate it (macOS/Linux):

`source venv/bin/activate`

## 3. Create Local Files
Create any files you'll use:

- `README.md` – describes the project
- `.gitignore` – prevent versioning unwanted files like `venv/`


## 4. Initialize Git and Connect to Remote
Initialize Git:

`git init`

Create initial commit:

`git add .`  
`git commit -m "Initial commit"`

Link to GitHub:

`git remote add origin https://github.com/your-username/your-repo-name.git`

Rename the branch to main (if needed):

`git branch -M main`

Push:

`git push -u origin main`

## 5. Track Dependencies (if using Python)
Install packages as needed:

`pip install requests`

Save them:

`pip freeze > requirements.txt`

Ensure you update this after installing new packages.

## 8. Notes
- Never push secrets or `.env` files
- Always add `venv/` to `.gitignore`
- Only commit files that are necessary for running or maintaining the project
