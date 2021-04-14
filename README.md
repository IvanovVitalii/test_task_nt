Python file functions.py contains 6 functions.

Your task is to create a back-end service with one end-point (f.e. /start) with the following properties:

- [x] It can receive a REST GET request with the following structure (f.e):

{'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}

where 'data' - a list of numbers (float, int) of undefined length, 'rule' - a list (sequence) of rules to be executed upon the 'data' list.

- [x] Your service should take a sentence of 'rules', match it with functions from the functions.py, and append functions to the 'data' list in the same order.

- [x] The order of rules may vary, repeat, but contain only provided 6 functions.

- [x] The response should be as following (f.e.):

{'result' : [5.1, 5.4, 5.9, 6.6, 7.5]}

- [x] Your solution should be scalable for any number of functions in functions.py (in theory).

- [x] The resulting server should be put in a docker container.

    {'data':
        {
        '1': 1,
        '2': 2,
        '3': 3
        },
     'rule':
        {
        '1': ['a','b','c'],
        '2': ['a','b','c','d','e','f'],
        '3':['b','c','d','e']
        }
    }

- [x] Extra task: Propose your own way to pass a sequence of rules instead of a 'rule' list.


  Вспомогательный материал:
```python
def fun_a(x):
    return x ** 2


def fun_b(x):
    return 2 * x + 1


def fun_c(x):
    return x - 1


def fun_d(x):
    return x / 10


def fun_e(x):
    return x + 10


def fun_f(x):
    return x/2
```


