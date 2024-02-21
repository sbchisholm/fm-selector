FM Selector
===========

Description
-----------

A simple webapp to send remote commands to a NAD C422 tuner.

Building
--------

Note that on a raspberry pi 2 building the rust portion of pydantic-core is too
much for it. In order to avoid needing the build anything we can take advantage
of pip's `--only-binary` option.

Generate a requirements.txt file:

```
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

Create virtualenv and activate it:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies using pip:

```
pip install -r requirements.txt --only-binary=:all:
```
