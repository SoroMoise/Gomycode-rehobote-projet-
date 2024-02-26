from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from controler.page_manager import page_manager
from os import path

from view.summary_page.summary_page import SummaryPage


class HomePage(Screen):
	apps = ObjectProperty()
	name = "home_page"
	
	def go_summary(self):
		# print(self.apps)
		# print(page_manager.current)
		if not page_manager.has_screen("summary_page"):
			Builder.load_file(path.join(path.dirname(path.dirname(__file__)), "summary_page/summary_page.kv"))
			page_manager.add_widget(SummaryPage())
		self.apps.change_page("summary_page")

	def go_connection(self):
		# if not page_manager.has_screen("connect_page"):
		# 	Builder.load_file(path.join(path.dirname(path.dirname(__file__)), "connect_page/connect_page.kv"))
		# 	page_manager.add_widget(SummaryPage())
		page_manager.transition.direction = "right"
		self.apps.change_page("connect_page")
	
