# CAFE
Concrete Analysis for Explanations (CAFE) is a framework for delivering personalized feedback based on concrete code analysis.
CAFE is built on top of the [autograder-py](https://github.com/edulinq/autograder-py) python package,
and uses the assignment and question objects it defines.

## Documentation
TODO: Release documentation after first release.

## Installation / Requirements

This project requires [Python](https://www.python.org/) >= 3.10.

Standard Python requirements are listed in `pyproject.toml`.
The project and Python dependencies can be installed from source with:
```sh
pip3 install .
```

## The CLI

This project contains tools for profiling and analysis between submissions for assignment.

To profile a submission to an assignment you can run:
```sh
python3 -m cafe.cli.profile -s <submission-dir> <qulaified-assignment-ref>
```
To analys two submission you can run:

```sh
python3 -m cafe.cli.explain submission-1.json submission-2.json
```

## Resources
 - [CAFE (this repo)](#)
 - [Python Interface](https://github.com/edulinq/autograder-py)
