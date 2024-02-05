import signin_locators
from pageObjects.base_page import CommonClass


class SignInPage(CommonClass):
    spl = SignInPageLocators

    def title_page(self):
        actual_title = self.driver.title
        return actual_title

    def sign_in_text(self):
        text = self.get_text_from_element('CSS_SELECTOR', self.spl.sign_in_heading_css)
        return text

    def send_phone(self, text):
        self.send_keys_to_element('CSS_SELECTOR', self.spl.phone_text_box, "")
        self.send_keys_to_element('CSS_SELECTOR', self.spl.phone_text_box, text)

    def click_send_button(self):
        self.click_element('XPATH', self.spl.send_code_button_xpath)

    def txt_instruct_sign_in(self):
        text = self.get_text_from_element('CSS_SELECTOR', self.spl.instruction_sign_in_css)
        return text

    def text_phone_number(self):
        text = self.get_text_from_element('CSS_SELECTOR', self.spl.txt_phone_number_css)
        return text

    def instruct_phone(self):
        text = self.get_text_from_element('XPATH', self.spl.instruction_phone_xpath)
        return text

    def txt_verification_code(self):
        self.get_text_from_element('CSS_SELECTOR', self.spl.text_verification_code_css)

    def instruction_verify_code(self):
        self.get_text_from_element('XPATH', self.spl.instruction_ver_code)

    def alert_for_invalid_num(self):
        text = self.get_text_from_element('CSS_SELECTOR', self.spl.alert_invalid_css)
        return text

    def send_code(self, text):
        self.send_keys_to_element('NAME', self.spl.otp_txt_box_name, text)

    def click_sign_in_btn(self):
        self.click_element('XPATH', self.spl.sign_in_button)

    def click_apple_link(self):
        self.click_element('XPATH', self.spl.apple_link_xpath)

    def click_google_link(self):
        self.click_element('ID', self.spl.google_link_id)

    def click_facebook_link(self):
        self.click_element('XPATH', self.spl.facebook_link_xpath)

    def click_resend_button(self):
        self.click_element('XPATH', self.spl.resend_code_xpath)

    def send_password(self, text):
        self.send_keys_to_element('NAME', self.spl.password_input_name, text)
