from GraphLexer import GraphLexer
from GraphParser import GraphParser
from ExecVisitor import ExecVisitor
from antlr4 import CommonTokenStream, FileStream
from antlr4.InputStream import InputStream
from Points import Points
from Plotter import Plotter

import argparse
import os

def interactive():
    plotter = Plotter()
    plotter.interactive(True)

    parser = GraphParser(None)
    visitor = ExecVisitor()
    visitor.setPlotter(plotter)

    lineno = 1


    while True:
        line = input(f"Graph [{lineno}]> ")

        istream = InputStream(line)
        lexer = GraphLexer(istream)
        lexer.line = lineno
        lexer.column = 0
        token_stream = CommonTokenStream(lexer)
        parser.setInputStream(token_stream)
        tree = parser.statement()

        result = visitor.visit(tree)

        print(f"Out   [{lineno}]>", result, '\n')
        lineno += 1

def file_interpreter(filename: str):
    plotter = Plotter()
    plotter.interactive(False)
    
    istream = FileStream(filename)
    lexer = GraphLexer(istream)
    token_stream = CommonTokenStream(lexer)
    parser = GraphParser(token_stream)
    tree = parser.program()

    visitor = ExecVisitor()
    visitor.visit(tree)

    plotter.show()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", metavar="filename", nargs=1, help="File interpreter mode")
    parser.add_argument("-i", "--interactive", action='store_true', help="Interactive shell mode")
    result = parser.parse_args()

    if result.file == None and result.interactive == False:
        parser.print_help()
        parser.error("[-i] or [-f filename] is required.")
        return
    
    if result.file != None and result.interactive == True:
        parser.print_help()
        parser.error("Cannot use [-i] and [-f filename] together.")
        return
    
    if result.interactive:
        interactive()
        return
    
    file_interpreter(result.file[0])

if __name__ == "__main__":
    parse_arguments()
