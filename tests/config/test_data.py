class Initialize:
    BASE_URL = "https://www.saucedemo.com/"

class LoginFunctionalityData:
    users = {
        "standard": "standard_user",
        "locked_out": "locked_out_user",
        "problem": "problem_user",
        "performance_glitch": "performance_glitch_user",
        "error": "error_user",
        "visual": "visual_user",
        "invalid_username": "shawn"
    }

    password = {
        "valid": "secret_sauce",
        "invalid": "invalid_password"
    }

    login_error_msg = {
        "username_required": "Epic sadface: Username is required",
        "password_required": "Epic sadface: Password is required",
        "incorrect_creds": "Epic sadface: Username and password do not match any user in this service"
    }

class InventoryFunctionalityData:
    nav_menu_items = {
        "all": "All Items",
        "about": "About",
        "logout": "Logout",
        "reset": "Reset App State"
    }

    product_img = {
        "correct_img": "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg",
        "incorrect_img": "/static/media/sl-404.168b1cce.jpg"
    }