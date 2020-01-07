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

A sample graphing program can be found at `sample_graph.txt`.

#### Statements

Note that statements should end with ";". However statements without ";" are tolerated in interactive mode.

Statement                                                      | Description
:------------------------------------------------------------- | :---------------------------------------------------
`FOR T FROM <A> TO <B> STEP <C> DRAW(<X>,<Y>)`                 | Draw points in a loop. X & Y are expressions containing the iterated vairable T.
`SCALE IS (<X>, <Y>)`                                          | Set the scale of X & Y axis.
`ORIGIN IS (<X>, <Y>)`                                         | Set the origin of X & Y axis.
`ROT IS (<RAD>)`                                               | Rotate the coordinates by its origin for RAD radian.
`COLOR IS <COLOR>` or `COLOR IS (<R>,<G>,<B>)`                 | Set the color of points to draw next. COLOR can be RED, BLACK, YELLOW, GREEN, BLUE. R ,G & B are valid between 0~255.
`--<Comment>` or `//<Comment>` or `/* <Multi-line comment> */` | Comments!

#### Expressions

Expressions are where calculations are made. 
 * Numbers can be represented as `1`, `1.1` or `1.1E3`. 
 * Arithmetic operations `+`, `-`, `*`, `/`, `**` (power) are supported.
 * Mathmatic functions sin, cos, tan, ln, exp, sqrt are supported.
 * Constants `e` and `pi`.
 * Use `()` to priortize operations.

