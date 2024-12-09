# Portfolio

## FOR WHAT REASON?
This is my portfolio project that will also serve as my main portfolio.

## TO RUN AND INITIALIZE

# linux
```sh
    cd <project-name>
    python3 -m venv venv

    #to activate
    source venv/bin/activate
```

# Windows
```powershell
    cd <project-name>
    python -m venv venv
    .\venv\Scripts\activate
```

# install required Dependencies 
go to the root of the file with (in requirements.txt)
```powershell   
    pip install -r requirements.txt
```

# to start
```powershell
    cd .\portfolio\
    python manage.py runserver <port>
```

# NOTES
if you are in mars code you need to have 
in settings.py

the url's that i use in here is my url use the url that marscode will give you
```python
    CSRF_TRUSTED_ORIGINS = [
        # for origin and csrf_token in the forms
        'https://ftvd7g7t-04u2tkb8-ok58ctvccia8.ac4-preview.marscode.dev'
    ]
    ALLOWED_HOSTS = [
        # to allow anyone running
        '*'
        # name of the website with https
        "https://ftvd7g7t-04u2tkb8-ok58ctvccia8.ac4-preview.marscode.dev", 
        # with no https
        "ftvd7g7t-04u2tkb8-ok58ctvccia8.ac4-preview.marscode.dev"
    ]
```

in `launch.json` that marscode will provide in order to run just paste this 
```json
    // launch.json is for marscode 
    {
      "version": "0.0.1",
      "configurations": [
        {
          "name": "Start Application",
          "type": "debugpy",
          "request": "launch",
          "program": "portfolio/manage.py",
          "args": [
              "runserver",
              "0.0.0.0:8080"
          ],
          "console": "internalConsole",
          "justMyCode": true
      }
      ]
    }
``` 