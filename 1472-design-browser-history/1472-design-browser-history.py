class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentIndex = 0
        self.urls = [homepage]

    def visit(self, url: str) -> None:
        self.urls = self.urls[0:self.currentIndex+1]
        self.urls.append(url)
        self.currentIndex = len(self.urls)-1
        return None

    def back(self, steps: int) -> str:
        index = self.currentIndex
        self.currentIndex = 0 if self.currentIndex - steps < 0 else self.currentIndex - steps
        return self.urls[self.currentIndex]
    def forward(self, steps: int) -> str:
        index = self.currentIndex
        self.currentIndex = len(self.urls)-1 if self.currentIndex + steps >=  len(self.urls) else self.currentIndex + steps
        return self.urls[self.currentIndex]

