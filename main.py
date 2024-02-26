from os import path
from time import time

from view.connect_page.connect_page import ConnectPage
from view.main_page.main_page import MainPage
from view.seen_page.seen_page import SeenPage
from view.summary_page.summary_page import SummaryPage

deb = time()
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

from controler.page_manager import page_manager
from view.home_page.home_page import HomePage


class MainApp(MDApp):
	title = "Gomycode / Apprenez à développer avec Python"
	# Window.size = [1400, 650]
	# Window.minimum_width = 1020
	# Window.minimum_height = 500
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# print(path.join(path.dirname(__file__), "view/home_page/home_page.kv"))
		Builder.load_file(path.join(path.dirname(__file__), "view/connect_page/connect_page.kv"))
		Window.bind(on_keyboard=self.on_keyboard)
		Window.bind(on_resize=self.on_resize)
		page_manager.add_widget(ConnectPage(name="connect_page"))
	
	def build(self):
		return page_manager
	
	def on_start(self):
		print(f"Le temps total est : {time() - deb}")
	
	def on_pause(self):
		"""
		call whenever the system(OS) put this software on pause
		:return:
		"""
		return True
	
	def on_stop(self):
		print("je quite avec exit dans on_stop")
		exit()
	
	def on_keyboard(self, *kwargs):
		"""
		It's call whenever keyboard is pressed
		:param kwargs:
		:return:
		"""
		code = kwargs[1]
		# print(code, page_manager.current)
		if code == 27:
			if page_manager.current == "home_page":
				page_manager.transition.direction = "right"
				page_manager.current = "connect_page"
				return True
			elif page_manager.current == "summary_page":
				page_manager.transition.direction = "right"
				page_manager.current = "home_page"
				return True
			elif page_manager.current == "seen_page":
				page_manager.transition.direction = "right"
				page_manager.current = "summary_page"
				return True
			
			
	def on_resize(self, *kwargs):
		"""
		It's call whenever window is resize
		:param kwargs: (obj, width, height)
		:return:
		"""
		# print(kwargs)
		pass
	
	def change_page(self, page_name):
		# page_manager.current =
		if page_name == "summary_page":
			page_manager.transition.direction = "left"
			
		elif page_name == "seen_page":
			page_manager.transition.direction = "left"
		elif page_name == "home_page":
			print("le home page")
			page_manager.transition.direction = "left"
			page_manager.add_widget(HomePage(name="home_page"))
		page_manager.current = page_name


if __name__ == '__main__':
	MainApp().run()
