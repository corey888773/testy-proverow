from z3 import *

Object = DeclareSort('Object')

var10 = Function('var10', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms0 = [
	ForAll([x], Not(var10(x))),
	ForAll([x], Not(Not(var48(x)))),
	ForAll([x], Not(Not(var6(x)))),
	ForAll([x], Not(Not(var6(x)))),
	ForAll([x], Not(Not(var30(x)))),
	ForAll([x], Not(Not(var31(x)))),
	ForAll([x], Not(Not(var44(x)))),
	ForAll([x], Not(Not(var33(x)))),
	ForAll([x], Not(Not(var44(x)))),
	ForAll([x], Not(var10(x))),
	ForAll([x], Not(var20(x))),
	ForAll([x], Not(Not(var13(x)))),
	Exists([x], var50(x)),
	Exists([x], Not(var9(x))),
	Exists([x], var18(x)),
	Exists([x], Not(var24(x))),
	Exists([x], var3(x)),
	Exists([x], var2(x)),
	Exists([x], Not(var1(x))),
	Exists([x], Not(var44(x))),
	Exists([x], Not(var21(x))),
	Exists([x], Not(var20(x))),
	Exists([x], Not(var2(x))),
	Exists([x], var3(x)),
	Exists([x], var5(x)),
	ForAll([x], Not(Or(Not(var6(x)), var49(x), var18(x), var28(x), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var10(x)), Not(var23(x)), Not(var46(x)), Not(var7(x)), var26(x)))),
	ForAll([x], Not(Or(Not(var13(x)), Not(var14(x)), Not(var1(x)), Not(var25(x)), Not(var30(x))))),
	ForAll([x], Not(Or(var43(x), var20(x), Not(var28(x)), var31(x), Not(var36(x))))),
	ForAll([x], Not(Or(var49(x), Not(var5(x)), Not(var37(x)), var10(x), Not(var18(x))))),
	ForAll([x], Not(Or(Not(var14(x)), var26(x), var50(x), Not(var25(x)), Not(var33(x))))),
	ForAll([x], Not(Or(var40(x), var28(x), Not(var6(x)), var16(x), var37(x)))),
	ForAll([x], Not(Or(Not(var9(x)), Not(var6(x)), Not(var49(x)), var4(x), var31(x)))),
	ForAll([x], Not(Or(Not(var10(x)), var19(x), Not(var28(x)), var44(x), var29(x)))),
	ForAll([x], Not(Or(var40(x), var13(x), Not(var37(x)), var30(x), var28(x)))),
	ForAll([x], Not(Or(Not(var32(x)), Not(var7(x)), Not(var18(x)), Not(var22(x)), var5(x)))),
	ForAll([x], Not(Or(var46(x), var38(x), var41(x), var34(x), Not(var35(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), Or(var9(x), var13(x), var28(x), var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var26(x1), var44(x1)), Or(var24(x), var47(x), Not(var12(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var42(x1), Not(var37(x1))), Or(var39(x), Not(var7(x)), Not(var24(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var35(x1), Not(var41(x1)), var14(x1), Not(var49(x1))), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var42(x1)), var26(x1)), Or(Not(var18(x)), Not(var36(x)), Not(var39(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var14(x1)), Not(var23(x1)), Not(var41(x1))), Or(Not(var36(x)), var6(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var8(x1)), Not(var25(x1))), Or(var9(x), var32(x), var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var22(x1)), Not(var10(x1)), var21(x1), var48(x1)), Not(var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var49(x1)), var24(x1)), Or(Not(var46(x)), var33(x), var43(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), Or(var44(x), var26(x), Not(var48(x)), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var1(x1), Not(var19(x1)), Not(var15(x1))), Or(Not(var49(x)), Not(var27(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var11(x1), Not(var4(x1))), Or(Not(var44(x)), var37(x), var47(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var27(x1), Not(var11(x1)), Not(var24(x1))), Or(var31(x), var18(x)))))),
	ForAll([x], Not(Or(var48(x), var5(x), Not(var30(x)), Not(var26(x)), var45(x), var4(x), Not(var11(x)), var20(x), var32(x), var31(x)))),
	ForAll([x], Not(Or(Not(var4(x)), var24(x), var33(x), Not(var18(x)), Not(var41(x)), Not(var37(x)), Not(var48(x)), Not(var1(x)), Not(var2(x)), Not(var27(x))))),
	ForAll([x], Not(Or(var1(x), var27(x), Not(var22(x)), var46(x), Not(var12(x)), var23(x), Not(var25(x)), Not(var32(x)), var50(x), Not(var31(x))))),
	ForAll([x], Not(Or(Not(var24(x)), var14(x), var25(x), var16(x), Not(var4(x)), Not(var48(x)), var15(x), var45(x), Not(var36(x)), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var48(x)), Not(var12(x)), var43(x), Not(var26(x)), Not(var8(x)), Not(var49(x)), var41(x), Not(var24(x)), var6(x)))),
	ForAll([x], Not(Or(Not(var43(x)), Not(var6(x)), Not(var20(x)), Not(var9(x)), Not(var38(x)), Not(var39(x)), var22(x), var35(x), Not(var44(x)), var33(x)))),
	ForAll([x], Not(Or(Not(var2(x)), Not(var42(x)), Not(var31(x)), var48(x), Not(var20(x)), var34(x), Not(var5(x)), var16(x), Not(var27(x)), var29(x)))),
	ForAll([x], Not(Or(var9(x), var23(x), Not(var33(x)), var12(x), var4(x), Not(var10(x)), Not(var43(x)), Not(var22(x)), Not(var16(x)), Not(var35(x))))),
	ForAll([x], Not(Or(var21(x), var7(x), var27(x), Not(var2(x)), Not(var12(x)), var47(x), Not(var40(x)), Not(var3(x)), Not(var11(x)), var44(x)))),
	ForAll([x], Not(Or(var6(x), Not(var23(x)), var21(x), var39(x), var11(x), Not(var47(x)), Not(var2(x)), var33(x), var24(x), Not(var17(x))))),
	ForAll([x], Not(Or(Not(var20(x)), Not(var45(x)), var7(x), Not(var21(x)), Not(var35(x)), Not(var50(x)), var2(x), var13(x), var26(x), Not(var5(x))))),
	ForAll([x], Not(Or(var41(x), Not(var7(x)), var39(x), var47(x), var11(x), var6(x), var20(x), Not(var8(x)), var19(x), var32(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var22(x1), Not(var5(x1)), Not(var12(x1)), Not(var6(x1)), Not(var26(x1)), var37(x1), Not(var16(x1)), Not(var27(x1))), Or(var40(x), var36(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var13(x1)), var34(x1), var3(x1), Not(var41(x1)), var47(x1), var24(x1)), Or(Not(var23(x)), Not(var8(x)), var6(x), Not(var15(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var23(x1), Not(var22(x1)), Not(var20(x1)), Not(var18(x1)), Not(var43(x1)), var8(x1)), Or(Not(var13(x)), var15(x), Not(var33(x)), Not(var3(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var48(x1), Not(var24(x1)), Not(var2(x1)), var30(x1), Not(var4(x1)), Not(var45(x1)), var15(x1)), Or(Not(var43(x)), var20(x), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var47(x1)), Not(var46(x1))), Or(var32(x), var49(x), var12(x), var6(x), var13(x), var48(x), var34(x), var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var24(x1), var11(x1)), Or(Not(var7(x)), var2(x), var36(x), var46(x), var40(x), var33(x), Not(var8(x)), var12(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var30(x1)), Not(var27(x1)), var33(x1), Not(var8(x1)), Not(var36(x1))), Or(Not(var49(x)), var38(x), Not(var44(x)), var43(x), var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var5(x1), Not(var24(x1)), var44(x1), var17(x1), Not(var33(x1)), Not(var37(x1)), var20(x1), Not(var9(x1)), var26(x1)), var36(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var10(x1), Or(var4(x), Not(var37(x)), var24(x), Not(var19(x)), var25(x), var45(x), var31(x), Not(var8(x)), var38(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var12(x1), var14(x1), Not(var18(x1)), var29(x1)), Or(var8(x), var31(x), var44(x), Not(var3(x)), Not(var49(x)), var32(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Or(var49(x), var10(x), Not(var45(x)), Not(var46(x)), Not(var33(x)), Not(var40(x)), var5(x), var1(x), var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var17(x1)), Not(var29(x1)), var30(x1), var45(x1)), Or(Not(var19(x)), Not(var50(x)), Not(var14(x)), var20(x), Not(var3(x)), Not(var11(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var16(x1)), var48(x1), var35(x1), Not(var9(x1)), Not(var50(x1)), var19(x1), var10(x1), Not(var34(x1)), var23(x1)), Not(var3(x)))))),
	ForAll([x], Not(Or(var16(x), Not(var12(x)), Not(var28(x)), Not(var1(x)), Not(var31(x)), var17(x), var38(x), var27(x), Not(var2(x)), var45(x), Not(var20(x)), var50(x), Not(var22(x)), Not(var11(x)), Not(var5(x)), Not(var41(x)), Not(var46(x)), Not(var37(x)), var40(x), Not(var9(x))))),
	ForAll([x], Not(Or(Not(var44(x)), Not(var31(x)), Not(var24(x)), Not(var17(x)), Not(var2(x)), Not(var12(x)), Not(var47(x)), Not(var29(x)), var32(x), var18(x), var39(x), var4(x), var5(x), var41(x), var6(x), var37(x), var25(x), Not(var49(x)), Not(var45(x)), Not(var16(x))))),
	ForAll([x], Not(Or(var18(x), Not(var3(x)), Not(var25(x)), Not(var24(x)), Not(var42(x)), var23(x), var34(x), var15(x), var8(x), Not(var32(x)), var27(x), var21(x), Not(var11(x)), Not(var9(x)), Not(var5(x)), var48(x), Not(var28(x)), var36(x), Not(var19(x)), Not(var49(x))))),
	ForAll([x], Not(Or(var1(x), var5(x), Not(var35(x)), Not(var25(x)), var44(x), Not(var38(x)), Not(var22(x)), Not(var10(x)), var49(x), var7(x), Not(var37(x)), Not(var39(x)), var9(x), var50(x), Not(var48(x)), var13(x), Not(var24(x)), var41(x), Not(var18(x)), Not(var31(x))))),
	ForAll([x], Not(Or(var36(x), Not(var42(x)), Not(var8(x)), var15(x), var1(x), Not(var41(x)), var35(x), var7(x), var12(x), Not(var26(x)), Not(var33(x)), Not(var39(x)), var14(x), var50(x), Not(var24(x)), var4(x), Not(var25(x)), Not(var6(x)), Not(var30(x)), var29(x)))),
	ForAll([x], Not(Or(Not(var1(x)), Not(var15(x)), Not(var39(x)), var2(x), Not(var45(x)), var21(x), var46(x), Not(var13(x)), Not(var18(x)), Not(var9(x)), var4(x), var25(x), var47(x), Not(var19(x)), Not(var7(x)), var24(x), Not(var22(x)), Not(var26(x)), Not(var35(x)), Not(var42(x))))),
	ForAll([x], Not(Or(var27(x), Not(var50(x)), var36(x), Not(var11(x)), var13(x), var28(x), Not(var25(x)), Not(var45(x)), Not(var41(x)), Not(var4(x)), var49(x), Not(var24(x)), Not(var6(x)), var14(x), var12(x), Not(var18(x)), Not(var23(x)), var3(x), Not(var34(x)), var31(x)))),
	ForAll([x], Not(Or(Not(var5(x)), Not(var27(x)), var30(x), var2(x), Not(var38(x)), var4(x), Not(var13(x)), Not(var42(x)), var24(x), var46(x), var12(x), Not(var39(x)), var14(x), var28(x), var3(x), Not(var43(x)), var1(x), Not(var36(x)), Not(var32(x)), Not(var6(x))))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var23(x)), Not(var44(x)), Not(var35(x)), Not(var6(x)), Not(var17(x)), var42(x), var8(x), var5(x), var12(x), Not(var7(x)), Not(var49(x)), var2(x), var20(x), Not(var27(x)), var18(x), Not(var19(x)), var15(x), var33(x), var9(x)))),
	ForAll([x], Not(Or(Not(var2(x)), Not(var40(x)), Not(var17(x)), Not(var20(x)), Not(var22(x)), var49(x), Not(var42(x)), Not(var9(x)), Not(var13(x)), var33(x), Not(var35(x)), var38(x), var4(x), var44(x), var24(x), var27(x), Not(var18(x)), Not(var32(x)), Not(var3(x)), var30(x)))),
	ForAll([x], Not(Or(var38(x), var35(x), var33(x), var9(x), var19(x), Not(var49(x)), Not(var11(x)), Not(var20(x)), Not(var44(x)), var34(x), Not(var29(x)), Not(var45(x)), Not(var15(x)), var16(x), var31(x), var18(x), Not(var12(x)), Not(var36(x)), var41(x), var2(x)))),
	ForAll([x], Not(Or(Not(var41(x)), var20(x), Not(var6(x)), Not(var14(x)), var39(x), Not(var7(x)), Not(var37(x)), Not(var2(x)), Not(var40(x)), var22(x), Not(var12(x)), Not(var21(x)), var18(x), var16(x), Not(var8(x)), var1(x), Not(var33(x)), Not(var43(x)), Not(var17(x)), var27(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var46(x1), Not(var34(x1)), Not(var13(x1))), Or(var28(x), Not(var20(x)), var32(x), var41(x), Not(var18(x)), var12(x), var50(x), var10(x), var21(x), var24(x), Not(var49(x)), Not(var14(x)), Not(var27(x)), var4(x), var6(x), var2(x), var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var19(x1), var40(x1), var39(x1), Not(var36(x1)), var16(x1), var41(x1), Not(var43(x1)), Not(var48(x1)), Not(var50(x1))), Or(Not(var47(x)), var7(x), Not(var29(x)), Not(var11(x)), Not(var5(x)), Not(var30(x)), var31(x), var46(x), Not(var25(x)), var10(x), var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var12(x1)), Not(var31(x1)), Not(var1(x1)), Not(var35(x1))), Or(Not(var47(x)), var50(x), Not(var36(x)), Not(var27(x)), Not(var24(x)), Not(var7(x)), var17(x), var43(x), var18(x), Not(var20(x)), Not(var2(x)), Not(var44(x)), Not(var5(x)), var8(x), Not(var26(x)), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var39(x1)), Not(var23(x1)), Not(var40(x1)), Not(var9(x1)), Not(var11(x1)), Not(var37(x1)), var27(x1), Not(var10(x1)), var44(x1), Not(var33(x1)), Not(var50(x1)), Not(var13(x1)), var41(x1)), Or(var4(x), Not(var24(x)), Not(var19(x)), Not(var30(x)), var18(x), Not(var5(x)), Not(var25(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var43(x1)), Not(var12(x1)), var7(x1), Not(var2(x1)), Not(var17(x1)), Not(var14(x1))), Or(Not(var28(x)), var40(x), Not(var3(x)), var49(x), Not(var15(x)), var6(x), var8(x), Not(var45(x)), var35(x), var48(x), Not(var19(x)), Not(var9(x)), Not(var26(x)), var4(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var45(x1)), Not(var12(x1)), Not(var17(x1)), var6(x1), var43(x1), Not(var38(x1)), Not(var47(x1)), Not(var41(x1)), Not(var3(x1)), Not(var10(x1)), Not(var19(x1)), Not(var30(x1)), Not(var50(x1)), var14(x1)), Or(var28(x), var16(x), var48(x), var24(x), Not(var20(x)), Not(var37(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var28(x1)), var36(x1), var26(x1), Not(var39(x1)), Not(var40(x1)), Not(var31(x1)), var48(x1), var3(x1), var4(x1)), Or(Not(var23(x)), var27(x), Not(var16(x)), var1(x), var29(x), var15(x), var8(x), Not(var41(x)), Not(var6(x)), var33(x), var42(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var22(x1), Not(var25(x1)), var16(x1), var2(x1), var34(x1), Not(var35(x1))), Or(Not(var30(x)), Not(var39(x)), Not(var32(x)), var12(x), Not(var8(x)), var19(x), var27(x), Not(var18(x)), var45(x), var41(x), Not(var24(x)), Not(var42(x)), var48(x), Not(var47(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var38(x1), Not(var2(x1)), var10(x1), Not(var30(x1)), var5(x1), var21(x1), var36(x1), var31(x1), var13(x1), var18(x1), Not(var39(x1)), var12(x1), var33(x1), var37(x1), Not(var34(x1))), Or(var32(x), var47(x), Not(var20(x)), Not(var16(x)), var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var31(x1)), var1(x1), Not(var40(x1)), Not(var45(x1)), var39(x1), var28(x1), Not(var5(x1)), var9(x1), var34(x1), Not(var48(x1)), var49(x1), Not(var19(x1))), Or(var29(x), Not(var36(x)), var47(x), var41(x), var21(x), Not(var33(x)), var12(x), var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var20(x1)), var21(x1), var48(x1), var50(x1), var43(x1), var22(x1), Not(var31(x1)), var37(x1), Not(var12(x1)), Not(var1(x1)), Not(var7(x1)), var13(x1)), Or(var45(x), var33(x), Not(var42(x)), Not(var46(x)), var16(x), var3(x), Not(var5(x)), var6(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var2(x1), Not(var23(x1)), var9(x1), Not(var24(x1)), Not(var43(x1)), Not(var28(x1)), Not(var3(x1)), var35(x1), var5(x1), Not(var19(x1)), Not(var44(x1)), var16(x1), Not(var18(x1)), var47(x1), Not(var29(x1)), Not(var32(x1)), Not(var49(x1))), Or(var6(x), var31(x), var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var9(x1), Not(var26(x1)), Not(var46(x1)), var50(x1), var2(x1), var20(x1), var36(x1), var15(x1), Not(var12(x1)), Not(var4(x1)), var43(x1), var13(x1), var28(x1), var14(x1), Not(var34(x1)), var22(x1), Not(var23(x1)), var33(x1), var24(x1)), Not(var5(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms0)
print(s.check())
print(s.statistics())
