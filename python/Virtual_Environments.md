# Py Virtual Environments
## Why?
- Isolates dependencies per project
- Prevents version conflicts
- Keeps global Python installation clean
- Essential for deployment, sharing, or serious development

## When?
- Always, unless running short scripts with no external packages
- Required when:
  - Installing packages with `pip`
  - Preparing a project to share
  - Working on multiple projects that may have different requirements

## Creating and Activating a Virtual Environment
### Create the environment
Windows and macOS/Linux
`python -m venv venv`

## .gitignore Configuration
Disable venev from git
`echo "venv/" >> .gitignore`

### Activate the environment
PowerShell – Windows
`.\venv\Scripts\Activate.ps1`

macOS / Linux / WSL
`source venv/bin/activate`

## After Activation
### Install packages using pip
`pip install requests`
 Always run `pip freeze > requirements.txt` after installing a package that is not in testing

### Save current packages to a requirements.txt file
Only when venv is activated, and always after intalling new packages
`pip freeze > requirements.txt`

### Install from an existing requirements.txt
`pip install -r requirements.txt`

## Deactivating the Environment
`deactivate`

## Notes
- Use one virtual environment per project
- Do not push the venv/ folder to GitHub
- Naming can vary (venv, .venv, env) — be consistent across projects
- Ensure the editor is using the virtual environment interpreter
