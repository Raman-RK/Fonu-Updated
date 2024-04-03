import time
import allure
import pytest
from signin.page import SignInPage
from utilities.read_properties import ReadConfig
from utilities.customlogger import LogGen
from helpers.conf_test import setup


class TestSignIn:
    @pytest.fixture(autouse=True)
    def var_setup(self, setup):
        self.driver = setup
        config_reader = ReadConfig()
        # Get configuration values
        self.baseURL = config_reader.get_application_url()
        self.number = config_reader.get_number()
        self.otp = config_reader.get_otp()
        self.invalid_number = config_reader.get_invalid_number()
        self.unregistered_number = config_reader.get_unregistered_number()
        self.invalid_verification_code = config_reader.invalid_verification_code()
        self.Title_website = config_reader.get_title()
        self.txt_sign_in = config_reader.text_sign_in()
        self.txt_number = config_reader.txt_phone_number()
        self.instruct_sign_in = config_reader.text_instruction_sig_in()
        self.instruct_phone = config_reader.txt_phone_instruction()
        self.txt_verify_code = config_reader.txt_verification_code()
        self.instruct_verify = config_reader.instruct_verify_code()
        self.alert_invalid = config_reader.alert_number_invalid()
        self.alert_unregistered = config_reader.alert_not_registered()
        self.logger = LogGen.loggen()

    @allure.feature('Title Verification')
    @allure.story('Verify Title')
    def test_title_verification(self, var_setup):
        print("Test method started")
        self.logger.info("__Test One.")
        self.logger.info("__Verifying Title.")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.sp = SignInPage(self.driver)
        act_title = self.driver.title
        self.logger.info("__ Title.")
        print(act_title)
        time.sleep(5)
        assert self.Title_website == act_title
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="Title is same",
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('Text Verification')
    @allure.story('Verify expected text with actual text')
    def test_text_assertion(self, setup):
        self.logger.info("____________Test Two__________")
        self.driver = setup
        self.sp = SignInPage(self.driver)
        assert self.sp.sign_in_text() == self.txt_sign_in
        assert self.sp.txt_instruct_sign_in() == self.instruct_sign_in
        assert self.sp.text_phone_number() == self.txt_number
        self.logger.info("__excepted text is same as actual text.")

    @allure.feature('Alert Verification')
    @allure.story('Verify Alert Messages')
    def test_alert_verification(self, setup):
        self.logger.info("__Test Three")
        self.driver = setup
        self.sp = SignInPage(self.driver)
        self.sp.send_phone(self.invalid_number)
        time.sleep(2)
        assert self.sp.alert_for_invalid_num() == self.alert_invalid
        self.sp.send_phone(self.unregistered_number)
        assert self.sp.alert_for_invalid_num() == self.alert_unregistered

    @allure.feature('Sign-in with verification')
    @allure.story('Verify successful Sign-in with verification.')
    def test_login_wit_verification(self, setup):
        self.logger.info("__Test One")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("__Url entered.")
        self.driver.maximize_window()
        self.sp = SignInPage(self.driver)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sign-in page",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.send_phone("+234 878 685 8483")
        self.logger.info("__Number entered.")
        allure.attach(self.driver.get_screenshot_as_png(), name="Phone number",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.send_password('Demo@123')
        self.logger.info("__Password entered")
        allure.attach(self.driver.get_screenshot_as_png(), name="Password",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.click_sign_in_btn()
        self.logger.info("__Clicked Sign in.")
        allure.attach(self.driver.get_screenshot_as_png(), name="Alert message",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.click_sign_in_btn()
        self.logger.info("__Clicked Sign in.")
        self.sp.click_sign_in_btn()
        allure.attach(self.driver.get_screenshot_as_png(), name="Title is same",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("__Clicked Sign in.")
        self.sp.click_send_button()
        time.sleep(3)
        self.logger.info("__Clicked Send.")
        self.sp.send_code("123456")
        self.logger.info("__Entered verification Code.")
        self.sp.click_sign_in_btn()
        self.logger.info("__Clicked Sign in.")

    def test_login_with_valid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sp = SignInPage(self.driver)
        allure.attach(self.driver.get_screenshot_as_png(), name="Sign-in page",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.send_phone("+234 878 685 8483")
        allure.attach(self.driver.get_screenshot_as_png(), name="Entered number",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.send_password('OhMG@1234')
        allure.attach(self.driver.get_screenshot_as_png(), name="Entered password",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(10)
        self.sp.click_sign_in_btn()
        allure.attach(self.driver.get_screenshot_as_png(), name="Clicked sign in button",
                      attachment_type=allure.attachment_type.PNG)
