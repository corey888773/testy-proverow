from z3 import *

Object = DeclareSort('Object')

var23 = Function('var23', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var23(x)), Not(var80(x))))),
	ForAll([x], Not(Or(var66(x), Not(var83(x))))),
	ForAll([x], Not(Or(var81(x), var33(x)))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var6(x))))),
	ForAll([x], Not(Or(var73(x), Not(var34(x))))),
	ForAll([x], Not(Or(var11(x), Not(var59(x))))),
	ForAll([x], Not(Or(var87(x), var52(x)))),
	ForAll([x], Not(Or(Not(var68(x)), var5(x)))),
	ForAll([x], Not(Or(var18(x), Not(var39(x))))),
	ForAll([x], Not(Or(Not(var38(x)), Not(var14(x))))),
	ForAll([x], Not(Or(var36(x), Not(var95(x))))),
	ForAll([x], Not(Or(var51(x), Not(var88(x))))),
	ForAll([x], Not(Or(var19(x), Not(var22(x))))),
	ForAll([x], Not(Or(var50(x), Not(var35(x))))),
	ForAll([x], Not(Or(Not(var42(x)), var61(x)))),
	ForAll([x], Not(Or(Not(var100(x)), Not(var9(x))))),
	ForAll([x], Not(Or(var97(x), Not(var56(x))))),
	ForAll([x], Not(Or(var89(x), var79(x)))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var72(x))))),
	ForAll([x], Not(Or(Not(var63(x)), var29(x)))),
	ForAll([x], Not(Or(Not(var40(x)), Not(var53(x))))),
	ForAll([x], Not(Or(Not(var64(x)), var91(x)))),
	ForAll([x], Not(Or(var1(x), Not(var26(x))))),
	ForAll([x], Not(Or(var8(x), Not(var31(x))))),
	ForAll([x], Not(Or(Not(var48(x)), Not(var60(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var75(x1)), var69(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var41(x1), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var93(x1), Not(var58(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var32(x1)), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var76(x1)), var24(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var7(x1)), Not(var28(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var70(x1), Not(var90(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var77(x1)), var20(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var54(x1)), Not(var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var85(x1)), var13(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var94(x1)), Not(var62(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var49(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var10(x1)), Not(var43(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), Not(var92(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var67(x1), Not(var71(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var78(x1)), var98(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var74(x1), Not(var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), Not(var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var82(x1), var4(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var25(x1), var15(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var3(x1)), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var55(x1), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var84(x1)), Not(var65(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), var99(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var57(x1)), var46(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())