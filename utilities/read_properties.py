import os
import configparser


class ReadConfig:
    config = configparser.ConfigParser()
    config_file_path = os.path.join(os.path.dirname(__file__), '../data/config.ini')

    def __init__(self):
        self.config.read(self.config_file_path, encoding='utf-8')

    def get_application_url(self):
        url = self.config.get('common info', 'baseURL')
        print(url)
        return url

    def get_number(self):
        number = self.config.get('credentials', 'number')
        return number

    def get_otp(self):
        otp = self.config.get('credentials', 'otp')
        return otp

    def get_invalid_number(self):
        invalid_number = self.config.get('number input', 'wrongPhoneNumber')
        return invalid_number

    def get_unregistered_number(self):
        invalid_number = self.config.get('number input', 'unregisteredNumber')
        return invalid_number

    def invalid_verification_code(self):
        invalid_code = self.config.get('number input', 'wrongVerificationcode')
        return invalid_code

    def get_title(self):
        title = self.config.get('text login page', 'title')
        return title

    def text_sign_in(self):
        txt = self.config.get('text login page', 'signin')
        return txt

    def txt_phone_number(self):
        txt = self.config.get('text login page', 'phoneNumber')
        return txt

    def text_instruction_sig_in(self):
        instruction1 = self.config.get('text login page', 'instructionSignIn')
        return instruction1

    def txt_phone_instruction(self):
        instruction2 = self.config.get('text login page', 'phoneInstruction')
        return instruction2

    def txt_verification_code(self):
        text_code = self.config.get('text login page', 'verificationCode')
        return text_code

    def instruct_verify_code(self):
        instruction3 = self.config.get('text login page', 'verificationInstruction')
        return instruction3

    def alert_number_invalid(self):
        alert1 = self.config.get('alert messages', 'alertInvalidNumber')
        return alert1

    def alert_not_registered(self):
        code = self.config.get('alert messages', 'alertNotRegistered')
        return code


class TeamReadConfig:
    config = configparser.ConfigParser()
    config_file_path = os.path.join(os.path.dirname(__file__), '../data/config.ini')

    def __init__(self):
        self.config.read(self.config_file_path, encoding='utf-8')

    def add_member_f_name(self):
        f_name = self.config.get('member input data', 'firstName')
        return f_name

    def add_member_l_name(self):
        l_name = self.config.get('member input data', 'lastName')
        return l_name

    def add_member_number(self):
        number = self.config.get('member input data', 'number')
        return number

    def add_member_num_vth_spaces(self):
        number = self.config.get('member input data', 'numberWithSpaces')
        return number

    def add_member_special_char(self):
        special_character = self.config.get('member input data', 'specialCharacters')
        return special_character

    def add_member_repeating_char(self):
        repeating_char = self.config.get('member input data', 'repeatingCharacters')
        return repeating_char

    def add_member_registered_email(self):
        registered_email = self.config.get('member input data', 'registeredEmail')
        return registered_email

    def add_member_email(self):
        email = self.config.get('member input data', 'email')
        return email

    def team_name(self):
        team = self.config.get('team input', 'teamName')
        return team

    def txt_heading(self):
        heading = self.config.get('member text data', 'headingText')
        return heading

    def search_place_holder(self):
        search = self.config.get('member text data', 'searchPlaceholder')
        return search

    def add_member_text(self):
        text = self.config.get('member text data', 'addMemberButton')
        return text

    def name_table(self):
        text = self.config.get('member text data', 'tableHeadingName')
        return text

    def email_table(self):
        email = self.config.get('member text data', 'tableHeadingEmail')
        return email

    def team_heading(self):
        team = self.config.get('member text data', 'tableHeadingTeam')
        return team

    def phone_heading(self):
        phone = self.config.get('member text data', 'tableHeadingPhone')
        return phone

    def role_table(self):
        role = self.config.get('member text data', 'tableHeadingRole')
        return role

    def status_table(self):
        status = self.config.get('member text data', 'tableHeadingStatus')
        return status


class CallDetailsReadConfig(TeamReadConfig):
    def heading_text_table(self):
        text = self.config['call details']['headerText'].split(',')
        return text

    def side_bar_text(self):
        text = self.config['call page']['sideBarText'].split(',')
        return text

    def manage_call_txt(self):
        text = self.config.get('call details', 'manageCallText')
        return text

    def set_forwarding_all_text(self):
        text = self.config['set forwarding call details']['setForwardingText'].split('.')
        return text
