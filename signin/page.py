from signin import locators as lo
from helpers.base_page import *


class SignInPage(CommonClass):

    def title_page(self):
        actual_title = self.driver.title
        return actual_title

    def sign_in_text(self):
        text = self.get_text_from_element('CSS_SELECTOR', lo.sign_in_heading_css)
        return text

    def send_phone(self, text):
        self.send_keys_to_element('CSS_SELECTOR', lo.phone_text_box, "")
        self.send_keys_to_element('CSS_SELECTOR', lo.phone_text_box, text)

    def click_send_button(self):
        self.click_element('XPATH', lo.send_code_button_xpath)

    def txt_instruct_sign_in(self):
        text = self.get_text_from_element('CSS_SELECTOR', lo.instruction_sign_in_css)
        return text

    def text_phone_number(self):
        text = self.get_text_from_element('CSS_SELECTOR', lo.txt_phone_number_css)
        return text

    def instruct_phone(self):
        text = self.get_text_from_element('XPATH', lo.instruction_phone_xpath)
        return text

    def txt_verification_code(self):
        self.get_text_from_element('CSS_SELECTOR', lo.text_verification_code_css)

    def instruction_verify_code(self):
        self.get_text_from_element('XPATH', lo.instruction_ver_code)

    def alert_for_invalid_num(self):
        text = self.get_text_from_element('CSS_SELECTOR', lo.alert_invalid_css)
        return text

    def send_code(self, text):
        self.send_keys_to_element('NAME', lo.otp_txt_box_name, text)

    def click_sign_in_btn(self):
        self.click_element('XPATH', lo.sign_in_button)

    def click_apple_link(self):
        self.click_element('XPATH', lo.apple_link_xpath)

    def click_google_link(self):
        self.click_element('ID', lo.google_link_id)

    def click_facebook_link(self):
        self.click_element('XPATH', lo.facebook_link_xpath)

    def click_resend_button(self):
        self.click_element('XPATH', lo.resend_code_xpath)

    def send_password(self, text):
        self.send_keys_to_element('NAME', lo.password_input_name, text)
