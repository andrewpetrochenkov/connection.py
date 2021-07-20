[![](https://img.shields.io/badge/released-2021.7.20-green.svg?longCache=True)](https://pypi.org/project/connection/)
[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

### Installation
```bash
$ pip install connection
```

### Examples
```python
>>> import connection
>>> connection.check()
True
```

timeout
```python
>>> connection.check(timeout=2)
```

url
```python
>>> connection.check(url='https://github.com/')
```

