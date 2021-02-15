from selenium import webdriver
from datetime import datetime


def chrome(name_browser,link):
	start = datetime.now()
	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get("https://rk.gov.ru/")
	browser.save_screenshot(f'{name_browser}.png')
	browser.close()
	print(datetime.now() - start,name_browser)

def firefox(name_browser,link):
	start = datetime.now()
	browser = webdriver.Firefox()
	browser.maximize_window()
	browser.get("https://rk.gov.ru/")
	browser.save_screenshot(f'{name_browser}.png')
	browser.close()
	print(datetime.now() - start,name_browser)

def opera(name_browser,link):
	start = datetime.now()
	browser = webdriver.Opera()
	browser.maximize_window()
	browser.get("https://rk.gov.ru/")
	browser.save_screenshot(f'{name_browser}.png')
	browser.close()
	print(datetime.now() - start,name_browser)


def main():
	""" Проверка кроссбраузерности сайта """
	link = "https://rk.gov.ru/"
	#link = input("Введите ссылку ")
	chrome("chrome",link)
	firefox("firefox",link)
	opera("opera",link)

if __name__ == '__main__':
	main()
