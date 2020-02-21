# nod32keys_bot
Bot for parsing keys Eset NOD32. Written in Python 3.8.

## File Description
```
│── config-sample  # Token, proxy
│── cron.py # Cron task for automatic update keys
│── requirements.txt  # Dependencies
│── run.py  # Bot launch
│── utils.py  # Main functions
```

### Install
* Install the dependencies:
```
pip install -r requirements.txt
```
* Make new **config.py** for ourselves from **config-sample**.
* Add a cron task to the server, put the execution every 8 hours.