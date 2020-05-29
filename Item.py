class Item(object):
    def __init__(self, site, classificacao):
        self.site = site
        self.classificacao = classificacao

    def __str__(self):
        return self.site


