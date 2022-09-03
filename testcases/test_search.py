import pytest
from libs.default import start


def test_main(get_driver):
    start(get_driver)
