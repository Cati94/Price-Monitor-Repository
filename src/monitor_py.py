from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selectors import load_products
from emailer import send_email


def fetch_price(url, selector):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Navegador invisível
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    sleep(3)

    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        price = element.text
        driver.quit()
        return price
    except:
        driver.quit()
        return None


if __name__ == "__main__":
    products = load_products()
    report = []

    for product in products:
        report.append(f"\n### {product['name']} ###")

        for site in product["sites"]:
            price = fetch_price(site["url"], site["selector"])
            if price:
                report.append(f"{site['url']}: {price}")
            else:
                report.append(f"{site['url']}: preço não encontrado")

    final_report = "\n".join(report)
    print(final_report)

    send_email("Relatório Diário de Preços", final_report)
    print("Email enviado!")
