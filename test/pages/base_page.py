from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

  def __init__(self, driver, url=None):
    if url:
      self.url = url
    self.driver = driver

  def open(self):
    if not self.url:
      raise Exception("Must set page URL")
    self.driver.get(self.url)

  def url_matches(self, driver, url_match, timeout = 5):
    return WebDriverWait(driver, timeout).until(EC.url_matches(url_match))