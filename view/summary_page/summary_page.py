from os import path

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from controler.page_manager import page_manager
from view.seen_page.seen_page import SeenPage
from data.basic_datas import page_number


class SummaryPage(Screen):
	apps = ObjectProperty()
	name = "summary_page"
	
	def go_seen_page(self, num_title):
		print("le numero du titr est  : ", num_title)
		SeenPage.num_page = num_title
		if not page_manager.has_screen("seen_page"):
			Builder.load_file(path.join(path.dirname(path.dirname(__file__)), "seen_page/seen_page.kv"))
			page_manager.add_widget(SeenPage())
		self.apps.change_page("seen_page")

	def go_home(self):
		page_manager.transition.direction = "rigth"
		page_manager.current = "home_page"
		# self.apps.change_page("home_page")