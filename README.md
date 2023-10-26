# Demo

Demo project to highlight possible django bug.

- Needs to run in python 3.11
```
mkvirtualenv -p `which python3.11` -r requirements.txt tutorial-py311
```


[Issue](https://code.djangoproject.com/ticket/34930)

```
./manage.py test --parallel
```