from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from all_functions import *

#✅test 1 - Attempt to navigate to some invalid URL withing the app
def TEST_navigate_invalid_url():
    FUN_open_app_invalid_url()
    FUN_validate_not_in_Login_page()
    FUN_finish_test()
#TEST_navigate_invalid_url()


#✅test 2 - Confirm that username, password field and Login button are present in the Login page.
def TEST_validate_username_password_Login():
    FUN_open_app_valid_url()
    FUN_validate_username_field()
    FUN_validate_password_field()
    FUN_validate_login_button()
    FUN_finish_test()
#TEST_validate_username_password_Login()


#✅test 3 - Confirm the red robot picture exists in the webpage.
def TEST_validate_robot_picture_Login_page():
    FUN_open_app_valid_url()
    FUN_validate_robot_picture_exists()
    FUN_finish_test()
#TEST_validate_robot_picture_Login_page()


#✅test 4 - Use the locked-out credentials user to attempt to Login and validate "Epic sadface: Sorry, this user has been locked out." error message.
def TEST_locked_out_user_error_message_validation():
    FUN_open_app_valid_url()
    FUN_login_with_locked_user()
    FUN_validate_error_message_locked_user()
    FUN_finish_test()
#TEST_locked_out_user_error_message_validation()


#✅test 5 - Use completely made up credentials user to attempt to Login and validate "Epic sadface: Username and password do not match any user in this service" error message.
def TEST_Login_invalid_credentials_error_message_validation():
    FUN_open_app_valid_url()
    FUN_login_invalid_credentials()
    FUN_validate_error_message_invalid_user()
    FUN_finish_test()
#TEST_Login_invalid_credentials_error_message_validation()


#✅test 6 - Validate "products" header exists
def TEST_validate_products_header():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_validate_products_header_appears()
    FUN_finish_test()
#TEST_validate_products_header()


#✅test 7 - Validate footer of webpage exists and the date it correct (note - it's actually incorrect)
def TEST_validate_footer_products_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_go_to_footer()
    FUN_validate_footer_of_current_page()
    FUN_finish_test()
#TEST_validate_footer_products_page()


#✅test 8 - Validate footer picture of white robot is present
def TEST_validate_white_robot_products_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_go_to_footer()
    FUN_validate_white_robot_products_page()
    FUN_finish_test()
#TEST_validate_white_robot_products_page()


#✅test 9 - Validate buttons' of social media exist (Twitter / Facebook / LinkedIn)
def TEST_validate_social_media_buttons_product_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_go_to_footer()
    FUN_validate_twitter_button()
    FUN_validate_facebook_button()
    FUN_validate_linkedin_button()
    FUN_finish_test()
#TEST_validate_social_media_buttons_product_page()


#✅test 10 - Validate hamburger menu on left side exists
def TEST_validate_hamburger_menu_product_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_validate_hamburger_menu()
    FUN_finish_test()
#TEST_validate_hamburger_menu_product_page()


#✅test 11 - Validate 4 options that should appear after clicking on the hamburger menu.
def TEST_validate_four_hamburger_menu_buttons():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_hamburger_menu()
    FUN_validate_all_items_button()
    FUN_validate_about_button()
    FUN_validate_LOCout_button()
    FUN_validate_reset_app_state_button()
    FUN_finish_test()
#TEST_validate_four_hamburger_menu_buttons()


#✅test 12 - Validate X button exists after opening the left menu.
def TEST_validate_X_button_on_hamburger_menu():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_hamburger_menu()
    FUN_validate_X_button_on_hamburger_menu()
    FUN_finish_test()
#TEST_validate_X_button_on_hamburger_menu()


#✅test 13 - Validate shopping cart icon exists
def TEST_validate_shopping_cart_icon():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_validate_shopping_cart_button()
    FUN_finish_test()
#TEST_validate_shopping_cart_icon()


#✅test 14 - Validate that for every product, there is:
#	a. A name (header)
#	b. A description
#	c. A picture
#	d. A price
#	e. A button to add to cart
def TEST_validate_name_description_picture_price_add_to_cart_for_every_product():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_validate_names_of_existing_products()
    FUN_validate_descriptions_of_existing_products()
    FUN_validate_pictures_of_existing_products()
    FUN_validate_prices_of_existing_products()
    FUN_validate_add_to_cart_of_existing_products()
    FUN_finish_test()
