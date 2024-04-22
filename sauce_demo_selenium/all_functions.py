from all_variables_locators import *
import time
import random

def FUN_get_random_ranges(bottom, top):
    return random.randint(bottom, top)

def FUN_open_app_valid_url():
    VAR_browser.get(VAR_sauce_url)
    VAR_browser.maximize_window()
    time.sleep(0.5)

def FUN_open_app_invalid_url():
    VAR_browser.get(VAR_invalid_url)
    VAR_browser.maximize_window()
    time.sleep(0.5)

# def FUN_navigate_to_Login_webpage():
#     VAR_browser.get(VAR_sauce_url)

def FUN_finish_test():
    VAR_browser.close()
    #VAR_browser.quit()

def FUN_validate_in_login_page():
    time.sleep(1)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_login_page_logo), f"🔴 Login Page Logo did not appear."
        print(f"🟢 Login Page logo did appear.")
    except:
        print(f"🔴 Login Page logo did not appear.")

def FUN_validate_not_in_Login_page():
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_login_page_logo), f"🟢 Login Page LOCo did not appear."
        print(f"🔴 Login Page LOCo did appear.")
    except:
        print(f"🟢 Login Page LOCo did not appear.")

def FUN_validate_username_field():
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_username_input), f"🔴 Username field doesn't appear."
        print(f"🟢 Username field appears.")
    except:
        print(f"🔴 Username field doesn't appear.")

def FUN_validate_password_field():
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_password_input), f"🔴 Password field doesn't appear."
        print(f"🟢 Password field appears.")
    except:
        print(f"🔴 Password field doesn't appear.")

def FUN_validate_login_button():
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_login_button), f"🔴 Login button doesn't appear."
        print(f"🟢 Login button appears.")
    except:
        print(f"🔴 Login button doesn't appear.")          

def FUN_validate_robot_picture_exists():
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_robot_img), f"🔴 Red-Robot image doesn't appear."
        print(f"🟢 Red-Robot image appears.")
    except:
        print(f"🔴 Red-Robot image doesn't appear.") 

def FUN_login_with_standard_user():
    username_field = VAR_browser.find_element(By.XPATH, LOC_username_input)
    password_field = VAR_browser.find_element(By.XPATH, LOC_password_input)
    login_button = VAR_browser.find_element(By.XPATH, LOC_login_button)
    time.sleep(1)
    username_field.send_keys(VAR_standard_username)
    password_field.send_keys(VAR_standard_password)
    login_button.click()

def FUN_login_with_locked_user():
    username_field = VAR_browser.find_element(By.XPATH, LOC_username_input)
    password_field = VAR_browser.find_element(By.XPATH, LOC_password_input)
    login_button = VAR_browser.find_element(By.XPATH, LOC_login_button)
    time.sleep(1)
    username_field.send_keys(VAR_locked_username)
    password_field.send_keys(VAR_standard_password)
    login_button.click()

def FUN_login_with_problem_user():
    username_field = VAR_browser.find_element(By.XPATH, LOC_username_input)
    password_field = VAR_browser.find_element(By.XPATH, LOC_password_input)
    login_button = VAR_browser.find_element(By.XPATH, LOC_login_button)
    time.sleep(1)
    username_field.send_keys(VAR_problem_username)
    password_field.send_keys(VAR_standard_password)
    login_button.click()

def FUN_login_with_glitch_user():
    username_field = VAR_browser.find_element(By.XPATH, LOC_username_input)
    password_field = VAR_browser.find_element(By.XPATH, LOC_password_input)
    login_button = VAR_browser.find_element(By.XPATH, LOC_login_button)
    time.sleep(1)
    username_field.send_keys(VAR_glitch_username)
    password_field.send_keys(VAR_standard_password)
    login_button.click()

def FUN_login_invalid_credentials():
    username_field = VAR_browser.find_element(By.XPATH, LOC_username_input)
    password_field = VAR_browser.find_element(By.XPATH, LOC_password_input)
    login_button = VAR_browser.find_element(By.XPATH, LOC_login_button)
    time.sleep(1)
    username_field.send_keys(VAR_invalid_username)
    password_field.send_keys(VAR_invalid_password)
    login_button.click()

def FUN_validate_error_message_locked_user():
    time.sleep(1)
    locker_error = VAR_browser.find_element(By.XPATH, LOC_locked_user_error)
    try:
        assert locker_error.text == "Epic sadface: Sorry, this user has been locked out.", "🔴 Locked User error message did not appear"
        print("🟢 Locked user error message appears")
    except:
        #print(locker_error.text)
        print(f"🔴 Locked user error message did not appear.")

