import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver as sw
import pyperclip
import time


_MENU_XPATH = "/html/body/div[1]/div[1]/div/div[2]/div[1]/nav/div[2]/button/div"
_EXPORT_IPORT_XPATH = "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/a[9]/div[2]"
_EXPORT_XPATH = "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/a[2]"
_EXPORT_BUTTON_XPATH = "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[3]"
_DOWNLOAD_DIRECTORY = "Downloads"


class StackeditParser:
    driver: sw.Firefox

    def __init__(self) -> None:
        self.driver = sw.Firefox()
        self.driver.get("https://stackedit.io/app")
        time.sleep(5)

    def insert_text(self, text: str):
        pyperclip.copy(text)
        editor = self.driver.switch_to.active_element
        editor.send_keys(Keys.CONTROL, "a")
        editor.send_keys(Keys.DELETE)
        editor.send_keys(Keys.CONTROL, "v")

    def download(self):
        menu = self.driver.find_element(By.XPATH, _MENU_XPATH)
        menu.click()
        export_import = self.driver.find_element(By.XPATH, _EXPORT_IPORT_XPATH)
        export_import.click()
        export = self.driver.find_element(By.XPATH, _EXPORT_XPATH)
        export.click()
        export_button = self.driver.find_element(By.XPATH, _EXPORT_BUTTON_XPATH)
        export_button.click()
        time.sleep(1)

    def get_html(self) -> str:
        path = os.path.join(os.path.expanduser("~"), _DOWNLOAD_DIRECTORY)
        files = [os.path.join(path, f) for f in os.listdir(path)]

        if not files:
            raise RuntimeError("Download of converted file failed")

        downloaded_file = max(files, key=os.path.getctime)
        html = open(downloaded_file, 'r').read()
        os.remove(downloaded_file)

        return html

    def destroy(self):
        self.driver.close()

