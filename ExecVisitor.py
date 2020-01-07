
from GraphVisitor import GraphVisitor
from GraphParser import GraphParser
from Plotter import Plotter
from Points import Points
import numpy as np
import math

class ExecVisitor(GraphVisitor):

    def __init__(self):
        self.origin_x = 0
        self.origin_y = 0
        self.scale_x = 1
        self.scale_y = 1
        self.rot = 0
        self.t = 0
        self.color = (0,0,0)
        super().__init__()

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            result = self.visit(statement)
            print(f" - {result}")

    def visitStatOrigin(self, ctx) -> str:
        self.origin_x = self.visit(ctx.expr(0))
        self.origin_y = self.visit(ctx.expr(1))
        return f"Origin: ({self.origin_x}, {self.origin_y})"

    def visitStatScale(self, ctx) -> str:
        self.scale_x = self.visit(ctx.expr(0))
        self.scale_y = self.visit(ctx.expr(1))
        return f"Scale: ({self.scale_x}, {self.scale_y})"

    def visitStatRot(self, ctx) -> str:
        self.rot = self.visit(ctx.expr())
        return f"Rotation: {self.rot}"
    
    def visitStatFor(self, ctx) -> str:
        start = self.visit(ctx.expr(0))
        end = self.visit(ctx.expr(1))
        step = self.visit(ctx.expr(2))

        batch = Points()
        batch.setcolor(self.color)

        for t in np.arange(start, end, step):
            self.t = t
            x = self.visit(ctx.expr(3))
            y = self.visit(ctx.expr(4))

            x *= self.scale_x
            y *= self.scale_y

            rot_x = x*math.cos(self.rot) + y*math.sin(self.rot)
            rot_y = y*math.cos(self.rot) - x*math.sin(self.rot)

            x = rot_x + self.origin_x
            y = rot_y + self.origin_y
            batch.addpoint(x, y)
        
        Plotter.draw_points(batch)

        return f"Drew points"

    def visitBuiltinColor(self, ctx) -> str:
        self.color = ctx.C.text
        return f"Color: {self.color}"
    
    def visitCustomColor(self, ctx) -> str:
        r = self.visit(ctx.expr(0))
        g = self.visit(ctx.expr(1))
        b = self.visit(ctx.expr(2))
        self.color = (r,g,b)
        return f"Color: {self.color}"

    def visitPowerExpr(self, ctx) -> float:
        base = self.visit(ctx.expr(0))
        power = self.visit(ctx.expr(1))
        return base**power
    
    def visitUnaryExpr(self, ctx) -> float:
        val = self.visit(ctx.expr())
        if ctx.op.type == GraphParser.MINUS:
            return -val
        return val

    def visitMulDivExpr(self, ctx) -> float:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == GraphParser.MUL:
            return left * right
        return left / right

    def visitPlusMinusExpr(self, ctx) -> float:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == GraphParser.PLUS:
            return left + right
        return left - right
    
    def visitConst(self, ctx) -> float:
        cst = ctx.CONST_ID().getText().lower()
        
        try:
            return float(cst)
        except ValueError:
            constant_map = {'pi': math.pi, 'e': math.e}
            try:
                return constant_map[cst]
            except KeyError:
                raise ValueError(f"{cst} is not a valid constant")

    def visitVarT(self, ctx) -> float:
        return self.t

    def visitFuncExpr(self, ctx) -> float:
        pre_function = self.visit(ctx.expr())
        func = ctx.ID().getText().lower()

        funcmap = {
            'sin': math.sin, 
            'cos': math.cos,
            'tan': math.tan,
            'ln' : math.log,
            'exp': math.exp,
            'sqrt': math.sqrt,
        }

        try:
            return funcmap[func](pre_function)
        
        except KeyError:
            raise AttributeError(f"Function '{ctx.ID().getText()}' invalid")

    def visitNestedExpr(self, ctx) -> float:
        return self.visit(ctx.expr())

