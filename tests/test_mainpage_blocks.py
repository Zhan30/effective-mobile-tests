import  allure
import pytest
from allure_commons.types import Severity

from pages.main_page import MainPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@allure.tag(AllureTag.MAINPAGE)
@allure.epic(AllureEpic.MAINPAGE)
@allure.feature(AllureFeature.MAINPAGE_BLOCKS)
@allure.story(AllureStory.TEST_MAINPAGE_BLOCKS)
class TestMainPageBlocks:

    @allure.tag(AllureTag.BLOCKS_CLICK)
    @allure.title("Check block transitions by click")
    @allure.severity(Severity.NORMAL)
    def test_blocks_click(self, main_page: MainPage):
        main_page.visit("https://effective-mobile.ru/")

        main_page.check_visible()

        main_page.click_about_link()
        main_page.click_services_link()
        main_page.click_projects_link()
        main_page.click_reviews_link()
        main_page.click_contacts_link()
        main_page.click_specialist_link()