def FUN_validate_error_message_invalid_user():
    time.sleep(1)
    invalid_user_error = VAR_browser.find_element(By.XPATH, LOC_invalid_user_error)
    try:
        assert invalid_user_error.text == "Epic sadface: Username and password do not match any user in this service", "🔴 Invalid User error message did not appear"
        print("🟢 Invalid user error message appears")
    except:
        #print(locker_error.text)
        print(f"🔴 Invalid user error message did not appear.")

def FUN_validate_products_header_appears():
    time.sleep(1)
    try:
        products_header = VAR_browser.find_element(By.XPATH, LOC_products_header)
        assert products_header.text == "Products", f"🔴 'PRODUCTS' header did not appear."
        print("🟢 'PRODUCTS' header did appear")
    except:
        print(f"🔴 'PRODUCTS' header did not appear.")

def FUN_validate_products_header_doesnt_appear():
    time.sleep(1)
    try:
        products_header = VAR_browser.find_element(By.XPATH, LOC_products_header)
        assert products_header.text == "Products", f"🟢 'PRODUCTS' header did not appear."
        print(f"🔴 'PRODUCTS' header did appear")
    except:
        print(f"🟢 'PRODUCTS' header did not appear.")

def FUN_go_to_footer():
    time.sleep(1)
    for _ in range(2):
        VAR_actions.send_keys(Keys.PAGE_DOWN)
        VAR_actions.perform()

def FUN_validate_footer_of_current_page():
    time.sleep(0.5)
    try:
        footer = VAR_browser.find_element(By.XPATH, LOC_footer)
        assert footer.text == "© 2020 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy", f"🔴 Footer doesn't appear"
        print(f"🟢 Footer does appear.")
    except:
        print(f"🔴 Footer doesn't appear")

def FUN_validate_white_robot_current_page():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_white_robot), f"🔴 White-Robot image at footer doesn't appear."
        print(f"🟢 White-Robot image at footer does appear.")
    except:
        print(f"🔴 White-Robot image at footer doesn't appear.") 

def FUN_validate_twitter_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_twitter_button), f"🔴 Twitter button at footer doesn't appear."
        print(f"🟢 Twitter button at footer appears.")
    except:
        print(f"🔴 Twitter button at footer doesn't appear.")

def FUN_validate_facebook_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_facebook_button), f"🔴 Facebook button at footer doesn't appear."
        print(f"🟢 Facebook button at footer appears.")
    except:
        print(f"🔴 Facebook button at footer doesn't appear.")

def FUN_validate_linkedin_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_linkedin_button), f"🔴 LinkedIn button at footer doesn't appear."
        print(f"🟢 LinkedIn button at footer appears.")
    except:
        print(f"🔴 LinkedIn button at footer doesn't appear.")

def FUN_validate_hamburger_menu():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_hamburger_menu), f"🔴 Hamburger Menu button doesn't appear."
        print(f"🟢 Hamburger Menu button appears.")
    except:
        print(f"🔴 Hamburger Menu button doesn't appear.")

def FUN_click_on_hamburger_menu():
    time.sleep(0.5)
    try:
        hamburger_menu_button = VAR_browser.find_element(By.XPATH, LOC_hamburger_menu)
        time.sleep(0.5)
        hamburger_menu_button.click()
    except:
        print(f"❗ Hamburger Menu button could not be clicked.")

def FUN_click_all_items_in_hamburger_menu():
    time.sleep(0.5)
    try:
        all_items_link = VAR_browser.find_element(By.XPATH, LOC_all_items_button)
        time.sleep(0.25)
        all_items_link.click()
    except:
        print(f"❗ 'All Items' link could not be clicked.")


def FUN_click_about_in_hamburger_menu():
    time.sleep(0.5)
    try:
        about_link = VAR_browser.find_element(By.XPATH, LOC_about_button)
        time.sleep(0.25)
        about_link.click()
    except:
        print(f"❗ 'About' link could not be clicked.")

def FUN_click_LOCout_in_hamburger_menu():
    time.sleep(0.5)
    try:
        LOCout_link = VAR_browser.find_element(By.XPATH, LOC_LOCout_button)
        time.sleep(0.25)
        LOCout_link.click()
    except:
        print(f"❗ 'LOCout' link could not be clicked.")

