from kivy.lang import Builder
from kivymd.app import MDApp
import requests
from kivy.core.clipboard import Clipboard # helps with the copy to clipboard function

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lightblue"
        return Builder.load_file('main.kv')
    
    def submit(self):
        original_url = self.root.ids.url_input.text
        api_url = "https://tinyurl.com/api-create.php"
        response = requests.post(api_url, data={"url": original_url})

        if response.ok:
            shorterned_url = response.text
            self.root.ids.copy_label.text = f"{shorterned_url}"
        else:
            self.root.ids.copy_label.text = "Error: Failed to Shortern URL"

    def copy_to_clipboard(self):
       text_to_copy = self.root.ids.copy_label.text
       Clipboard.copy(text_to_copy) 

MainApp().run()
#Done Please Like and Subscribe, Share
# Link(Github) and Explanation in the description below