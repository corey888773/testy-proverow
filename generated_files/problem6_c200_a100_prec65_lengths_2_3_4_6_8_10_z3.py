from z3 import *

Object = DeclareSort('Object')

var77 = Function('var77', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var77(x)), Not(var72(x))))),
	ForAll([x], Not(Or(var41(x), var30(x)))),
	ForAll([x], Not(Or(Not(var11(x)), Not(var82(x))))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var99(x))))),
	ForAll([x], Not(Or(Not(var33(x)), Not(var80(x))))),
	ForAll([x], Not(Or(var59(x), Not(var97(x))))),
	ForAll([x], Not(Or(var59(x), var48(x)))),
	ForAll([x], Not(Or(Not(var53(x)), var8(x)))),
	ForAll([x], Not(Or(Not(var35(x)), var34(x)))),
	ForAll([x], Not(Or(var50(x), Not(var5(x))))),
	ForAll([x], Not(Or(Not(var90(x)), Not(var74(x))))),
	ForAll([x], Not(Or(Not(var13(x)), Not(var92(x))))),
	ForAll([x], Not(Or(var7(x), var80(x)))),
	ForAll([x], Not(Or(var3(x), Not(var83(x))))),
	ForAll([x], Not(Or(Not(var66(x)), Not(var92(x))))),
	ForAll([x], Not(Or(var12(x), var14(x)))),
	ForAll([x], Not(Or(var22(x), var20(x)))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var39(x))))),
	ForAll([x], Not(Or(Not(var36(x)), var57(x)))),
	ForAll([x], Not(Or(var67(x), var42(x)))),
	ForAll([x], Not(Or(var83(x), var68(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var84(x1), Not(var61(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), Not(var53(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var48(x1)), var23(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var25(x1)), Not(var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var85(x1), Not(var79(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Not(var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var73(x1)), Not(var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var26(x1)), var90(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var55(x1), Not(var40(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var47(x1), Not(var94(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), Not(var58(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var37(x1)), var38(x))))),
	ForAll([x], Not(Or(var11(x), Not(var76(x)), var38(x)))),
	ForAll([x], Not(Or(Not(var29(x)), var15(x), var76(x)))),
	ForAll([x], Not(Or(var3(x), Not(var89(x)), Not(var57(x))))),
	ForAll([x], Not(Or(Not(var60(x)), Not(var21(x)), var87(x)))),
	ForAll([x], Not(Or(Not(var44(x)), var51(x), var78(x)))),
	ForAll([x], Not(Or(var86(x), var43(x), var89(x)))),
	ForAll([x], Not(Or(var62(x), Not(var34(x)), var15(x)))),
	ForAll([x], Not(Or(Not(var57(x)), var21(x), var2(x)))),
	ForAll([x], Not(Or(Not(var100(x)), var99(x), Not(var13(x))))),
	ForAll([x], Not(Or(var8(x), Not(var71(x)), Not(var57(x))))),
	ForAll([x], Not(Or(Not(var68(x)), Not(var30(x)), var22(x)))),
	ForAll([x], Not(Or(Not(var5(x)), Not(var87(x)), var57(x)))),
	ForAll([x], Not(Or(var97(x), Not(var94(x)), Not(var50(x))))),
	ForAll([x], Not(Or(var95(x), Not(var64(x)), var44(x)))),
	ForAll([x], Not(Or(var12(x), Not(var88(x)), Not(var51(x))))),
	ForAll([x], Not(Or(Not(var12(x)), Not(var82(x)), Not(var2(x))))),
	ForAll([x], Not(Or(Not(var33(x)), var48(x), var87(x)))),
	ForAll([x], Not(Or(var8(x), var47(x), var78(x)))),
	ForAll([x], Not(Or(Not(var86(x)), Not(var97(x)), Not(var35(x))))),
	ForAll([x], Not(Or(var80(x), Not(var64(x)), var18(x)))),
	ForAll([x], Not(Or(Not(var46(x)), Not(var55(x)), Not(var93(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var90(x1)), var3(x1)), Not(var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var66(x1)), var27(x1)), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var62(x1), Not(var87(x1))), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var99(x1), var8(x1)), Not(var10(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var17(x1), Or(var98(x), var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var6(x1), Or(var78(x), Not(var100(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var100(x1), var16(x1)), var64(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var45(x1), Not(var92(x1))), var67(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var29(x1), Not(var96(x1))), Not(var51(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var42(x1), Not(var82(x1))), var25(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var75(x1), Not(var37(x1))), Not(var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var41(x1), Or(var35(x), Not(var68(x))))))),
	ForAll([x], Not(Or(Not(var25(x)), var37(x), Not(var45(x)), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var18(x)), var40(x), var67(x), var76(x)))),
	ForAll([x], Not(Or(var59(x), var61(x), Not(var70(x)), var84(x)))),
	ForAll([x], Not(Or(Not(var8(x)), Not(var75(x)), var95(x), var19(x)))),
	ForAll([x], Not(Or(var61(x), var38(x), Not(var43(x)), var36(x)))),
	ForAll([x], Not(Or(var52(x), Not(var16(x)), var1(x), Not(var67(x))))),
	ForAll([x], Not(Or(var14(x), Not(var68(x)), var46(x), var95(x)))),
	ForAll([x], Not(Or(var92(x), var83(x), Not(var16(x)), var85(x)))),
	ForAll([x], Not(Or(var23(x), var58(x), var10(x), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var60(x)), Not(var25(x)), var88(x), Not(var31(x))))),
	ForAll([x], Not(Or(Not(var76(x)), var93(x), Not(var67(x)), var5(x)))),
	ForAll([x], Not(Or(var89(x), Not(var98(x)), Not(var39(x)), Not(var87(x))))),
	ForAll([x], Not(Or(var91(x), var81(x), Not(var35(x)), Not(var52(x))))),
	ForAll([x], Not(Or(Not(var56(x)), var13(x), Not(var76(x)), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var59(x)), var94(x), Not(var58(x)), var49(x)))),
	ForAll([x], Not(Or(var10(x), var80(x), Not(var17(x)), var65(x)))),
	ForAll([x], Not(Or(var98(x), Not(var6(x)), var91(x), var38(x)))),
	ForAll([x], Not(Or(Not(var16(x)), Not(var14(x)), Not(var79(x)), Not(var72(x))))),
	ForAll([x], Not(Or(var54(x), Not(var93(x)), var85(x), var87(x)))),
	ForAll([x], Not(Or(Not(var91(x)), var35(x), Not(var61(x)), Not(var19(x))))),
	ForAll([x], Not(Or(Not(var27(x)), Not(var20(x)), Not(var36(x)), Not(var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var31(x1), Or(Not(var72(x)), Not(var63(x)), Not(var94(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var73(x1)), Or(var21(x), Not(var87(x)), var4(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var80(x1)), var71(x1)), Or(var20(x), var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var32(x1)), Or(Not(var38(x)), Not(var82(x)), Not(var41(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var74(x1)), Not(var37(x1))), Or(var66(x), var56(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var66(x1)), Or(Not(var54(x)), var85(x), var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var77(x1)), Not(var9(x1))), Or(Not(var97(x)), Not(var26(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var96(x1)), var85(x1)), Or(Not(var95(x)), Not(var8(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var24(x1)), Not(var12(x1))), Or(var29(x), var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var3(x1), var4(x1)), Or(var45(x), Not(var47(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var54(x1)), var90(x1), Not(var65(x1))), Not(var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var54(x1)), var43(x1), Not(var8(x1))), Not(var63(x)))))),
	ForAll([x], Not(Or(var2(x), Not(var29(x)), var60(x), Not(var74(x)), Not(var34(x)), Not(var86(x))))),
	ForAll([x], Not(Or(var31(x), var51(x), var92(x), Not(var7(x)), Not(var78(x)), var46(x)))),
	ForAll([x], Not(Or(Not(var51(x)), var3(x), var47(x), var69(x), var56(x), var61(x)))),
	ForAll([x], Not(Or(Not(var45(x)), var22(x), var40(x), var58(x), var15(x), var74(x)))),
	ForAll([x], Not(Or(Not(var21(x)), Not(var4(x)), Not(var40(x)), Not(var54(x)), Not(var93(x)), var3(x)))),
	ForAll([x], Not(Or(var71(x), var1(x), var52(x), Not(var81(x)), var87(x), Not(var93(x))))),
	ForAll([x], Not(Or(Not(var24(x)), Not(var34(x)), Not(var13(x)), Not(var57(x)), Not(var72(x)), Not(var44(x))))),
	ForAll([x], Not(Or(var94(x), var2(x), var20(x), var61(x), Not(var63(x)), var25(x)))),
	ForAll([x], Not(Or(var42(x), var13(x), Not(var85(x)), Not(var81(x)), var45(x), Not(var53(x))))),
	ForAll([x], Not(Or(Not(var14(x)), var9(x), var86(x), Not(var16(x)), Not(var60(x)), var80(x)))),
	ForAll([x], Not(Or(var99(x), var28(x), var25(x), var34(x), Not(var45(x)), var5(x)))),
	ForAll([x], Not(Or(Not(var49(x)), Not(var75(x)), var39(x), Not(var55(x)), Not(var98(x)), var70(x)))),
	ForAll([x], Not(Or(var42(x), var82(x), Not(var98(x)), Not(var20(x)), Not(var13(x)), Not(var1(x))))),
	ForAll([x], Not(Or(Not(var78(x)), var4(x), Not(var71(x)), var27(x), Not(var38(x)), var28(x)))),
	ForAll([x], Not(Or(var47(x), var51(x), var53(x), var3(x), var20(x), var60(x)))),
	ForAll([x], Not(Or(var47(x), Not(var98(x)), var26(x), var72(x), Not(var48(x)), var75(x)))),
	ForAll([x], Not(Or(Not(var9(x)), var76(x), var62(x), Not(var48(x)), Not(var30(x)), Not(var54(x))))),
	ForAll([x], Not(Or(var98(x), var18(x), Not(var63(x)), Not(var19(x)), Not(var71(x)), Not(var34(x))))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var83(x)), Not(var33(x)), var97(x), Not(var71(x)), var10(x)))),
	ForAll([x], Not(Or(var82(x), Not(var31(x)), Not(var11(x)), Not(var61(x)), var13(x), var76(x)))),
	ForAll([x], Not(Or(Not(var44(x)), Not(var100(x)), var86(x), Not(var84(x)), Not(var50(x)), Not(var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var63(x1), var8(x1), var58(x1)), Or(Not(var5(x)), Not(var71(x)), Not(var10(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var3(x1)), Not(var70(x1)), var73(x1)), Or(Not(var67(x)), Not(var34(x)), var18(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var88(x1)), var51(x1), Not(var82(x1)), Not(var56(x1))), Or(Not(var25(x)), Not(var60(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var45(x1)), var95(x1), var24(x1), var91(x1)), Or(var78(x), Not(var21(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var59(x1)), var41(x1), Not(var70(x1)), Not(var56(x1))), Or(var99(x), Not(var4(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var91(x1)), Or(Not(var80(x)), var82(x), Not(var48(x)), var1(x), var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var5(x1), Not(var47(x1)), Not(var44(x1)), var26(x1)), Or(var20(x), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var51(x1)), Not(var34(x1))), Or(Not(var9(x)), var76(x), var79(x), var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var25(x1), var17(x1), Not(var73(x1)), var82(x1)), Or(var70(x), var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var39(x1)), Not(var8(x1)), Not(var40(x1)), Not(var49(x1))), Or(Not(var3(x)), Not(var46(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var31(x1)), Not(var56(x1)), Not(var88(x1)), Not(var24(x1)), Not(var99(x1))), var38(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var15(x1)), Not(var57(x1)), Not(var18(x1))), Or(Not(var17(x)), var10(x), Not(var98(x))))))),
	ForAll([x], Not(Or(var20(x), Not(var40(x)), var60(x), var18(x), Not(var9(x)), var92(x), Not(var58(x)), Not(var93(x))))),
	ForAll([x], Not(Or(Not(var67(x)), var84(x), var73(x), Not(var22(x)), Not(var59(x)), Not(var16(x)), Not(var33(x)), Not(var85(x))))),
	ForAll([x], Not(Or(Not(var89(x)), Not(var8(x)), var1(x), Not(var92(x)), var16(x), Not(var28(x)), var10(x), var45(x)))),
	ForAll([x], Not(Or(var2(x), var16(x), var25(x), var8(x), Not(var29(x)), var54(x), var35(x), var40(x)))),
	ForAll([x], Not(Or(Not(var44(x)), Not(var5(x)), Not(var20(x)), var89(x), var77(x), var48(x), Not(var40(x)), Not(var7(x))))),
	ForAll([x], Not(Or(var86(x), Not(var47(x)), Not(var48(x)), Not(var85(x)), var53(x), var15(x), Not(var80(x)), var17(x)))),
	ForAll([x], Not(Or(Not(var18(x)), Not(var100(x)), Not(var37(x)), var99(x), Not(var75(x)), Not(var58(x)), var20(x), Not(var87(x))))),
	ForAll([x], Not(Or(Not(var24(x)), var77(x), var53(x), var78(x), var87(x), Not(var6(x)), var31(x), var100(x)))),
	ForAll([x], Not(Or(Not(var55(x)), var15(x), Not(var19(x)), var94(x), Not(var33(x)), var32(x), Not(var24(x)), var44(x)))),
	ForAll([x], Not(Or(var51(x), Not(var86(x)), Not(var94(x)), var6(x), var89(x), var95(x), Not(var52(x)), var31(x)))),
	ForAll([x], Not(Or(var49(x), Not(var75(x)), Not(var7(x)), var61(x), Not(var100(x)), var67(x), Not(var54(x)), Not(var89(x))))),
	ForAll([x], Not(Or(var8(x), var32(x), Not(var81(x)), var51(x), var13(x), Not(var74(x)), Not(var83(x)), var76(x)))),
	ForAll([x], Not(Or(var38(x), var63(x), var65(x), Not(var40(x)), Not(var91(x)), Not(var31(x)), var25(x), Not(var62(x))))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var80(x)), Not(var70(x)), Not(var78(x)), Not(var23(x)), Not(var49(x)), Not(var43(x)), Not(var10(x))))),
	ForAll([x], Not(Or(Not(var67(x)), var30(x), var94(x), var62(x), Not(var92(x)), Not(var64(x)), Not(var6(x)), Not(var76(x))))),
	ForAll([x], Not(Or(Not(var69(x)), var92(x), Not(var10(x)), Not(var36(x)), Not(var4(x)), Not(var53(x)), Not(var61(x)), Not(var3(x))))),
	ForAll([x], Not(Or(var15(x), Not(var69(x)), var62(x), var78(x), Not(var61(x)), var67(x), Not(var17(x)), var86(x)))),
	ForAll([x], Not(Or(var51(x), var65(x), Not(var41(x)), Not(var93(x)), var84(x), Not(var57(x)), Not(var95(x)), var9(x)))),
	ForAll([x], Not(Or(var92(x), var67(x), Not(var21(x)), var48(x), var56(x), Not(var86(x)), var25(x), var7(x)))),
	ForAll([x], Not(Or(var6(x), Not(var41(x)), var40(x), var47(x), Not(var98(x)), Not(var82(x)), Not(var74(x)), Not(var66(x))))),
	ForAll([x], Not(Or(Not(var26(x)), var95(x), var40(x), var45(x), var25(x), var49(x), var60(x), Not(var93(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var2(x1)), var97(x1), var77(x1), var9(x1), Not(var91(x1))), Or(Not(var76(x)), var17(x), Not(var5(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var29(x1), var93(x1), Not(var28(x1)), var73(x1), var55(x1)), Or(var37(x), var25(x), var27(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var100(x1)), Not(var96(x1)), var84(x1), var15(x1), Not(var32(x1)), var46(x1), Not(var95(x1))), var62(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var48(x1), var30(x1), var22(x1), var62(x1), Not(var53(x1)), var13(x1), var74(x1)), var33(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var69(x1)), Not(var18(x1)), Not(var25(x1)), Not(var64(x1)), Not(var22(x1)), var38(x1), var71(x1)), Not(var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var93(x1), Not(var28(x1))), Or(Not(var88(x)), var84(x), Not(var26(x)), var90(x), Not(var96(x)), Not(var86(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var59(x1)), Or(var66(x), var63(x), Not(var32(x)), Not(var28(x)), Not(var5(x)), Not(var22(x)), Not(var93(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var60(x1), Not(var93(x1)), Not(var86(x1)), Not(var50(x1))), Or(var65(x), Not(var81(x)), var17(x), Not(var26(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var75(x1), var60(x1), Not(var66(x1)), Not(var73(x1))), Or(Not(var27(x)), var98(x), Not(var15(x)), var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var64(x1)), var70(x1), var57(x1), var24(x1), Not(var66(x1))), Or(Not(var1(x)), var94(x), Not(var95(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var85(x1)), var84(x1), var10(x1), var38(x1)), Or(Not(var3(x)), Not(var15(x)), var2(x), var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var17(x1)), Or(var19(x), Not(var89(x)), var5(x), Not(var62(x)), var52(x), Not(var22(x)), Not(var48(x))))))),
	ForAll([x], Not(Or(var29(x), var7(x), Not(var20(x)), var27(x), var40(x), var11(x), Not(var57(x)), Not(var46(x)), Not(var71(x)), var95(x)))),
	ForAll([x], Not(Or(Not(var74(x)), Not(var25(x)), var22(x), Not(var35(x)), var28(x), Not(var86(x)), Not(var40(x)), Not(var10(x)), var41(x), Not(var89(x))))),
	ForAll([x], Not(Or(Not(var18(x)), Not(var6(x)), Not(var47(x)), Not(var89(x)), Not(var35(x)), Not(var50(x)), Not(var14(x)), var38(x), Not(var10(x)), var2(x)))),
	ForAll([x], Not(Or(Not(var70(x)), Not(var36(x)), Not(var97(x)), var20(x), Not(var96(x)), var31(x), var28(x), Not(var64(x)), Not(var9(x)), var94(x)))),
	ForAll([x], Not(Or(Not(var4(x)), var5(x), var35(x), var78(x), Not(var98(x)), Not(var12(x)), var95(x), Not(var74(x)), Not(var75(x)), var99(x)))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var6(x)), Not(var30(x)), Not(var38(x)), var4(x), Not(var33(x)), var15(x), var24(x), Not(var44(x)), var96(x)))),
	ForAll([x], Not(Or(var54(x), Not(var18(x)), Not(var89(x)), Not(var37(x)), Not(var92(x)), Not(var9(x)), var67(x), var57(x), var41(x), Not(var46(x))))),
	ForAll([x], Not(Or(Not(var91(x)), var99(x), var94(x), Not(var4(x)), Not(var2(x)), Not(var97(x)), var17(x), var92(x), var3(x), Not(var37(x))))),
	ForAll([x], Not(Or(var79(x), Not(var74(x)), Not(var22(x)), var70(x), Not(var59(x)), Not(var49(x)), Not(var56(x)), var36(x), var44(x), var13(x)))),
	ForAll([x], Not(Or(Not(var78(x)), Not(var95(x)), Not(var53(x)), Not(var28(x)), Not(var74(x)), Not(var10(x)), var32(x), var63(x), Not(var20(x)), Not(var47(x))))),
	ForAll([x], Not(Or(Not(var75(x)), var71(x), var11(x), Not(var39(x)), var91(x), var17(x), Not(var13(x)), var1(x), var42(x), var21(x)))),
	ForAll([x], Not(Or(Not(var18(x)), var22(x), Not(var82(x)), Not(var5(x)), var13(x), var34(x), var98(x), Not(var53(x)), Not(var58(x)), var10(x)))),
	ForAll([x], Not(Or(Not(var89(x)), var49(x), Not(var17(x)), var41(x), var95(x), Not(var30(x)), Not(var77(x)), var26(x), var67(x), Not(var73(x))))),
	ForAll([x], Not(Or(var33(x), var62(x), Not(var46(x)), Not(var23(x)), var77(x), Not(var19(x)), var30(x), var76(x), Not(var14(x)), Not(var27(x))))),
	ForAll([x], Not(Or(Not(var24(x)), Not(var82(x)), var5(x), Not(var87(x)), var58(x), Not(var93(x)), Not(var76(x)), Not(var85(x)), var46(x), Not(var3(x))))),
	ForAll([x], Not(Or(var94(x), var65(x), var85(x), Not(var17(x)), var69(x), var82(x), var80(x), var38(x), var19(x), var3(x)))),
	ForAll([x], Not(Or(var59(x), var38(x), Not(var24(x)), Not(var1(x)), Not(var28(x)), var57(x), Not(var73(x)), Not(var19(x)), var65(x), var20(x)))),
	ForAll([x], Not(Or(Not(var89(x)), var55(x), var33(x), Not(var37(x)), Not(var97(x)), var87(x), var15(x), Not(var25(x)), var32(x), Not(var26(x))))),
	ForAll([x], Not(Or(var39(x), var18(x), var71(x), Not(var42(x)), var60(x), var86(x), Not(var12(x)), Not(var85(x)), var36(x), Not(var44(x))))),
	ForAll([x], Not(Or(var86(x), Not(var100(x)), Not(var29(x)), Not(var76(x)), Not(var45(x)), Not(var10(x)), var31(x), Not(var5(x)), Not(var75(x)), var82(x)))),
	ForAll([x], Not(Or(var10(x), Not(var12(x)), Not(var13(x)), var33(x), var88(x), var21(x), Not(var49(x)), var51(x), var62(x), var7(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var82(x1)), Or(var40(x), Not(var79(x)), var62(x), var90(x), Not(var87(x)), var45(x), var55(x), var69(x), Not(var91(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var3(x1), Not(var86(x1)), var95(x1)), Or(var100(x), var73(x), Not(var35(x)), var97(x), Not(var51(x)), var85(x), Not(var49(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var26(x1), Not(var10(x1)), Not(var45(x1))), Or(Not(var74(x)), Not(var21(x)), Not(var52(x)), var82(x), Not(var32(x)), Not(var1(x)), Not(var17(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var54(x1), var69(x1), var94(x1)), Or(var28(x), Not(var52(x)), var98(x), Not(var12(x)), var68(x), var11(x), Not(var32(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var4(x1), Not(var46(x1)), var100(x1), Not(var67(x1)), Not(var50(x1))), Or(Not(var93(x)), var71(x), var24(x), Not(var60(x)), var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var50(x1)), Not(var92(x1))), Or(var49(x), var47(x), var100(x), Not(var87(x)), Not(var39(x)), Not(var56(x)), var59(x), Not(var82(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var47(x1)), var90(x1)), Or(var54(x), Not(var58(x)), var30(x), Not(var87(x)), Not(var24(x)), Not(var60(x)), Not(var15(x)), var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var21(x1), var24(x1), Not(var63(x1)), Not(var47(x1)), Not(var1(x1))), Or(var55(x), var69(x), Not(var66(x)), var87(x), Not(var4(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var83(x1), var70(x1), Not(var68(x1)), Not(var39(x1)), Not(var24(x1)), Not(var41(x1)), var2(x1), var5(x1)), Or(var58(x), var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var92(x1), Or(Not(var76(x)), var7(x), var94(x), var16(x), var11(x), var45(x), Not(var17(x)), Not(var39(x)), Not(var89(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var10(x1)), Not(var12(x1)), Not(var51(x1)), Not(var95(x1)), var99(x1), var1(x1), Not(var35(x1)), Not(var97(x1)), Not(var80(x1))), var52(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var5(x1), Not(var64(x1))), Or(var66(x), Not(var59(x)), var29(x), var42(x), Not(var25(x)), Not(var78(x)), var57(x), var90(x)))))),
	ForAll([x], Not(Or(Not(var66(x)), var48(x), var89(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var25(x1)), var41(x1), var3(x1)), var73(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())