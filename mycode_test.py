# Python/Pytest
import pytest

from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'



options_data = [{'appium:app': '/path/to/app/UICatalog.app.zip'}, None]
# Test with two options
@pytest.mark.parametrize('create_ios_driver_fix', options_data, indirect=True)
def test_ios_click_with_options(appium_service, create_ios_driver_fix):
    # with create_ios_driver_fix as driver:
    #     el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
    #     el.click()
    pass
