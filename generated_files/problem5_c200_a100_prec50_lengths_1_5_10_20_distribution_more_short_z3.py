from z3 import *

Object = DeclareSort('Object')

var89 = Function('var89', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(var89(x))),
	ForAll([x], Not(var46(x))),
	ForAll([x], Not(var84(x))),
	ForAll([x], Not(Not(var97(x)))),
	ForAll([x], Not(Not(var99(x)))),
	ForAll([x], Not(Not(var65(x)))),
	ForAll([x], Not(var39(x))),
	ForAll([x], Not(var28(x))),
	ForAll([x], Not(Not(var78(x)))),
	ForAll([x], Not(var39(x))),
	ForAll([x], Not(Not(var50(x)))),
	ForAll([x], Not(Not(var44(x)))),
	ForAll([x], Not(var45(x))),
	ForAll([x], Not(Not(var2(x)))),
	ForAll([x], Not(Not(var30(x)))),
	ForAll([x], Not(Not(var100(x)))),
	ForAll([x], Not(Not(var77(x)))),
	ForAll([x], Not(var80(x))),
	ForAll([x], Not(Not(var75(x)))),
	ForAll([x], Not(Not(var56(x)))),
	ForAll([x], Not(var63(x))),
	ForAll([x], Not(Not(var9(x)))),
	ForAll([x], Not(Not(var91(x)))),
	ForAll([x], Not(var19(x))),
	ForAll([x], Not(var20(x))),
	ForAll([x], Not(var38(x))),
	ForAll([x], Not(var28(x))),
	ForAll([x], Not(var21(x))),
	ForAll([x], Not(Not(var27(x)))),
	ForAll([x], Not(Not(var3(x)))),
	ForAll([x], Not(var54(x))),
	ForAll([x], Not(Not(var34(x)))),
	ForAll([x], Not(Not(var49(x)))),
	Exists([x], var48(x)),
	Exists([x], var21(x)),
	Exists([x], Not(var25(x))),
	Exists([x], Not(var26(x))),
	Exists([x], var67(x)),
	Exists([x], Not(var10(x))),
	Exists([x], Not(var62(x))),
	Exists([x], Not(var99(x))),
	Exists([x], Not(var39(x))),
	Exists([x], var17(x)),
	Exists([x], var35(x)),
	Exists([x], Not(var30(x))),
	Exists([x], Not(var33(x))),
	Exists([x], var61(x)),
	Exists([x], Not(var58(x))),
	Exists([x], var82(x)),
	Exists([x], var44(x)),
	Exists([x], var34(x)),
	Exists([x], Not(var61(x))),
	Exists([x], var82(x)),
	Exists([x], var25(x)),
	Exists([x], Not(var63(x))),
	Exists([x], var29(x)),
	Exists([x], Not(var88(x))),
	Exists([x], Not(var64(x))),
	Exists([x], var42(x)),
	Exists([x], var34(x)),
	Exists([x], Not(var31(x))),
	Exists([x], Not(var14(x))),
	Exists([x], var64(x)),
	Exists([x], var23(x)),
	Exists([x], Not(var11(x))),
	Exists([x], Not(var11(x))),
	ForAll([x], Not(Or(Not(var93(x)), var91(x), var58(x), Not(var3(x)), var82(x)))),
	ForAll([x], Not(Or(Not(var47(x)), var26(x), var36(x), Not(var2(x)), var61(x)))),
	ForAll([x], Not(Or(var47(x), Not(var4(x)), var85(x), Not(var29(x)), Not(var14(x))))),
	ForAll([x], Not(Or(Not(var39(x)), Not(var13(x)), Not(var2(x)), Not(var96(x)), var82(x)))),
	ForAll([x], Not(Or(Not(var96(x)), var19(x), Not(var73(x)), Not(var12(x)), var68(x)))),
	ForAll([x], Not(Or(Not(var59(x)), var3(x), var34(x), var78(x), Not(var66(x))))),
	ForAll([x], Not(Or(Not(var6(x)), var88(x), var70(x), var47(x), var90(x)))),
	ForAll([x], Not(Or(Not(var94(x)), var100(x), Not(var75(x)), var67(x), var30(x)))),
	ForAll([x], Not(Or(Not(var43(x)), var73(x), Not(var57(x)), var38(x), Not(var42(x))))),
	ForAll([x], Not(Or(Not(var26(x)), Not(var94(x)), Not(var23(x)), Not(var63(x)), var24(x)))),
	ForAll([x], Not(Or(var91(x), var48(x), var3(x), var29(x), var68(x)))),
	ForAll([x], Not(Or(Not(var6(x)), var100(x), Not(var3(x)), var10(x), Not(var74(x))))),
	ForAll([x], Not(Or(var87(x), var75(x), Not(var33(x)), Not(var1(x)), var61(x)))),
	ForAll([x], Not(Or(Not(var25(x)), Not(var51(x)), var46(x), Not(var2(x)), Not(var6(x))))),
	ForAll([x], Not(Or(var10(x), Not(var78(x)), var8(x), var93(x), Not(var7(x))))),
	ForAll([x], Not(Or(var41(x), var95(x), Not(var44(x)), var45(x), Not(var34(x))))),
	ForAll([x], Not(Or(Not(var73(x)), Not(var60(x)), Not(var84(x)), var67(x), Not(var32(x))))),
	ForAll([x], Not(Or(Not(var38(x)), Not(var100(x)), var64(x), Not(var42(x)), Not(var60(x))))),
	ForAll([x], Not(Or(var51(x), var84(x), var57(x), var39(x), var87(x)))),
	ForAll([x], Not(Or(Not(var22(x)), Not(var65(x)), var85(x), Not(var64(x)), var51(x)))),
	ForAll([x], Not(Or(var34(x), var43(x), var47(x), var32(x), Not(var96(x))))),
	ForAll([x], Not(Or(var5(x), var35(x), var83(x), Not(var62(x)), Not(var58(x))))),
	ForAll([x], Not(Or(Not(var89(x)), Not(var84(x)), Not(var78(x)), Not(var14(x)), Not(var21(x))))),
	ForAll([x], Not(Or(Not(var75(x)), var16(x), Not(var83(x)), var26(x), var90(x)))),
	ForAll([x], Not(Or(Not(var45(x)), var65(x), Not(var47(x)), var1(x), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var18(x)), Not(var95(x)), var20(x), Not(var29(x)), Not(var32(x))))),
	ForAll([x], Not(Or(var100(x), var87(x), var72(x), Not(var38(x)), var55(x)))),
	ForAll([x], Not(Or(Not(var10(x)), var72(x), var76(x), var59(x), var61(x)))),
	ForAll([x], Not(Or(Not(var38(x)), var52(x), var39(x), var44(x), Not(var59(x))))),
	ForAll([x], Not(Or(var55(x), var4(x), Not(var17(x)), var59(x), var62(x)))),
	ForAll([x], Not(Or(var8(x), var93(x), Not(var13(x)), var53(x), Not(var16(x))))),
	ForAll([x], Not(Or(var35(x), var55(x), Not(var44(x)), Not(var99(x)), Not(var100(x))))),
	ForAll([x], Not(Or(var15(x), Not(var56(x)), var41(x), var89(x), var94(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var76(x1)), Or(var51(x), var42(x), var83(x), Not(var75(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var75(x1)), Not(var88(x1))), Or(Not(var87(x)), Not(var73(x)), Not(var29(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var75(x1), var17(x1), var77(x1)), Or(var82(x), var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var15(x1)), var1(x1)), Or(Not(var6(x)), Not(var10(x)), var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var44(x1)), var97(x1), var90(x1), Not(var56(x1))), Not(var48(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var67(x1)), var99(x1), var42(x1)), Or(var26(x), Not(var4(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var33(x1), Not(var84(x1))), Or(var17(x), var6(x), Not(var72(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var80(x1), var57(x1), Not(var84(x1)), Not(var8(x1))), Not(var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var40(x1), var81(x1), var36(x1)), Or(var15(x), Not(var13(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var47(x1), var35(x1), var63(x1)), Or(Not(var97(x)), var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var77(x1), var75(x1), Not(var71(x1)), var16(x1)), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var67(x1), var13(x1)), Or(var58(x), Not(var79(x)), var20(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var32(x1)), Or(Not(var56(x)), var51(x), Not(var38(x)), var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var38(x1), var99(x1), var95(x1)), Or(Not(var10(x)), Not(var36(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var72(x1), Or(var83(x), var60(x), var93(x), var76(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), var42(x1), var21(x1), var36(x1)), var24(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var7(x1), Or(Not(var43(x)), var70(x), Not(var13(x)), var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var34(x1)), Not(var31(x1))), Or(Not(var33(x)), Not(var92(x)), var52(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var91(x1), Not(var52(x1)), var82(x1)), Or(var62(x), var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var12(x1), var28(x1)), Or(var91(x), Not(var9(x)), var83(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var86(x1), Not(var27(x1)), var48(x1)), Or(var62(x), var4(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var24(x1)), var84(x1)), Or(Not(var31(x)), var61(x), var62(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var65(x1), Not(var82(x1))), Or(Not(var54(x)), Not(var1(x)), Not(var71(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var72(x1)), Or(Not(var40(x)), Not(var42(x)), var62(x), Not(var69(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var84(x1)), var13(x1), Not(var69(x1))), Or(Not(var31(x)), var18(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var46(x1)), Or(Not(var16(x)), var48(x), Not(var20(x)), var26(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var23(x1)), var21(x1), Not(var98(x1))), Or(Not(var39(x)), var63(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), Or(Not(var18(x)), Not(var60(x)), Not(var81(x)), var49(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var92(x1)), var67(x1), var89(x1), Not(var7(x1))), Not(var26(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var99(x1)), var1(x1), Not(var72(x1))), Or(Not(var57(x)), var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var93(x1), var6(x1), Not(var81(x1))), Or(Not(var24(x)), var5(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var88(x1), Not(var54(x1))), Or(Not(var21(x)), var65(x), Not(var46(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var35(x1)), Or(var32(x), var7(x), var97(x), var24(x)))))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var86(x)), var74(x), Not(var71(x)), var50(x), Not(var55(x)), Not(var57(x)), Not(var52(x)), var38(x), var58(x)))),
	ForAll([x], Not(Or(var11(x), Not(var79(x)), var61(x), Not(var28(x)), var44(x), var55(x), var30(x), var16(x), Not(var98(x)), var83(x)))),
	ForAll([x], Not(Or(Not(var53(x)), Not(var95(x)), Not(var19(x)), Not(var61(x)), Not(var11(x)), Not(var63(x)), var41(x), Not(var76(x)), var50(x), Not(var68(x))))),
	ForAll([x], Not(Or(var75(x), var20(x), Not(var13(x)), Not(var49(x)), var22(x), var1(x), var36(x), Not(var47(x)), var44(x), Not(var94(x))))),
	ForAll([x], Not(Or(var49(x), Not(var57(x)), Not(var29(x)), Not(var8(x)), var40(x), var74(x), Not(var81(x)), Not(var77(x)), Not(var93(x)), var24(x)))),
	ForAll([x], Not(Or(var7(x), Not(var57(x)), var68(x), Not(var98(x)), Not(var65(x)), var62(x), var82(x), Not(var66(x)), var87(x), var34(x)))),
	ForAll([x], Not(Or(var57(x), Not(var78(x)), var96(x), Not(var86(x)), var74(x), var29(x), Not(var33(x)), Not(var24(x)), Not(var98(x)), var12(x)))),
	ForAll([x], Not(Or(Not(var76(x)), Not(var40(x)), Not(var82(x)), Not(var25(x)), Not(var46(x)), var66(x), var23(x), Not(var80(x)), var47(x), var64(x)))),
	ForAll([x], Not(Or(Not(var98(x)), var53(x), var2(x), var62(x), Not(var57(x)), var75(x), var74(x), var87(x), var43(x), var14(x)))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var98(x)), var13(x), var85(x), var83(x), Not(var65(x)), var59(x), var46(x), Not(var53(x)), var84(x)))),
	ForAll([x], Not(Or(Not(var97(x)), var15(x), Not(var2(x)), Not(var24(x)), Not(var55(x)), Not(var4(x)), Not(var77(x)), Not(var35(x)), Not(var90(x)), var73(x)))),
	ForAll([x], Not(Or(var71(x), var81(x), Not(var55(x)), Not(var5(x)), var15(x), Not(var42(x)), Not(var33(x)), var43(x), Not(var23(x)), var35(x)))),
	ForAll([x], Not(Or(Not(var42(x)), var11(x), var40(x), var54(x), Not(var84(x)), Not(var48(x)), Not(var73(x)), Not(var6(x)), var96(x), var89(x)))),
	ForAll([x], Not(Or(Not(var37(x)), var9(x), Not(var88(x)), Not(var30(x)), var51(x), var17(x), Not(var99(x)), Not(var81(x)), Not(var29(x)), var40(x)))),
	ForAll([x], Not(Or(var68(x), Not(var81(x)), Not(var88(x)), Not(var8(x)), var50(x), Not(var2(x)), Not(var69(x)), var17(x), Not(var58(x)), var41(x)))),
	ForAll([x], Not(Or(var72(x), var84(x), var28(x), var98(x), Not(var37(x)), Not(var65(x)), var80(x), Not(var58(x)), var33(x), var20(x)))),
	ForAll([x], Not(Or(var95(x), Not(var91(x)), Not(var64(x)), var71(x), var9(x), Not(var36(x)), var7(x), var72(x), var33(x), Not(var100(x))))),
	ForAll([x], Not(Or(var69(x), Not(var42(x)), var70(x), Not(var36(x)), Not(var43(x)), Not(var99(x)), Not(var75(x)), var50(x), Not(var27(x)), var92(x)))),
	ForAll([x], Not(Or(Not(var3(x)), Not(var46(x)), var77(x), var40(x), Not(var10(x)), Not(var38(x)), Not(var37(x)), Not(var42(x)), var90(x), Not(var12(x))))),
	ForAll([x], Not(Or(Not(var31(x)), var54(x), var6(x), var15(x), Not(var38(x)), var83(x), Not(var77(x)), var56(x), var26(x), var74(x)))),
	ForAll([x], Not(Or(Not(var99(x)), Not(var77(x)), var21(x), Not(var20(x)), var11(x), var5(x), var28(x), var41(x), var32(x), Not(var82(x))))),
	ForAll([x], Not(Or(var26(x), var70(x), var25(x), var75(x), var18(x), var30(x), var12(x), Not(var5(x)), Not(var96(x)), Not(var58(x))))),
	ForAll([x], Not(Or(Not(var41(x)), Not(var35(x)), Not(var99(x)), var43(x), var44(x), Not(var4(x)), Not(var79(x)), var92(x), var30(x), var75(x)))),
	ForAll([x], Not(Or(var84(x), Not(var62(x)), Not(var80(x)), var25(x), var35(x), var1(x), Not(var18(x)), Not(var72(x)), var51(x), var50(x)))),
	ForAll([x], Not(Or(Not(var75(x)), var100(x), Not(var48(x)), Not(var14(x)), Not(var2(x)), Not(var5(x)), var24(x), Not(var58(x)), var43(x), Not(var83(x))))),
	ForAll([x], Not(Or(var62(x), Not(var12(x)), var77(x), var95(x), var2(x), Not(var1(x)), Not(var11(x)), var23(x), Not(var69(x)), Not(var38(x))))),
	ForAll([x], Not(Or(Not(var98(x)), Not(var34(x)), var81(x), Not(var14(x)), Not(var59(x)), var13(x), Not(var100(x)), var18(x), var1(x), Not(var52(x))))),
	ForAll([x], Not(Or(Not(var57(x)), var80(x), var93(x), Not(var82(x)), Not(var5(x)), Not(var52(x)), var16(x), Not(var34(x)), var12(x), Not(var50(x))))),
	ForAll([x], Not(Or(var91(x), Not(var28(x)), var88(x), var26(x), var87(x), Not(var64(x)), Not(var78(x)), Not(var52(x)), Not(var16(x)), Not(var6(x))))),
	ForAll([x], Not(Or(var73(x), var13(x), var48(x), Not(var92(x)), Not(var19(x)), var33(x), Not(var55(x)), Not(var61(x)), var68(x), Not(var38(x))))),
	ForAll([x], Not(Or(var87(x), var4(x), Not(var97(x)), var56(x), var91(x), Not(var72(x)), var82(x), var3(x), Not(var15(x)), var17(x)))),
	ForAll([x], Not(Or(var65(x), Not(var94(x)), var27(x), var34(x), var42(x), Not(var13(x)), var40(x), var52(x), Not(var88(x)), Not(var98(x))))),
	ForAll([x], Not(Or(Not(var14(x)), var67(x), var56(x), var12(x), Not(var55(x)), Not(var1(x)), var8(x), Not(var74(x)), Not(var3(x)), Not(var51(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var86(x1)), Not(var93(x1)), Not(var87(x1)), Not(var63(x1)), Not(var72(x1)), Not(var39(x1)), Not(var45(x1)), var75(x1), Not(var46(x1))), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var98(x1)), Not(var91(x1)), Not(var39(x1)), Not(var42(x1)), var36(x1), var25(x1)), Or(Not(var83(x)), var4(x), var16(x), Not(var13(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var28(x1), Not(var64(x1)), var30(x1), Not(var51(x1)), var68(x1)), Or(var74(x), var12(x), Not(var16(x)), var86(x), Not(var81(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var13(x1), Or(var65(x), Not(var7(x)), var44(x), var82(x), var46(x), Not(var32(x)), Not(var38(x)), Not(var74(x)), var10(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var100(x1)), var47(x1)), Or(var85(x), Not(var59(x)), var93(x), var17(x), var39(x), Not(var26(x)), var42(x), var4(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var23(x1), var14(x1), var72(x1), Not(var25(x1)), var89(x1), Not(var36(x1)), Not(var39(x1)), Not(var52(x1))), Or(Not(var69(x)), Not(var41(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var97(x1), Not(var32(x1)), var65(x1), Not(var14(x1)), var18(x1), Not(var87(x1)), var77(x1), var39(x1), Not(var66(x1))), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var44(x1), var85(x1), Not(var94(x1)), var50(x1)), Or(Not(var53(x)), Not(var20(x)), Not(var56(x)), var69(x), var59(x), var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var3(x1)), var28(x1), Not(var96(x1)), var64(x1), var23(x1), var4(x1), var80(x1), Not(var7(x1))), Or(var34(x), Not(var43(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var58(x1)), Or(var65(x), var52(x), var33(x), var50(x), Not(var19(x)), Not(var97(x)), Not(var6(x)), Not(var99(x)), Not(var96(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var20(x1)), Not(var70(x1)), Not(var93(x1)), Not(var37(x1)), Not(var59(x1)), Not(var11(x1)), var50(x1)), Or(Not(var61(x)), Not(var46(x)), var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var24(x1)), var58(x1), Not(var1(x1)), Not(var27(x1)), Not(var35(x1)), var75(x1), var74(x1), var99(x1)), Or(Not(var61(x)), Not(var66(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var98(x1)), Not(var33(x1)), Not(var100(x1)), Not(var18(x1))), Or(var23(x), Not(var75(x)), var55(x), var39(x), Not(var46(x)), Not(var89(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var41(x1), Not(var39(x1))), Or(var88(x), var36(x), var51(x), var6(x), Not(var95(x)), var5(x), var79(x), Not(var85(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var67(x1)), var51(x1), var12(x1), Not(var54(x1)), var98(x1), var100(x1), var42(x1), Not(var69(x1)), Not(var25(x1))), Not(var52(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var81(x1), Not(var1(x1)), Not(var5(x1)), var68(x1), var52(x1), Not(var47(x1)), var13(x1), var43(x1)), Or(var72(x), var74(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var26(x1)), var95(x1), Not(var53(x1)), Not(var67(x1))), Or(var76(x), Not(var10(x)), var100(x), var60(x), var8(x), var85(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var67(x1)), var41(x1), Not(var49(x1)), var10(x1), var18(x1)), Or(var65(x), Not(var59(x)), var87(x), var90(x), Not(var22(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var34(x1), Not(var41(x1))), Or(var26(x), Not(var27(x)), Not(var48(x)), var10(x), Not(var84(x)), var53(x), var70(x), var58(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var42(x1)), Not(var16(x1))), Or(Not(var52(x)), var19(x), Not(var55(x)), Not(var93(x)), var9(x), var61(x), var29(x), var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var56(x1), var35(x1), var49(x1), var82(x1), var69(x1), Not(var6(x1)), Not(var67(x1))), Or(var61(x), Not(var40(x)), Not(var50(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var87(x1)), var96(x1), Not(var49(x1)), Not(var98(x1)), var85(x1), var39(x1), var72(x1), var22(x1)), Or(var56(x), Not(var66(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var42(x1)), var4(x1), var99(x1), Not(var93(x1)), Not(var43(x1))), Or(var26(x), Not(var7(x)), Not(var97(x)), var60(x), Not(var46(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var3(x1)), var45(x1), var4(x1), Not(var44(x1)), Not(var93(x1)), var53(x1), var75(x1)), Or(var18(x), var32(x), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var62(x1)), Or(var59(x), var98(x), var88(x), var1(x), Not(var72(x)), var46(x), Not(var19(x)), var38(x), var71(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var90(x1)), var30(x1)), Or(var9(x), var36(x), var37(x), Not(var38(x)), var51(x), Not(var29(x)), var3(x), Not(var63(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var91(x1)), var74(x1), var64(x1), var85(x1), Not(var8(x1)), var26(x1), var41(x1), var38(x1)), Or(var23(x), var56(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var64(x1), Not(var14(x1)), Not(var72(x1))), Or(Not(var57(x)), var36(x), var29(x), Not(var78(x)), Not(var90(x)), var97(x), Not(var37(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var75(x1), Not(var71(x1)), var23(x1), Not(var79(x1)), Not(var10(x1))), Or(var85(x), var87(x), Not(var86(x)), Not(var47(x)), Not(var3(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), var23(x1)), Or(var59(x), Not(var94(x)), var17(x), Not(var56(x)), Not(var82(x)), var15(x), Not(var21(x)), Not(var97(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var55(x1), var25(x1)), Or(Not(var37(x)), Not(var74(x)), Not(var45(x)), Not(var22(x)), var51(x), var96(x), var8(x), var52(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var86(x1), Or(Not(var73(x)), Not(var14(x)), var7(x), Not(var11(x)), Not(var82(x)), Not(var37(x)), Not(var76(x)), var78(x), Not(var90(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var38(x1), var31(x1), Not(var76(x1))), Or(Not(var86(x)), var21(x), Not(var23(x)), Not(var15(x)), var48(x), var5(x), var80(x)))))),
	ForAll([x], Not(Or(var92(x), var20(x), Not(var58(x)), Not(var57(x)), var56(x), Not(var51(x)), var47(x), Not(var74(x)), Not(var68(x)), Not(var81(x)), var86(x), Not(var84(x)), var87(x), var97(x), Not(var39(x)), var40(x), var35(x), var90(x), Not(var77(x)), Not(var60(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var23(x1), Not(var33(x1)), Not(var62(x1)), Not(var25(x1))), Or(Not(var35(x)), Not(var77(x)), var54(x), Not(var58(x)), Not(var75(x)), var34(x), Not(var66(x)), var32(x), Not(var74(x)), var44(x), Not(var94(x)), Not(var57(x)), Not(var12(x)), Not(var52(x)), Not(var48(x)), var84(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())