from pages.base_page import BasePage

class HomePage(BasePage):

    def open_home(self):
        self.open("/")
    
    def get_home_title(self) -> str:
        return self.get_title()
