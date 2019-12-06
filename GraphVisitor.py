# Generated from Graph.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphParser import GraphParser
else:
    from GraphParser import GraphParser

# This class defines a complete generic visitor for a parse tree produced by GraphParser.

class GraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphParser#program.
    def visitProgram(self, ctx:GraphParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#statement.
    def visitStatement(self, ctx:GraphParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#statOrigin.
    def visitStatOrigin(self, ctx:GraphParser.StatOriginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#statScale.
    def visitStatScale(self, ctx:GraphParser.StatScaleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#statRot.
    def visitStatRot(self, ctx:GraphParser.StatRotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#statFor.
    def visitStatFor(self, ctx:GraphParser.StatForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#BuiltinColor.
    def visitBuiltinColor(self, ctx:GraphParser.BuiltinColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#CustomColor.
    def visitCustomColor(self, ctx:GraphParser.CustomColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#PowerExpr.
    def visitPowerExpr(self, ctx:GraphParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:GraphParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#VarT.
    def visitVarT(self, ctx:GraphParser.VarTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#Const.
    def visitConst(self, ctx:GraphParser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#PlusMinusExpr.
    def visitPlusMinusExpr(self, ctx:GraphParser.PlusMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#NestedExpr.
    def visitNestedExpr(self, ctx:GraphParser.NestedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#UnaryExpr.
    def visitUnaryExpr(self, ctx:GraphParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphParser#FuncExpr.
    def visitFuncExpr(self, ctx:GraphParser.FuncExprContext):
        return self.visitChildren(ctx)



del GraphParser