from pages.login_page import Login
from pages.alert_page import AlertPage


def test_login(browser):
    login = Login(browser)
    login.go_to_site()
    login.login_func('automation-qa', 'automationQAtest')

def test_alert_valid(browser):
    login = Login(browser)
    login.go_to_site()
    login.login_func('automation-qa', 'automationQAtest')
    alert = AlertPage(browser)
    alert.alert_valid()
#

def test_alert_invalid(browser):
    login = Login(browser)
    login.go_to_site()
    login.login_func('automation-qa', 'automationQAtest')
    alert = AlertPage(browser)
    alert.alert_invalid()



