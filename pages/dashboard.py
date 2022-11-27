import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'
    add_player_button_xpath = "//[text()='Add player']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    password_xpath = "//*[@id='password']"
    login_xpath = "//*[@type='text']"
    remind_password_xpath = "//*[text()='Remind password']"
    language_selector_xpath = "//div[2]/div/div"
    scouts_panel_xpath = "//*[text()='Scouts Panel']"
    sign_in_button_xpath = "//button[@type='submit']"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