def FUN_click_reset_app_state_in_hamburger_menu():
    time.sleep(0.5)
    try:
        reset_app_state_link = VAR_browser.find_element(By.XPATH, LOC_reset_app_state_button)
        time.sleep(0.25)
        reset_app_state_link.click()
    except:
        print(f"❗ 'Reset App State' link could not be clicked.")

def FUN_validate_all_items_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_all_items_button), f"🔴 'all items' button doesn't appear."
        print(f"🟢 'all items' button appears.")
    except:
        print(f"🔴 'all items' button doesn't appear.")


def FUN_validate_about_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_about_button), f"🔴 'about' button doesn't appear."
        print(f"🟢 'about' button appears.")
    except:
        print(f"🔴 'about' button doesn't appear.")

def FUN_validate_LOCout_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_LOCout_button), f"🔴 'LOCout' button doesn't appear."
        print(f"🟢 'LOCout' button appears.")
    except:
        print(f"🔴 'LOCout' button doesn't appear.")


def FUN_validate_reset_app_state_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_reset_app_state_button), f"🔴 'reset app state' button doesn't appear."
        print(f"🟢 'reset app state' button appears.")
    except:
        print(f"🔴 'reset app state' button doesn't appear.")

def FUN_validate_X_button_on_hamburger_menu():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_X_button), f"🔴 'X' button doesn't appear."
        print(f"🟢 'X' button appears.")
    except:
        print(f"🔴 'X' button doesn't appear.")

def FUN_click_X_button_on_hamburger_menu():
    time.sleep(0.5)
    try:
        hamburger_X_button = VAR_browser.find_element(By.XPATH, LOC_X_button)
        time.sleep(0.25)
        hamburger_X_button.click()
    except:
        print(f"❗ 'X' button could not be clicked.")

def FUN_validate_shopping_cart_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_Shopping_Cart_button), f"🔴 Shopping Cart button doesn't appear."
        print(f"🟢 Shopping Cart button appears.")
    except:
        print(f"🔴 Shopping Cart button doesn't appear.")

def FUN_validate_names_of_existing_products():
    time.sleep(0.5)
    try:
        all_existing_product_names = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_names)
        assert len(all_existing_product_names) == 6, f"🔴 The number of product names is not as expected"
        print(f"🟢 The number of product names is as expected")
    except:
        print(f"🔴 The number of product names is not as expected")




def FUN_validate_descriptions_of_existing_products():
    time.sleep(0.5)
    try:
        all_existing_product_descriptions = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_descriptions)
        assert len(all_existing_product_descriptions) == 6, f"🔴 The number of product descriptions is not as expected"
        print(f"🟢 The number of product descriptions is as expected")
    except:
        print(f"🔴 The number of product descriptions is not as expected")



def FUN_validate_pictures_of_existing_products():
    time.sleep(0.5)
    try:
        all_existing_product_pictures = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_pictures)
        assert len(all_existing_product_pictures) == 6, f"🔴 The number of product pictures is not as expected"
        print(f"🟢 The number of product pictures is as expected")
    except:
        print(f"🔴 The number of product pictures is not as expected")



def FUN_validate_prices_of_existing_products():
    time.sleep(0.5)
    try:
        all_existing_product_prices = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_prices)
        assert len(all_existing_product_prices) == 6, f"🔴 The number of product prices is not as expected"
        print(f"🟢 The number of product prices is as expected")
    except:
        print(f"🔴 The number of product prices is not as expected")



def FUN_validate_add_to_cart_of_existing_products():
    time.sleep(0.5)
    try:
        all_existing_product_add_to_card_buttons = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_add_to_cart)
        assert len(all_existing_product_add_to_card_buttons) == 6, f"🔴 The number of product add-to-cart buttons is not as expected"
        print(f"🟢 The number of product add-to-cart buttons is as expected")
    except:
        print(f"🔴 The number of product add-to-cart buttons is not as expected")

def FUN_validate_readable_product_price():
    time.sleep(0.5)
    passed = True
    try:
        all_existing_product_prices = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_prices)

        for price in all_existing_product_prices:
            digits_after_decimal = price.text[price.text.find('.') + 1:]
            if (len(str(digits_after_decimal)) > 2):
                passed = False
                break

        assert passed == True, f"🔴 Not all prices of all products are readable"
        print(f"🟢 All prices of all products are readable")
    except:
        print(f"🔴 Not all prices of all products are readable")

