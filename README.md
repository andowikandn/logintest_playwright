🛠️ Using Playwright framework with Python

Basic testing to login testing

Precondition should have to:
- pip install python
- pip install playwright
- pip playwright install
- pip install pytest
- pip install pytest-html

Makesure all already installed:
- pip list

How to run:
- pytest -m negativetest --html=reportnegativetest.html (run negativetest)
- pytest -m positivetest --html=reportpositivetest.html (run positivetest)
- pytest -v test_herokuappw.py --html=reportautomation.html (end to end test)
