import time
from selenium.webdriver import ActionChains
import pandas as pd
from helpers.base_page import *
from team import locators_teams as lt
from signin.locators import teams_heading_xpath


class TeamPage(CommonClass):
    bp = Base()

    def close_small_window(self):
        self.click_element('XPATH', '//div[text() = "Skip for now"]')

    def click_teams_heading(self):
        self.click_element('XPATH', teams_heading_xpath)

    def click_subheading_teams(self):
        self.click_element('CSS_SELECTOR', lt.teams_sub_heading_css)

    def click_create_team(self):
        self.click_element('CSS_SELECTOR', lt.create_team_btn_css)

    def send_team_name(self, text):
        self.send_keys_to_element('XPATH', lt.team_name_xpath, text)

    def select_members_drpdown(self):
        self.click_element('XPATH', lt.select_members_xpath)

    def dropdown_list_select_members(self):
        element_text = []
        elements = self.driver.find_elements(By.XPATH, lt.select_members_xpath_list)

        for element in elements:
            element_text.append(element.text[1:])  # Remove the leading '\n'

        # Strip leading and trailing whitespaces from each element's text
        stripped_text = [text.strip().split(' ') for text in element_text]

        # Print the stripped text for each element
        for text in stripped_text:
            print(text)
            dynamic_xpath = f"//dropdown-menu-item//label[@for='{text[0]}']"
            time.sleep(2)
            # self.driver.find_element(By.XPATH, dynamic_xpath)
            self.click_element('XPATH', dynamic_xpath)
            time.sleep(2)
            self.select_members_drpdown()
        # Print the list after stripping
        print(stripped_text)
        print(element_text)

    def click_submit_create_team(self):
        time.sleep(2)
        self.click_element('XPATH', lt.submit_create_team_xpath)

    def click_drpdwn_for_first_team(self):
        element = self.driver.find_element(By.XPATH, lt.dot_menu_xpath)
        # for option in element:
        ActionChains(self.driver).move_to_element(element).click().perform()

    def click_edit_team(self):
        self.click_element('XPATH', lt.action_edit_team_xpath)

    def change_team_name(self, text):

        random_team_name = self.bp.generate_random_team_name()
        element = self.driver.find_element(By.NAME, lt.name_field_by_name)
        # element.send_keys('abc')
        element.clear()
        element.send_keys(text)

    def modify_dropdown_elements(self):
        element_text = []
        elements = self.driver.find_elements(By.XPATH, lt.select_members_xpath_list)

        for element in elements:
            element_text.append(element.text[1:])  # Remove the leading '\n'

        # Strip leading and trailing whitespaces from each element's text
        stripped_text = [text.strip().split(' ') for text in element_text]

        # Check if all options are initially checked
        all_checked = all(element.get_attribute("checked") is not None for element in elements)

        # Check if the element is not checked, then click to check it
        for text in stripped_text:
            check_element = self.driver.find_element(By.XPATH, f"//dropdown-menu-item//label[@for='{text[0]}']")
            all_checked = all(check_element.get_attribute("checked") is not None for element in elements)
            if check_element.get_attribute("checked") is None:
                check_element.click()

            self.select_members_drpdown()

        # If all options were initially checked, uncheck them all
        if all_checked:
            for text in stripped_text:
                dynamic_xpath = f"//dropdown-menu-item//label[@for='{text}']"
                time.sleep(2)
                self.driver.find_element(By.XPATH, dynamic_xpath).click()
                self.select_members_drpdown()

    def click_invite_2_team(self):
        self.click_element('XPATH', lt.action_invite_to_team_xpath)

    def select_members_to_send_invite(self):
        element_text = []
        elements = self.driver.find_elements(By.XPATH, "//div[@class='flex flex-col gap-1'] /div[@class='flex "
                                                       "items-center text-sm font-medium	 text-grey-900'][text()]")

        for element in elements:
            element_text.append(element.text)  # Remove the leading '\n'

        # Strip leading and trailing whitespaces from each element's text
        stripped_text = [text.strip() for text in element_text]
        first_name = [name.split()[0] for name in stripped_text]
        print(stripped_text)
        print(first_name)

        # Check if all options are initially checked
        all_checked = all(element.get_attribute("checked") is not None for element in elements)

        # Check if the element is not checked, then click to check it
        for text in first_name:
            check_element = self.driver.find_element(By.XPATH, f"//div[@class='flex flex-col gap-1'] /div[@class='flex "
                                                               f"items-center text-sm font-medium	 text-grey-900']["
                                                               f"text() = '{text}']")
            all_checked = all(check_element.get_attribute("checked") is not None for element in elements)
            if check_element.get_attribute("checked") is None:
                check_element.click()

            # self.select_members_drpdown()

        # If all options were initially checked, uncheck them all
        if all_checked:
            for text in stripped_text:
                dynamic_xpath = (f"//div[@class='flex flex-col gap-1'] /div[@class='flex items-center text-sm "
                                 f"font-medium	 text-grey-900'][text() = '{text}']")
                time.sleep(2)
                continue

    def click_send_invite(self):
        self.click_element('XPATH', lt.btn_send_invite_xpath)

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
        self.common_table_data(lt.table_css, "table_data_teams", 'CSS_SELECTOR', "Members")

    def table_data_members(self):
        self.common_table_data(lt.table_members_xpath, "table_data_members", "XPATH", "Name")

    def click_to_select_all(self):
        self.click_element('XPATH', lt.select_all_checkbox)

    def delete_in_bulk(self):
        self.click_element('XPATH', lt.delete_bulk_xpath)