def FUN_click_add_to_cart_one_random_item():
    time.sleep(0.5)
    try:
        all_existing_product_add_to_card_buttons = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_add_to_cart)
        rndm_button_number = random.randint(1, len(all_existing_product_add_to_card_buttons))
        time.sleep(0.25)
        all_existing_product_add_to_card_buttons[rndm_button_number].click()
    except:
        print(f"❗ Could not click on randomly selected 'add-to-cart' item")

def FUN_validate_random_single_button_became_remove():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_single_random_remove), f"🔴 'REMOVE' button doesn't appear."
        print(f"🟢 'REMOVE' button appears.")
    except:
        print(f"🔴 'REMOVE' button doesn't appear.")

def FUN_validate_filtering_button_exists():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_filtering_button), f"🔴 Item filter button doesn't appear."
        print(f"🟢 Item filter button appears.")
    except:
        print(f"🔴 Item filter button doesn't appear.")

def FUN_click_on_filtering_button():
    time.sleep(0.5)
    try:
        item_filtering_button =  VAR_browser.find_element(By.XPATH, LOC_filtering_button)
        time.sleep(0.25)
        item_filtering_button.click()
    except:
        print(f"❗ Could not click on item filtering button")

def FUN_validate_az_filtering_option():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_filtering_az_option), f"🔴 'a-z' filtering option doesn't appear."
        print(f"🟢 'a-z' filtering option appears.")
    except:
        print(f"🔴 'a-z' filtering option doesn't appear.")


def FUN_validate_za_filtering_option():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_filtering_za_option), f"🔴 'z-a' filtering option doesn't appear."
        print(f"🟢 'z-a' filtering option appears.")
    except:
        print(f"🔴 'z-a' filtering option doesn't appear.")




def FUN_validate_lowhigh_filtering_option():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_filtering_lowhigh_option), f"🔴 'low-high' filtering option doesn't appear."
        print(f"🟢 'low-high' filtering option appears.")
    except:
        print(f"🔴 'low-high' filtering option doesn't appear.")

def FUN_validate_highlow_filtering_option():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_filtering_highlow_option), f"🔴 'high-low' filtering option doesn't appear."
        print(f"🟢 'high-low' filtering option appears.")
    except:
        print(f"🔴 'high-low' filtering option doesn't appear.")

def FUN_click_on_az_filter():
    time.sleep(0.5)
    try:
        az_filter_button = VAR_browser.find_element(By.XPATH, LOC_filtering_az_option)
        time.sleep(0.25)
        az_filter_button.click()
        VAR_actions.send_keys(Keys.ESCAPE)
        VAR_actions.perform()
    except:
        print("❗ 'az' filter button could not get clicked on")

def FUN_click_on_za_filter():
    time.sleep(0.5)
    try:
        za_filter_button = VAR_browser.find_element(By.XPATH, LOC_filtering_za_option)
        time.sleep(0.25)
        za_filter_button.click()
        VAR_actions.send_keys(Keys.ESCAPE)
        VAR_actions.perform()
    except:
        print("❗ 'za' filter button could not get clicked on")

def FUN_click_on_lowhigh_filter():
    time.sleep(0.5)
    try:
        lowhigh_filter_button = VAR_browser.find_element(By.XPATH, LOC_filtering_lowhigh_option)
        time.sleep(0.25)
        lowhigh_filter_button.click()
        VAR_actions.send_keys(Keys.ESCAPE)
        VAR_actions.perform()
    except:
        print("❗ 'low-high' filter button could not get clicked on")

def FUN_click_on_highlow_filter():
    time.sleep(0.5)
    try:
        highlow_filter_button = VAR_browser.find_element(By.XPATH, LOC_filtering_highlow_option)
        time.sleep(0.25)
        highlow_filter_button.click()
        VAR_actions.send_keys(Keys.ESCAPE)
        VAR_actions.perform()
    except:
        print("❗ 'high-low' filter button could not get clicked on")

def FUN_validate_item_order_by_az():
    time.sleep(0.5)
    passed = True
    list_names = []
    try:
        all_item_names = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_names)
        time.sleep(0.25)
        for name in all_item_names:
            list_names.append(name.text)
        for cnt in range(0, len(list_names) - 1, 1):
            if (list_names[cnt] > list_names[cnt + 1]):
                passed = False
                break
        assert passed == True, f"🔴 The items are not listed by a-z order"
        print(f"🟢 The items are listed by a-z order")
    except:
        print(f"🔴 The items are not listed by a-z order")

