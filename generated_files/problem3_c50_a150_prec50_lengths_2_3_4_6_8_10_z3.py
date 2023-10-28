from z3 import *

Object = DeclareSort('Object')

var22 = Function('var22', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var22(x), var8(x)))),
	ForAll([x], Not(Or(var103(x), Not(var50(x))))),
	ForAll([x], Not(Or(var51(x), var68(x)))),
	ForAll([x], Not(Or(Not(var64(x)), Not(var147(x))))),
	ForAll([x], Not(Or(var69(x), var90(x)))),
	ForAll([x], Not(Or(Not(var42(x)), var1(x)))),
	ForAll([x], Not(Or(Not(var59(x)), Not(var46(x))))),
	ForAll([x], Not(Or(Not(var2(x)), var15(x)))),
	ForAll([x], Not(Or(var125(x), Not(var45(x))))),
	ForAll([x], Not(Or(var14(x), Not(var5(x))))),
	ForAll([x], Not(Or(var93(x), var97(x)))),
	ForAll([x], Not(Or(var16(x), var114(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var13(x1), var35(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var73(x1)), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Not(var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var63(x1), Not(var133(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var81(x1), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var10(x1)), var6(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var39(x1)), Not(var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var4(x1), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var36(x1)), Not(var75(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var134(x1), Not(var77(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), var57(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var53(x1)), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var34(x1)), var54(x))))),
	ForAll([x], Not(Or(Not(var26(x)), Not(var129(x)), var128(x)))),
	ForAll([x], Not(Or(Not(var21(x)), Not(var66(x)), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var49(x)), Not(var144(x)), var86(x)))),
	ForAll([x], Not(Or(var28(x), Not(var150(x)), Not(var102(x))))),
	ForAll([x], Not(Or(var60(x), var62(x), Not(var78(x))))),
	ForAll([x], Not(Or(var76(x), Not(var40(x)), Not(var71(x))))),
	ForAll([x], Not(Or(var7(x), Not(var127(x)), var37(x)))),
	ForAll([x], Not(Or(Not(var138(x)), var109(x), Not(var72(x))))),
	ForAll([x], Not(Or(Not(var25(x)), var17(x), var43(x)))),
	ForAll([x], Not(Or(var55(x), var19(x), var84(x)))),
	ForAll([x], Not(Or(var94(x), Not(var18(x)), var88(x)))),
	ForAll([x], Not(Or(Not(var65(x)), Not(var83(x)), Not(var95(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var31(x1)), var124(x1)), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var47(x1), Not(var80(x1))), var117(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var119(x1), var92(x1)), Not(var56(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var132(x1), Not(var120(x1))), Not(var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var29(x1), Or(Not(var121(x)), var101(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), Or(Not(var33(x)), Not(var91(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var85(x1)), Or(Not(var27(x)), Not(var122(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var108(x1), var11(x1)), var89(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var100(x1)), Or(var99(x), var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var118(x1), Not(var52(x1))), Not(var20(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var61(x1), var79(x1)), var145(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var149(x1), Or(var110(x), var58(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var32(x1)), Or(Not(var38(x)), var30(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
