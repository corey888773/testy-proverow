from z3 import *

Object = DeclareSort('Object')

var23 = Function('var23', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(var23(x))),
	ForAll([x], Not(var11(x))),
	ForAll([x], Not(Not(var18(x)))),
	ForAll([x], Not(var50(x))),
	ForAll([x], Not(var32(x))),
	ForAll([x], Not(Not(var1(x)))),
	ForAll([x], Not(Not(var7(x)))),
	ForAll([x], Not(var20(x))),
	ForAll([x], Not(var27(x))),
	Exists([x], Not(var5(x))),
	Exists([x], var44(x)),
	ForAll([x], Not(Or(var18(x), Not(var3(x))))),
	ForAll([x], Not(Or(var11(x), Not(var46(x))))),
	ForAll([x], Not(Or(var25(x), Not(var21(x))))),
	ForAll([x], Not(Or(var50(x), Not(var2(x))))),
	ForAll([x], Not(Or(Not(var40(x)), Not(var28(x))))),
	ForAll([x], Not(Or(var18(x), var31(x)))),
	ForAll([x], Not(Or(var9(x), Not(var35(x))))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var4(x))))),
	ForAll([x], Not(Or(var20(x), Not(var2(x))))),
	ForAll([x], Not(Or(var6(x), var7(x)))),
	ForAll([x], Not(Or(var23(x), var21(x)))),
	ForAll([x], Not(Or(Not(var17(x)), var40(x)))),
	ForAll([x], Not(Or(var28(x), Not(var19(x))))),
	ForAll([x], Not(Or(var3(x), Not(var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var15(x1)), Not(var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), Not(var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var4(x1), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var32(x1), var3(x))))),
	ForAll([x], Not(Or(var5(x), Not(var38(x)), Not(var41(x))))),
	ForAll([x], Not(Or(Not(var20(x)), var50(x), Not(var10(x))))),
	ForAll([x], Not(Or(var17(x), Not(var13(x)), Not(var31(x))))),
	ForAll([x], Not(Or(Not(var45(x)), Not(var2(x)), Not(var40(x))))),
	ForAll([x], Not(Or(var48(x), Not(var33(x)), var32(x)))),
	ForAll([x], Not(Or(Not(var19(x)), Not(var35(x)), var20(x)))),
	ForAll([x], Not(Or(var34(x), Not(var49(x)), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var48(x)), var3(x), var46(x)))),
	ForAll([x], Not(Or(Not(var45(x)), Not(var40(x)), Not(var41(x))))),
	ForAll([x], Not(Or(Not(var9(x)), Not(var18(x)), Not(var8(x))))),
	ForAll([x], Not(Or(var25(x), var9(x), Not(var15(x))))),
	ForAll([x], Not(Or(var29(x), var12(x), var47(x)))),
	ForAll([x], Not(Or(Not(var10(x)), Not(var2(x)), var43(x)))),
	ForAll([x], Not(Or(var16(x), Not(var35(x)), var8(x)))),
	ForAll([x], Not(Or(var42(x), Not(var47(x)), Not(var50(x))))),
	ForAll([x], Not(Or(Not(var41(x)), Not(var29(x)), Not(var17(x))))),
	ForAll([x], Not(Or(var28(x), Not(var35(x)), var12(x)))),
	ForAll([x], Not(Or(var32(x), Not(var7(x)), var46(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var16(x1)), Or(var12(x), Not(var31(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var10(x1)), Or(var7(x), var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var17(x1)), Not(var25(x1))), var10(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), Or(var40(x), var22(x)))))),
	ForAll([x], Not(Or(var24(x), var30(x), Not(var21(x)), var8(x)))),
	ForAll([x], Not(Or(var11(x), Not(var31(x)), Not(var6(x)), Not(var43(x))))),
	ForAll([x], Not(Or(Not(var22(x)), Not(var47(x)), var30(x), Not(var46(x))))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var41(x)), Not(var27(x)), Not(var34(x))))),
	ForAll([x], Not(Or(Not(var14(x)), Not(var35(x)), var28(x), Not(var3(x))))),
	ForAll([x], Not(Or(Not(var26(x)), var1(x), Not(var21(x)), var15(x)))),
	ForAll([x], Not(Or(Not(var8(x)), var49(x), var40(x), var12(x)))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var37(x)), Not(var30(x)), var44(x)))),
	ForAll([x], Not(Or(Not(var3(x)), Not(var17(x)), var47(x), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var20(x)), Not(var18(x)), Not(var14(x)), Not(var4(x))))),
	ForAll([x], Not(Or(var32(x), var47(x), var18(x), var31(x)))),
	ForAll([x], Not(Or(var20(x), Not(var1(x)), var38(x), var29(x)))),
	ForAll([x], Not(Or(var30(x), var40(x), var38(x), var48(x)))),
	ForAll([x], Not(Or(Not(var42(x)), Not(var16(x)), Not(var6(x)), var29(x)))),
	ForAll([x], Not(Or(var30(x), Not(var43(x)), var46(x), Not(var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var20(x1), Not(var6(x1))), Or(var28(x), var33(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var7(x1), var39(x1), Not(var11(x1))), Not(var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var32(x1), Not(var35(x1)), Not(var33(x1))), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var44(x1)), var36(x1), var22(x1)), Not(var25(x)))))),
	ForAll([x], Not(Or(var6(x), var14(x), var5(x), var8(x), Not(var49(x))))),
	ForAll([x], Not(Or(var46(x), var30(x), var10(x), Not(var7(x)), var17(x)))),
	ForAll([x], Not(Or(var35(x), Not(var23(x)), Not(var2(x)), var6(x), var36(x)))),
	ForAll([x], Not(Or(var1(x), Not(var43(x)), Not(var36(x)), Not(var40(x)), Not(var45(x))))),
	ForAll([x], Not(Or(var43(x), var30(x), Not(var7(x)), var22(x), var10(x)))),
	ForAll([x], Not(Or(Not(var47(x)), var8(x), var24(x), Not(var29(x)), Not(var23(x))))),
	ForAll([x], Not(Or(Not(var18(x)), var33(x), var41(x), Not(var3(x)), var16(x)))),
	ForAll([x], Not(Or(var41(x), var20(x), var24(x), var35(x), var9(x)))),
	ForAll([x], Not(Or(Not(var46(x)), var6(x), var12(x), var24(x), var10(x)))),
	ForAll([x], Not(Or(Not(var27(x)), var26(x), Not(var16(x)), var35(x), var40(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var25(x1)), Not(var16(x1))), Or(var38(x), Not(var5(x)), Not(var9(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var14(x1), Not(var5(x1)), Not(var26(x1))), Or(Not(var16(x)), var35(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var23(x1), var49(x1), Not(var7(x1)), Not(var28(x1))), Not(var15(x)))))),
	ForAll([x], Not(Or(var42(x), Not(var2(x)), Not(var37(x)), var38(x), var1(x), Not(var15(x))))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var43(x)), var44(x), var25(x), Not(var16(x)), var41(x)))),
	ForAll([x], Not(Or(Not(var13(x)), Not(var11(x)), Not(var48(x)), var17(x), var40(x), var25(x)))),
	ForAll([x], Not(Or(var34(x), var2(x), Not(var18(x)), Not(var5(x)), var19(x), Not(var38(x))))),
	ForAll([x], Not(Or(var2(x), var11(x), Not(var36(x)), var10(x), var31(x), var8(x)))),
	ForAll([x], Not(Or(Not(var26(x)), Not(var17(x)), Not(var1(x)), var3(x), Not(var20(x)), Not(var13(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var46(x1)), Or(var34(x), Not(var5(x)), var50(x), Not(var30(x)), Not(var3(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var44(x1), Or(var45(x), Not(var1(x)), var36(x), var10(x), Not(var48(x))))))),
	ForAll([x], Not(Or(Not(var7(x)), var11(x), Not(var10(x)), Not(var37(x)), var40(x), Not(var5(x)), var30(x)))),
	ForAll([x], Not(Or(var18(x), var11(x), var48(x), Not(var30(x)), var7(x), var6(x), var15(x)))),
	ForAll([x], Not(Or(Not(var46(x)), var30(x), Not(var36(x)), Not(var5(x)), var1(x), Not(var24(x)), Not(var19(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), Not(var25(x1)), Not(var11(x1))), Or(Not(var24(x)), Not(var34(x)), Not(var46(x)), Not(var45(x))))))),
	ForAll([x], Not(Or(var12(x), var25(x), Not(var40(x)), var34(x), Not(var33(x)), Not(var18(x)), var31(x), var28(x)))),
	ForAll([x], Not(Or(var1(x), var24(x), var28(x), Not(var12(x)), Not(var16(x)), Not(var3(x)), Not(var43(x)), var36(x)))),
	ForAll([x], Not(Or(var48(x), var10(x), Not(var8(x)), Not(var43(x)), var6(x), var21(x), Not(var2(x)), Not(var45(x)), var11(x)))),
	ForAll([x], Not(Or(Not(var33(x)), var18(x), Not(var37(x)), Not(var2(x)), Not(var40(x)), Not(var30(x)), Not(var43(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var11(x1), var32(x1), var35(x1)), var36(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