def FUN_validate_item_order_by_za():
    time.sleep(0.5)
    passed = True
    list_names = []
    try:
        all_item_names = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_names)
        time.sleep(0.25)
        for name in all_item_names:
            list_names.append(name.text)
        for cnt in range(0, len(list_names) - 1, 1):
            if (list_names[cnt] < list_names[cnt + 1]):
            #if (list_names[cnt] > list_names[cnt + 1]):
                passed = False
                break
        assert passed == True, f"🔴 The items are not listed by z-a order"
        print(f"🟢 The items are listed by z-a order")
    except:
        print(f"🔴 The items are not listed by z-a order")

def FUN_validate_item_order_by_lowhigh():
    time.sleep(0.5)
    passed = True
    list_prices = []
    try:
        all_item_prices = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_prices)
        time.sleep(0.25)
        for price in all_item_prices:
            list_prices.append(float(price.text[price.text.find('$') + 1:]))
        #print(list_prices)
        for cnt in range(0, len(list_prices) - 1, 1):
            if (list_prices[cnt] > list_prices[cnt + 1]):
                passed = False
                break
        assert passed == True, f"🔴 The items are not listed by low-high price order"
        print(f"🟢 The items are listed by low-high price order")
    except:
        print(f"🔴 The items are not listed by low-high price order")

def FUN_validate_item_order_by_highlow():
    time.sleep(0.5)
    passed = True
    list_prices = []
    try:
        all_item_prices = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_prices)
        time.sleep(0.25)
        for price in all_item_prices:
            list_prices.append(float(price.text[price.text.find('$') + 1:]))
        #print(list_prices)
        for cnt in range(0, len(list_prices) - 1, 1):
            if (list_prices[cnt] < list_prices[cnt + 1]):
                passed = False
                break
        assert passed == True, f"🔴 The items are not listed by high-low price order"
        print(f"🟢 The items are listed by high-low price order")
    except:
        print(f"🔴 The items are not listed by high-low price order")

def FUN_click_shopping_cart_icon():
    time.sleep(0.5)
    try:
        Shopping_Cart_icon = VAR_browser.find_element(By.XPATH, LOC_Shopping_Cart_button)
        time.sleep(0.25)
        Shopping_Cart_icon.click()
    except:
        print("❗ 'Shopping-Cart' Icon could not get clicked on")

def FUN_click_continue_shopping_button():
    time.sleep(0.5)
    try:
        continue_shopping_button = VAR_browser.find_element(By.XPATH, LOC_continue_shopping_button)
        time.sleep(0.25)
        continue_shopping_button.click()
    except:
        print("❗ 'Shopping-Cart' Icon could not get clicked on")

def FUN_validate_previous_filter_selected():
    time.sleep(1)
    item_filtering_button =  VAR_browser.find_element(By.XPATH, LOC_filtering_button)
    try:
        assert item_filtering_button.text == "Name (A to Z)", f"🔴 Filter-setting is different than before navigating."
        print(f"🟢 Filter-setting is the same as before navigating.")
    except:
        print(item_filtering_button.text)
        print(f"🔴 Filter-setting is different than before navigating.")

def FUN_add_specifically_random_number_of_items_to_cart(rndm):
    time.sleep(1)
    try:
        all_existing_product_add_to_card_buttons = VAR_browser.find_elements(By.XPATH, LOC_all_existing_product_add_to_cart)
        for cnt in range(rndm):
            all_existing_product_add_to_card_buttons[cnt].click()
        #print(f"rndm was: {rndm}")
        #time.sleep(500000)
    except:
        print("❗ Could not add {rndm} items to cart.")

def FUN_LOCout():
    time.sleep(1)
    try:
        FUN_click_on_hamburger_menu()
        FUN_click_LOCout_in_hamburger_menu()
    except:
        print(f"❗ Could not LOCout from the application.")

def FUN_validate_specifically_random_number_of_items_added_to_cart(rndm):
    time.sleep(1)
    try:
        item_count = VAR_browser.find_element(By.XPATH, LOC_Shopping_Cart_item_count)
        time.sleep(0.25)
        assert int(item_count.text) == int(rndm), f"🔴 Filter-setting is different than before navigating."
        print(f"🟢 Filter-setting is the same as before navigating.")
    except:
        print(item_count.text)
        print(f"🔴 Filter-setting is different than before navigating.")

def FUN_validate_zero_items_shopping_cart():
    time.sleep(1)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_Shopping_Cart_item_count), f"🟢 There are zero items in cart."
        print(f"🔴 There are more than zero items in cart.")
    except:
        print(f"🟢 There are zero items in cart.")

