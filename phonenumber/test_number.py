import time
from phonenumber.page_number import PhonePage
from signin.page import SignInPage
from team.page_teams import TeamPage
from utilities.customlogger import LogGen
from utilities.read_properties import ReadConfig
from helpers.conf_test import setup


class TestPhone:
    config_reader1 = ReadConfig()
    otp = config_reader1.get_otp()
    number1 = config_reader1.get_number()
    logger = LogGen.loggen()
    baseURL = config_reader1.get_application_url()

    def test_one(self, setup):
        self.driver = setup
        self.pp = PhonePage(self.driver)
        self.tp = TeamPage(self.driver)
        self.sp = SignInPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.sp.send_phone("+234 878 685 8483")
        self.sp.send_password("Demo@1234")
        self.sp.click_sign_in_btn()
        self.logger.info("__Successful login")
        self.pp.click_heading()
        self.pp.click_three_dot_menu()
        self.pp.click_assign_to()
        self.pp.select_members_to_assign()
        self.pp.click_assign_button()
        self.pp.click_three_dot_menu()
        self.pp.update_forwarding()
        self.pp.click_drpdown_forward_call_to()
        time.sleep(3)
        self.pp.forward_call_to_team()
        time.sleep(3)
        self.pp.select_drpdown_team_for_forwarding()
        time.sleep(3)
        self.pp.select_team()
        self.pp.click_drpdwn_forward_how_long()
        self.pp.select_time_for_ring()
        self.pp.click_button_submit_forwarding()
        time.sleep(3)
        self.pp.click_three_dot_menu()
        self.pp.update_forwarding()
        self.pp.click_drpdown_forward_call_to()
        self.pp.forward_call_to_member()
        self.pp.select_member_from_list()
        self.pp.click_button_submit_forwarding()
