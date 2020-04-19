# -*- coding: utf-8 -*-
import os
from os import path
from java_class import Abstraction_class
from interface import Abstraction_interface
from java_file import File
from regular_exspression import Regular_expressions as reg
import re
from comment import Comment


class Java_handler:

    def __init__(self, directory):
        self.dir = directory

        self.files = []

        self.is_class = False
        self.is_interface = False
        self.is_comment = False
        self.is_method = False

    def get_files_from_dir(self):
        for file in os.listdir(self.dir):
            if file.endswith(".java"):
                f = self.read_java_file(file)
                self.files.append(f)
        return self.files

    def read_java_file(self, file):
        parse_file = File()
        with open(path.join(self.dir, file), encoding="utf8") as f:
            for line in f:
                if not self.is_class and not self.is_interface:
                    if reg.import_pattern.match(line):
                        parse_file.add_imports(reg
                                               .import_pattern
                                               .match(line)
                                               .group(1))
                    elif reg.package_pattern.match(line):
                        parse_file.add_package(reg
                                               .package_pattern
                                               .match(line)
                                               .group(1))
                    elif reg.class_pattern.match(line):
                        self.is_class = True
                        cl = self.parse_class_name(reg
                                                   .class_pattern
                                                   .match(line))
                    elif reg.interface_pattern.match(line):
                        self.is_interface = True
                        inter = self.parse_inter_name(reg
                                                      .interface_pattern
                                                      .match(line))
                    elif reg.start_comm_big.match(line) \
                            and not self.is_comment:
                        buf = line
                        comment = Comment()
                        self.is_comment = True
                    elif self.is_comment \
                            and reg.finish_comm_big.match(line) is None:
                        buf += line
                        comment.parse_comment(line)
                    elif self.is_comment and reg.finish_comm_big.match(line):
                        self.is_comment = False
                        parse_file.add_comments(comment)

                elif self.is_class:
                    if reg.start_comm_big.match(line) \
                            and not self.is_comment:
                        buf = line
                        comment = Comment()
                        self.is_comment = True
                        stop = False
                    elif self.is_comment \
                            and reg.finish_comm_big.match(line) is None \
                            and not stop:
                        buf += line
                        comment.parse_comment(line)
                    elif reg.finish_comm_big.match(line):
                        stop = True
                    elif reg.method_pattern.match(line) and\
                            self.is_method is False:
                        self.is_method = True
                        if self.is_comment:
                            self.parse_method_name(reg
                                                   .method_pattern
                                                   .match(line), cl,
                                                   comment=comment)
                            self.is_comment = False
                            stop = False
                        else:
                            self.parse_method_name(reg
                                                   .method_pattern
                                                   .match(line), cl)
                    elif self.is_method and "   }" in line:
                        self.is_method = False
                    elif reg.field_pattern.match(line) and \
                            self.is_method is False:
                        self.parse_field_name(reg
                                              .field_pattern
                                              .match(line), cl)
                elif self.is_interface:
                    if reg.method_pattern_inter.match(line):
                        self.parse_method_iter_name(reg
                                                    .method_pattern_inter
                                                    .match(line), inter)
                    elif reg.field_pattern.match(line) and \
                            self.is_method is False:
                        self.parse_field_name(reg
                                              .field_pattern
                                              .match(line), inter)
        if self.is_class:
            parse_file.add_class(cl)
            self.is_class = False
        if self.is_interface:
            parse_file.add_interface(inter)
            self.is_interface = False
        self.is_comment = False
        self.is_method = False
        parse_file.add_name(file)
        return parse_file

    @staticmethod
    def parse_method_name(match, obj, comment=None):
        index = match.group(1).rfind(' ')
        name = match.group(1)[index:].strip()
        type_ = match.group(1)[:index]
        args = match.group(3)
        if type_.find('public') != -1:
            mod = "public"
            type_ = type_[9:]
        elif type_.find('private') != -1:
            mod = "private"
            type_ = type_[7:]
        elif type_.find('protected') != -1:
            mod = 'protected'
            type_ = type_[9:]
        else:
            mod = "package-private"
        type_ = type_.strip()
        if comment is not None:
            obj.add_method(match.group(0), mod, name, args, type_, comment)
        else:
            obj.add_method(match.group(0), mod, name, args, type_)

    @staticmethod
    def parse_class_name(match):
        cl = Abstraction_class(match.group(2), match.group(1))
        property_ = match.group(3)
        if re.match(r"extends (.*) implements (.*)", property_):
            cl.add_parent(re.match(r"extends (.*) implements (.*)",
                                   property_).group(1))
            cl.add_interface(re.match(r"extends (.*) implements (.*)",
                                      property_).group(2))
        if re.match(r"extends (.*)", property_):
            cl.add_parent(re.match(r"extends (.*)",
                                   property_).group(1))
        if re.match(r"implements (.*)", property_):
            cl.add_interface(re.match(r"implements (.*)",
                                      property_).group(1))
        return cl

    @staticmethod
    def parse_inter_name(match):
        inter = Abstraction_interface(match.group(2), match.group(1))
        return inter

    @staticmethod
    def parse_field_name(match, obj):
        name = match.group(2).split(' ').pop()
        type_ = match.group(1).strip()
        if type_.find('public') != -1:
            mod = "public"
            type_ = type_[9:]
        elif type_.find('private') != -1:
            mod = "private"
            type_ = type_[7:]
        elif type_.find('protected') != -1:
            mod = 'protected'
            type_ = type_[9:]
        else:
            mod = "package-private"
        type_ = type_.strip()
        if '=' in type_:
            type_ = type_.split('=')[0].strip().split(' ')
            name = type_[len(type_) - 1].strip()
            type_ = type_[0].strip()
        obj.add_field(mod, name, type_)

    @staticmethod
    def parse_method_iter_name(match, inter):
        type_ = match.group(1)
        name = match.group(2)
        args = match.group(3)
        if type_.find('public') != -1:
            mod = "public"
            type_ = type_[9:]
        elif type_.find('private') != -1:
            mod = "private"
            type_ = type_[7:]
        elif type_.find('protected') != -1:
            mod = 'protected'
            type_ = type_[9:]
        else:
            mod = "package-private"
        type_ = type_.strip()
        inter.add_method(match.group(0), mod, name, args, type_)
