from imgkit import from_url
from requests import get
import signal

def main():
	""" Для примера возьмем не самую популярную запись(https://rk.gov.ru/ru/article/show/10080 160 просмотров) и увеличим ей число просмотров """

	url = input('Ссылка для накрутки просмотров ')
	from_url(url, 'до_накрутки_.jpg')#делаем скрин на начало теста

	def signal_handler(sig, frame):

		from_url(url, 'после_накрутки.jpg')#делаем скрин в конце теста
		print("You pressed Ctrl+C!")
		exit()


	while True:
		get(url)

		signal.signal(signal.SIGINT, signal_handler)


	signal.pause()



if __name__ == '__main__':
	main()

