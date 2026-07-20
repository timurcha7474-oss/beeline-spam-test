from pages.base_page import BasePage

class FormPage (BasePage):
    def navigate(self):
        self.page.goto("https://moskva.beeline.ru/spam-feedback/", timeout=60000)

    def fill_name (self, name):
        self.page.locator('[name="person"]').fill(name)

    def fill_date (self, date):
        self.page.locator('[name="callStart"]').fill(date)

    def fill_phone (self, phone):
        self.page.locator('[name="ctnB"]').fill(phone)

    def select_sms (self):
        self.page.get_by_role("checkbox", name="СМС").check()

    def fill_sender (self, sender):
        self.page.locator('[name="ctnA"]').fill(sender)

    def fill_description (self, description):
        self.page.get_by_role("textbox", name="Описание").fill(description)

    def accept_policy (self):
        self.page.get_by_role("checkbox", name="Нажимая кнопку «Отправить», вы подтверждаете, что ознакомились с Политикой «Обработка персональных данных «ПАО «ВымпелКом».").check()

    def click_sumbit(self):
        self.page.get_by_role("button", name="Отправить").click()

    def success_message(self):
        return self.page.get_by_text("спасибо за информацию!")



