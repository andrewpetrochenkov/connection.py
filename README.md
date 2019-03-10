<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/connection.svg?longCache=True)](https://pypi.org/project/connection/)
[![](https://img.shields.io/pypi/v/connection.svg?maxAge=3600)](https://pypi.org/project/connection/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/connection.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/connection.py/)

#### Installation
```bash
$ [sudo] pip install connection
```

#### Functions
function|`__doc__`
-|-
`connection.check(timeout=None)` |return True if connection is ok, else False

#### Examples
```python
>>> import connection
>>> connection.check()
True
```

timeout
```python
>>> connection.check(timeout=2)
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>