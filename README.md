# supertime: a living example of the superfunctions

[![Downloads](https://static.pepy.tech/badge/supertime/month)](https://pepy.tech/project/supertime)
[![Downloads](https://static.pepy.tech/badge/supertime)](https://pepy.tech/project/supertime)
[![Coverage Status](https://coveralls.io/repos/github/pomponchik/supertime/badge.svg?branch=main)](https://coveralls.io/github/pomponchik/supertime?branch=main)
[![Lines of code](https://sloc.xyz/github/pomponchik/supertime/?category=code)](https://github.com/boyter/scc/)
[![Hits-of-Code](https://hitsofcode.com/github/pomponchik/supertime?branch=main)](https://hitsofcode.com/github/pomponchik/supertime/view?branch=main)
[![Test-Package](https://github.com/pomponchik/supertime/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/pomponchik/supertime/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/supertime.svg)](https://pypi.python.org/pypi/supertime)
[![PyPI version](https://badge.fury.io/py/supertime.svg)](https://badge.fury.io/py/supertime)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


The [transfunctions](https://github.com/pomponchik/transfunctions) library introduces a new type of function: `superfunction`. They can behave both as regular and asynchronous functions, depending on the context, that is, on how the user uses them. This micro-library demonstrates the smallest example of this concept that I could come up with.

Install it:

```bash
pip install supertime
```

And try:

```python
from asyncio import run
from supertime import supersleep

supersleep(5)  # sleeps 5 sec.
run(supersleep(5))  # sleeps 5 sec., but ASYNCHRONOUSLY.
```

As you can see, the superfunction can automatically adjust to how the calling code uses it.
