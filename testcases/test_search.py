import pytest
from libs.default import start


def test_main(get_driver, config_name, user_name):
    start(get_driver)
