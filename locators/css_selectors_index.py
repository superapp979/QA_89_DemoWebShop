from selenium import webdriver
from selenium.webdriver.common.by import By


TAGS = ("div", "a", "img", "ul", "li", "form", "input", "label", "h2", "p")


def main():
    with webdriver.Chrome() as driver:
        driver.get("https://demowebshop.tricentis.com/")
        print("Tag      TAG_NAME  CSS_SELECTOR")
        for tag in TAGS:
            by_tag = driver.find_elements(By.TAG_NAME, tag)
            by_css = driver.find_elements(By.CSS_SELECTOR, tag)
            print(f"{tag:<8} {len(by_tag):>8}  {len(by_css):>12}")
            assert by_tag, f"No elements found for <{tag}>"
            assert by_tag == by_css, f"Different elements found for <{tag}>"


if __name__ == "__main__":
    main()