def FUN_validate_navigation_to_about_page():
    time.sleep(1)
    try:
        current_url = VAR_browser.current_url
        time.sleep(0.25)
        assert current_url == "https://saucelabs.com/", f"🔴 Application did not navigate to expected URL"
        print(f"🟢 Application navigated to expected URL")
    except:
        print(f"🔴 Application did not navigate to expected URL")

def FUN_validate_your_cart_header():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_continue_shopping_button), f"🔴 'Your Cart' header doesn't appear."
        print(f"🟢 'Your Cart' header appears.")
    except:
        print(f"🔴 'Your Cart' header doesn't appear.")

def FUN_click_on_remove_of_first_remove_button():
    time.sleep(1)
    try:
        # time.sleep(500000)
        all_remove_buttons = VAR_browser.find_elements(By.XPATH, LOC_all_remove_buttons)
        time.sleep(0.25)
        print(all_remove_buttons[0])
        all_remove_buttons[0].click()
        # time.sleep(500000)
    except:
        print(f"❗ Could not click on first remove button.")

def FUN_validate_one_less_items_in_shopping_cart_icon(rndm):
    time.sleep(1)
    try:
        if (rndm == 1):
            try:
                assert VAR_browser.find_element(By.XPATH, LOC_Shopping_Cart_item_count), f"🟢 There is one item less in the shopping cart"
                print(f"🔴 Number of items in shopping cart not as expected")
            except:
                print(f"🟢 There is one item less in the shopping cart")
        else:
            try:
                item_count = VAR_browser.find_element(By.XPATH, LOC_Shopping_Cart_item_count)
                assert int(item_count.text) == int(rndm - 1), f"🔴 Number of items in shopping cart not as expected"
                print(f"🟢 There is one item less in the shopping cart")
            except:
                # print(item_count.text)
                print(f"🔴 Number of items in shopping cart not as expected")
    except:
        print(f"🔴 Could not validate number of items in shopping cart.")

def FUN_select_random_filter_other_than_az():
    try:
        rndm = random.randint(2,4)
        if (rndm == 2):
            rndm_filter = VAR_browser.find_element(By.XPATH, LOC_filtering_za_option)
        elif (rndm == 3):
            rndm_filter = VAR_browser.find_element(By.XPATH, LOC_filtering_lowhigh_option)
        elif (rndm == 4):
            rndm_filter = VAR_browser.find_element(By.XPATH, LOC_filtering_highlow_option)
        time.sleep(0.25)
        rndm_filter.click()
        time.sleep(0.25)
        VAR_actions.send_keys(Keys.ESCAPE)
        VAR_actions.perform()
        time.sleep(0.75)
    except:
        print(f"❗ Could not click on randomly selected filter button.")

def FUN_validate_qty_in_your_cart_page():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_qty_text), f"🔴 'QTY' text doesn't appear."
        print(f"🟢 'QTY' text appears.")
    except:
        print(f"🔴 'QTY' text doesn't appear.")

def FUN_validate_description_in_your_cart_page():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_description_text), f"🔴 'DESCRIPTION' text doesn't appear."
        print(f"🟢 'DESCRIPTION' text appears.")
    except:
        print(f"🔴 'DESCRIPTION' text doesn't appear.")

def FUN_validate_continue_shopping_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_continue_shopping_button), f"🔴 'CONTINUE SHOPPING' button doesn't appear."
        print(f"🟢 'CONTINUE SHOPPING' button appears.")
    except:
        print(f"🔴 'CONTINUE SHOPPING' button doesn't appear.")

def FUN_validate_checkout_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_checkout_button), f"🔴 'CHECKOUT' button doesn't appear."
        print(f"🟢 'CHECKOUT' button appears.")
    except:
        print(f"🔴 'CHECKOUT' button doesn't appear.")

def FUN_click_checkout_button():
    time.sleep(0.5)
    try:
        checkout_button = VAR_browser.find_element(By.XPATH, LOC_checkout_button)
        time.sleep(0.25)
        checkout_button.click()
    except:
        print("❗ 'Checkout' button could not get clicked on")

def FUN_validate_hamburger_menu_closed():
    time.sleep(0.5)
    try:
        FUN_click_continue_shopping_button()
        time.sleep(0.5)
        products_header = VAR_browser.find_element(By.XPATH, LOC_products_header)
        assert products_header.text == "Products", f"🔴 Hamburger menu was not closed."
        print("🟢 Hamburger Menu has been closed.")
    except:
        print(f"🔴 Hamburger menu was not closed.")\
        
