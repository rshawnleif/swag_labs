class LoginPageElements:

    # Login-related XPaths
    login_logo_xpath = "//div[@class='login_logo']"
    username_xpath = "//input[@id='user-name']"
    password_xpath = "//input[@id='password']"
    login_button_xpath = "//input[@id='login-button']"
    login_error_msg_xpath = "//h3[@data-test='error' and contains(text(), '{}')]"
     