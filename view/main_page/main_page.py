from os import path

from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

from view.home_page.home_page import HomePage


class MainPage(RelativeLayout):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		print("page", path.join(path.dirname(path.dirname(__file__)), "home_page/home_page.kv"))
		Builder.load_file(path.join(path.dirname(path.dirname(__file__)), "home_page/home_page.kv"))
		# self.page_manager = self.ids.page_manager
		# self.page_manager.add_widget(HomePage(name="home_page"))
