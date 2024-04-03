import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import ReadConfig


class Base:
    def __init__(self, domain="@gmail.com"):
        self.domain = domain

    def generate_random_email(self):
        # Generate a random username (combination of letters)
        username = ''.join(random.choices(string.ascii_lowercase, k=10))

        # Combine username with the email domain
        email = username + self.domain

        return email

    @staticmethod
    def generate_random_first_name(length=6):
        letters = string.ascii_letters
        random_first_name = ''.join(random.choice(letters) for _ in range(length))
        return random_first_name.capitalize()

    @staticmethod
    def generate_random_10_digit_number():
        random_number = ''.join(random.choices('0123456789', k=10))
        return "+234" + random_number

    @staticmethod
    def generate_random_team_name(length=6):
        letters = string.ascii_letters
        random_team_name = ''.join(random.choice(letters) for _ in range(length))
        return random_team_name.capitalize()

    @staticmethod
    def generate_random_name():
        name_list = (
            "Raman", "Sandeep", "Aman", "Simran", "Sarb", "Ajay", "Abhishek", "Danish", "Deepesh", "Gagan", "Shakil",
            "Hitesh")
        random_name = random.choice(name_list)
        return random_name


class CommonClass:
    config_reader1 = ReadConfig()
    baseURL = config_reader1.get_application_url()

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_strategy, locator_value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((getattr(By, locator_strategy), locator_value))
        )
        element.click()

    def send_keys_to_element(self, locator_strategy, locator_value, input_text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((getattr(By, locator_strategy), locator_value))
        )
        element.clear()
        element.send_keys(input_text)

    def get_text_from_element(self, locator_strategy, locator_value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((getattr(By, locator_strategy), locator_value))
        )
        element_text = element.text
        print(element_text)
        return element_text
