import  allure
import pytest

from pages.main_page import MainPage

@pytest.mark.courses
@pytest.mark.regression
class TestMainPageBlocks:

    def test_blocks_click(self, main_page: MainPage):
        main_page.visit("https://effective-mobile.ru/")

        main_page.check_visible()

        main_page.click_about_link()
        main_page.click_services_link()
        main_page.click_projects_link()
        main_page.click_reviews_link()
        main_page.click_contacts_link()
        main_page.click_specialist_link()