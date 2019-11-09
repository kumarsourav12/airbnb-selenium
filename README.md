# Airbnb Automation Suite - Instructions to run the tests

After setting up the local environment (venv with python 3.7.x), please follow the instructions below to execute test cases
We will be using pytest as our base framework.

### Requirements
Setup your venv with python 3.7.x and install the requirements
All the requirements are listed under requirements.txt in root folder.

### Submodules and Files
There are multiple folders categorized according the functionality or usage

* configs : Will be used to store configs depending upon environment
* drivers : different drivers for different browsers and versions. Please add your suitable browser version driver
* pages : Everything related to particular web pages. Locators, methods to interact with elements etc.
* reports : Folder containing all the reports of current execution, execution log and HTML report
* screenshots : will contain screenshots
* tests : Will contain test scripts
* utils : contains common utilities

### Running the tests

After all the prerequisites have met, we can execute the test cases. Since we are using **pytest** to run the tests, please use below command to run the tests.
> python -m pytest /<loaction of test file> --html=reports/report.html

For e.g:
>python -m pytest tests/test_booking_simple_path.py -s --html=reports/report.html

### Execution Logs

You can find the logs in file named **pytest.log** under the **reports** folder. I have left a sample log from my execution for you to check if you wish to.

### Test Report

Location of test report in HTML format is also under the reports folder with the name **report.html**.