from z3 import *

Object = DeclareSort('Object')

var71 = Function('var71', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var71(x)), Not(var39(x))))),
	ForAll([x], Not(Or(var59(x), Not(var190(x))))),
	ForAll([x], Not(Or(var17(x), var65(x)))),
	ForAll([x], Not(Or(var134(x), Not(var30(x))))),
	ForAll([x], Not(Or(var68(x), var141(x)))),
	ForAll([x], Not(Or(var8(x), Not(var35(x))))),
	ForAll([x], Not(Or(Not(var50(x)), var119(x)))),
	ForAll([x], Not(Or(var57(x), var9(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var77(x1), Not(var54(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var164(x1)), Not(var6(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var105(x1)), var85(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var176(x1), var28(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var178(x1)), Not(var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var26(x1)), Not(var56(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var20(x1), var32(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var12(x1), Not(var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var75(x)))))),
	ForAll([x], Not(Or(Not(var179(x)), Not(var47(x)), var99(x)))),
	ForAll([x], Not(Or(var67(x), var44(x), Not(var125(x))))),
	ForAll([x], Not(Or(var64(x), Not(var158(x)), Not(var19(x))))),
	ForAll([x], Not(Or(Not(var149(x)), var18(x), Not(var15(x))))),
	ForAll([x], Not(Or(var70(x), Not(var84(x)), Not(var41(x))))),
	ForAll([x], Not(Or(Not(var33(x)), var38(x), Not(var76(x))))),
	ForAll([x], Not(Or(var199(x), var90(x), var152(x)))),
	ForAll([x], Not(Or(var148(x), var60(x), Not(var3(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var72(x1), Not(var88(x1))), var43(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var1(x1)), Or(Not(var160(x)), Not(var144(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), Or(Not(var80(x)), Not(var182(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var46(x1), Or(var66(x), var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var138(x1)), var104(x1)), Not(var36(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var69(x1), Or(var51(x), Not(var55(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var196(x1)), Not(var170(x1))), Not(var180(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var187(x1)), Not(var102(x1))), var106(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var42(x1)), var86(x1)), Not(var136(x)))))),
	ForAll([x], Not(Or(var61(x), Not(var52(x)), Not(var7(x)), Not(var40(x))))),
	ForAll([x], Not(Or(Not(var11(x)), var5(x), Not(var4(x)), Not(var94(x))))),
	ForAll([x], Not(Or(var27(x), var22(x), Not(var45(x)), Not(var87(x))))),
	ForAll([x], Not(Or(Not(var83(x)), var169(x), var128(x), Not(var197(x))))),
	ForAll([x], Not(Or(Not(var91(x)), var23(x), Not(var82(x)), Not(var2(x))))),
	ForAll([x], Not(Or(Not(var111(x)), var14(x), Not(var62(x)), var121(x)))),
	ForAll([x], Not(Or(var122(x), Not(var34(x)), var183(x), Not(var48(x))))),
	ForAll([x], Not(Or(var89(x), var200(x), var143(x), var58(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var109(x1)), Or(Not(var166(x)), Not(var53(x)), Not(var79(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var74(x1)), Or(var92(x), Not(var49(x)), Not(var29(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var184(x1)), Or(Not(var78(x)), var24(x), var140(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var13(x1), Not(var186(x1)), var73(x1)), Not(var115(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var10(x1)), Or(var168(x), Not(var154(x)), var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var97(x1)), var108(x1)), Or(Not(var127(x)), Not(var124(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var81(x1)), Not(var142(x1)), Not(var133(x1))), var171(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var198(x1), var177(x1), Not(var63(x1))), Not(var153(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
