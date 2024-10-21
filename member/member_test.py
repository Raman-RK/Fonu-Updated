import time
from utilities.read_properties import TeamReadConfig, ReadConfig
from member.member_page import *
from utilities.customlogger import LogGen
from helpers.conf_test import setup
from signin.page import SignInPage
from helpers.base_page import Base


class TestTeam:
    config_reader = TeamReadConfig()
    l_name = config_reader.add_member_l_name()
    config_reader1 = ReadConfig()
    otp = config_reader1.get_otp()
    baseURL = config_reader1.get_application_url()
    number1 = config_reader1.get_number()
    number_and_spaces = config_reader.add_member_num_vth_spaces()
    special_char = config_reader.add_member_special_char()
    repeating_char = config_reader.add_member_repeating_char()
    registered_email = config_reader.add_member_registered_email()
    txt_heading = config_reader.txt_heading()
    search_place_holder = config_reader.search_place_holder()
    add_member_txt = config_reader.add_member_text()
    name_heading_txt = config_reader.name_table()
    email_heading_txt = config_reader.email_table()
    teams_heading_txt = config_reader.team_heading()
    phone_heading_txt = config_reader.phone_heading()
    role_heading_txt = config_reader.role_table()
    status_heading_txt = config_reader.status_table()
    logger = LogGen.loggen()
    bp = Base()

    @allure.feature('Adding a member')
    @allure.story('Verify member is added successfully.')
    def test_add_member(self, setup):
        self.random_name = self.bp.generate_random_name()
        self.random_email = self.bp.generate_random_email()
        self.random_number = self.bp.generate_random_10_digit_number()
        self.logger.info("__Test One")
        self.logger.info("__Adding Member")
        self.driver = setup
        self.mp = MemberPage(self.driver)
        self.sp = SignInPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.sp.send_phone("+234 878 685 8483")
        allure.attach(self.driver.get_screenshot_as_png(), name="Sending number",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.send_password("Demo@1234")
        allure.attach(self.driver.get_screenshot_as_png(), name="Sending Password",
                      attachment_type=allure.attachment_type.PNG)
        self.sp.click_sign_in_btn()
        allure.attach(self.driver.get_screenshot_as_png(), name="Clicked sign in button",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("__Successful login")
        allure.attach(self.driver.get_screenshot_as_png(), name="Login successfully on Dashboard",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        self.mp.click_teams_heading()
        allure.attach(self.driver.get_screenshot_as_png(), name="teams heading clicked",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("____________Team on header is clicked.")
        time.sleep(2)

        self.mp.click_add_member_btn()
        allure.attach(self.driver.get_screenshot_as_png(), name="Add member modal",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("____________Clicked add member.")
        self.mp.send_f_name(self.random_name)
        self.logger.info("____________First name is entered.")
        self.mp.send_l_name(self.l_name)
        self.logger.info("____________Last name is entered.")
        self.mp.send_email(self.random_email)
        self.logger.info("Email is entered.")
        self.mp.send_phone_member(self.random_number)
        self.logger.info("____________Phone number is entered")
        self.mp.select_role_dropdown()
        self.logger.info("____________Clicked on dropdown to select the role")
        self.mp.select_role_member()
        allure.attach(self.driver.get_screenshot_as_png(), name="Info added",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        self.logger.info("____________Selected the role")
        time.sleep(2)
        self.mp.click_submit_add_member()
        allure.attach(self.driver.get_screenshot_as_png(), name="received success message",
                      attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        self.logger.info("__Member added successfully")
        self.mp.table_data_members()

    def test_create_an_admin(self, setup):
        self.random_name = self.bp.generate_random_name()
        self.random_email = self.bp.generate_random_email()
        self.random_number = self.bp.generate_random_10_digit_number()
        self.driver = setup
        self.mp = MemberPage(self.driver)
        self.mp.click_add_member_btn()
        self.logger.info("____________Clicked add member.")
        self.mp.send_f_name(self.random_name)
        self.logger.info("____________First name is entered.")
        self.mp.send_l_name(self.l_name)
        self.logger.info("____________Last name is entered.")
        self.mp.send_email(self.random_email)
        self.logger.info("Email is entered.")
        self.mp.send_phone_member(self.random_number)
        self.logger.info("____________Phone number is entered")
        self.mp.select_role_dropdown()
        self.logger.info("____________Clicked on dropdown to select the role")
        self.mp.select_role_admin()
        allure.attach(self.driver.get_screenshot_as_png(), name="Added_role",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("____________Selected the role as member")
        time.sleep(2)
        self.mp.click_submit_add_member()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="Add member screenshot",
                      attachment_type=allure.attachment_type.PNG)
        self.logger.info("__Member added successfully")
        self.mp.table_data_members()

    def test_perform_actions_member(self, setup):
        self.driver = setup
        self.mp = MemberPage(self.driver)
        time.sleep(3)
        self.mp.click_member_subheading()
        time.sleep(3)
        self.mp.member_perform_actions()
        self.mp.click_to_select_all()
        self.mp.delete_in_bulk()
