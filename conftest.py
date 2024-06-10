# Python/Pytest
import pytest
import logging
from appium import webdriver
# Options are only available since client version 2.3.0
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

# Adding logging: Helps to debug and verify the behavior of your fixture during test runs.
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()


# 下面的这种写法呢？是我认为较为简洁的实现，请对比并解释这两种代码实现的区别
@pytest.fixture()
def create_ios_driver_fix(request):
    """
    Pytest fixture to create an iOS driver with optional custom options.

    If 'request.param' is provided, it will be used to load custom capabilities.
    Otherwise, default capabilities are used.

    Yields:
        WebDriver: An instance of the Appium WebDriver.
    """
    options = XCUITestOptions()
    options.platformVersion = '13.4'
    options.udid = '123456789ABC'
    # If you want to pass None to the create_ios_driver_fix fixture, it can be handled appropriately within the fixture function.
    # Handle the case where request.param might be None
    custom_opts = request.param if hasattr(request, 'param') else None 
    if custom_opts is not None:
        logger.info(f"Loading custom options: {custom_opts}")
        options.load_capabilities(custom_opts)

    # # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    # driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

    # yield driver 
    # driver.quit()
    pass

