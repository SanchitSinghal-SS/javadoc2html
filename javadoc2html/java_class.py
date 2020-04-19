class Abstraction_class:

    def __init__(self, name, modifier):
        self.name = name
        self.interface = ""
        self.parent = ""
        self.mod = modifier
        self.methods = []
        self.fields = []

    def add_method(self, prototype, mod, name, args, type_ret, comment=None):
        method_dict = {
            "prot": prototype,
            "mod": mod,
            "name": name,
            "args": args,
            "return": type_ret,
            "comment": comment
        }

        self.methods.append(method_dict)

    def add_field(self, mod, name, type_):
        field = {
            "mod": mod,
            "name": name,
            "type": type_
        }

        self.fields.append(field)

    def add_interface(self, row):
        self.interface = row

    def add_parent(self, row):
        self.parent = row
