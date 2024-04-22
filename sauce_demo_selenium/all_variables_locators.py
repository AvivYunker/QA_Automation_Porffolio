from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



# PAGE SETUP
VAR_browser = webdriver.Chrome()
VAR_actions = ActionChains(VAR_browser)

# Locator that never exists
LOC_never_exists = "//div[text()='abcdefghijklmnopqrstuvwxyz']"

# URL
VAR_sauce_url = "https://www.saucedemo.com/v1/index.html"
VAR_invalid_url = "https://www.saucedemo.com/v1/oapksd3o"

# Login PAGE
LOC_login_page_logo = "//div[@class='login_logo']"
LOC_username_input = "//input[@placeholder='Username']"
LOC_password_input = "//input[@placeholder='Password']"
LOC_login_button = "//input[@value='LOGIN']"
LOC_robot_img = "//img[@class='bot_column']"

# USERNAMES & PASSWORDS
VAR_standard_username = "standard_user"
VAR_locked_username = "locked_out_user"
VAR_problem_username = "problem_user"
VAR_glitch_username = "performance_glitch_user"
VAR_invalid_username = "zzzzzzzz"


VAR_standard_password = "secret_sauce"
VAR_invalid_password = "zzzzzzzz"

# Login ERROR MESSAGES
LOC_locked_user_error = "//h3[text()='Epic sadface: '][text()='Sorry, this user has been locked out.']"
LOC_invalid_user_error = "//h3[text()='Epic sadface: '][text()='Username and password do not match any user in this service']"


# PRODUCTS PAGE
LOC_products_header = "//div[text()='Products']"
LOC_footer = "//div[@class='footer_copy']"
LOC_white_robot = "//img[@class='footer_robot']"
LOC_twitter_button = "//li[@class='social_twitter']"
LOC_facebook_button = "//li[@class='social_twitter']"
LOC_linkedin_button = "//li[@class='social_twitter']"
LOC_Shopping_Cart_button = "//div[@id='shopping_cart_container']"
LOC_Shopping_Cart_item_count = "//span[@class='fa-layers-counter shopping_cart_badge']"

# item filtering
LOC_filtering_button = "//select[@class='product_sort_container']"
LOC_filtering_az_option = "//option[@value='az']"
LOC_filtering_za_option = "//option[@value='za']"
LOC_filtering_lowhigh_option = "//option[@value='lohi']"
LOC_filtering_highlow_option = "//option[@value='hilo']"


# Hamburger Menu
LOC_hamburger_menu = "//button[text()='Open Menu']"
LOC_all_items_button = "//a[@id='inventory_sidebar_link']"
LOC_about_button = "//a[@id='about_sidebar_link']"
LOC_LOCout_button = "//a[@id='LOCout_sidebar_link']"
LOC_reset_app_state_button = "//a[@id='reset_sidebar_link']"
LOC_X_button = "//button[text()='Close Menu']"

# Existing products
LOC_all_existing_product_names = "//div[@class='inventory_item_name']"
LOC_all_existing_product_descriptions = "//div[@class='inventory_item_desc']"
LOC_all_existing_product_pictures = "//div[@class='inventory_item_img']"
LOC_all_existing_product_prices = "//div[@class='inventory_item_price']"
LOC_all_existing_product_add_to_cart = "//button[@class='btn_primary btn_inventory']"

LOC_prices_of_selected_items = "//button[text()='REMOVE']/..//div"
LOC_descriptions_of_selected_items = "//button[text()='REMOVE']/..//div/../..//div[@class='inventory_item_label']//a//div"


LOC_all_remove_buttons = "//button[text()='REMOVE']"
LOC_single_random_remove = "//button[@class='btn_secondary btn_inventory']"

# YOUR CART PAGE
LOC_your_cart_header = "//div[@class='subheader']"
LOC_continue_shopping_button = "//a[text()='Continue Shopping']"
LOC_checkout_button = "//a[text()='CHECKOUT']"
LOC_qty_text = "//div[@class='cart_quantity_label']"
LOC_description_text = "//div[@class='cart_desc_label']"

# CHECKOUT PAGE
LOC_first_name_input = "//input[@placeholder='First Name']"
LOC_last_name_input = "//input[@placeholder='Last Name']"
LOC_zip_postal_input = "//input[@placeholder='Zip/Postal Code']"
LOC_cancel_button = "//a[@class='cart_cancel_link btn_secondary']"
LOC_continue_button = "//input[@class='btn_primary cart_button']"

LOC_firstname_missing_error = "//h3[text()='Error: '][text()='First Name is required']"
LOC_lastname_missing_error = "//h3[text()='Error: '][text()='Last Name is required']"
LOC_postalcode_missing_error = "//h3[text()='Error: '][text()='Postal Code is required']"

# CHECKOUT: OVERVIEW PAGE
LOC_payment_information_text = "(//div[@class='summary_info_label'])[1]"
LOC_sauce_card_text = "(//div[@class='summary_value_label'])[1]"
LOC_shipping_information_text = "(//div[@class='summary_info_label'])[2]"
LOC_free_pony_text = "(//div[@class='summary_value_label'])[2]"
LOC_item_total_text = "//div[@class='summary_subtotal_label']"
LOC_selected_item_descriptions = "//div[@class='inventory_item_name']"
LOC_finished_button = "//a[text()='FINISH']"

# FINISH PAGE
LOC_finish_header = "//div[text()='Finish']"
LOC_thank_you_header = "//h2[text()='THANK YOU FOR YOUR ORDER']"
LOC_dispatched_text = "//div[@class='complete-text']"
LOC_big_pony_express_image = "//img[@class='pony_express']"