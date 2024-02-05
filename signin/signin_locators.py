class SignInPageLocators:
    sign_in_heading_css = '[class="flex flex-col "] div:first-child'
    instruction_sign_in_css = '[class="flex flex-col "] div:last-child'
    txt_phone_number_css = 'label[for="Phone number"]'
    number_field_id = 'Phone number'
    send_code_button_xpath = '//button//div[@class="flex gap-1 items-center"]'
    password_input_name = 'password'
    instruction_phone_xpath = ("//div[text()='We would send you a verification code to confirm this is your phone "
                               "number.']")
    text_verification_code_css = 'label[for="Verification code"]'
    instruction_ver_code = '//div[text()="Enter the verification code sent to your phone number."]'
    sign_in_button = "//button[text()='Sign in']"
    phone_text_box = '[class="relative flex items-center "] input'
    alert_invalid_css = 'small[class*="text-danger"]'
    otp_txt_box_name = 'otp'
    google_link_id = "custom-google-login-btn"
    facebook_link_xpath = "//div[contains(text(), 'Facebook')]"
    apple_link_xpath = "//div[contains(text(), 'Apple')]"
    resend_code_xpath = "//div[text() = 'Resend code']"