#TEST_validate_name_description_picture_price_add_to_cart_for_every_product()


#✅test 15 - Validate prices are in reasonable number (only 2 digits after the decimal dot).
def TEST_validate_readable_product_price():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_validate_readable_product_price()
    FUN_finish_test()
#TEST_validate_readable_product_price()


#✅test 16 - Click on a "ADD TO CART" button, and confirm that the text became "REMOVE".
def TEST_validate_remove_after_click():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_add_to_cart_one_random_item()
    FUN_validate_random_single_button_became_remove()
    FUN_finish_test()
#TEST_validate_remove_after_click()


#✅test 17 - Validate the Filtering button is present
def TEST_validate_filtering_button_exists():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_validate_filtering_button_exists()
    FUN_finish_test()
#TEST_validate_filtering_button_exists()


#✅test 18 - Click on the filtering option on the right, and confirm that there are 4 options to filter.
def TEST_confirm_four_filtering_buttons():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_filtering_button()
    FUN_validate_az_filtering_option()
    FUN_validate_za_filtering_option()
    FUN_validate_lowhigh_filtering_option()
    FUN_validate_highlow_filtering_option()
    FUN_finish_test()
#TEST_confirm_four_filtering_buttons()


#✅test 19 - Select "Name (A to Z)" option - and confirm all items ordered by A to Z.
def TEST_validate_item_order_after_az_filter_selection():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_filtering_button()
    FUN_click_on_az_filter()
    FUN_validate_item_order_by_az()
    FUN_finish_test()
#TEST_validate_item_order_after_az_filter_selection()


#✅test 20 - Select "Name (Z to A)" option - and confirm all items ordered by Z to A.
def TEST_validate_item_order_after_za_filter_selection():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_filtering_button()
    FUN_click_on_za_filter()
    FUN_validate_item_order_by_za()
    FUN_finish_test()
#TEST_validate_item_order_after_za_filter_selection()


#✅test 21 - Select "Price (low to high)" option - and confirm all items ordered by price - low to high.
def TEST_validate_item_order_after_lowhigh_filter_selection():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_filtering_button()
    FUN_click_on_lowhigh_filter()
    FUN_validate_item_order_by_lowhigh()
    FUN_finish_test()
#TEST_validate_item_order_after_lowhigh_filter_selection()


#✅test 22 - Select "Price (high to low)" option - and confirm all items ordered by price - high to low.
def TEST_validate_item_order_after_highlow_filter_selection():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_filtering_button()
    FUN_click_on_highlow_filter()
    FUN_validate_item_order_by_highlow()
    FUN_finish_test()
#TEST_validate_item_order_after_highlow_filter_selection()


#✅test 23 - Select a random menu option - click on the shopping cart icon, then click "CONTINUE SHOPPING" at the checkout page, and once navigate back to "products" page, and confirm that the filtering is back to default (the default is "Name (A to Z)").
def TEST_validate_same_filtering_applied_after_navigating_backto_products():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_filtering_button()
    FUN_select_random_filter_other_than_az()
    #FUN_click_add_to_cart_one_random_item()
    FUN_click_shopping_cart_icon()
    FUN_click_continue_shopping_button()
    FUN_validate_item_order_by_az()
    FUN_finish_test()
#TEST_validate_same_filtering_applied_after_navigating_backto_products()


#✅test 24 - Add some items to the cart, store the red number next to the card inside a variable. LOCout of the current user. LOC back into the app with the same user, and validate number next to the cart icon is the same as the number stored inside the variable.
def TEST_validate_same_no_of_items_in_cart_after_Login():
    rndm = FUN_get_random_ranges(1,6)
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_add_specifically_random_number_of_items_to_cart(rndm)
    FUN_LOCout()
    FUN_login_with_standard_user()
    FUN_validate_specifically_random_number_of_items_added_to_cart(rndm)
    FUN_finish_test()
#TEST_validate_same_no_of_items_in_cart_after_Login()


