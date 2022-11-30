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
    scouts_panel_heading_xpath = "(//div[contains(@class, 'MuiToolbar-root')])/h6"
    main_page_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[1]/div[1]/div/span"
    players_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[1]/div[2]/div/span"
    languange_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[2]/div[1]/div/span"
    sign_out_menu_item_xpath = "(//ul[contains(@class, 'MuiList-root')])[2]/div[2]/div/span"
    players_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[2]/div/b"
    matches_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[3]/div/b"
    reports_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[4]/div/b"
    events_get_count_xpath = "(//div[contains(@class, 'MuiPaper-root')])[5]/div/b"
    dev_team_contact_link_xpath = "//*[contains(@class, 'MuiCardActions-root')]/a"
    add_player_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[7]/div/a"
    last_created_player_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[8]/div/a[1]"
    last_updated_player_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[8]/div/a[2]"
    last_updated_report_link_xpath = "(//div[contains(@class, 'MuiPaper-root')])[8]/div/a[3]"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_sign_out_button(self):
        self.click_on_the_element(self.sign_out_menu_item_xpath)

    def wait_for_sign_out_will_be_visible(self):
        self.wait_for_element_to_be_visible(self.sign_out_menu_item_xpath)

    def wait_for_add_player_will_be_visible(self):
        self.click_on_the_element(self.add_player_link_xpath)

    def click_on_add_player(self):
        self.click_on_the_element(self.add_player_link_xpath)
