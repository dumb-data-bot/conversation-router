Conversation Manager
===
## Setup
```
pip install -r requirements.txt
```

## Execution
```
gunicorn -b :6677 router:app  --log-level DEBUG
```

![flow chart](images/flow.png)
