# -*- coding: utf-8 -*-
import os


class Converter:

    def __init__(self, files, project_name):
        self.project_name = project_name + "_html"
        self.project = project_name
        self.files = files
        self.create_dir()
        self.create_common_file()

    def create_dir(self):
        try:
            os.mkdir(self.project_name)
            with open(os.path.join(self.project_name, "css.css"), "w") as f:
                f.write(self.create_css())
        except FileExistsError:
            with open(os.path.join(self.project_name, "css.css"), "w") as f:
                f.write(self.create_css())
        except OSError as e:
            print(e)

    @staticmethod
    def create_css():
        css = "body{display: flex;flex-direction: column;}" \
              ".left{padding-left:125px;}}li{padding-top:6px;}" \
              "ul{padding:10px;}.flex-container{display:flex;" \
              " flex-wrap: wrap;justify-content:left;}" \
              "h3,h2{text-align:center;}.shell{display:flex;}" \
              ".flex-container>div{width: 20%;" \
              "margin-top:20px;margin-left:2%;" \
              "margin-right:2%;margin-bottom:25px;}" \
              ".lname {font-weight:bold;}"
        return css

    def create_html_files(self):
        for file in self.files:
            self.create_html_file(file)

    def create_html_file(self, file):
        name = file.name
        name = name.replace(".java", ".html")
        with open(os.path.join(self.project_name, name), "w",
                  encoding="utf8") as f:
            f.write('<head> <link rel="stylesheet"'
                    ' href="css.css">'
                    '<meta http-equiv="Content-Type"'
                    ' content="text/html; charset=charset=utf-8">'
                    '<style> '
                    'body{font-family: Trebuchet MS, Arial, Helvetica,'
                    ' sans-serif !important;}'
                    '#tbl {  font-family: Trebuchet MS, Arial,'
                    'Helvetica, sans-serif; '
                    ' border-collapse: collapse;  width: 100%;}#tbl td, '
                    '#tbl th {  border: 1px solid #ddd;  padding: 8px;}'
                    '#tbl tr:nth-child(even){background-color: #f2f2f2;}'
                    '#tbl tr:hover {background-color: #ddd;}#tbl '
                    'th {  padding-top: 12px;  padding-bottom: 12px; '
                    ' text-align: left;  background-color: #457abb;'
                    'color: white;}'
                    '.details {background-color: #457abb;padding:5px;'
                    'color:white;'
                    ' margin-bottom:0; padding-left:20px;}'
                    '.detblock{padding-top:10px;padding-bottom:10px;'
                    'background-color:#f2f2f2}'
                    '.left {margin-top:0 !important; }'
                    '</style>'
                    '</head> <body>')
            f.write("<h2> Documentation : " + file.name + " </h1>")
            f.write("<br></br>")
            for com in file.comments:
                com_html = self.comments_file_to_html(com)
                f.write(com_html)
            f.write("<br></br><br></br>")
            f.write("<h4 class = 'left'>Imported modules"
                    " and packages: </h3>")
            f.write("<ul class = 'left'>")
            for imp in file.imports:
                f.write("<li>" + imp + "</li>")
            for p in file.packages:
                f.write("<li>" + p + "</li>")
            f.write("<br></br>")
            f.write("</ul>")
            f.write("<h4 class = 'left'>" +
                    file.name +
                    " contains class / interface:</h3>")
            for cl in file.classes:
                cl_html = self.class_to_html(cl)
                f.write(cl_html)
            for inter in file.interfaces:
                inter_html = self.interface_to_html(inter)
                f.write(inter_html)

    def create_common_file(self):
        with open(os.path.join(self.project_name, self.project + ".html"),
                  "w", encoding="utf8") as f:
            f.write('<head>'
                    '<link rel="stylesheet" href="css.css">'
                    '<meta http-equiv="Content-Type"'
                    ' content="text/html; charset=charset=utf-8">'
                    '<style> body{font-family: Trebuchet MS, Arial,'
                    ' Helvetica, sans-serif !important;}'
                    '#tbl {  font-family: Trebuchet MS, Arial,'
                    ' Helvetica, sans-serif; '
                    ' border-collapse: collapse;  width: 100%;}#tbl td, '
                    '#tbl th {  border: 1px solid #ddd;  padding: 8px;}'
                    '#tbl tr:nth-child(even){background-color: #f2f2f2;}'
                    '#tbl tr:hover {background-color: #ddd;}#tbl '
                    'th {  padding-top: 12px;  padding-bottom: 12px; '
                    ' text-align: left;  background-color: #457abb;'
                    '  color: white;}</style>'
                    '</head>'
                    '<body>')
            f.write("<br></br>")
            f.write("<h1>Project " + self.project + "</h1>")
            f.write("<br></br>")
            f.write('<table id = "tbl">'
                    '<tr><th colspan="2">'
                    'Java files</th></tr>')
            for file in self.files:
                name = file.name.replace(".java", ".html")
                f.write('<tr><td><a href="' +
                        os.path.join(name) + '">' +
                        file.name +
                        '</a></td><td>' +
                        file.comments[0].description +
                        '</td></tr>')
            f.write("</table></body>")

    @staticmethod
    def class_to_html(cl):
        buff = '<p class = "left">' + "Class name: " + cl.name + "</br>"
        buff += "Access modifier: " + cl.mod + "</br>"
        if cl.parent:
            buff += "Parent: " + cl.parent + "<br>"
        if cl.interface:
            buff += "Implements interface: " + cl.interface + "<br>"
        buff += "</p><ul>"
        buff += "<h3>Class " + cl.name + " contains fields: </h3>"
        field_html = Converter.field_to_html(cl.fields)
        met_html = Converter.method_to_html(cl.methods)
        met_details = Converter.create_method_details(cl.methods)
        buff += field_html
        buff += "<br></br><br></br>"
        buff += "<h3>Class " + cl.name + \
                " contains methods: </h3>"
        buff += met_html + "</div>"
        buff += met_details
        return buff

    @staticmethod
    def interface_to_html(inter):
        buff = '<p class = "left">' + "Interface name: " \
               + inter.name + "</br>"
        buff += "Access modifier: " + inter.mod + "</br>"
        if inter.interface:
            buff += "Implements interface: " + inter.interface + "<br>"
        buff += "</p><ul>"
        buff += "<h3>Interface " + inter.name + " contains fields: </h3>"
        field_html = Converter.field_to_html(inter.fields)
        met_html = Converter.method_to_html(inter.methods)
        buff += field_html
        buff += "<br></br><br></br>"
        buff += "<h3>Interface " + inter.name + \
                " contains methods: </h3>"
        buff += met_html + "</div>"
        return buff

    @staticmethod
    def comments_file_to_html(comment):
        buf = ""
        if comment.author:
            buf += "<p class = 'left'>Author:   " + comment.author + "</p>"
        if comment.version:
            buf += "<p class = 'left'>Version:   " + comment.version + "</p>"
        if comment.since:
            buf += "<p class = 'left'>Available since version " + \
                   comment.since + "</p>"
        if comment.deprecated:
            buf += "<p class = 'left'>Deprecated " + \
                   str.lower(comment.deprecated) + "</p>"
        if comment.see:
            buf += "<p class = 'left'>Also see:   " + \
                   '<a href="' + os.path.join(comment.see + ".html") + '">' + \
                   comment.see + '</a></p>'
        if comment.description:
            buf += "<p class = 'left'>Description:  " + \
                   comment.description + "</p>"
        return buf

    @staticmethod
    def method_to_html(methods):
        buff = '<table id = "tbl"><tr><th>Method name</th><th>Prototype</th> ' \
               '<th>Description</th></tr>'
        for method in methods:
            name = method["name"]
            buff += "<tr>"
            buff += '<td>' + name + '</td>'
            buff += "<td>" + method["prot"] + "</td>"
            if method["comment"] is not None:
                if method["comment"].description:
                    buff += "<td>" + method["comment"].description + "</td>"
                else:
                    buff += "<td>Returns " + \
                            method["comment"].returns + "</td>"
            else:
                buff += "<td>  —  </td>"
            buff += '</tr>'
        buff += '</table>'
        return buff

    @staticmethod
    def field_to_html(fields):
        buff = '<table id = "tbl"><tr><th>Field name</th><th>Modifier</th> ' \
               '<th>Type</th></tr>'
        for field in fields:
            mod = field["mod"]
            name = field["name"]
            type_ = field['type']
            buff += "<tr>"
            buff += '<td>' + name + "</td>"
            buff += "<td>" + mod + "</td>"
            buff += "<td>" + type_ + "</td>"
            buff += "</tr>"
        buff += '</table>'
        return buff

    @staticmethod
    def create_method_details(methods):
        buf = "<h3>Method Details:</h3>"
        buf += "<br></br>"
        for method in methods:
            buf += "<h4 class = 'details'><i>method</i> " + method["name"] \
                   + " :</h4><div class = 'detblock'>"
            buf += "<p class = 'left'>" + method["prot"] + "</p>"
            buf += "<p class = 'left'><i>Access modifier:</i> " + \
                   method["mod"] + "</p>"
            if method['return'] == "":
                pass
            elif method['return'].strip() != "void":
                buf += "<p class = 'left'><i>Returns:</i> " + \
                       method["return"] + "</p>"
            else:
                buf += "<p class = 'left'><i>Returns nothing</i></p>"
            if method["comment"] is not None:
                comm = Converter.comments_to_html(method["comment"])
                buf += comm
            buf += "</div>"
        return buf

    @staticmethod
    def comments_to_html(comm):
        buf = ""
        if comm.description:
            buf += "<p class = 'left'>" + comm.description + "</p>"
        if comm.param:
            buf += "<p class = 'left'><i>Parameters:</i></p>"
            for p in comm.param:
                buf += "<p class = 'left'>" + p + "</p>"
        if comm.returns:
            buf += "<p class = 'left'><i>Returns</i> "\
                   + comm.returns + "</p>"
        return buf
