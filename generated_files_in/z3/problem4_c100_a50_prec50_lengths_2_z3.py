from z3 import *

Object = DeclareSort('Object')

var12 = Function('var12', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var12(x), Not(var37(x))))),
	ForAll([x], Not(Or(Not(var50(x)), Not(var30(x))))),
	ForAll([x], Not(Or(Not(var50(x)), Not(var4(x))))),
	ForAll([x], Not(Or(var15(x), var23(x)))),
	ForAll([x], Not(Or(Not(var34(x)), Not(var2(x))))),
	ForAll([x], Not(Or(Not(var12(x)), Not(var50(x))))),
	ForAll([x], Not(Or(var36(x), var18(x)))),
	ForAll([x], Not(Or(Not(var3(x)), Not(var31(x))))),
	ForAll([x], Not(Or(Not(var31(x)), var7(x)))),
	ForAll([x], Not(Or(Not(var45(x)), Not(var13(x))))),
	ForAll([x], Not(Or(Not(var41(x)), Not(var12(x))))),
	ForAll([x], Not(Or(var36(x), var44(x)))),
	ForAll([x], Not(Or(Not(var46(x)), Not(var8(x))))),
	ForAll([x], Not(Or(var44(x), var28(x)))),
	ForAll([x], Not(Or(var37(x), var6(x)))),
	ForAll([x], Not(Or(var7(x), var22(x)))),
	ForAll([x], Not(Or(var9(x), Not(var21(x))))),
	ForAll([x], Not(Or(Not(var2(x)), Not(var40(x))))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var2(x))))),
	ForAll([x], Not(Or(var50(x), var6(x)))),
	ForAll([x], Not(Or(var18(x), var40(x)))),
	ForAll([x], Not(Or(Not(var43(x)), var46(x)))),
	ForAll([x], Not(Or(var7(x), var41(x)))),
	ForAll([x], Not(Or(var44(x), var7(x)))),
	ForAll([x], Not(Or(Not(var48(x)), var50(x)))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var14(x))))),
	ForAll([x], Not(Or(var39(x), var22(x)))),
	ForAll([x], Not(Or(var31(x), var20(x)))),
	ForAll([x], Not(Or(var42(x), var21(x)))),
	ForAll([x], Not(Or(Not(var27(x)), var6(x)))),
	ForAll([x], Not(Or(Not(var48(x)), var25(x)))),
	ForAll([x], Not(Or(Not(var27(x)), Not(var32(x))))),
	ForAll([x], Not(Or(Not(var49(x)), Not(var26(x))))),
	ForAll([x], Not(Or(Not(var41(x)), Not(var11(x))))),
	ForAll([x], Not(Or(var38(x), Not(var12(x))))),
	ForAll([x], Not(Or(Not(var43(x)), var5(x)))),
	ForAll([x], Not(Or(Not(var17(x)), var27(x)))),
	ForAll([x], Not(Or(var40(x), var24(x)))),
	ForAll([x], Not(Or(var21(x), var8(x)))),
	ForAll([x], Not(Or(Not(var11(x)), var48(x)))),
	ForAll([x], Not(Or(Not(var29(x)), var19(x)))),
	ForAll([x], Not(Or(var44(x), var19(x)))),
	ForAll([x], Not(Or(var30(x), Not(var1(x))))),
	ForAll([x], Not(Or(var19(x), var3(x)))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var18(x))))),
	ForAll([x], Not(Or(var26(x), Not(var15(x))))),
	ForAll([x], Not(Or(var45(x), var16(x)))),
	ForAll([x], Not(Or(Not(var7(x)), Not(var13(x))))),
	ForAll([x], Not(Or(Not(var17(x)), var45(x)))),
	ForAll([x], Not(Or(var33(x), Not(var16(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), var18(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), var46(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var32(x1), var1(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), var6(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var6(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var49(x1)), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var27(x1)), Not(var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var4(x1), var43(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), var40(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), var20(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var39(x1)), var30(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), var34(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var23(x1)), Not(var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var23(x1), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var11(x1), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var2(x1)), Not(var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var33(x1), var40(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var1(x1)), Not(var27(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), var3(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var33(x1)), var4(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var10(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), Not(var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var40(x1)), var31(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), var22(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), var19(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), Not(var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var5(x1), Not(var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var19(x1)), Not(var33(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var48(x1)), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var12(x1)), var25(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var47(x1)), Not(var41(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var39(x1)), Not(var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var11(x1)), var40(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var35(x1)), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var45(x1), Not(var48(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var37(x1)), Not(var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var42(x1)), var10(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var5(x1)), var38(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var5(x1)), Not(var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var35(x1), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var8(x1), Not(var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var41(x1)), Not(var17(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var39(x1), Not(var28(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var19(x1), Not(var42(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), var42(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
