<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/50069473/179423541-5c3510a0-0000-47f4-af16-9266003728d1.png">
</p>

<h1 align="center">
 🪄 🌟 pretty-match 
</h1>
<p align="center">
  <a href="https://github.com/skonik/pretty-match/actions/workflows/test.yml">
    <img alt="Test" src="https://github.com/skonik/pretty-match/actions/workflows/test.yml/badge.svg">
  </a>
  <a href="https://github.com/skonik/pretty-match" target="_blank">
    <img src="https://img.shields.io/badge/python-3.10-blue" alt="python">
  </a>
</p>

A set of utils to be used with match-case statements.

```python
from pretty_match import results
from pretty_match.attrs import FirstNoneAttr, AttrIsNone
from pretty_match.comparable import Number

user = User(balance=1500)
product = Product(price=150)
match Number(user.balance).compare(product.price):
    case results.Less:
        raise NotEnoughMoney
    case results.Greater | results.Equal:
        process_transaction(user, product)

query = Query(token='test', start=None, end=2)
attrs_to_check = ['token', 'start', 'end']
match FirstNoneAttr(*attrs_to_check, instance=query):
    case AttrIsNone(name='token'):
        print('token required!')
    case AttrIsNone(name='start'):
        print('start required!')
    case AttrIsNone(name='end'):
        print('end required!')
```

## Requirements
* python 3.10


## Development and contribution
Feel free to contribute.
To start development use the following commands:

1. `pre-commit install`

2. `poetry install`

Now you are ready to contribue and develop new feature.

Additional commands:

* `make lint` - run linters and checks;
* `make test` - run tests;
