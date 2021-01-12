# AFFE-CORE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/ABL-TDM-Lab/AFFE-CORE/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![dist](https://github.com/ABL-TDM-Lab/AFFE-CORE/workflows/dist/badge.svg)](https://github.com/ABL-TDM-Lab/AFFE-CORE/actions?query=workflow%3Adist)

Core modules for data processing in PKU-AFFE program

### Git Hooks

1. pre-commit hooks:
    - install pre-commit: `pip install pre-commit`
    - run install: `pre-commit install`
    - run hooks for the first time: `pre-commit run --all-files`

2. build `.exe`:
    - `pyinstaller hello.spec`