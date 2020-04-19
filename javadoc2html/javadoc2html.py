from javadoc_handler import Java_handler
from convert_to_html import *
import argparse


def main(args=None):
    try:
        if args.project:
            handler = Java_handler(args.project)
            files = handler.get_files_from_dir()
            converter = Converter(files, args.project)
            converter.create_html_files()
    except Exception as e:
        print(str(e))
    else:
        handler = Java_handler("test")
        files = handler.get_files_from_dir()
        converter = Converter(files, "test")
        converter.create_html_files()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="javadoc2html")
    parser.add_argument("-project", "-p",  type=str,
                        help="Input dir with java files (project dir).")
    arg = parser.parse_args()
    main(arg)
