# Install Django

## Step 1 : Create a virtual environment
```sh
python -m venv env
```
## Step 2 : Activate the virtual environment:
- On Windows cmd:
```sh
env\Scripts\activate.bat
```
- On Windows PowerShell:
```sh
env/Scripts/activate.ps1
```

For PowerShell you may have to allow scripts to run using this commande on PowerShell(Admin): 
```sh 
set-executionpolicy RemoteSigned
 ``` 

- On Mac or Linux:
```sh
source env/bin/activate
```

### To deactivate the virtual environment:
```sh
deactivate
```

## Step 3: install Django
```sh
pip install django
```

By installing Django, other packages needed by Django are also installed.
Keep a trace of all the packages needed in a file :
```sh
pip freeze > requirements.txt
```

# Configure a new project with Django

```sh
django-admin startproject myproject
```