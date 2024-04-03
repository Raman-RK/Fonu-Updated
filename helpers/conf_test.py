import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup(request):
    """
    Fixture to set up a WebDriver instance for browser automation testing.

    Args:
        request (pytest.FixtureRequest): Provides access to configuration information.

    Returns:
        WebDriver: Instance of the WebDriver (in this case, Chrome).
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver
