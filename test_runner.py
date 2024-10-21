import os
import pytest


def test_run():
    # test_signin_path = os.path.join(os.path.dirname(__file__), 'signin/test_signin.py')
    test_teams_path = os.path.join(os.path.dirname(__file__), 'team/test_teams.py')
    # test_member_path = os.path.join(os.path.dirname(__file__), 'member/member_test.py')
    allure_results_path = os.path.join(os.path.dirname(__file__), 'allure-results')

    # Run the tests
    pytest.main(['--capture=tee-sys','-q', '--alluredir', allure_results_path, test_teams_path])


if __name__ == "__main__":
    test_run()
