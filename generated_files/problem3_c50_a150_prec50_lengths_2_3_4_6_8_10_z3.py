from z3 import *

Object = DeclareSort('Object')

var77 = Function('var77', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var77(x)), var110(x)))),
	ForAll([x], Not(Or(var4(x), Not(var38(x))))),
	ForAll([x], Not(Or(var85(x), var40(x)))),
	ForAll([x], Not(Or(Not(var35(x)), Not(var74(x))))),
	ForAll([x], Not(Or(Not(var12(x)), var16(x)))),
	ForAll([x], Not(Or(var65(x), var58(x)))),
	ForAll([x], Not(Or(var136(x), var27(x)))),
	ForAll([x], Not(Or(Not(var32(x)), var67(x)))),
	ForAll([x], Not(Or(var79(x), var128(x)))),
	ForAll([x], Not(Or(Not(var146(x)), Not(var50(x))))),
	ForAll([x], Not(Or(Not(var39(x)), var41(x)))),
	ForAll([x], Not(Or(Not(var94(x)), Not(var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), var71(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var7(x1)), var73(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var24(x1)), Not(var112(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var31(x1)), var1(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var25(x1)), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), Not(var91(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var148(x1)), Not(var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var23(x1)), var81(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var6(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var72(x1), var134(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), var107(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var131(x1)), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var49(x1)), var22(x))))),
	ForAll([x], Not(Or(var84(x), var78(x), Not(var62(x))))),
	ForAll([x], Not(Or(var109(x), Not(var105(x)), var42(x)))),
	ForAll([x], Not(Or(Not(var70(x)), var69(x), var57(x)))),
	ForAll([x], Not(Or(var55(x), Not(var121(x)), Not(var17(x))))),
	ForAll([x], Not(Or(Not(var140(x)), Not(var75(x)), Not(var11(x))))),
	ForAll([x], Not(Or(var124(x), Not(var34(x)), Not(var64(x))))),
	ForAll([x], Not(Or(Not(var115(x)), Not(var21(x)), var46(x)))),
	ForAll([x], Not(Or(var101(x), Not(var125(x)), var82(x)))),
	ForAll([x], Not(Or(Not(var86(x)), var8(x), var95(x)))),
	ForAll([x], Not(Or(Not(var28(x)), var56(x), Not(var13(x))))),
	ForAll([x], Not(Or(Not(var51(x)), var97(x), Not(var33(x))))),
	ForAll([x], Not(Or(Not(var120(x)), var52(x), var36(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var15(x1), Not(var59(x1))), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var63(x1)), Not(var29(x1))), var61(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var96(x1)), Or(var19(x), var98(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var88(x1), var138(x1)), Not(var53(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var93(x1), Not(var89(x1))), Not(var104(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var54(x1), var43(x1)), var20(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var100(x1), Or(var5(x), Not(var145(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var83(x1)), Or(var130(x), Not(var92(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var47(x1)), Or(Not(var80(x)), var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Or(var37(x), var144(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var123(x1)), Or(Not(var141(x)), var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var133(x1), Or(Not(var26(x)), var10(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var14(x1)), Not(var68(x1))), var18(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
