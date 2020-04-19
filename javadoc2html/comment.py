# -*- coding: utf-8 -*-
class Comment:

    def __init__(self):
        self.author = ""
        self.version = ""
        self.deprecated = ""
        self.since = ""
        self.see = ""
        self.throws = ""
        self.exception = ""
        self.param = []
        self.returns = ""
        self.description = ""
        self.link = []

    def parse_comment(self, comm):
        if comm.find("@author") != -1:
            self.author = comm.split('@author')[1].strip()
        elif comm.find("@version") != -1:
            self.version = comm.split('@version')[1].strip()
        elif comm.find("@since") != -1:
            self.since = comm.split('@since')[1].strip()
        elif comm.find("@deprecated") != -1:
            self.deprecated = comm.split('@deprecated')[1].strip()
        elif comm.find("@see") != -1:
            self.see = comm.split('@see')[1].strip()
        elif comm.find("@throws") != -1:
            self.throws = comm.split('@throws')[1].strip()
        elif comm.find("@exception") != -1:
            self.exception = comm.split('@exception')[1].strip()
        elif comm.find("@param") != -1:
            self.param.append(comm.split('@param')[1].strip())
        elif comm.find("@return") != -1:
            self.returns = comm.split('@return')[1].strip()
        elif comm.find("@link") != -1:
            try:
                self.link.append(comm
                                 .split("@link")[0]
                                 .replace("* ", "").strip())
                self.link.append(comm
                                 .split("@link")[1].strip())
            except Exception as e:
                print(e)
        else:
            self.description = comm.replace("* ", "").strip()
