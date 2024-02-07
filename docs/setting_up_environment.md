# Setting up environment

Before properly starting the project, it is important to setup the environment.

## Installing python
First things first, to install python and manage different versions of it, 
it was used pyenv.

## Creating repository
After python installed, it was created the repository, adding a .gitignore file,
to exclude py_cache and .env files.

Also, it was created a virtual env to use python locally: ``python3 -m venv .venv``. </br>

For initialize the env, it was used: ``source .venv/bin/activate``.

And the dependencies were registered in the development process by using, ``pip3 freeze > requirements.txt``.

Doubts, check [env documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

## Formatter
For keeping a standard pattern on code, it was used pylint, also pre-commit to check on always pylint rules before pushing commits.

Installation command: ``pip3 install pylint``.
Initialize config file command: ``pylint --generate-rcfile > .pylintrc``.

After initialized config file, below <b>[Main]</b>, it was disabled some rules, such as:

```py
disable=
    C0114, # Missing-module-docstring
    C0115, # Missing-class-docstring
    C0116, # Missing-function-docstring
    C0117, # Catching too general excepction Exception
```
---

Using pre-commit to check pylint rules before every commit.

Installation: ``pip3 install pre-commit``.
Create a file, .pre-commit-config.yaml, and set it up:
```
repos:
  - repo: local
    hooks:
      - id: pylint
        name: pylint
        entry: pylint
        language: system
        types: [python]
        args: 
          [
            "-rn", # Only display messages
            "-sn", # Don't display the score
            "--rcfile=pylintrc", # Link to your config file
            "--load-plugins=pylint.extensions.docparams", # Load an extension
          ]
```
Link to git: ```pre-commit install``.

## Requirements
After all set up, since .venv packages is not committed, it is necessary
to have all packages described somewhere, thus, there is a command: 
``.venv/bin/pip3 freeze > requirements.txt``