from GraphLexer import GraphLexer
from GraphParser import GraphParser
from ExecVisitor import ExecVisitor
from antlr4 import CommonTokenStream
from antlr4.InputStream import InputStream
from Points import Points
from Plotter import Plotter


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


if __name__ == "__main__":
    interactive()
