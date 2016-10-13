from pages.pages import MainGooglePage
import pytest


@pytest.mark.usefixtures("setup_and_close_safari_on_ios")
class TestGoogleSearch:

    def test_search(self):
        main_google_page = MainGooglePage()
        main_google_page.search('Python guide')
        main_google_page.is_search_result_contains('Python')

    def test_search2(self):
        main_google_page = MainGooglePage()
        main_google_page.search('Java guide')
        main_google_page.is_search_result_contains('Java')
