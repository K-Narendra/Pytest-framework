from selenium.webdriver.common.by import By
class Icewarp:
    Icewarp_logo = (By.XPATH, '//*[@id="primary-menu"]/a')
    Product_link = (By.XPATH, '//*[@id="main-menu"]/li[1]/a')
    Download_link = (By.XPATH, '//div[contains(text(),"Download")]/ancestor::a')
    Btn_Contiune_apps = (By.XPATH, '//*[@class="downloads-main-card-wrapper"]/div[3]//a')
    Download_btns = (By.XPATH, '//*[starts-with(@class,"download-apps")]')


    # // *[contains(text(), "IceWarp Mobile")]
    # //*[@class ="download-box-app-left-bottom"]/a