from kivy.lang import Builder
from kivymd_extensions.akivymd import*
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
import requests


import urllib.robotparser
from urllib.parse import urlparse
from kivymd.uix.button import MDFloatingActionButton
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.button import MDRoundFlatButton
import threading
from kivymd_extensions.akivymd import*
import threading 
from kivy.uix.behaviors import ButtonBehavior
custom_sheet = None
from kivy.uix.image import Image,AsyncImage
from kivy.network.urlrequest import UrlRequest
#from kivymd_extensions.sweetalert import SweetAlert 
from kivy.uix.textinput import TextInput
from kivy.uix.codeinput import CodeInput
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.recycleview import RecycleView 
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.uix.image import Image
from kivymd.uix.swiper import MDSwiper,MDSwiperItem
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.screen import MDScreen
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.toast import toast
from bs4 import BeautifulSoup
from kivymd.app import MDApp
from kivy.properties import StringProperty,ObjectProperty,NumericProperty
from kivy.utils import get_color_from_hex
from android.storage import app_storage_path

app_storage_directory_path = app_storage_path()


KV = '''
#:import threading threading
#: import NoTransition kivy.uix.screenmanager.NoTransition    
#: import HtmlLexer pygments.lexers.html.HtmlLexer
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import SliverToolbar __main__.SliverToolbar
#:set text_color get_color_from_hex("#4a4939")
#:set focus_color get_color_from_hex("#e7e4c0")
#:set ripple_color get_color_from_hex("#c5bdd2")
#:set bg_color get_color_from_hex("#f7f4e7")
#:set selected_color get_color_from_hex("#0c6c4d")
<ItemForCustomBottomSheet@OneLineListItem>:
    on_release:app.imagescreen()
<SliverToolbar>:
	right_action_items: [["dots-vertical", lambda x: app.open_content_for_all_download()]]
	left_action_items: [["arrow-left", lambda x: app.change_to_whole_screen()]]
	
<MyButton>:
	size_hint:None,None
	size:dp(360),dp(130)
<Ca>:
	elevation:20
	size_hint_y:None
	height:dp(130)	
	ripple_behavior:True
	on_release:app.abc(self)				
		#	on_release:app.oneimage()
	MDRelativeLayout:
		MDProgressBar:
			id:sp
			max:1
			value:0
			color: app.theme_cls.accent_color
			pos:(1.0,1.0)
		AKImageLoader:
			id:ab
			source:root.source									
		Myicon:
			id:cd
			sourcea:root.sourcea
			icon:"download"
			on_release:app.abcd(self)
			pos_hint: {'center_x': .9, 'center_y': .5}
		
<ContentSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "150dp"

    MDTopAppBar:
        title: 'Download all images'

    ScrollView:

        MDGridLayout:
            cols: 1
            adaptive_height: True

            ItemForCustomBottomSheet:
                icon: "download"
                text: "download"
                on_release:app.download_all_images()

            ItemForCustomBottomSheet:
                icon: "exit-to-app"
                text: "Exit"
	
<MyLabel@MDLabel>
    valign: "center"
    theme_text_color: "Custom"
    text_color: 1,1,1,1
<Lan@MDCard+FitImage>	
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: focus_color
    unfocus_color: bg_color
    text_color: text_color
    icon_color: text_color
    ripple_color: ripple_color
    selected_color: selected_color


<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: bg_color
    text_color: text_color
    icon_color: text_color
    _no_ripple_effect: True
<DownloadCustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height:dp(140)
    ScrollView
	    MDGridLayout:
	    	cols: 1
	        adaptive_height: True
	        OneLineListItem:	        	
	        	text:"In html"
	        	on_release:app.download_in_html()
	        	
	        
	        OneLineListItem:
	        	text:"In text"
	        	on_release:app.download_in_text()
	        OneLineListItem:
	        	text:"download in both format"	        						
	        	on_release:app.download_in_both_format()
	        
<ContentCustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: dp(300)
    ScrollView
	    MDGridLayout:
	    	cols: 1
	        size_hint_y: None
   		 height: self.minimum_height
	        ItemForCustomBottomSheet:
	        	
	        	text:"images in the website"
	        	
	        
	        OneLineListItem:
	        	text:"videos in the website"
	        
	        
	        OneLineListItem:
	        	text:"audios in the website"
	        
	        
	        
	        OneLineListItem:
	        	text:"Extreme scraper support"
	        	on_release:app.change_to_extreme_screen()
	        
	        OneLineListItem:
	  	  	text:"Download html"
	  	  	on_release:app.open_download()
	        OneLineListItem:
	  	  	text:"clear all"	  	  
	  	  	on_release:app.refresh()
	  	  
	       
	         
	        
	        
	        	
    
    		
    
MDScreen:

    MDNavigationLayout:

        ScreenManager:
			id:a
            MDScreen:
            	name:"home screen"
            	MDFloatLayout:
					MDBoxLayout:
						spacing:dp(7)
						orientation:"vertical"
		                MDTopAppBar:
		                    id:toolbar
		                    title: "Home screen"
		                    elevation: 10
		                    radius:[dp(0),dp(0),dp(30),dp(30)]
		                    pos_hint: {"top": 1}
		                    md_bg_color: focus_color
		                    specific_text_color: text_color

		                    left_action_items:
		                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
		                    
						ScrollView: 
							do_scroll_x: False
		    				do_scroll_y: True
							MDBoxLayout:
								adaptive_size: True
								orientation:"vertical"
								spacing:dp(15)
								
								
								MD3Card:
									md_bg_color:get_color_from_hex("#f4dedc")
									orientation:"vertical"
									size_hint: None, None
				   				 size: root.width, "200dp"
				   				 elevation:10
				   				 radius:[30,]
				   				 spacing:dp(5)
				   				 on_release:app.change_to_whole_screen()
								
									FitImage:
										source:"code-1076536__480.webp"
									
										elevation:15
				   				 	radius:[30,]
				   				 MDLabel:
								    	text:"Scrap whole website"
								    	pos_hint:{"center_x":.5}
								   	 adaptive_size: True
								   	 theme_text_color: "Custom"
								   	 outline_width:10
								   	 outline_color:(0,1,0)
								   	 text_color:0,0,1,1
			
				   				 
								MD3Card:
									size_hint: None, None
				   				 size: root.width, "100dp"
				   				 elevation:15
				   				 radius:[30,]
									MDLabel:
										text:"click"
									
			MDScreen:
				name:"scrap_web"	
				MDFloatLayout:
					id:html_collect_page
					md_bg_color:app.theme_cls.primary_dark
					MDGridLayout:
						cols:1
#						orientation:"vertical"
						spacing:dp(8)
						MDTopAppBar:
		                    title: "Scrap_whole_website"
		                    elevation: 10
		                    opposite_colors: True
		                    pos_hint: {"top": 1}
		                    md_bg_color:.3,.6,.3,1
		                    specific_text_color: text_color
		                   

		                    left_action_items:
		                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
						MD3Card:
							orientation:"horizontal"
							size_hint: None, None
							pos_hint:{"top":1}
					   	 size: root.width, "40dp"
				   		 elevation:15
					   	 radius:[30,]
					   	 line_color:(230/255, 230/255, 200/255, 0.8)
					   	 md_bg_color: 217/255, 217/255, 217/255,1
					   	 TextInput:
					   	 	id:enter_url_inputbox
					   	 	foreground_color: [86/255,150/255,79/255,1]
				    			hint_text:"enter url example https://xyz.com"
				    			padding:[20,10,0,0,]
						    	background_color:0,0,0,0
						    	font_size:"24sp"
						    	multiline:False
							    cursor_width:8
							    on_text_validate:threading.Thread(target=app.check_url).start()														
							
					
							
															    
																			
							    
							
						MD3Card:
						    id:html_card
						    size: "360dp", "800dp"
						    orientation:"vertical"		 
						    radius:[dp(26),dp(26),dp(0),dp(0)]
						    
						    md_bg_color:.1,0.7,.2,.89
						    RecycleView:					
						        viewclass:'Text'
						       
						        RecycleBoxLayout:
						            id:abn
						            default_size:None, dp(36)
						            default_size_hint:1, None
						            size_hint_y:None
						            height:self.minimum_height
						            orientation:'vertical'		              			       		 					              			                        							               			
					MDIconButton:
						id:playicon						
						icon:"play"
						pos_hint:{"center_x":.95,"center_y":.9}					
						on_release:threading.Thread(target=app.check_url).start()	         		 				                				              			       		 					              			                        											           		 				                				              			       		 					              			                        							
				           		 				                				              			       		 					              			                        							                
			MDScreen:
				on_enter:app.add()
				on_leave:app.remove_image()
				name:"imagescreen"	
				MDSliverAppbar:
					background_color: get_color_from_hex("2d4a50")


					toolbar_cls: SliverToolbar()
					MDSliverAppbarHeader:

            			MDRelativeLayout:
            			
            				FitImage:
            			
        
            					source:"undraw_Image_viewer_re_7ejc.png"
            				

					MDSliverAppbarContent:
			        	id: bo
			            orientation: "vertical"
			            padding: "12dp"
			            spacing: "12dp"
			            adaptive_height: True
			            
			           
			            	
			MDScreen:
		    	name:"ExtremeScrap"
		    	MDGridLayout:
		    		cols:1
		    		spacing:dp(5)
		    		MDTopAppBar:
					    id:tool_bar_info
			        	title: "Tag search page"
			            elevation: 10
			            pos_hint: {"top": 1}
			            md_bg_color: focus_color
			            specific_text_color: text_color
			            left_action_items:
			            	[['arrow-left', lambda x:app.change_to_whole_screen()]]
		    		MDFloatLayout:
		    			size_hint:.9,.07
		    			padding:20
		    			pos_hint:{"center_x":.5,"center_y":.8}
		    			canvas.before:
							Color:
								rgba:230/255,230/255,230/255,1
							RoundedRectangle:
								size:self.size
								pos:self.pos
								radius:[70]
		    		
		    			
				    	TextInput:	
				    		id:tag_search		    		
		    				pos_hint:{"center_x":.5,"center_y":.5}				    				    			
				    		multiline:False				    
				            foreground_color: [86/255,150/255,79/255,1]
				            cursor_width:8
				            hint_text: "Enter tag name here"
				            background_color: [1,1,1,0]
				            font_size:"20sp"
				            padding:[28]
				        MDIconButton:
				        	icon:"play"
				        	pos_hint:{"center_x":.9,"center_y":.5}
				        	on_release:app.get_tag_info()
				        					        					        						    								            									  				    						    					
			    	RV:
					    viewclass: 'Ab'			
					    RecycleGridLayout:
					        cols:4
					        default_size: None, dp(30) 
					        default_size_hint: 1, None
					        size_hint_y: None
					        height: self.minimum_height
					        spacing: dp(10)
			MDScreen:
				name:"tag_info"
				on_leave:app.del_info()
				MDFloatLayout:
					MDBoxLayout:
						orientation:"vertical"
						MDTopAppBar:
						    id:tool_bar_info
				        	title: ""
				            elevation: 10
				            pos_hint: {"top": 1}
				            md_bg_color: focus_color
				            specific_text_color: text_color
				            left_action_items:
				            	[['arrow-left', lambda x:app.change_to_extreme_screen()]]	
				        ScrollView:
				        	MDBoxLayout:
				        		id:info_text
				        		orientation:"vertical"
				        		spacing:dp(10)
				        		size_hint_y:None
				        		height:self.minimum_height
				    MDFloatingActionButton:
				    	icon:"magnify"
				    	pos_hint: {'center_x': .85, 'center_y': .08}
				    	on_release:app.get_attr()

#attribute screen				       				       
			MDScreen:
				name:"attribute"
				MDBoxLayout:
					orientation:"vertical"
					MDIconButton:
						icon:"arrow-left"
						on_release:a.current="tag_info"
						pos_hint:{"center_x":.05,"center_y":.94}
						
					RecycleView:					
						viewclass:'Text'
							       
						RecycleBoxLayout
							id:attri 
						    default_size:None, dp(36)
						    default_size_hint:1, None
					        size_hint_y:None
					        height:self.minimum_height
						    orientation:'vertical'	
					
							        		
		        			        	
		        		    
						
								
			OneImage:
				name:"Oneimage"
				MDBoxLayout:
					orientation:"vertical"
					MDIconButton:
						icon:"arrow-left"
						on_release:
							app.imagescreen()
						pos_hint:{"center_x":.05,"center_y":.94}
		
					AKImageLoader:
						id:ab
			#			size_hint:1,.2
						source:""
						allow_stretch:True
						pos_hint:{"center_x":.5,"center_y":.5}
		
											
													
																	
											
				
					                    

        MDNavigationDrawer:
            id: nav_drawer
            enable_swiping:True
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Web Scrapper"
                    title_color: text_color
                    text: "Header text"
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Scrap Web"

                DrawerClickableItem:
                    icon: "home"
#                    right_text: "+99"
                    text_right_color: text_color
                    text: "Home"
                    on_release:a.current="home screen"

                DrawerClickableItem:
                    icon: "web"
                    text: "Full web scrap"
                    on_release:a.current="scrap_web"

                    

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "#kivy"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "#kivymd"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "#akivymd"
<Ab>:
	on_release:app.change_to_info_screen(self)                   
<Floatingicon>:
	icon:"play"      
	pos_hint: {'center_x': .85, 'center_y': .08}
	on_release:app.callback()      
	elevation:20   


<Infotext>:
	size_hint_y:None
	height:self.minimum_height	
<Text>:
	size_hint_y:None
	height:self.minimum_height	
	adaptive_height:True
	background_color:0,0,0,0
	foreground_color: [0,0,0,1]
	font_size:"16sp"
<MyModal@ModalView>:
	size_hint:.3,.3
	background_color:0,0,0,0
	

    BoxLayout:
        orientation: 'vertical'

        MDSpinner:
        	active:True
'''
#req = UrlRequest('https://httpbin.org/headers', got_json) 
class Ca(MDCard):
	source=StringProperty()
	sourcea=StringProperty()	

	
	
	#def on_touch_down(self,instance):
