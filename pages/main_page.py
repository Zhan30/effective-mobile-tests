import re

from playwright.sync_api import Page

from elements.link import Link
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.about_link = Link(page, '//div[@data-elem-id="1680606406481"]', 'About')
        self.services_link = Link(page, '//div[@data-elem-id="1680606406485"]', 'Services')
        self.projects_link = Link(page, '//div[@data-elem-id="1680606406489"]', 'Projects')
        self.reviews_link = Link(page, '//div[@data-elem-id="1706704571141"]', 'Reviews')
        self.contacts_link = Link(page, '//div[@data-elem-id="1680606406492"]', 'Contacts')
        self.specialist_link = Link(page, '//div[@data-elem-id="1680606406495"]', 'Specialist')

    def check_visible(self):
        self.about_link.check_visible()
        self.about_link.check_have_text('[ О нас ]')

        self.services_link.check_visible()
        self.services_link.check_have_text('[ Услуги ]')

        self.projects_link.check_visible()
        self.projects_link.check_have_text('[ Проекты ]')

        self.reviews_link.check_visible()
        self.reviews_link.check_have_text('[ Отзывы ]')

        self.contacts_link.check_visible()
        self.contacts_link.check_have_text('[ Контакты ]')

        self.specialist_link.check_visible()
        self.specialist_link.check_have_text('Выбрать специалиста')

    def click_about_link(self):
        self.about_link.click()
        self.check_current_url(re.compile(".*/#about"))

    def click_services_link(self):
        self.services_link.click()
        self.check_current_url(re.compile(".*/#moreinfo"))

    def click_projects_link(self):
        self.projects_link.click()
        self.check_current_url(re.compile(".*/#cases"))

    def click_reviews_link(self):
        self.reviews_link.click()
        self.check_current_url(re.compile(".*/#cases"))

    def click_contacts_link(self):
        self.contacts_link.click()
        self.check_current_url(re.compile(".*/#contacts"))

    def click_specialist_link(self):
        self.specialist_link.click()
        self.check_current_url(re.compile(".*/#specialists"))
