from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Edge()
        print("Launching Edge browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

#---------------HTML Pytest Report-------------------
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "nopCommerce"
    config.stash[metadata_key]["Module Name"] = "Customer"
    config.stash[metadata_key]["Tester Name"] = "Sachin B Revankar"

#-------------To Delete and Modify HTML Reports--------
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA Home",None)
    metadata.pop("Plugins", None)
