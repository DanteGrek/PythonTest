from pages.pages import MainGooglePage
import pytest


@pytest.mark.usefixtures("start_and_close_desktop_chrome")
class TestGoogleSearch:

    def test_search(self):
        main_google_page = MainGooglePage()
        main_google_page.search('Go guide')
        main_google_page.is_search_result_contains('Go')


@pytest.mark.usefixtures("start_and_close_desktop_chrome")
class TestGoogleSearch2:

    def test_search2(self):
        main_google_page = MainGooglePage()
        main_google_page.search('JavaScript guide')
        main_google_page.is_search_result_contains('Java')
