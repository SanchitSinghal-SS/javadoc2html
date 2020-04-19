class File:

    def __init__(self):
        self.classes = []
        self.interfaces = []
        self.comments = []
        self.imports = []
        self.packages = []
        self.name = ''
        self.description = ""

    def add_class(self, class_):
        self.classes.append(class_)

    def add_imports(self, row):
        self.imports.append(row)

    def add_interface(self, interface):
        self.interfaces.append(interface)

    def add_comments(self, comment):
        self.comments.append(comment)

    def add_package(self, package):
        self.packages.append(package)

    def add_name(self, name):
        self.name = name