#		print(instance.source)	
#
class Allimage(MDScreen):
	pass
			
class Text(TextInput):
	pass
class Floatingicon(MDFloatingActionButton):
	pass	


class Myicon(MDIconButton):
	sourcea=StringProperty()	


class Tab(MDTabsBase,MDFloatLayout):
	pass


class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type_height = "medium"
        self.headline_text = "Headline medium"
       
        
        
class OneImage(MDScreen):
	pass


class MyButton(ButtonBehavior, AsyncImage):
	pass	
	
class Ab(MDRoundFlatButton):
	pass

class Infotext(TextInput):
	pass
class MD3Card(MDCard, RoundedRectangularElevationBehavior):
	text = StringProperty()

			
# Tag of html search									
class RV(RecycleView):
	html_tag_list=["!--...--","!DOCTYPE","a","abbr","acronym","abbr", "address","applet","embed","object","area","article","aside","audio","b","base","basefont","bdi","bdo","big","blockquote","body","br","button","canvas","caption","center","cite","code","col","colgroup","colgroup","data","datalist","dd","del","details","dfn","dialog","dir",	"div","dl","dt","em","embed","fieldset","figcaption","figure","font","footer","form",	"frame","frameset","h1", "h6","head","header","hr","html","i","iframe","img","input","ins","kbd",	"label","input","legend","li","link","main","map",	"mark","meta","meter","nav","noframes","noscript","object","ol","optgroup","option",	"output","p","param","picture","pre","progress",	"q","rp","rt","ruby","s","samp","script","section","select","small","source","span","strike", "s","strong","style","sub","summary", "details", "sup","svg","table","tbody","td","template","textarea",	"tfoot","th","thead","time","title","tr","track","tt",	"u","ul","var","video","wbr"]
	def __init__(self, **kwargs):
	    super(RV, self).__init__(**kwargs)
	    self.data = [{'text': str(x)} for x in self.html_tag_list]


