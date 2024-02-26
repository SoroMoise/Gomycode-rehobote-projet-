from os import path

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog

from controler.page_manager import page_manager
from view.home_page.home_page import HomePage


def user():
	import json
	set_dir = path.join(path.dirname(path.dirname(path.dirname(__file__))), "data/data_base.json")
	print("le chemain est : ", set_dir)
	# print("Le chemain est : ", set_dir)
	with open(set_dir, "r") as setting:
		return json.load(setting)


class ContentLoad:
	width_sreen = Window.width
	height_sreen = Window.height
	definition = ""


class APropos(BoxLayout):
	width_sreen = Window.width
	height_sreen = Window.height
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	a_propos = "Nous somme une plate forme de formation dans le domaine du digital et nous formons la prochaine génération tech aux technologies les plus récentes et aux métiers du futur pour les préparer au monde professionnel et renforcer leur employabilité."


class ConnectPage(Screen):
	passe = False
	menu = None
	dialog_a_propos = None
	width_sreen = Window.width
	height_sreen = Window.height
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# self.dial = MDDialog(
		# 		title=f"[b][u]Téléchargement du cour...[/u][/b]",
		# 		opacity=1,
		# 		# width_offset=30,
		# 		type="custom",
		# 		padding=[0, 0, 0, 0],
		# 		radius=[45, 45, 45, 45],
		# 		height=self.height,
		# 		content_cls=ContentLoad(),
		# 	)
	
	def connection(self, mail, pwd):
		print(mail, pwd)
		users = user()
		for i in users.values():
			if mail == i["login"] and pwd == i["pwd"]:
				print(mail, i["login"], "    ", pwd, i["pwd"])
				self.passe = True
				if not page_manager.has_screen("home_page"):
					Builder.load_file(path.join(path.dirname(path.dirname(__file__)), "home_page/home_page.kv"))
				self.apps.change_page("home_page")
				break
		
		if not self.passe:
			if mail == "" or pwd == "":
				self.ids.error.text = "Erreur de saisie, veillez renseigner tout les champs"
			else:
				self.ids.error.text = "Erreur de saisie, veillez verrifier votre e-mail ou votre mot de passe"

	def affiche_menu(self, button):
		"""
		Cette fonction est appelé quant on clic sur le 'dot-vertical' en haut a gauche pour afficher le menu
		"""
		if not self.menu:
			menu_dictionnaire = {"info": "A propos",
			                     "quiter": "Quiter"}
			menu_items = [
				{
					"viewclass": "OneLineListItem",
					"text": f"{menu_dictionnaire[i]}",
					"height": dp(45),
					"halign": "center",
					"on_release": lambda x=f"{i}": self.clic_menu(x),
				} for i in menu_dictionnaire
				# Ajouter des icons par la suite
			]
			from kivymd.uix.menu import MDDropdownMenu
			self.menu = MDDropdownMenu(
				items=menu_items,
				# position="center",
				width_mult=4,
				opening_time=0.1,
			)
			self.menu.caller = button
		self.menu.open()
	
	def clic_menu(self, text_item: str):  # exporté
		"""Executer qand on clique sur un element du menu"""
		self.menu.dismiss()  # Permet de fermer le menu
		
		if text_item == "info":
			self.a_propos()
		
		elif text_item == "quiter":
			exit()
	
	def a_propos(self):
		"""
		Executer qand on clique sur un element du menu
		:return:
		"""
		# recupere le font_name actuel pour ne pas le chercher plusueur fois

		if not self.dialog_a_propos:
			self.dialog_a_propos = MDDialog(
				title="A propos",
				# opacity=1,
				# width_offset=30,
				type="custom",
				padding=[0, 0, 0, 0],
				radius=[45, 45, 45, 45],
				height=self.height,
				content_cls=APropos(),
			)
			
			self.dialog_a_propos.width = self.width_sreen * 0.9
			# cls.dialog_a_propos.ids.title.md_bg_color = [1, 0, 0, 0.5]
			self.dialog_a_propos.ids.title.halign = "center"
			self.dialog_a_propos.ids.container.padding = ["10dp", "10dp", "-5dp", "10dp"]
		# Permet d'appliquer la nouvelle police au MDDialog A propos
		self.dialog_a_propos.open()
