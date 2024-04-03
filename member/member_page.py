import allure
from selenium.webdriver import ActionChains
import pandas as pd
from helpers.base_page import *
from member import member_locators as ml
from team.test_teams import TestTeam


class MemberPage(CommonClass):
    bp = Base()

    def close_small_window(self):
        self.click_element('XPATH', '//div[text() = "Skip for now"]')

    def click_teams_heading(self):
        self.click_element('XPATH', ml.teams_heading_xpath)

    def click_add_member_btn(self):
        self.click_element('CSS_SELECTOR', ml.add_member_btn_css)

    def send_f_name(self, text):
        self.send_keys_to_element('NAME', ml.f_name_name, text)

    def send_l_name(self, text):
        self.send_keys_to_element('NAME', ml.l_name_name, text)

    def send_email(self, text):
        self.send_keys_to_element('XPATH', ml.email_xpath, text)

    def send_phone_member(self, text):
        element = self.driver.find_element(By.CSS_SELECTOR, ml.phone_css)
        element.clear()
        element.send_keys(text)

    def select_role_dropdown(self):
        self.click_element('XPATH', ml.dropdown_role_xpath)

    def select_role_member(self):
        self.click_element('XPATH', ml.role_member_xpath)

    def select_role_admin(self):
        self.click_element('XPATH', ml.admin_role_xpath)

    def click_submit_add_member(self):
        action = ActionChains(self.driver)
        hidden_element = self.driver.find_element(By.XPATH, ml.add_member_submit_xpath)
        action.click(on_element=hidden_element)
        action.perform()

    def click_menu_member(self):
        self.click_element('XPATH', ml.action_dot_menu_member_xpath)

    def click_member_subheading(self):
        self.click_element('XPATH', ml.member_subheading_xpath)

    def click_assign_team(self):
        self.click_element('XPATH', ml.assign_team_xpath)

    def click_assign_number(self):
        self.click_element('XPATH', ml.assign_number_xpath)

    def click_delete_member(self):
        self.click_element('XPATH', ml.delete_member_xpath)

    def select_team_to_assign(self):
        self.click_element('XPATH', ml.select_team)

    def click_submit_assign_team(self):
        self.click_element('CSS_SELECTOR', ml.submit_assign_team_css)

    def click_number_from_list(self):
        try:
            # Assuming `click_element` is a method you have that clicks an element
            self.click_element('CSS_SELECTOR', ml.select_number_css)
            print("Element clicked successfully.")
        except self.click_element('XPATH', ml.assign_number_close_btn):
            print("skipping")

    def get_status(self):
        text = self.get_text_from_element('XPATH', ml.status_member_xpath)
        return text

    def click_submit_assign_number(self):
        self.click_element('CSS_SELECTOR', ml.submit_assign_number_css)

    def click_unassign(self):
        self.click_element('XPATH', ml.unassign_number_xpath)

    def click_unassign_submit(self):
        self.click_element('CSS_SELECTOR', ml.unassign_submit_css)

    def click_edit_member(self):
        self.click_element('XPATH', ml.edit_member_xpath)

    def change_member_name(self, text):
        self.send_keys_to_element('NAME', ml.edit_member_name_by_name, text)

    def click_submit_edit_member(self):
        self.click_element('CSS_SELECTOR', ml.submit_edit_member_css)

    def common_table_data(self, locator, file_name, locator_strategy, column_name='None', timeout=10):
        table = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((getattr(By, locator_strategy), locator))
        )
        table_html = table.get_attribute("outerHTML")
        df = pd.read_html(table_html)[0]  # Assuming there is only one table on the page
        df = df.loc[:, df.columns.notna()]  # filter out columns with no data
        df[column_name] = df[column_name].str[1:]
        excel_file_path = f"{file_name}.xlsx"
        df.to_excel(excel_file_path, index=False)

    def table_data_teams(self):
        self.common_table_data(ml.table_css, "table_data_teams", 'CSS_SELECTOR', "Name")

    def table_data_members(self):
        self.common_table_data(ml.table_members_xpath, "table_data_members", "XPATH", "Name")

    def click_to_select_all(self):
        self.click_element('XPATH', ml.select_all_checkbox)

    def delete_in_bulk(self):
        self.click_element('XPATH', ml.delete_bulk_xpath)

    def resend_invitation(self):
        self.click_element('XPATH', ml.resend_invitation_xpath)

    def member_perform_actions(self):
        if self.get_status() == "Activated":
            self.click_menu_member()
            allure.attach(self.driver.get_screenshot_as_png(), name="Clicked on three dots",
                          attachment_type=allure.attachment_type.PNG)
            self.click_assign_team()
            allure.attach(self.driver.get_screenshot_as_png(), name="Assign team",
                          attachment_type=allure.attachment_type.PNG)
            self.select_team_to_assign()
            self.click_submit_assign_team()
            allure.attach(self.driver.get_screenshot_as_png(), name="Team assigned",
                          attachment_type=allure.attachment_type.PNG)
            self.click_menu_member()
            self.click_assign_number()
            allure.attach(self.driver.get_screenshot_as_png(), name="Assign number modal",
                          attachment_type=allure.attachment_type.PNG)
            self.click_number_from_list()
            allure.attach(self.driver.get_screenshot_as_png(), name="Number selected",
                          attachment_type=allure.attachment_type.PNG)
            self.click_submit_assign_number()
            allure.attach(self.driver.get_screenshot_as_png(), name="Number assigned",
                          attachment_type=allure.attachment_type.PNG)
            self.click_menu_member()
            self.click_unassign()
            self.click_unassign_submit()
            allure.attach(self.driver.get_screenshot_as_png(), name="number is unassigned",
                          attachment_type=allure.attachment_type.PNG)
            # self.tp.click_menu_member()
            self.click_edit_member()
            allure.attach(self.driver.get_screenshot_as_png(), name="Edit member modal",
                          attachment_type=allure.attachment_type.PNG)
            self.change_member_name(TestTeam.random_name)
            self.click_submit_edit_member()
            allure.attach(self.driver.get_screenshot_as_png(), name="Member edited",
                          attachment_type=allure.attachment_type.PNG)
            self.click_menu_member()
            self.click_delete_member()

        else:
            self.click_menu_member()
            self.resend_invitation()
