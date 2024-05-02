import time

from selenium.common import NoSuchElementException

from test.Utilitiies.TestObjectActions import ObjectActions
from test.Pages.Icewarp import Icewarp
from selenium.webdriver.common.by import By
from test.conftest import BaseTest


class Test_icewrap(BaseTest):
    try:

        def test_icewrap(self):
            ObjectActions.click_object(self.driver, Icewarp.Product_link)
            time.sleep(2)
            ObjectActions.click_object(self.driver, Icewarp.Download_link)
            window_title = ObjectActions.get_current_window_title(self.driver)
            assert window_title == "Download IceWarp Apps"

            time.sleep(2)

            New_Installation = self.driver.find_element(By.XPATH, '//h3[contains(text()," New installation")]')
            Update = self.driver.find_element(By.XPATH, '//h3[contains(text()," Update")]')
            Apps = self.driver.find_element(By.XPATH, '//h3[contains(text(),"Apps")]')

            assert New_Installation.is_displayed()
            assert Update.is_displayed()
            assert Apps.is_displayed()

            ObjectActions.click_object(self.driver, Icewarp.Btn_Contiune_apps)
            time.sleep(2)

            All_items = self.driver.find_elements(By.XPATH, '//*[@class="download-box-apps"]/div/div[1]/div[1]/div[1]')
            # Download_btns = self.driver.find_elements(By.XPATH, '//*[@class ="download-box-app-left-bottom"]')

            # for item in All_items:
            #     assert item.is_displayed()
            #     btns = item.find_elements(By.XPATH, './/*[@class ="download-box-app-left-bottom"]/a')
            #     for btn in btns:
            #         try:
            #             if btn.is_displayed():
            #                 print(item.text)
            #                 pass
            #         except NoSuchElementException as e:
            #             print(f"AssertionError: {e} for {item.text}")

            for module in All_items:
                module_name = module.text
                if module.is_displayed():
                    # Check if there is at least one download button for the module
                    download_buttons_for_module = module.find_elements(By.XPATH,
                                                                       './/*[@class="download-box-app-left-bottom"]/a')
                    if not download_buttons_for_module:
                        raise NoSuchElementException(f"No download button found for module: {module_name}")

            time.sleep(2)
            ObjectActions.click_object(self.driver, Icewarp.Icewarp_logo)
            assert ObjectActions.get_current_window_title(
                self.driver) == "IceWarp® - Business Email Server & Collaboration Hub"




    except:
        pass

    else:
        pass


'''
 for item in All_items:
                download_buttons = item.find_elements(By.XPATH, './/*[@class="download-box-app-left-bottom"]')
                print(f"Number of download buttons found for item '{item.text}': {len(download_buttons)}")

                if len(download_buttons) > 0:
                    print("Download buttons found")
                    # Your further code logic here
                else:
                    print("No download buttons found")
                    # Your further code logic here
                download_button_found = False

                if item.is_displayed():
                    download_buttons = item.find_elements(By.XPATH, './/*[@class="download-box-app-left-bottom"]')
                    for btn in download_buttons:
                        if btn.is_displayed():
                            download_button_found = True
                            break
                    if not download_button_found:
                        # print(f"Download button not found for the item: {item.text}")
                        raise NoSuchElementException(f"Download button not found for the item: {item.text}")

'''
