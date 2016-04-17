## Algorithms and data structures implemented in Python 3

- graphs and graph search algorithms
- sorts
- search data structures
- lists, stacks, queues
- some other algorithms and types

I am working on tests and assets for these files. Unit tests are in the `tests` directory, and some modules have doc tests. Some data structures make assertions or have methods for making assertions that check invariants.

#### Unit tests
`python -m unittest discover tests -v`

#### Doc tests
`python <module.py> -v`

#### Python Path
To ensure that Python can import the modules in this package, the parent directory of the package has to be in the `PYTHONPATH`. Instead of doing this in `.bash_profile` or another startup script, you can do it in the activate script of a __virtualenv__: `$HOME/.virtualenvs/{virtualenv}/bin/activate`.

~~~sh
unset PYTHONPATH
PYTHONPATH="/Users/kylebebak/Dropbox/Code/Python/_modules"
export PYTHONPATH
~~~
