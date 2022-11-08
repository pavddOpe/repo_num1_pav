from pages.base_page import BasePage


class Dashboard(BasePage):
    login_field_xpath = "/html/body/div/form/div/div[1]/div[1]/div/input;user01@getnada.com"
    password_field_xpath="/html/body/div/form/div/div[1]/div[2]/div/input;Test-1234"
    button_xpath="//*[@id='_next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    main_page_xpath="//html/body/div/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    add_player_xpath="//*[@id='_next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    activity_xpath="//*[@id='_next']/div[1]/main/div[3]/div[3]/div/div/h2"
    players_xpath="/html/body/div/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_xpath="//*[@id='_next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    signout_button_xpath="//*[@id='_next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    scouts_panel_xpath="/html/body/div/div[1]/header/div/h6"
    playerscount_xpath="//div[text()='Players count']"
    pass