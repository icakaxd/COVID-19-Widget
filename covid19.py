#  Pythonista widget for iOS
#    sources: https://www.mh.government.bg/bg/informaciya-za-grazhdani/potvrdeni-sluchai-na-koronavirus-na-teritoriyata-na-r-blgariya/
import appex, ui
from bs4 import BeautifulSoup
import requests
import time

class CovidBulgaria:
	
	data = []
	lastupdate = -1
	
	def __init__(self):
		try:
			while True:
				self.update()
				self.view()
		except KeyboardInterrupt:
			print('Killing script..')
			os._exit()
		except Exception as e:
			print(e)
	
	def view(self):
		
		view = ui.View()
		
		for i in range(len(self.data )):
			view.add_subview(ui.Label(font=('Menlo', 14), alignment=ui.ALIGN_CENTER, text=self.data[i], width=385, y=(15*i)))
		
		appex.set_widget_view(view)
	
	def update(self):
		
		if self.lastupdate != time.localtime()[3]:
			self.data = self.get_data()
			self.lastupdate = time.localtime()[3]
		else:
			time.sleep(1000)
		
	
	def get_data(self, source = None):
		
		if source == None:
			
			source = 'https://www.mh.government.bg/bg/informaciya-za-grazhdani/potvrdeni-sluchai-na-koronavirus-na-teritoriyata-na-r-blgariya/'
			
		source = requests.get(source).text
		soup = BeautifulSoup(source, 'html5lib')
		items = soup.find_all('td')
		
		result = [
			f'Потвърдени случаи: {str.rjust(items[1].text.strip(), 3)}.',
			f' От които смъртни: {str.rjust(items[3].text.strip(), 3)}.',
			f'     и излекувани: {str.rjust(items[5].text.strip(), 3)}.',
		]
		
		print(result)
		return result


CovidBulgaria()
