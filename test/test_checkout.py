from selenium import webdriver
from .pages.cart import CartPage
from .pages.checkout import CheckoutPage

def test_checkout_kits(browser):
    cart_page = CartPage(browser, 'https://store.23andme.com/en-us/cart/')
    cart_page.open()
    assert cart_page.url_matches(browser, 'https://store.23andme.com/en-us/cart/'), 'Cart page not reached'

    cart_page.add_kit('HEALTH')
    cart_page.add_kit('ANCESTRY')
    cart_page.continue_cart()

    checkout_page = CheckoutPage(browser, 'https://store.23andme.com/en-us/checkout/')
    assert checkout_page.url_matches(browser, 'https://store.23andme.com/en-us/checkout/'), 'Checkout page not reached'

    checkout_page.first_name('Felipe')
    checkout_page.last_name('Oliveira')
    checkout_page.company('Quality Assured')
    checkout_page.address('123 Evergreen St')
    checkout_page.address_2('APT 373')
    checkout_page.city('Springfield')
    checkout_page.state('MA')
    checkout_page.zip_code('23122')
    checkout_page.email('felipe.oliveira@company.com')
    checkout_page.phone('(352)7412568')
    checkout_page.continue_checkout()

    assert checkout_page.address_verified(), 'Shipping Address Not Verified'
    checkout_page.close_verification_modal()
    checkout_page.select_express_shipping()
    checkout_page.continue_billing()
    assert checkout_page.billing_address_present(), 'Billing Address Not Present'
    