#✅test 25 - Add "X" number of items to the cart, store the red number next to the card inside a variable. Remove one of the items from the cart, validate that the red number next to the cart is one less (X - 1) than the previous value which was stored inside a variable.
def validate_one_less_item_in_shopping_cart_after_one_removal():
    rndm = FUN_get_random_ranges(1,6)
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_add_specifically_random_number_of_items_to_cart(rndm)
    FUN_click_on_remove_of_first_remove_button()
    FUN_validate_one_less_items_in_shopping_cart_icon(rndm)
    FUN_finish_test()
#validate_one_less_item_in_shopping_cart_after_one_removal()


#✅test 26 - Click on the hamburger menu, click on the "All Items" button, and confirm app redirected back to "Products" section.
def TEST_validate_redirection_to_products_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_hamburger_menu()
    FUN_click_all_items_in_hamburger_menu()
    FUN_validate_products_header_appears()
    FUN_finish_test()
#TEST_validate_redirection_to_products_page()


#✅test 27 - Select a few items to add to cart, then click on the hamburger menu, and then click on the "reset app state", then close the hamburger menu with the "X" icon, and validate number next to cart icon doesn't appear.
def TEST_validate_reset_app_state_zeroes_shopping_cart_icon():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_add_to_cart_one_random_item()
    FUN_click_on_hamburger_menu()
    FUN_click_reset_app_state_in_hamburger_menu()
    FUN_click_X_button_on_hamburger_menu()
    FUN_validate_zero_items_shopping_cart()
    FUN_finish_test()
#TEST_validate_reset_app_state_zeroes_shopping_cart_icon()
    

#✅test 28 - Click on the hamburger menu, click on the "About" button, and validate redirection to the "https://saucelabs.com/" site.
def TEST_validate_navigation_to_about_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_on_hamburger_menu()
    FUN_click_about_in_hamburger_menu()
    FUN_validate_navigation_to_about_page()
    FUN_finish_test()
#TEST_validate_navigation_to_about_page()


#✅test 29 - Click on the hamburger menu, click on the "LOCout" button, and confirm that app is redirected to the Login page.
def validate_Login_page_after_LOCging_out():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_LOCout()
    FUN_validate_in_Login_page()
    FUN_finish_test()
#validate_Login_page_after_LOCging_out()


#✅test 30 - Click on the shopping cart icon, and validate "Your cart" header appears.
def TEST_validate_your_cart_header():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_validate_your_cart_header()
    FUN_finish_test()
#TEST_validate_your_cart_header()



#✅test 31 - Click on the shopping cart icon, and validate footer year and other text
def TEST_validate_footer_of_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_go_to_footer()
    FUN_validate_footer_of_current_page()
    FUN_finish_test()
#TEST_validate_footer_of_your_cart_page()


#✅test 32 - Validate footer picture of white robot is present
def TEST_validate_white_robot_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_go_to_footer()
    FUN_validate_white_robot_current_page()
    FUN_finish_test()
#TEST_validate_white_robot_your_cart_page()

#✅test 33 - Click on the shopping cart icon, and validate presence of "QTY" and "DESCRIPTION"
def TEST_validate_qty_and_description_in_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_validate_qty_in_your_cart_page()
    FUN_validate_description_in_your_cart_page()
    FUN_finish_test()
#TEST_validate_qty_and_description_in_your_cart_page()


#✅test 34 - Click on the shopping cart icon, and validate presence of "CONTINUE SHOPPING" button
def TEST_validate_continue_shopping_button_in_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_validate_continue_shopping_button()
    FUN_finish_test()
#TEST_validate_continue_shopping_button_in_your_cart_page()

#✅test 35 - Click on the shopping cart icon, and validate presence of "CHECKOUT" button
def TEST_validate_checkout_button_in_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_validate_checkout_button()
    FUN_finish_test()
#TEST_validate_checkout_button_in_your_cart_page()

#✅test 36 - Click on the shopping cart icon, and click on the "CONTINUE SHOPPING" button, and validate that redirected back to the products page.
def TEST_validate_products_header_after_clicking_continue_shopping():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_continue_shopping_button()
    FUN_validate_products_header_appears()
    FUN_finish_test()
#TEST_validate_products_header_after_clicking_continue_shopping()

#✅test 37 - Click on the shopping cart icon, and then click on the shopping cart icon again, and validate were on the same page.
def TEST_click_shopping_cart_in_your_cart_page_validate_same_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_shopping_cart_icon()
    FUN_validate_your_cart_header()
    FUN_finish_test()
