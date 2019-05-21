Conversation Manager
===
The router is used to connect all the rest components.

## APIs

### `GET /`
Used for testing purpose.

### `GET/POST /messenger`
Web-hook to be called by messenger.

### `POST /backend`
Used by session manager/user workspace to initiate a message to user.

## Setup
```
pip install -r requirements.txt
```

## Execution
```
gunicorn -b :6677 router:app  --log-level DEBUG
```

![flow chart](images/flow.png)
