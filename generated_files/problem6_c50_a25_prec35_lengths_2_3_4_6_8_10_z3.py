from z3 import *

Object = DeclareSort('Object')

var5 = Function('var5', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var5(x), var1(x)))),
	ForAll([x], Not(Or(Not(var3(x)), var8(x)))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var11(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var23(x1), var20(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var14(x1), var18(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var5(x1)), Not(var15(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var25(x1)), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Not(var8(x)))))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var5(x)), Not(var13(x))))),
	ForAll([x], Not(Or(Not(var14(x)), var24(x), var4(x)))),
	ForAll([x], Not(Or(Not(var11(x)), Not(var8(x)), Not(var18(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var3(x1)), Or(Not(var23(x)), var15(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var15(x1)), Or(Not(var3(x)), var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var22(x1)), var4(x1)), var23(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var19(x1)), Or(Not(var23(x)), Not(var13(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var2(x1), var18(x1)), var16(x))))),
	ForAll([x], Not(Or(var9(x), Not(var1(x)), Not(var8(x)), Not(var17(x))))),
	ForAll([x], Not(Or(Not(var10(x)), var17(x), Not(var9(x)), var11(x)))),
	ForAll([x], Not(Or(Not(var19(x)), Not(var20(x)), var5(x), var25(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var20(x1), var7(x1)), Or(Not(var9(x)), Not(var14(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var14(x1)), Not(var2(x1)), Not(var5(x1))), Not(var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var5(x1)), Or(Not(var9(x)), Not(var22(x)), var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var3(x1)), var21(x1)), Or(var4(x), var5(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var13(x1), var10(x1)), Or(var9(x), var21(x)))))),
	ForAll([x], Not(Or(Not(var4(x)), Not(var9(x)), Not(var11(x)), Not(var13(x)), var3(x), var21(x)))),
	ForAll([x], Not(Or(var3(x), var1(x), var21(x), Not(var18(x)), var15(x), var5(x)))),
	ForAll([x], Not(Or(Not(var11(x)), var9(x), Not(var1(x)), var24(x), Not(var5(x)), Not(var25(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var7(x1)), var3(x1), var23(x1), var6(x1)), Or(var22(x), Not(var16(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var21(x1)), var17(x1), var11(x1)), Or(var25(x), var23(x), Not(var10(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var6(x1)), Not(var14(x1))), Or(var3(x), Not(var16(x)), var4(x), var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var3(x1)), Not(var17(x1)), var2(x1), var22(x1), var9(x1)), Not(var20(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var6(x1)), Not(var2(x1)), Not(var9(x1))), Or(var4(x), Not(var22(x)), var23(x)))))),
	ForAll([x], Not(Or(Not(var7(x)), Not(var25(x)), Not(var15(x)), var9(x), Not(var19(x)), var10(x), Not(var17(x)), Not(var18(x))))),
	ForAll([x], Not(Or(Not(var15(x)), Not(var25(x)), Not(var20(x)), Not(var24(x)), Not(var23(x)), Not(var11(x)), Not(var4(x)), var13(x)))),
	ForAll([x], Not(Or(Not(var16(x)), Not(var24(x)), Not(var2(x)), var25(x), var4(x), Not(var18(x)), var20(x), Not(var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var21(x1)), Not(var20(x1)), var15(x1), var10(x1), var9(x1)), Or(Not(var19(x)), var3(x), var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var12(x1), Not(var21(x1)), var2(x1), var22(x1), var24(x1), var7(x1)), Or(var13(x), var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var22(x1)), Not(var16(x1)), var23(x1), Not(var2(x1)), var14(x1), Not(var1(x1))), Or(var3(x), var13(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var19(x1), Not(var22(x1)), Not(var12(x1))), Or(var6(x), Not(var11(x)), Not(var3(x)), var1(x), Not(var9(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var8(x1), var5(x1), var14(x1), var25(x1), var18(x1), var3(x1)), Or(var17(x), var20(x)))))),
	ForAll([x], Not(Or(Not(var13(x)), var25(x), var11(x), Not(var8(x)), var23(x), Not(var15(x)), var4(x), var21(x), Not(var10(x)), var3(x)))),
	ForAll([x], Not(Or(Not(var10(x)), Not(var12(x)), Not(var1(x)), var4(x), var20(x), Not(var23(x)), Not(var9(x)), Not(var25(x)), var14(x), Not(var19(x))))),
	ForAll([x], Not(Or(var9(x), Not(var8(x)), var4(x), Not(var7(x)), Not(var19(x)), Not(var1(x)), Not(var25(x)), Not(var2(x)), Not(var20(x)), Not(var16(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var13(x1), Not(var20(x1)), Not(var1(x1)), Not(var21(x1)), var2(x1), var11(x1)), Or(Not(var9(x)), var5(x), var10(x), var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var11(x1), var20(x1), var18(x1), var17(x1), var2(x1), var7(x1), var10(x1), var15(x1), var13(x1)), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var18(x1)), Not(var21(x1)), var1(x1), Not(var5(x1)), var22(x1), var4(x1), Not(var10(x1)), Not(var16(x1)), var9(x1)), var25(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var7(x1)), var19(x1)), Or(var3(x), var23(x), var1(x), Not(var11(x)), Not(var17(x)), var20(x), var13(x), var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var4(x1), Not(var9(x1)), var23(x1), Not(var6(x1)), var8(x1), var10(x1)), Or(Not(var14(x)), Not(var2(x)), Not(var15(x)), Not(var1(x))))))),
	ForAll([x], Not(Or(var10(x), Not(var19(x)), var21(x), Not(var24(x)), var4(x), Not(var5(x)), var14(x), var22(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var9(x1)), Not(var20(x1)), var3(x1), var11(x1), var19(x1)), Or(var25(x), var14(x), Not(var22(x)), var18(x), var7(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())