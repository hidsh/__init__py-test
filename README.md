# __init__py-test

An Example of using packages and `__init__.py` in Python

# Folder tree

```
$ tree .
.
|-- main.py
|-- my_package
|   |-- __init__.py
|   `-- module.py
`-- tests.py
```


# Calling function in a package
```
$ python main.py
hoge!!!
```


# Unit test

```
$ python tests.py
hoge!!!
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
  1 from my_package import say_hoge

OK
```