class Scrap(MDApp):	
	custom_sheet = None    				
	download_sheet=None     


	def get_attr(self):
		ab=self.root.ids.tool_bar_info.title
		self.root.ids.a.current="attribute"
		L=[]
		n=BeautifulSoup(ab, 'html.parser')
		for tag in soup.find_all(ab):
			print(tag)
			print(type(tag))
			attribute = tag.attrs 
		
		  
		# Print the output 
		
			L.append(str(attribute))
		self.root.ids.attri.parent.data=[{'text': x} for x in L]
		
	
	def oneimage(self):
		self.root.ids.a.current="Oneimage"
	def change_to_info_screen(self,instance):
		
		self.root.ids.a.current="tag_info"
		self.root.ids.tool_bar_info.title=instance.text
		ab=str(soup.find_all(instance.text))
		cd=ab.replace("[","")
		da=cd.replace("]","")
		ea=da.rsplit(", ")
		for i in ea:
			self.root.ids.info_text.add_widget(Infotext(text=i))
		
	def get_tag_info(self):
		self.root.ids.a.current="tag_info"
		self.root.ids.tool_bar_info.title=self.root.ids.tag_search.text
		ab=str(soup.find_all(self.root.ids.tag_search.text))
		cd=ab.replace("[","")
		da=cd.replace("]","")
		ea=da.rsplit(", ")
		for i in ea:
			self.root.ids.info_text.add_widget(Infotext(text=i))
		
		
				
		
		
	
	def build(self):
		self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
		self.theme_cls.primary_hue = "A700"
