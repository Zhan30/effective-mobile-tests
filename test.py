from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного режима и проверки

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://effective-mobile.ru/#specialists")

    # Находим поле "Email" и заполняем его
    blok_about = page.locator('//div[@data-elem-id="1680606406481"]')
    blok_about.click()

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)