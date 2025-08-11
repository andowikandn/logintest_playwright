🛠️ Using Playwright framework with Python

Basic testing to login testing

First of all:
- Download python https://www.python.org/downloads then install

Create folder project in vscode

Create environment:
- python -m venv nama_env
- nama_env\Scripts\activate (Windows)
- source nama_env/bin/activate (MacOS)
- deactivate (Disable)

Then to do:
- pip install playwright
- pip playwright install
- pip install pytest
- pip install pytest-html

Makesure all already installed:
- pip list

How to run:
- pytest -m negativetest --html=reportnegativetest.html
- pytest -m positivetest --html=reportpositivetest.html
- pytest -v test_herokuappw.py --html=reportautomation.html
