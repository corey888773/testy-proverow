from z3 import *

Object = DeclareSort('Object')

var34 = Function('var34', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var34(x), Not(var54(x))))),
	ForAll([x], Not(Or(var81(x), Not(var8(x))))),
	ForAll([x], Not(Or(var19(x), Not(var49(x))))),
	ForAll([x], Not(Or(var1(x), var47(x)))),
	ForAll([x], Not(Or(Not(var32(x)), Not(var64(x))))),
	ForAll([x], Not(Or(Not(var63(x)), Not(var53(x))))),
	ForAll([x], Not(Or(Not(var85(x)), Not(var7(x))))),
	ForAll([x], Not(Or(Not(var11(x)), var21(x)))),
	ForAll([x], Not(Or(Not(var54(x)), var23(x)))),
	ForAll([x], Not(Or(Not(var50(x)), Not(var35(x))))),
	ForAll([x], Not(Or(Not(var64(x)), Not(var10(x))))),
	ForAll([x], Not(Or(Not(var75(x)), var38(x)))),
	ForAll([x], Not(Or(Not(var90(x)), var14(x)))),
	ForAll([x], Not(Or(var75(x), Not(var30(x))))),
	ForAll([x], Not(Or(Not(var19(x)), var74(x)))),
	ForAll([x], Not(Or(var17(x), var82(x)))),
	ForAll([x], Not(Or(var82(x), Not(var8(x))))),
	ForAll([x], Not(Or(var5(x), var44(x)))),
	ForAll([x], Not(Or(var59(x), Not(var86(x))))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var13(x))))),
	ForAll([x], Not(Or(Not(var63(x)), var62(x)))),
	ForAll([x], Not(Or(var36(x), Not(var80(x))))),
	ForAll([x], Not(Or(var28(x), Not(var85(x))))),
	ForAll([x], Not(Or(var17(x), Not(var54(x))))),
	ForAll([x], Not(Or(var71(x), var41(x)))),
	ForAll([x], Not(Or(var6(x), Not(var66(x))))),
	ForAll([x], Not(Or(var88(x), var63(x)))),
	ForAll([x], Not(Or(var98(x), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var23(x)), var71(x)))),
	ForAll([x], Not(Or(var22(x), var60(x)))),
	ForAll([x], Not(Or(var95(x), Not(var69(x))))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var77(x))))),
	ForAll([x], Not(Or(var70(x), var78(x)))),
	ForAll([x], Not(Or(Not(var54(x)), var68(x)))),
	ForAll([x], Not(Or(var7(x), Not(var69(x))))),
	ForAll([x], Not(Or(Not(var35(x)), var34(x)))),
	ForAll([x], Not(Or(Not(var32(x)), Not(var50(x))))),
	ForAll([x], Not(Or(var21(x), var99(x)))),
	ForAll([x], Not(Or(Not(var85(x)), Not(var6(x))))),
	ForAll([x], Not(Or(var41(x), Not(var69(x))))),
	ForAll([x], Not(Or(Not(var31(x)), Not(var88(x))))),
	ForAll([x], Not(Or(var90(x), var27(x)))),
	ForAll([x], Not(Or(Not(var66(x)), Not(var56(x))))),
	ForAll([x], Not(Or(Not(var18(x)), Not(var12(x))))),
	ForAll([x], Not(Or(Not(var90(x)), Not(var52(x))))),
	ForAll([x], Not(Or(Not(var53(x)), var27(x)))),
	ForAll([x], Not(Or(var19(x), Not(var30(x))))),
	ForAll([x], Not(Or(var43(x), Not(var4(x))))),
	ForAll([x], Not(Or(Not(var5(x)), Not(var54(x))))),
	ForAll([x], Not(Or(Not(var70(x)), var14(x)))),
	ForAll([x], Not(Or(Not(var99(x)), var59(x)))),
	ForAll([x], Not(Or(var2(x), var4(x)))),
	ForAll([x], Not(Or(var98(x), Not(var18(x))))),
	ForAll([x], Not(Or(Not(var36(x)), Not(var12(x))))),
	ForAll([x], Not(Or(var71(x), var4(x)))),
	ForAll([x], Not(Or(Not(var22(x)), var96(x)))),
	ForAll([x], Not(Or(var84(x), Not(var75(x))))),
	ForAll([x], Not(Or(var100(x), Not(var32(x))))),
	ForAll([x], Not(Or(var49(x), var97(x)))),
	ForAll([x], Not(Or(var87(x), var26(x)))),
	ForAll([x], Not(Or(var61(x), var99(x)))),
	ForAll([x], Not(Or(Not(var62(x)), Not(var22(x))))),
	ForAll([x], Not(Or(var57(x), var19(x)))),
	ForAll([x], Not(Or(Not(var48(x)), Not(var65(x))))),
	ForAll([x], Not(Or(Not(var13(x)), Not(var84(x))))),
	ForAll([x], Not(Or(var16(x), Not(var4(x))))),
	ForAll([x], Not(Or(Not(var4(x)), var27(x)))),
	ForAll([x], Not(Or(Not(var94(x)), var5(x)))),
	ForAll([x], Not(Or(var93(x), var77(x)))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var41(x))))),
	ForAll([x], Not(Or(var8(x), var10(x)))),
	ForAll([x], Not(Or(var38(x), Not(var46(x))))),
	ForAll([x], Not(Or(var86(x), var39(x)))),
	ForAll([x], Not(Or(var17(x), Not(var57(x))))),
	ForAll([x], Not(Or(var72(x), var55(x)))),
	ForAll([x], Not(Or(var3(x), Not(var96(x))))),
	ForAll([x], Not(Or(var80(x), Not(var42(x))))),
	ForAll([x], Not(Or(Not(var1(x)), Not(var82(x))))),
	ForAll([x], Not(Or(Not(var30(x)), var32(x)))),
	ForAll([x], Not(Or(var17(x), var51(x)))),
	ForAll([x], Not(Or(var15(x), Not(var31(x))))),
	ForAll([x], Not(Or(var83(x), var72(x)))),
	ForAll([x], Not(Or(Not(var32(x)), var77(x)))),
	ForAll([x], Not(Or(Not(var99(x)), Not(var45(x))))),
	ForAll([x], Not(Or(var75(x), Not(var92(x))))),
	ForAll([x], Not(Or(Not(var7(x)), Not(var37(x))))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var23(x))))),
	ForAll([x], Not(Or(var41(x), var93(x)))),
	ForAll([x], Not(Or(var40(x), var3(x)))),
	ForAll([x], Not(Or(var56(x), var83(x)))),
	ForAll([x], Not(Or(Not(var96(x)), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var61(x))))),
	ForAll([x], Not(Or(Not(var96(x)), var100(x)))),
	ForAll([x], Not(Or(var3(x), Not(var45(x))))),
	ForAll([x], Not(Or(var43(x), Not(var75(x))))),
	ForAll([x], Not(Or(Not(var65(x)), Not(var70(x))))),
	ForAll([x], Not(Or(Not(var55(x)), Not(var62(x))))),
	ForAll([x], Not(Or(Not(var61(x)), Not(var24(x))))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var2(x))))),
	ForAll([x], Not(Or(Not(var31(x)), var39(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var15(x1)), var22(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var69(x1)), var97(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), var28(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var89(x1)), var85(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), var68(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), var82(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var20(x1)), var16(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var88(x1), Not(var38(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var93(x1), var28(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var52(x1)), Not(var71(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var30(x1), var68(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var99(x1), var59(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var17(x1), var100(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var55(x1), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), Not(var81(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var22(x1), Not(var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Not(var5(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var18(x1)), Not(var97(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var9(x1)), var93(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var24(x1)), Not(var49(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var64(x1), var50(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), var2(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var31(x1)), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var85(x1)), Not(var54(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var55(x1), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var85(x1)), var94(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var59(x1)), Not(var69(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var34(x1)), var61(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var27(x1), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var66(x1)), var79(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var24(x1)), Not(var79(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var37(x1), Not(var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var54(x1)), Not(var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), var93(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var34(x1), Not(var43(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var66(x1), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var97(x1), Not(var63(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var9(x1)), var10(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var93(x1)), Not(var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var88(x1)), var4(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), var85(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var40(x1)), Not(var84(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var1(x1), var78(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var35(x1), var71(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var94(x1)), var73(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var91(x1), var89(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var9(x1)), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var78(x1), var11(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var43(x1), var60(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var79(x1), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var66(x1)), Not(var98(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var11(x1)), Not(var59(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var25(x1)), Not(var79(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var96(x1), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var26(x1)), var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var31(x1), var71(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var90(x1)), Not(var35(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var47(x1), Not(var15(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var19(x1), Not(var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var37(x1), var35(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var85(x1), Not(var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var37(x1), Not(var12(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var13(x1), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var3(x1), var95(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var81(x1)), Not(var61(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var96(x1)), var67(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var79(x1)), var62(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var79(x1)), Not(var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var71(x1), var58(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var60(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var57(x1)), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var53(x1), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), Not(var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var8(x1), Not(var84(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var51(x1)), var77(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var68(x1)), var52(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var38(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var67(x1)), Not(var79(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var35(x1), var57(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var99(x1)), var17(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var79(x1), var57(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var90(x1)), Not(var95(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var57(x1), var6(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var29(x1), Not(var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var89(x1), var24(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var75(x1)), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var32(x1)), var55(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var52(x1)), Not(var18(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var40(x1)), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var33(x1)), Not(var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Not(var28(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var65(x1), Not(var18(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var39(x1)), var50(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var26(x1)), Not(var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var33(x1)), var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var7(x1), var30(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
