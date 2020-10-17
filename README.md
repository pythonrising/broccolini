# broccolini

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![CI_WITH_POETRY](https://github.com/pythonrising/broccolini/workflows/CI_WITH_POETRY/badge.svg)
![CodeQL](https://github.com/pythonrising/broccolini/workflows/CodeQL/badge.svg)
![Lint Code Base](https://github.com/pythonrising/broccolini/workflows/Lint%20Code%20Base/badge.svg)
[![codecov](https://codecov.io/gh/pythonrising/broccolini/branch/main/graph/badge.svg)](https://codecov.io/gh/pythonrising/broccolini)

## Python Version Warning

This library will always only support the latest version of python.  Expect breaking changes always.  If you are looking for stability please plan on forking and maintaining yourself.

## Description

Collection of utilities used in my programming projects.

## QuickStart

This directory is a collection of utilities helpful for my work process. It is heavily reliant on Hashicorp Vault. In order to use this effectively you will need to stand up a development instance of Vault. There are many good examples of how to do this. Once your vault is stood up you just need to add some secrets and begin using it.

## Using this repository

- pip install poetry
- git clone <https://github.com/pythonrising/broccolini.git>
- cd broccolini
- poetry install
- build working vault dev server
- create environment variables
- pytest -vv -s
- fix any issues
