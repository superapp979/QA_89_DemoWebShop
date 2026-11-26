from selenium import webdriver
from selenium.webdriver.common.by import By


TAGS = ("div", "a", "img", "ul", "li", "form", "input", "label", "h2", "p")


CLASS_NAMES = (
    "header-logo", "header-links", "ico-register", "ico-login", "search-box",
    "search-box-text", "header-menu", "top-menu", "page-title", "footer",
)
IDS = (
    "small-searchterms", "newsletter-email", "gender-male", "gender-female",
    "FirstName", "LastName", "Email", "Password", "ConfirmPassword", "register-button",
)
NAMES = (
    "q", "NewsletterEmail", "Gender", "FirstName", "LastName", "Email",
    "Password", "ConfirmPassword", "register-button", "__RequestVerificationToken",
)
# CSS and XPath for the same attribute on the same HTML tag.
ATTRIBUTES = (
    ("a", "href", "/login"),
    ("a", "href", "/register"),
    ("img", "alt", "Tricentis Demo Web Shop"),
    ("form", "action", "/search"),
    ("form", "action", "/register"),
    ("label", "for", "gender-male"),
    ("label", "for", "gender-female"),
    ("label", "for", "FirstName"),
    ("label", "for", "Email"),
    ("input", "value", "Register"),
)


def check_locator(driver, strategy, selector, xpath):
    elements = driver.find_elements(strategy, selector)
    by_xpath = driver.find_elements(By.XPATH, xpath)
    assert elements, f"No elements for {strategy}: {selector}"
    assert elements == by_xpath, f"Different matches for {selector} and {xpath}"
    print(f"{strategy:14} {selector:35} {len(elements):2}  {xpath}")


def main():
    with webdriver.Chrome() as driver:
        driver.get("https://demowebshop.tricentis.com/")
        print("Tag      TAG_NAME  CSS_SELECTOR  XPATH")
        for tag in TAGS:
            by_tag = driver.find_elements(By.TAG_NAME, tag)
            by_css = driver.find_elements(By.CSS_SELECTOR, tag)
            by_xpath = driver.find_elements(By.XPATH, f"//{tag}")
            print(f"{tag:<8} {len(by_tag):>8}  {len(by_css):>12}  {len(by_xpath):>5}")
            assert by_tag, f"No elements found for <{tag}>"
            assert by_tag == by_css == by_xpath, f"Different elements found for <{tag}>"

        driver.get("https://demowebshop.tricentis.com/register")
        for name in CLASS_NAMES:
            # Match one class even when the class attribute contains several.
            xpath = f"//*[contains(concat(' ', normalize-space(@class), ' '), ' {name} ')]"
            check_locator(driver, By.CLASS_NAME, name, xpath)

        for element_id in IDS:
            check_locator(driver, By.ID, element_id, f"//*[@id='{element_id}']")

        for tag, attribute, value in ATTRIBUTES:
            css = f"{tag}[{attribute}='{value}']"
            xpath = f"//{tag}[@{attribute}='{value}']"
            check_locator(driver, By.CSS_SELECTOR, css, xpath)

        for name in NAMES:
            check_locator(driver, By.NAME, name, f"//*[@name='{name}']")

        print("OK: 10 tags and 40 locator comparisons")


if __name__ == "__main__":
    main()
