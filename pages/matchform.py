from pages.base_page import BasePage


class MatchForm(BasePage):
    email_field_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    name_field_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_field_xpath = "//input[contains(@name,'surname')]"
    age_field_xpath = "//input[contains(@name,'age')]"
    leg_button_xpath = "//div[contains(@id,'mui')]"
    mainposition_xpath = "//input[starts-with(@name,'mainPosition')]"
    addlanguage_button_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[2]/div/div[15]/button/span[1]"
    achievements_xpath = "///input[contains(@name,'achievements')]"
    addlink_toyoutube_button_xpath = "//*[@id='_next']/div[1]/main/div[2]/form/div[2]/div/div[19]/button/span[1]"
    submit_button_xpath = "//span[text()='Submit']"
    clear_button_xpath = "//span[text()='Clear']"
    pass