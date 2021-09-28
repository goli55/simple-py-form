from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.lang import Builder
from kivy.base import runTouchApp

Builder.load_string('''
<RootWidget>:
    text: str('THE BACKGROUND')
    front_size: 150
    Image:
        source: 'img/img1.jpg'
        allow_stretch: True
        keep_ratio: False
 
    Image:
        source: 'img/img2.jpg'
        allow_stretch: True
        keep_ratio: False
    Image:
        source: 'img/img1-1.png'
        allow_stretch: True
        keep_ratio: False
    Image:
        source: 'img/img2-2.png'
        allow_stretch: True
        keep_ratio: False
  
 ''')

class RootWidget(Label):
    
    def do_layout(self,*args):
        number_of_children = len(self.children)
        width =self.width
        width_per_child = width // number_of_children

        positions = range(0,width,width_per_child)
        for position,child in zip(positions,self.children):
            child.height=self.height
            child.x = self.x + position
            child.y = self.y
            child.width = width_per_child 

    def on_size(self,*args):
        self.do_layout()

    def on_pos(self,*args):
        self.do_layout()
    
    def add_widget(self,widget):
        super(RootWidget,self).add_widget(widget)
        self.do_layout()

    def remove_widget(self,widget):
        super(RootWidget,self).remove_widget(widget)
        self.do_layout()

runTouchApp(RootWidget())