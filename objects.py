
class LoaderFactory(object):

    @staticmethod
    def make(loader):
        loaderClass = loader[0].upper() + loader[1:].lower() + 'Loader'
        return globals()[loaderClass]()

class JsonLoader(object):
    def load(self):
        return '{"name": "Bayo", "age": "18", "height": "6ft"}'

class TupleLoader(object):
    def load(self):
        return ("Kudi", 20, "5ft 11in")

class DictLoader(object):
    def load(self):
        return {'name': 'Femi', "age": 19, 'height': '5ft 10in'}

print LoaderFactory.make('json').load()
print LoaderFactory.make('tuple').load()
print LoaderFactory.make('dict').load()
