from selenium import webdriver

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://rk.gov.ru/ru/sitemap")
browser.save_screenshot("sitemap_ul_0.png")

search = browser.find_element_by_link_text("Сводный отчет о выполнении государственного задания ГБУ РК «Дирекция по обеспечению деятельности Совета министров Республики Крым и его Аппарата» за 2018 год")
browser.execute_script("return arguments[0].scrollIntoView(true);",search)

browser.save_screenshot("sitemap_ul_1.png")

browser.close()