#		
	
		return Builder.load_string(KV)
#	def got_json(req, result):
#		for key, value in req.resp_headers.items():
#			print('{}: {}'.format(key, value))

#One image one clicked on number of images got in the website		
	def abc(self,instance):
		self.root.ids.a.current="Oneimage"
		self.root.ids.ab.source=instance.source

		
						
	def del_info(self):
		self.root.ids.info_text.clear_widgets()	

#function applied on image card icon button		
	def abcd(self,instance):
		global ng
		ng=instance
		urla=instance.sourcea
		toast(urla)
		ab=urla.replace("/","")
		req=UrlRequest(urla,chunk_size=1024,on_progress=self.get_prog,file_path="images/"+ab)
	
	
	
	def redi(self,request,result):
		SweetAlert(window_control_buttons="mac-style").fire("The url you entered is redrecting",type='info')
		modal_inst.dismiss()	
		
	
	
	
	def get_prog(self,request, current_size, total_size):
		abde=current_size/total_size
		print(abde)
		ng.parent.children[2].value=abde
	
	
	
	def err(self,request,error):
		SweetAlert(window_control_buttons="mac-style").fire(str(error),type='info')
		modal_inst.dismiss()		
		
		
#		toast(str(error),gravity=70)
	
		
#	def got_value(self,current_size,total_size):
			


	def check_url(self):
		try:
			url = self.root.ids.enter_url_inputbox.text
			domain = urlparse(url).netloc
			if url.find("https")==0:
				an=f"https://{domain}"
				rp = urllib.robotparser.RobotFileParser()
				rp.set_url(f"{an}/robots.txt")
				rp.read()
				a=rp.can_fetch("*", url)
				if a==True:
					self.get_code()
				else:
					SweetAlert(window_control_buttons="mac-style").fire("Sorry This is not allowed to scrap",type='info')
			else:
				SweetAlert(window_control_buttons="mac-style").fire("I think you entered wrong url",type='info')
				
		except:
			SweetAlert(window_control_buttons="mac-style").fire("Please enter valid url",type='info')
				
	
				
    	
	def get_code(self):
		if self.root.ids.playicon.disabled!=True:
		#Clock.schedule_interval(self.abnge,1)
			url = self.root.ids.enter_url_inputbox.text
	#		self.root.ids.whole_code_text.hint_text="Running....."
			r = UrlRequest(url, self.got_code,on_error=self.err,on_redirect=self.redi)
			global modal_inst
			modal_inst = Factory.MyModal(auto_dismiss=False)
			if self.root.ids.abn.children==[]:
				modal_inst.open()
			else:
				modal_inst.dismiss()		

	
	def got_code(self, req, result):
		
		global url
		url=self.root.ids.enter_url_inputbox.text
		self.root.ids.playicon.disabled=True
