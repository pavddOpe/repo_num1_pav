from pages.base_page import BasePage


class AddingMatch(BasePage):
    my_team_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    enemy_team_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    my_team_score_xpath = "//input[contains(@name,'myTeamScore')]"
    enemy_team_score_xpath = "//input[contains(@name,'enemyTeamScore')]"
    date_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    league_xpath = "//input[starts-with(@name,'league')]"
    time_played_xpath = "//html/body/div/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    rating_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    submit_button_xpath = "//span[text()='Submit']"
    clear_button_xpath = "//span[text()='Clear']"