def FUN_valdiate_first_name_field():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_first_name_input), f"🔴 'First Name' field doesn't appear."
        print(f"🟢 'First Name' field appears.")
    except:
        print(f"🔴 'First Name' field doesn't appear.")

def FUN_valdiate_last_name_field():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_last_name_input), f"🔴 'Last Name' field doesn't appear."
        print(f"🟢 'Last Name' field appears.")
    except:
        print(f"🔴 'Last Name' field doesn't appear.")

def FUN_validate_zip_postal_code_field():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_zip_postal_input), f"🔴 'Zip/Postal Code' field doesn't appear."
        print(f"🟢 'Zip/Postal Code' field appears.")
    except:
        print(f"🔴 'Zip/Postal Code' field doesn't appear.")

def FUN_validate_cancel_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_cancel_button), f"🔴 'Cancel' button doesn't appear."
        print(f"🟢 'Cancel' button appears.")
    except:
        print(f"🔴 'Cancel' button doesn't appear.")

def FUN_validate_continue_button():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_continue_button), f"🔴 'Continue' button doesn't appear."
        print(f"🟢 'Continue' button appears.")
    except:
        print(f"🔴 'Continue' button doesn't appear.")

def FUN_click_on_continue_button():
    time.sleep(0.5)
    try:
        continue_button = VAR_browser.find_element(By.XPATH, LOC_continue_button)
        time.sleep(0.25)
        continue_button.click()
    except:
        print("❗ 'Continue' button could not get clicked on")

def FUN_click_cancel_button():
    time.sleep(0.5)
    try:
        cancel_button = VAR_browser.find_element(By.XPATH, LOC_cancel_button)
        time.sleep(0.25)
        cancel_button.click()
    except:
        print("❗ 'Cancel' button could not get clicked on")

def FUN_validate_error_of_first_name_missing():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_firstname_missing_error), f"🔴 First-Name error message doesn't appear."
        print(f"🟢 First-Name error message appears.")
    except:
        print(f"🔴 First-Name error message doesn't appear.")

def FUN_validate_error_of_last_name_missing():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_lastname_missing_error), f"🔴 Last-Name error message doesn't appear."
        print(f"🟢 Last-Name error message appears.")
    except:
        print(f"🔴 Last-Name error message doesn't appear.")

def FUN_validate_error_of_zip_postal_code_missing():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_postalcode_missing_error), f"🔴 Zip-Postal code error message doesn't appear."
        print(f"🟢 Zip-Postal code error message appears.")
    except:
        print(f"🔴 Zip-Postal code error message doesn't appear.")

def FUN_insert_first_name():
    time.sleep(0.5)
    try:
        first_name_field = VAR_browser.find_element(By.XPATH, LOC_first_name_input)
        time.sleep(0.25)
        first_name_field.send_keys("first")
    except:
        print("❗ Could not insert text into 'First Name' field.")

def FUN_insert_last_name():
    time.sleep(0.5)
    try:
        last_name_field = VAR_browser.find_element(By.XPATH, LOC_last_name_input)
        time.sleep(0.25)
        last_name_field.send_keys("last")
    except:
        print("❗ Could not insert text into 'Last Name' field.")

def FUN_insert_zip_postal_code():
    time.sleep(0.5)
    try:
        last_name_field = VAR_browser.find_element(By.XPATH, LOC_zip_postal_input)
        time.sleep(0.25)
        last_name_field.send_keys("123456")
    except:
        print("❗ Could not insert text into 'Zip/Postal Code' field.")

def FUN_validate_payment_information_text():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_payment_information_text), f"🔴 'Payment Information' text doesn't appear."
        print(f"🟢 'Payment Information' text appears.")
    except:
        print(f"🔴 'Payment Information' text doesn't appear.")

def FUN_validate_sauce_card_text():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_sauce_card_text), f"🔴 Sauce Card text doesn't appear."
        print(f"🟢 Sauce Card text appears.")
    except:
        print(f"🔴 Sauce Card text doesn't appear.")

def FUN_validate_shipping_information_text():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_shipping_information_text), f"🔴 Shipping Information text doesn't appear."
        print(f"🟢 Shipping Information text appears.")
    except:
        print(f"🔴 Shipping Information text doesn't appear.")

def FUN_validate_free_pony_text():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_free_pony_text), f"🔴 'Free Pony' text doesn't appear."
        print(f"🟢 'Free Pony' text appears.")
    except:
        print(f"🔴 'Free Pony' text doesn't appear.")

