class URLCrawler:
  def __init__(self):
    self.urls = set()

  def do_stuff(self, url):
    print('doing stuff: ' + url)

  def add(self, url):
    self.urls.add(url)

  def check(self, url):
    return url in self.urls

  def handle(self, url):
    if (not self.check(url)):
      self.do_stuff(url)
      self.add(url)

crawler = URLCrawler()
crawler.handle('dog')
crawler.handle('dog')
crawler.handle('cat')
crawler.handle('doggo')
crawler.handle('yolo')
crawler.handle('Anthony')
crawler.handle('yolo')
