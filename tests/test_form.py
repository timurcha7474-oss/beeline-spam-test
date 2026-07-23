import pytest
import allure
from playwright.sync_api import expect
from pages.form_pages import FormPage


@allure.title("Успешная отправка формы")
def test_success_send_sms(page):
    form = FormPage(page)

    form.navigate()
    form.fill_name("Иванов Иван Иванович")
    form.fill_date("12.07.2026")
    form.fill_phone("+79371234567")
    form.select_sms()
    form.fill_sender("+79377654321")
    form.fill_description("Реклама")
    if not page.locator("comment").is_visible(): pytest.fail("Поле 'Комментарий' не отображается на странице.")
    form.accept_policy ()

    form.click_sumbit()

    expect(page.get_by_role("button", name="Отправить")).to_be_enabled()


@allure.title("Отправка формы без огласия")
def test_send_without_policy(page):
    form = FormPage(page)

    form.navigate()
    form.fill_name("Иванов Иван Иванович")
    form.fill_date("12.07.2026")
    form.fill_phone("+79371234567")
    form.select_sms()
    form.fill_sender("+79377654321")
    form.fill_description("Реклама")

    expect(page.get_by_role("button", name="Отправить")).to_be_disabled()