#		store = JsonStore('hello.json')
		global soup
		soup = BeautifulSoup(result, 'html.parser')
		global code_text
		code_text=soup.prettify()
		ba=code_text.splitlines()
		self.root.ids.abn.parent.data=[{'text': x} for x in ba]
		
		modal_inst.dismiss()		
		self.root.ids.html_collect_page.add_widget(Floatingicon())
		self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
		self.custom_sheet.open()
		
		#for item in soup.find_all('img'):
#			self.root.ids.imagetab.add_widget(Ca(source=item['src']))
#		for item in soup.find_all('img'):
#		    self.root.ids.imagetab.add_widget(Ca(source=item['src']))
	def download_all_images(self):
		try:
			for item in soup.find_all('img'):
				if item['src'].find("https")==0:
					urla=item['src']
					ab=urla.replace("/","")
					req=UrlRequest(urla,file_path="images/"+ab)
				else:
					urla=url+item['src']
					ab=urla.replace("/","")
					req=UrlRequest(urla,file_path="images/"+ab)
		except:
			try:
				for item in soup.find_all('img'):
					if item['data-srcset'].find("https")==0:
						urla=item['data-srcset']
						ab=urla.replace("/","")
						req=UrlRequest(urla,file_path="images/"+ab)
					else:
						urla=url+item['data-srcset']
						ab=urla.replace("/","")
						req=UrlRequest(urla,file_path="images/"+ab)
			except:
				try:
					for item in soup.find_all('img'):
						if item['data-src'].find("https")==0:
							urla=item['data-src']
							ab=urla.replace("/","")
							req=UrlRequest(urla,file_path="images/"+ab)
						else:
							urla=url+item['data-src']
							ab=urla.replace("/","")
							req=UrlRequest(urla,file_path="images/"+ab)
					
				except:
					try:
						for item in soup.find_all('img'):
							if item['data-fallback-src'].find("https")==0:
								urla=item['data-fallback-src']
								ab=urla.replace("/","")
								req=UrlRequest(urla,file_path="images/"+ab)
							else:
								urla=url+item['data-fallback-src']
								ab=urla.replace("/","")
								req=UrlRequest(urla,file_path="images/"+ab)
					except:
						pass
					
				
		
	
	def add(self,*args):
		try:
			for item in soup.find_all('img'):
				if item['src'].find("https")==0:
					self.root.ids.bo.add_widget(Ca(source=item['src'],sourcea=item['src']))
				else:
					self.root.ids.bo.add_widget(Ca(source=url+item['src'],sourcea=url+item['src']))
		except:
			try:
				for item in soup.find_all('img'):
					if item['data-srcset'].find("https")==0:
						self.root.ids.bo.add_widget(Ca(source=item['data-srcset'],sourcea=item['data-srcset']))
					else:
						self.root.ids.bo.add_widget(Ca(source=url+item['data-srcset'],sourcea=url+item['data-srcset']))
			except:
				try:
					for item in soup.find_all('img'):
						if item['data-src'].find("https")==0:
							self.root.ids.bo.add_widget(Ca(source=item['data-src'],sourcea=item['data-src']))
						else:
							self.root.ids.bo.add_widget(Ca(source=url+item['data-srcset'],sourcea=url+item['data-src']))
				except:
					try:
						for item in soup.find_all('img'):
							if item['data-fallback-src'].find("https")==0:
								self.root.ids.bo.add_widget(Ca(source=item['data-fallback-src'],sourcea=item['data-fallback-src']))
							else:
								self.root.ids.bo.add_widget(Ca(source=url+item['data-fallback-src'],sourcea=url+item['data-fallback-src']))
					except:
						pass
			
							
