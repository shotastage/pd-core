from pds.pkg import Packager

class Dummy(Packager):
    
    def prepare(self):
        print('This packager is dummy.')

    def build(self):
        print('Building dummy package...')

    def install(self):
        print('Installing dummy package...')

    def register_pkg_backend(self, name):
        return 'pd'
