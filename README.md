# twistedxmlrpc
XMLRPC with twisted deployed to heroku


## Local
```
> virtualenv venv
> source venv/bin/activate
> pip install -r requirements.txt
> twistd -y service.tac
> export DEBUG=True
> python tests/test.py

```

## Heroku
```
> heroku apps:create xmlrpctest
> heroku git:remote -a xmlrpctest
> git push heroku master
> export DEBUG=False
> python tests/tests.py
```