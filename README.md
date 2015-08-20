# GitHub OAuth2 authentication demo project

## Launch the demo

### Requirements

* python 2.7
* virtualenv

First clone this repository.

### Launch the UI

1. open a new terminal console
1. cd to the `ui` folder of the repository
1. run `python -m SimpleHTTPServer 8000`

### Launch the API

1. open a new terminal console
1. cd to the `api` folder of the repository
1. run `virtualenv env`
1. run `source env/bin/activate`
1. run `pip install -r requirements.txt`
1. run `gunicorn -b 0.0.0.0:5000 api:app`

### Try it

1. Open your webbrower on http://localhost:8000
1. Have fun !
