import allure
from playwright.sync_api import Page, Locator, expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:  # Добавили свойство type_of
        return "base element"

        # Метод принимает кейворд аргументы (kwargs)

    def get_locator(self, **kwargs) -> Locator:  # объект Locator для взаимодействия с элементом
        # Инициализирует объект локатора, подставляя динамические значения в локатор
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-elem-id={locator}"'

        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):  # Добавили шаг
            # "Лениво" инициализируем локатор
            # Добавили аргумент nth и передаем его в get_locator
            locator = self.get_locator(**kwargs)
            logger.info(step)
            locator.click()

    def check_visible(self, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)