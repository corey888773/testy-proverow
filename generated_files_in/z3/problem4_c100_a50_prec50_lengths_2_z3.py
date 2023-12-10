from z3 import *

Object = DeclareSort('Object')

var48 = Function('var48', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms0 = [
	ForAll([x], Not(Or(Not(var48(x)), var32(x)))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var42(x))))),
	ForAll([x], Not(Or(Not(var18(x)), Not(var38(x))))),
	ForAll([x], Not(Or(Not(var41(x)), Not(var13(x))))),
	ForAll([x], Not(Or(var7(x), var1(x)))),
	ForAll([x], Not(Or(var7(x), var38(x)))),
	ForAll([x], Not(Or(var20(x), var45(x)))),
	ForAll([x], Not(Or(Not(var21(x)), Not(var19(x))))),
	ForAll([x], Not(Or(Not(var32(x)), Not(var28(x))))),
	ForAll([x], Not(Or(Not(var3(x)), var38(x)))),
	ForAll([x], Not(Or(var43(x), Not(var12(x))))),
	ForAll([x], Not(Or(var44(x), Not(var17(x))))),
	ForAll([x], Not(Or(Not(var6(x)), var16(x)))),
	ForAll([x], Not(Or(var12(x), Not(var34(x))))),
	ForAll([x], Not(Or(var15(x), var2(x)))),
	ForAll([x], Not(Or(Not(var8(x)), var21(x)))),
	ForAll([x], Not(Or(Not(var24(x)), var4(x)))),
	ForAll([x], Not(Or(var1(x), Not(var34(x))))),
	ForAll([x], Not(Or(var15(x), Not(var29(x))))),
	ForAll([x], Not(Or(var24(x), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var27(x)), Not(var18(x))))),
	ForAll([x], Not(Or(Not(var44(x)), Not(var4(x))))),
	ForAll([x], Not(Or(Not(var15(x)), Not(var23(x))))),
	ForAll([x], Not(Or(var10(x), var48(x)))),
	ForAll([x], Not(Or(Not(var9(x)), Not(var28(x))))),
	ForAll([x], Not(Or(Not(var17(x)), var14(x)))),
	ForAll([x], Not(Or(var33(x), Not(var45(x))))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var18(x))))),
	ForAll([x], Not(Or(var9(x), var3(x)))),
	ForAll([x], Not(Or(Not(var5(x)), var49(x)))),
	ForAll([x], Not(Or(var25(x), var39(x)))),
	ForAll([x], Not(Or(var41(x), var8(x)))),
	ForAll([x], Not(Or(var26(x), Not(var34(x))))),
	ForAll([x], Not(Or(var1(x), var37(x)))),
	ForAll([x], Not(Or(var28(x), var15(x)))),
	ForAll([x], Not(Or(var1(x), Not(var22(x))))),
	ForAll([x], Not(Or(var2(x), var41(x)))),
	ForAll([x], Not(Or(var9(x), Not(var36(x))))),
	ForAll([x], Not(Or(var36(x), var2(x)))),
	ForAll([x], Not(Or(Not(var35(x)), var15(x)))),
	ForAll([x], Not(Or(var23(x), Not(var24(x))))),
	ForAll([x], Not(Or(Not(var46(x)), var36(x)))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var22(x))))),
	ForAll([x], Not(Or(var14(x), Not(var39(x))))),
	ForAll([x], Not(Or(Not(var40(x)), Not(var45(x))))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var1(x))))),
	ForAll([x], Not(Or(var42(x), Not(var26(x))))),
	ForAll([x], Not(Or(Not(var32(x)), Not(var25(x))))),
	ForAll([x], Not(Or(var33(x), var19(x)))),
	ForAll([x], Not(Or(var47(x), Not(var15(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), Not(var18(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var37(x1)), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Not(var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var30(x1), Not(var41(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), Not(var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var25(x1), Not(var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var27(x1)), var3(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var33(x1), Not(var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var28(x1), var7(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), Not(var40(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var11(x1), Not(var10(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var12(x1)), var19(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var30(x1), Not(var12(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var25(x1), Not(var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var17(x1), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var33(x1), Not(var26(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), var46(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var39(x1)), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var8(x1), Not(var28(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var39(x1)), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var27(x1)), Not(var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var24(x1)), Not(var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var16(x1)), Not(var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var22(x1)), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), Not(var46(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), Not(var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), var19(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var45(x1), var38(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var9(x1)), Not(var41(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var15(x1)), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var37(x1)), Not(var15(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), Not(var15(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var20(x1), var5(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var14(x1), var5(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var11(x1)), var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var20(x1), Not(var26(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var6(x1)), var43(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var34(x1)), var1(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), Not(var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), Not(var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var6(x1)), Not(var41(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var46(x1)), var31(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var22(x1)), Not(var49(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var43(x1), Not(var32(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var41(x1)), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var41(x1), var9(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms0)
print(s.check())
print(s.statistics())
