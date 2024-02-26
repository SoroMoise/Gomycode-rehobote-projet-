from kivy.uix.screenmanager import Screen

from controler.page_manager import page_manager
from data.basic_datas import page_number

datas = {
	1: [
		"[b]1  Premiers pas en Python[/b]", "[b]Python[/b] est l’un des langages de programmation les plus utilisés. Apprendre à coder avec Python est une [b]compétence très recherchée[/b] dans beaucoup de métiers. Et pas uniquement pour les développeurs logiciels à temps plein. Tout le monde peut apprendre !\n\nCe cours s’adresse aux personnes qui n’ont jamais vu une ligne de code ou qui n’ont jamais entendu parler de Python. Nous allons avancer ensemble [b]pas à pas[/b] de façon [b]amusante[/b] et [b]facile à comprendre[/b]. Je sais ce que ça fait d’être intimidé par le code ou de n’y rien comprendre. Je veux donc m’assurer que personne ne ressente la même chose. "
	],
	2: [
		"2  Les bases de Python", "[b]Python définit trois types de valeurs numériques supportées :[/b]\n\n\n[b]-->[/b]  Le type int qui représente tout entier positif ou négatif ;\n\n[b]-->[/b]  Le type float qui représente les nombres décimaux et certaines expressions scientifiques comme le e pour désigner une exponentielle par exemple;\n\n[b]-->[/b]  Le type complex qui représente les nombres complexes ou nombres imaginaires et qui se sert de la lettre j pour représenter la partie imaginaire d’un nombre."
	],
	3: [
		"quiz ??", "quiz non disponible"
	],
	4: [
		"", ""
	],
}

class SeenPage(Screen):
	name = "seen_page"
	num_page = 1
	cours_title = datas[num_page][0]
	text = datas[num_page][1]
	
	def on_enter(self, *args):
		self.ids.cours_title.text = datas[self.num_page][0]
		self.ids.explane_text.text = datas[self.num_page][1]
	
	def ret_summary(self):
		page_manager.transition.direction = "right"
		page_manager.current = "summary_page"
		# self.apps.change_page("summary_page")