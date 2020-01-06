# Graphing Language Interpreter

Project for *SE5002L: Compiler Principles*, written w/ Python 3 & ANTLR 4.

## Getting Started

#### ANTLR Target Generation

Make sure you have Java & ANTLR [installed](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md). Target is generated using visitor mode.

```
java org.antlr.v4.Tool -Dlanguage=Python3 -no-listener -visitor Graph.g4
```

#### Python Runtimes

Matplotlib, Numpy & ANTLR runtime is required:

```
pip install matplotlib numpy antlr4-python3-runtime
```

#### Running the Interperter

Run the project via `python Runner.py`.

Two modes are offered by the interpreter: file input & interactive.

**File input**: Use `-f <filename>` to select a input file. For sample graph: `python Runner.py -f sample_graph.txt`

**Interactive**: Use `-i` to enter interactive mode.

## Graphing Language

#### Statements

#### Expressions

