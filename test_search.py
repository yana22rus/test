from selenium.webdriver import Firefox
from time import sleep

def main():
	browser = Firefox()

	browser.maximize_window()
	browser.implicitly_wait(5)

	browser.get("https://rk.gov.ru/")

	browser.find_element_by_id("acceptCookies").click()

	search_text = "Аксенов"
	#search_text = input()#или любой другой поисковый запрос

	l = []
	l.append(search_text)#Аксенов
	l.append(search_text.upper())#АКСЕНОВ
	l.append(search_text.lower())#аксенов
	l.append(search_text.swapcase())#аКСЕНОВ

	def test(search_word):

		search_main = browser.find_element_by_css_selector(".bottom-nav__pole")
		browser.execute_script("return arguments[0].scrollIntoView(true);", search_main)
		sleep(1)
		search_main.send_keys(search_word)
		browser.find_element_by_css_selector(".bottom-nav__button").click()
		print("Поиск по слову " + search_word)

		search_main = browser.find_element_by_css_selector(".bottom-nav__pole")
		browser.execute_script("return arguments[0].scrollIntoView(true);", search_main)
		sleep(1)
		search_main.send_keys(search_word)
		browser.find_element_by_css_selector(".bottom-nav__button").click()
		
		text = browser.find_element_by_xpath("//p[2]").text
		number = ''.join(x for x in text if x.isdigit())
		print(text)
		return number

	l = [test(i) for i in l]

	print("Поиск работает корректно, регистронезависимо" if len(set(l)) == 1 else "Не корректно работает поиск")

	browser.close()

if __name__ == '__main__':
	main()
