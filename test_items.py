link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_basket_button(browser):
    browser.get(link)
    assert browser.find_element_by_class_name("btn-add-to-basket"), "No basket-button on page"