#TEST_click_shopping_cart_in_your_cart_page_validate_same_page()

#✅test 38 - Click on the shopping cart icon, and then click on the hamburger menu, and validate 4 options present
def TEST_validate_four_hamburger_menu_buttons_in_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_on_hamburger_menu()
    FUN_validate_all_items_button()
    FUN_validate_about_button()
    FUN_validate_LOCout_button()
    FUN_validate_reset_app_state_button()
    FUN_finish_test()
#TEST_validate_four_hamburger_menu_buttons_in_your_cart_page()

#✅test 39 - Click on the shopping cart icon, and then click on the hamburger menu, and validate 4 "X" button present.
def TEST_validate_X_button_on_hamburger_menu_in_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_on_hamburger_menu()
    FUN_validate_X_button_on_hamburger_menu()
    FUN_finish_test()
#TEST_validate_X_button_on_hamburger_menu_in_your_cart_page()

#✅test 40 - Click on the shopping cart icon, and then click on the hamburger menu, and click on the "X" button and validate that menu is closed.
def TEST_validate_menu_closed_in_your_cart_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_on_hamburger_menu()
    FUN_click_X_button_on_hamburger_menu()
    FUN_validate_hamburger_menu_closed()
    FUN_click_shopping_cart_icon()
    FUN_finish_test()
#TEST_validate_menu_closed_in_your_cart_page()


#✅test 41 - Validate that the "First Name" text field appears.
def TEST_validate_first_name_field_in_checkout_page(): 
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_valdiate_first_name_field()
    FUN_finish_test()
#TEST_validate_first_name_field_in_checkout_page()

#✅test 42 - Validate that the "Last Name" text field appears.
def TEST_validate_last_name_field_in_checkout_page(): 
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_valdiate_last_name_field()
    FUN_finish_test()
#TEST_validate_last_name_field_in_checkout_page()

#✅test 43 - Validate that the "Zip/Postal code" text field appears.
def TEST_validate_zip_postal_code_field_in_checkout_page(): 
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_validate_zip_postal_code_field()
    FUN_finish_test()
#TEST_validate_zip_postal_code_field_in_checkout_page()


#✅test 44 - Validate that the "Cancel" button appears.
def TEST_validate_cancel_button_in_checkout_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_validate_cancel_button()
    FUN_finish_test()
#TEST_validate_cancel_button_in_checkout_page()

#✅test 45 - Click on the "Cancel" button - and validate that app redirected back to "Your Cart" page.
def TEST_validate_redirection_to_your_cart_page_after_cancel_button_clicked():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_click_cancel_button()
    FUN_validate_your_cart_header()
    FUN_finish_test()
#TEST_validate_redirection_to_your_cart_page_after_cancel_button_clicked()

#✅test 46 - Validate that the "Continue" button appears.
def TEST_validate_continue_button_in_checkout_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_validate_continue_button()
    FUN_finish_test()
#TEST_validate_continue_button_in_checkout_page()

#✅test 47 - Attempt to click on "Continue" without inserting a first name, and validate error message: "Error: First Name is required" appears.
def TEST_validate_first_name_missing_error_message():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_click_on_continue_button()
    FUN_validate_error_of_first_name_missing()
    FUN_finish_test()
#TEST_validate_first_name_missing_error_message()

#✅test 48 - Attempt to click on "Continue" after inserting a first name, but without inserting a last name and validate error message: "Error: Last Name is required" appears.
def TEST_validate_last_name_missing_error_message():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_click_on_continue_button()
    FUN_validate_error_of_last_name_missing()
    FUN_finish_test()
#TEST_validate_last_name_missing_error_message()

#✅test 49 - Attempt to click on "Continue" after inserting a first name and after inserting a last name, but without inserting a postal code and validate error message: "Error: Postal Code is required" appears.
def TEST_validate_zip_postal_code_missing_error_message():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_click_on_continue_button()
    FUN_validate_error_of_zip_postal_code_missing()
    FUN_finish_test()
#TEST_validate_zip_postal_code_missing_error_message()

