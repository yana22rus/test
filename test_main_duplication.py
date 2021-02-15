from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(5)

browser.get("https://rk.gov.ru/ru/structure/1?page=NaN")
browser.find_element_by_id("acceptCookies").click()

def main(n):
	""" Нажимае на кнопку n-e число раз получаем число дубликатов новостей """
	for i in range(n):
		button = browser.find_element_by_id("get-more")
		browser.execute_script("return arguments[0].scrollIntoView(true);", button)
		sleep(1)
		button.click()
	print(f"""Число дубликатов {len(browser.find_elements_by_xpath("//a[contains(.,'Минтранс РК: Дорожные службы Крыма обеспечивают безопасность дорожного движения на региональных и межмуниципальных дорогах республики')]"))}""")




if __name__ == '__main__':
	main(int(input("Сколько раз нажать? ")))


