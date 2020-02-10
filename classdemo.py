class Python:
    version = 2

    def __init__(self, version, pip):
        self.version = version
        self.pip = pip

    def get_version(self):
        print(self.version)

    def install_pip(self):
        if self.pip:
            print("already installed")
        else:
            self.pip = True
            print('installing')


pt = Python('1.21', False)
pt.get_version()
pt.install_pip()
pt.install_pip()
