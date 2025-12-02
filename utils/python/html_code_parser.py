from html.parser import HTMLParser


class CodeExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_code = False
        self.results = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "code":
            self.in_code = True

    def handle_endtag(self, tag):
        if tag.lower() == "code":
            self.in_code = False

    def handle_data(self, data):
        if self.in_code:
            self.results.append(data)