#	def abnge(self,dt):		
#		self.root.ids.abc.text="hshe"
			
	
	def remove_image(self):
		self.root.ids.bo.clear_widgets()
			
	def open_download(self):
		self.download_sheet = MDCustomBottomSheet(screen=Factory.DownloadCustomSheet())
		self.download_sheet.open()	
		self.custom_sheet.dismiss(force=False)		
	def download_in_html(self):
		url_of_html=self.root.ids.enter_url_inputbox.text
		ab_html=url_of_html.replace("/","")
		f = open(f"htmlpage/{ab_html}.html", "w+")
		f.write(code_text)
		f.close()
	
	def download_in_text(self):
		url_of_text=self.root.ids.enter_url_inputbox.text
		ab_text=url_of_text.replace("/","")
		f = open(f"textpage/{ab_text}.txt", "w+")
		f.write(code_text)
		f.close()
	
	def download_in_both_format(self):
		url_of_html=self.root.ids.enter_url_inputbox.text
		
		ab_html=url_of_html.replace("/","")
		f = open(f"htmlpage/{ab_html}.html", "w+")
		f.write(code_text)
		f.close()
		url_of_text=self.root.ids.enter_url_inputbox.text
		ab_text=url_of_text.replace("/","")
		f = open(f"textpage/{ab_text}.text", "w+")
		f.write(code_text)
		f.close()
		
	def refresh(self):
#		self.root.ids.enter_url_inputbox.readonly=False
		self.root.ids.abn.parent.data=[]		
		self.root.ids.enter_url_inputbox.text=""
		self.root.ids.playicon.disabled=False	
		self.root.ids.html_card.md_bg_color=.1,0.7,.2,.89	
		
				
			
			
	def callback(self):
		self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet())
		self.custom_sheet.open()			
			
#			self.root.ids.whole_code_text.text+=item['src']
#			store.put('tio', name=self.root.ids.whole_code_text.text)		
#		self.root.ids.whole_code_text.text=code_text 
	
	def open_content_for_all_download(self):
		self.custom_shee= MDCustomBottomSheet(screen=Factory.ContentSheet())
		self.custom_shee.open()
		
	
	def change_to_whole_screen(self):
		self.root.ids.a.transition = SlideTransition(direction='left', duration=.25)
		self.root.ids.a.current="scrap_web"
	
	def change_to_extreme_screen(self):
		self.root.ids.a.transition = SlideTransition(direction='left', duration=.25)
		self.root.ids.a.current="ExtremeScrap"
	        	
		
	def imagescreen(self):
		self.root.ids.a.transition = SlideTransition(direction='left', duration=.25)
		self.root.ids.a.current="imagescreen"
	


Scrap().run()