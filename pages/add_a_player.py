from pages.base_page import BasePage


class AddAPlayer(BasePage):
    main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_xpath = "//html/body/div/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    sign_out_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"


    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title('https://scouts-test.futbolkolektyw.pl/en')
        expected_title = 'Add player'
        assert actual_title == expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_xpath)

    @classmethod
    def tearDown(self):
        self.driver.quit()
