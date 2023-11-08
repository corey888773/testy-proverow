from z3 import *

Object = DeclareSort('Object')

var56 = Function('var56', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(var56(x))),
	ForAll([x], Not(Not(var37(x)))),
	Exists([x], Not(var2(x))),
	Exists([x], Not(var95(x))),
	Exists([x], Not(var18(x))),
	Exists([x], var97(x)),
	Exists([x], var32(x)),
	Exists([x], var90(x)),
	Exists([x], Not(var25(x))),
	Exists([x], Not(var53(x))),
	Exists([x], var90(x)),
	Exists([x], Not(var64(x))),
	Exists([x], Not(var26(x))),
	Exists([x], Not(var99(x))),
	Exists([x], var4(x)),
	Exists([x], Not(var36(x))),
	Exists([x], var83(x)),
	Exists([x], var40(x)),
	Exists([x], var50(x)),
	Exists([x], var86(x)),
	Exists([x], Not(var54(x))),
	ForAll([x], Not(Or(Not(var87(x)), Not(var34(x))))),
	ForAll([x], Not(Or(var62(x), var47(x)))),
	ForAll([x], Not(Or(Not(var38(x)), Not(var44(x))))),
	ForAll([x], Not(Or(var37(x), var31(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var81(x1), Not(var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var43(x1)), Not(var95(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var98(x1)), Not(var28(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var84(x1), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var77(x1)), var36(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var26(x1)), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Not(var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var75(x1), Not(var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var68(x1), var52(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var52(x1), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var37(x1)), var34(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var30(x1), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var91(x1), var5(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var22(x1), var60(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var68(x1), Not(var85(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var28(x1)), Not(var40(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var22(x1), var94(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var6(x1), Not(var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var31(x1), var50(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var52(x1)), var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var91(x1), var3(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), var81(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), var36(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var20(x1)), Not(var90(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var88(x1)), var7(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), var52(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var31(x1)), var26(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var53(x1), Not(var57(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var69(x1)), Not(var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var3(x1), Not(var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), Not(var76(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var41(x1)), Not(var89(x)))))),
	ForAll([x], Not(Or(var76(x), var36(x), var8(x)))),
	ForAll([x], Not(Or(var94(x), var68(x), var22(x)))),
	ForAll([x], Not(Or(var38(x), var37(x), var42(x)))),
	ForAll([x], Not(Or(var63(x), var52(x), Not(var43(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var65(x1), Or(var21(x), Not(var49(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), Or(var20(x), Not(var19(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var6(x1), Or(Not(var72(x)), Not(var11(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var71(x1), var72(x1)), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var92(x1)), Or(Not(var65(x)), Not(var86(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), Or(var89(x), Not(var55(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var68(x1), Or(Not(var14(x)), var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var22(x1), Or(Not(var26(x)), var56(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var3(x1)), Not(var26(x1))), var75(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var70(x1), Or(var96(x), Not(var28(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var33(x1), Or(Not(var76(x)), Not(var80(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var52(x1)), var30(x1)), Not(var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var10(x1), Not(var77(x1))), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var82(x1), Not(var29(x1))), var17(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var88(x1), Or(var81(x), Not(var36(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var43(x1)), Or(Not(var75(x)), var92(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var84(x1)), Or(Not(var91(x)), var60(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var42(x1), Not(var24(x1))), var88(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var61(x1)), Not(var48(x1))), Not(var67(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var94(x1), Or(Not(var79(x)), var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Or(var43(x), var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var8(x1)), var19(x1)), Not(var55(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var7(x1), var89(x1)), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var52(x1), Or(var42(x), Not(var77(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Or(Not(var92(x)), Not(var30(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var35(x1)), Or(var36(x), var83(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var32(x1), Or(var95(x), Not(var62(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var56(x1), var42(x1)), Not(var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var27(x1)), Or(var33(x), var98(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var10(x1), Or(var78(x), var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var46(x1), Not(var80(x1))), var81(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var23(x1)), Or(var45(x), Not(var63(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var56(x1)), Or(Not(var31(x)), Not(var90(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var73(x1), var90(x1)), Not(var47(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var6(x1), Or(Not(var1(x)), Not(var72(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var78(x1)), Not(var20(x1))), var68(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var75(x1), Not(var61(x1))), var23(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var54(x1)), Not(var78(x1))), var22(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var97(x1), Or(var31(x), Not(var100(x))))))),
	ForAll([x], Not(Or(var39(x), var16(x), Not(var37(x)), var44(x)))),
	ForAll([x], Not(Or(var88(x), var20(x), var93(x), Not(var51(x))))),
	ForAll([x], Not(Or(Not(var77(x)), Not(var48(x)), Not(var69(x)), Not(var26(x))))),
	ForAll([x], Not(Or(Not(var24(x)), var45(x), var83(x), Not(var57(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var81(x1), Not(var62(x1)), Not(var31(x1))), var89(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var20(x1), var55(x1)), Or(var72(x), Not(var56(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Or(var36(x), var86(x), var79(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var83(x1)), var20(x1), Not(var40(x1))), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var86(x1)), Or(Not(var1(x)), var63(x), var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), Or(Not(var16(x)), var70(x), var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var70(x1), var72(x1)), Or(var76(x), var80(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var65(x1), Not(var25(x1))), Or(var44(x), Not(var66(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var72(x1), Not(var14(x1))), Or(Not(var46(x)), Not(var100(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var28(x1)), var18(x1), var72(x1)), Not(var84(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var66(x1), Not(var82(x1))), Or(var96(x), Not(var59(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var20(x1)), Not(var48(x1)), var17(x1)), var30(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var60(x1), Or(Not(var15(x)), var20(x), var64(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var79(x1)), var19(x1)), Or(var7(x), var52(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var50(x1)), var48(x1), var23(x1)), Not(var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var32(x1)), Or(Not(var94(x)), Not(var19(x)), var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var88(x1)), var83(x1)), Or(Not(var40(x)), Not(var12(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var97(x1)), var74(x1), Not(var80(x1))), var81(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var86(x1)), Or(Not(var54(x)), Not(var87(x)), Not(var53(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var27(x1), Not(var42(x1)), var69(x1)), Not(var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Or(Not(var22(x)), Not(var39(x)), var65(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var26(x1), Not(var96(x1))), Or(var89(x), var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var9(x1)), var40(x1)), Or(Not(var83(x)), Not(var97(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var2(x1), Not(var38(x1)), Not(var86(x1))), Not(var81(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var77(x1), Not(var66(x1)), var18(x1)), var95(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), var38(x1)), Or(var98(x), Not(var74(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var52(x1)), Not(var54(x1))), Or(var57(x), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var25(x1)), Or(var68(x), Not(var1(x)), Not(var65(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var14(x1), Not(var77(x1)), var57(x1)), Not(var92(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var29(x1), var93(x1)), Or(Not(var67(x)), var71(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var12(x1)), Or(Not(var61(x)), var60(x), var5(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var32(x1), Or(Not(var35(x)), Not(var84(x)), Not(var93(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var92(x1), Not(var50(x1))), Or(Not(var19(x)), var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var59(x1)), Not(var98(x1)), var34(x1)), Not(var48(x)))))),
	ForAll([x], Not(Or(var10(x), var82(x), Not(var71(x)), Not(var43(x)), Not(var89(x))))),
	ForAll([x], Not(Or(Not(var6(x)), Not(var80(x)), var71(x), Not(var9(x)), Not(var72(x))))),
	ForAll([x], Not(Or(var21(x), var83(x), var60(x), var47(x), Not(var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var31(x1), Not(var79(x1)), Not(var54(x1))), Or(Not(var63(x)), Not(var75(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var77(x1), Not(var6(x1)), var23(x1)), Or(Not(var48(x)), var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var60(x1)), Not(var81(x1))), Or(var50(x), Not(var54(x)), Not(var8(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var8(x1)), Not(var91(x1)), Not(var75(x1))), Or(Not(var21(x)), Not(var30(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var87(x1), Not(var44(x1)), var94(x1)), Or(Not(var76(x)), Not(var60(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var3(x1)), Not(var29(x1)), var39(x1), Not(var82(x1))), Not(var79(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var73(x1), Or(Not(var20(x)), var7(x), Not(var61(x)), var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var7(x1)), Not(var44(x1)), Not(var31(x1)), var34(x1)), Not(var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var69(x1)), var27(x1)), Or(var16(x), var19(x), Not(var79(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var51(x1), Or(Not(var73(x)), Not(var33(x)), Not(var95(x)), Not(var58(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), Or(Not(var57(x)), Not(var4(x)), Not(var31(x)), var65(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var20(x1), var72(x1)), Or(Not(var21(x)), var31(x), Not(var10(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var4(x1)), Not(var73(x1)), var56(x1), Not(var23(x1))), Not(var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var75(x1), Or(Not(var46(x)), Not(var84(x)), Not(var28(x)), Not(var93(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var41(x1), Not(var9(x1))), Or(Not(var57(x)), Not(var35(x)), Not(var43(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var80(x1)), Not(var96(x1)), Not(var39(x1))), Or(Not(var52(x)), var75(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var98(x1)), Or(Not(var88(x)), var45(x), var86(x), Not(var40(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var49(x1)), Not(var86(x1))), Or(var51(x), Not(var24(x)), var63(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var76(x1)), Not(var66(x1)), Not(var8(x1))), Or(var41(x), Not(var51(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var43(x1)), Not(var79(x1)), var27(x1)), Or(var69(x), Not(var66(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var38(x1), Not(var45(x1)), var64(x1), Not(var54(x1))), Not(var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var76(x1), var22(x1)), Or(var13(x), var80(x), Not(var93(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var45(x1)), Not(var78(x1)), Not(var84(x1))), Or(Not(var96(x)), Not(var86(x))))))),
	ForAll([x], Not(Or(Not(var57(x)), Not(var13(x)), var40(x), Not(var75(x)), Not(var70(x)), Not(var55(x))))),
	ForAll([x], Not(Or(Not(var10(x)), var16(x), Not(var9(x)), Not(var17(x)), var41(x), var53(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var80(x1), Not(var42(x1)), Not(var27(x1)), Not(var68(x1))), Or(var37(x), var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var36(x1)), Not(var97(x1)), Not(var17(x1))), Or(var51(x), Not(var33(x)), var49(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var2(x1)), var28(x1), Not(var41(x1)), Not(var30(x1)), var14(x1)), var69(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var39(x1), Not(var35(x1)), var80(x1), var58(x1)), Or(var69(x), Not(var81(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var47(x1), Not(var82(x1))), Or(var26(x), Not(var29(x)), Not(var40(x)), var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var76(x1)), Not(var25(x1)), Not(var12(x1)), Not(var22(x1)), Not(var68(x1))), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var72(x1), Or(var91(x), var32(x), var1(x), Not(var83(x)), Not(var27(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var50(x1)), var25(x1), var89(x1), Not(var98(x1)), var94(x1)), var20(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var58(x1), Not(var2(x1))), Or(Not(var55(x)), var85(x), Not(var96(x)), var57(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var98(x1), var76(x1), var52(x1)), Or(var18(x), var64(x), var70(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var66(x1)), var11(x1), Not(var47(x1))), Or(var65(x), var90(x), var57(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var55(x1)), Not(var91(x1)), Not(var65(x1)), Not(var28(x1)), var33(x1)), var72(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var93(x1), var67(x1), Not(var39(x1)), var79(x1)), Or(var77(x), Not(var29(x))))))),
	ForAll([x], Not(Or(Not(var64(x)), var55(x), Not(var52(x)), Not(var84(x)), Not(var71(x)), var67(x), Not(var68(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var98(x1)), var24(x1), Not(var45(x1)), var88(x1), Not(var28(x1)), Not(var50(x1))), Not(var61(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var18(x1), var53(x1), var83(x1), Not(var17(x1)), Not(var15(x1))), Or(var36(x), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), Not(var23(x1)), Not(var14(x1))), Or(var38(x), var71(x), var8(x), var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var54(x1), var96(x1), Not(var17(x1))), Or(Not(var40(x)), var67(x), Not(var23(x)), Not(var53(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var9(x1)), var80(x1), var23(x1), var10(x1)), Or(Not(var6(x)), var75(x), var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var69(x1), Not(var26(x1))), Or(Not(var20(x)), var35(x), var59(x), var23(x), Not(var29(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var97(x1), var50(x1)), Or(Not(var21(x)), Not(var84(x)), Not(var55(x)), Not(var68(x)), var90(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var10(x1), var25(x1)), Or(Not(var46(x)), var21(x), Not(var43(x)), var7(x), Not(var26(x)), Not(var86(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var29(x1)), Not(var98(x1)), Not(var38(x1)), var84(x1), Not(var30(x1))), Or(Not(var94(x)), var25(x), Not(var88(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var26(x1), Not(var4(x1)), Not(var38(x1)), var8(x1), Not(var45(x1))), Or(var51(x), var25(x), var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var64(x1)), Or(Not(var35(x)), var3(x), var9(x), Not(var74(x)), Not(var42(x)), Not(var100(x)), var2(x), var38(x)))))),
	ForAll([x], Not(Not(var44(x)))),
	ForAll([x], Not(Or(Not(var48(x)), var57(x), Not(var32(x)), Not(var62(x)), Not(var17(x)), Not(var40(x)), var13(x), Not(var9(x)), Not(var2(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var54(x1), Not(var62(x1))), Or(var50(x), var67(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var65(x1), var20(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var7(x1)), Or(Not(var82(x)), var24(x), Not(var97(x)), var89(x), var84(x), var35(x), Not(var78(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var11(x1), var58(x1), var79(x1), var28(x1)), Not(var27(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var76(x1)), var98(x1), var14(x1), var96(x1), var5(x1), Not(var4(x1)), var49(x1)), Or(var84(x), Not(var30(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var99(x1)), Not(var23(x1)), var32(x1), Not(var26(x1)), Not(var39(x1))), Or(Not(var5(x)), Not(var24(x)), Not(var36(x)))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
