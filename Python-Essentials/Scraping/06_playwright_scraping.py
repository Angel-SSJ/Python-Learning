from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
url='https://midu.dev'
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,)
    page = browser.new_page()
    page.goto(url)

    first_article_anchor = page.locator('article a').first
    print(first_article_anchor.text_content())
    first_article_anchor.click()

    page.wait_for_load_state()
    screen=page.screenshot(path='miduTest.png')
    print(f'Screenshot obtenida {screen}')
    first_image = page.locator('main img').first
    image_src = first_image.get_attribute('src')
    print(f'La imagen del primer curso es: {image_src}')

    # Añade la ruta completa a la URL de la imagen
    #image_url = urljoin(url, image_src)
    # Emcontrar elementos Xpath
    #first_image = page.locator('xpath=/html/body/main/div[1]/img')
    #print(first_image.get_attribute('src'))

    curso_content_container = page.locator('text="Contenido del curso"')
    curso_content_sibling = curso_content_container.locator('xpath=following-sibling::ul')
    print(curso_content_container.text_content())
    print(curso_content_sibling.text_content())
browser.close()