class Abstraction_interface:

    def __init__(self, name, modifier, interface=None):
        self.name = name
        self.interface = interface
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
