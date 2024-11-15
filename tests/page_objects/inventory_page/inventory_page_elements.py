class InventoryPageElements:

    # Static Elements
    menu_button_xpath = "//div[@class='bm-burger-button']"
    app_logo_xpath = "//div[@class='app_logo']"
    cart_button_xpath = "//div[@id='shopping_cart_container']"

    # Navigation Menu
    nav_menu_items = "//a[@class='bm-item menu-item' and text()='{}']"
    """ The following are the item names:
        - All Items
        - About
        - Log out
        - Reset App State
    """

    # Products
    product_img_xpath = "//img[@alt='Sauce Labs Backpack' and @src='{}']"
    """ Since all redirections after logging in is the same, images are used to
        assert the successful redirection. There are two accounts ("standard" and
        "visual") that shows different images in the first product upon logging in. 
        The format pertains to the test data to be verified:
        - Correct image shows the black backpack
        - Incorrect image shows the bulldog
    """