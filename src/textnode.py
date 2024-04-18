# https://www.boot.dev/assignments/cdae7fca-a7dc-4706-b2c5-7a03d66db1c9


class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self):
        #if self.text == self.text_type:
        return True
        
    def __repr__(self):
        return f"{self.text}, {self.text_type}, {self.url}"
    