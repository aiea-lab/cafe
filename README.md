# CAFE
Concrete Analysis for Explanations (CAFE) is a framework for delivering personalized feedback based on concrete code analysis.
CAFE is built on top of the [autograder-py](https://github.com/edulinq/autograder-py) python package,
and uses the assignment and question objects it defines.

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
The output looks something like this:

```json
{
    "TC1": {
        "<python-standard>:ast.py:parse": 1
        "<python-packages>:autograder/assignment:__init__": 1
        "<submission-dir>:main.py:<module>": 2
        "<python-builtin>::_codecs.utf_8_decode": 3
        "<python-core>::_io._IOBase.__exit__": 1
        .....
    }
}
```

To analyse two submission you can run:

```sh
python3 -m cafe.cli.explain solution.json buggy-submission.json
```

The output looks something like this:
```sh
| Function                                  | Expected   | Your Code  | Delta      |
| <grading-dir>/main.py:__hash__            | 12         | 9          | 3          |
| <grading-dir>/main.py:enqueue             | 4          | 7          | -3         |

```

## Resources
 - [CAFE (this repo)](#)
 - [Python Interface](https://github.com/edulinq/autograder-py)