def FUN_get_bill_from_summing_up_selected_items():
    time.sleep(0.5)
    try:
        accum_sums = int(0)
        prices_of_selected_items = VAR_browser.find_elements(By.XPATH, LOC_prices_of_selected_items)
        for cnt in range(0, len(prices_of_selected_items), 1):
            accum_sums += float(prices_of_selected_items[cnt].text[prices_of_selected_items[cnt].text.find('$') + 1:])
        #print(f"accum_sums is: {accum_sums}")
        return accum_sums
    except:
        print("❗ Could not sum up the prices of the selected items.")

def FUN_validate_accumulated_price_to_item_total_in_overview(accum_bill):
    time.sleep(0.5)
    try:
        item_total_text = VAR_browser.find_element(By.XPATH, LOC_item_total_text)
        time.sleep(0.25)
        item_total_text = item_total_text.text[item_total_text.text.find('$') + 1:]
        #print(item_total_text)
        assert float(accum_bill) == float(item_total_text), f"🔴 The accumulated sum and the item total bill are not equal"
        print(f"🟢 The accumulated sum and the item total bill are equal")
    except:
        print(f"🔴 The accumulated sum and the item total bill are not equal")

def FUN_get_descriptions_of_added_items():
    time.sleep(0.5)
    try:
        descriptions_list = []
        descriptions_of_selected_items = VAR_browser.find_elements(By.XPATH, LOC_descriptions_of_selected_items)
        for cnt in range(0, len(descriptions_of_selected_items), 1):
            descriptions_list.append(descriptions_of_selected_items[cnt].text)
        return descriptions_list
    except:
        print("❗ Could not sum up the prices of the selected items.")

def FUN_validate_descriptions_of_added_items_in_overview(list_collected_descriptions):
    time.sleep(0.5)
    try:
        all_actual_descriptions = []
        all_actual_descriptions_raw = VAR_browser.find_elements(By.XPATH, LOC_selected_item_descriptions)
        for cnt in range(0, len(all_actual_descriptions_raw), 1):
            all_actual_descriptions.append(all_actual_descriptions_raw[cnt].text)
        #print(f"list 1: {list_collected_descriptions}")
        #print(f"list 2: {all_actual_descriptions}")
        assert list_collected_descriptions == all_actual_descriptions, f"🔴 listed descripions in overview page are idential to the list of accumulated descriptions."
        print(f"🟢 listed descripions in overview page are idential to the list of accumulated descriptions.")
    except:
        print(f"🔴 listed descripions in overview page are idential to the list of accumulated descriptions.")

def FUN_click_finish_button():
    time.sleep(0.5)
    try:
        finish_button = VAR_browser.find_element(By.XPATH, LOC_finished_button)
        time.sleep(0.5)
        finish_button.click()
    except:
        print(f"❗ Finish button could not be clicked.")

def FUN_validate_finish_header():
    time.sleep(0.5)
    try:
        finish_header = VAR_browser.find_element(By.XPATH, LOC_finish_header)
        assert finish_header.text == "Finish", f"🔴 'FINISH' header did not appear."
        print("🟢 'FINISH' header did appear")
    except:
        print(f"🔴 'FINISH' header did not appear.")

def FUN_validate_thank_you_header():
    time.sleep(0.5)
    try:
        thank_you_header = VAR_browser.find_element(By.XPATH, LOC_thank_you_header)
        assert thank_you_header.text == "THANK YOU FOR YOUR ORDER", f"🔴 'Thank You' header did not appear."
        print("🟢 'Thank You' header did appear")
    except:
        print(f"🔴 'Thank You' header did not appear.")

def FUN_validate_dispatch_text():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_dispatched_text), f"🔴 Dispatch text doesn't appear."
        print(f"🟢 Dispatch text appears.")
    except:
        print(f"🔴 Dispatch text doesn't appear.")

def FUN_validate_big_pony_express_image():
    time.sleep(0.5)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_big_pony_express_image), f"🔴 Big Pony Express image doesn't appear."
        print(f"🟢 Big Pony Express image appears.")
    except:
        print(f"🔴 Big Pony Express image doesn't appear.")

def FUN_validate_no_items_in_shopping_cart():
    time.sleep(1)
    try:
        assert VAR_browser.find_element(By.XPATH, LOC_all_remove_buttons), f"🟢 There aren't any items in the 'Your Cart' page."
        print(f"🔴 There are items in the 'Your Cart' page.")
    except:
        print(f"🟢 There aren't any items in the 'Your Cart' page.")