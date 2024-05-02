import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from test.Profile.profile import profile



@pytest.fixture(scope='class')
def init_driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(profile.URL)
    driver.implicitly_wait(profile.MAX_TIMEOUT)
    driver.set_page_load_timeout(profile.PAGE_LOAD_TIMEOUT)
    request.cls.driver = driver
    yield
    driver.quit()

#GRID
# @pytest.fixture(scope='class')
# def init_driverGrid(request):
#     driver = webdriver.Remote(
#         command_executor="18.204.23.115:4444",
#         options=webdriver.ChromeOptions()
#     )
#     driver.implicitly_wait(ENTProfile.MAX_TIMEOUT)
#     driver.get(ENTProfile.BASE_URL)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
