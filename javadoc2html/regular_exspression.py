import re


class Regular_expressions:

    start_comm_big = re.compile(r'.*/\*\*.*')

    finish_comm_big = re.compile(r'.*\*/.*')

    class_pattern = re.compile(r'(\w+\s)?class\s(\w+)\s(.*)?.*\s?')

    method_pattern = re.compile(r'^.(((?!if).)*)\((.*)\)(.*{)?$')

    method_pattern_inter = re.compile(r'(.*) (.*)\((.*)\);')

    interface_pattern = re.compile(r'(\w+)?.*interface.*\s(\w+).*')

    import_pattern = re.compile(r"import (.*);")

    package_pattern = re.compile(r"package (.*);")

    field_pattern = re.compile(r"(.*) (.*);")