#✅test 50 - Click the "Cancel" button and confirm redirection to the "Products" page.
def TEST_click_cancel_button_validate_redirection_to_products_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_click_cancel_button()
    FUN_validate_products_header_appears()
    FUN_finish_test()
#TEST_click_cancel_button_validate_redirection_to_products_page()


#✅test 51 - Validate "payment information" and "sauce card" values are present.
def TEST_validate_payyment_information_and_sauce_card_values():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_validate_payment_information_text()
    FUN_validate_sauce_card_text()
    FUN_finish_test()
#TEST_validate_payyment_information_and_sauce_card_values()

#✅test 52 - Validate "Shipping Information:" and "FREE PONY EXPRESS DELIVERY!" values are present.
def TEST_validate_shipping_information_and_free_pony_values_are_present():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_validate_shipping_information_text()
    FUN_validate_free_pony_text()
    FUN_finish_test()
#TEST_validate_shipping_information_and_free_pony_values_are_present()

#✅test 53 - Add random number of items to card, sum up the prices of all of them, do the process to proceed to checkout and then validate "Item total:" price is the total price of all items that have been added to cart.
def TEST_validate_final_bill_equal_price_all_selected_products():
    rndm = FUN_get_random_ranges(1,6)
    accum_bill = float(0)
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_add_specifically_random_number_of_items_to_cart(rndm)
    accum_bill = FUN_get_bill_from_summing_up_selected_items()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_validate_accumulated_price_to_item_total_in_overview(accum_bill)
    FUN_finish_test()
#TEST_validate_final_bill_equal_price_all_selected_products()


#✅test 54 - Add random number of items to card, sum up the prices of all of them, do the process to proceed to checkout and then validate that these items appear under "payment information" with the correct details of each of each of them.
def TEST_validate_details_of_added_items_in_overview():
    rndm = FUN_get_random_ranges(1,6)
    list_descriptions = []
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_add_specifically_random_number_of_items_to_cart(rndm)
    list_descriptions = FUN_get_descriptions_of_added_items()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_validate_descriptions_of_added_items_in_overview(list_descriptions)
    FUN_finish_test()
#TEST_validate_details_of_added_items_in_overview()


#✅test 55 - Validate the "Finish" header.
def TEST_validate_finish_header():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_click_finish_button()
    FUN_validate_finish_header()
    FUN_finish_test()
#TEST_validate_finish_header()


#✅test 56 - Validate that the header is: "THANK YOU FOR YOUR ORDER"
def TEST_validate_thank_you_header_in_finish_page():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_click_finish_button()
    FUN_validate_thank_you_header()
    FUN_finish_test()
#TEST_validate_thank_you_header_in_finish_page()

#✅test 57 - Validate the text: "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
def TEST_validate_dispatch_text():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_click_finish_button()
    FUN_validate_dispatch_text()
    FUN_finish_test()
#TEST_validate_dispatch_text()


#✅test 58 - Validate the big "Pony Express Sauce Labs" picture appearance
def TEST_validate_big_pony_express_image():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_click_finish_button()
    FUN_validate_big_pony_express_image()
    FUN_finish_test()
#TEST_validate_big_pony_express_image()

#✅test 59 - Validate that the shopping cart doesn't have a number next to it.
def TEST_validate_shopping_cart_doesnt_have_number():
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_click_finish_button()
    FUN_validate_zero_items_shopping_cart()
    FUN_finish_test()
#TEST_validate_shopping_cart_doesnt_have_number()

#✅test 60 - Click on the shopping cart icon, and validate that there are no items in the shopping cart.
def TEST_validate_no_items_in_shopping_cart_after_finish():
    rndm = FUN_get_random_ranges(1,6)
    FUN_open_app_valid_url()
    FUN_login_with_standard_user()
    FUN_add_specifically_random_number_of_items_to_cart(rndm)
    FUN_click_shopping_cart_icon()
    FUN_click_checkout_button()
    FUN_insert_first_name()
    FUN_insert_last_name()
    FUN_insert_zip_postal_code()
    FUN_click_on_continue_button()
    FUN_click_finish_button()
    FUN_click_shopping_cart_icon()
    FUN_validate_no_items_in_shopping_cart()
    FUN_finish_test()
#TEST_validate_no_items_in_shopping_cart_after_finish()