from pages.base_page import BasePage


class Dashboard(BasePage):
    password_xpath = "//*[@id='password']"
    password_xpath = "//*[@type='password']"
    password_xpath = "//*[@name='password']"
    login_xpath = "//*[@type='text']"
    login_xpath = "//*[@id='login']"
    login_xpath = "//*[@name='login']"
    remind_password_xpath = "//*[text()='Remind password']"
    language_selector_xpath = "//div[2]/div/div"
    scouts_panel_xpath = "// *[text() = 'Scouts Panel']"
    sign_in_button_xpath = "// *[text() = 'Sign in']"
    sign_in_button_xpath = "//span[1]"
