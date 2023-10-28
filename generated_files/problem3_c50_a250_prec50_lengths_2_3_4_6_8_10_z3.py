from z3 import *

Object = DeclareSort('Object')

var7 = Function('var7', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var7(x)), Not(var33(x))))),
	ForAll([x], Not(Or(Not(var36(x)), var162(x)))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var210(x))))),
	ForAll([x], Not(Or(var108(x), var147(x)))),
	ForAll([x], Not(Or(Not(var64(x)), var40(x)))),
	ForAll([x], Not(Or(Not(var45(x)), var10(x)))),
	ForAll([x], Not(Or(Not(var148(x)), Not(var60(x))))),
	ForAll([x], Not(Or(var18(x), Not(var5(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var219(x1)), Not(var243(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var51(x1)), Not(var153(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var160(x1), var92(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var88(x1)), Not(var80(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var28(x1), Not(var42(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var132(x1), var231(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var29(x1), var102(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var73(x1)), Not(var35(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var38(x1), Not(var27(x)))))),
	ForAll([x], Not(Or(Not(var128(x)), var49(x), var57(x)))),
	ForAll([x], Not(Or(var197(x), Not(var19(x)), var228(x)))),
	ForAll([x], Not(Or(Not(var34(x)), Not(var9(x)), Not(var90(x))))),
	ForAll([x], Not(Or(var8(x), Not(var16(x)), Not(var249(x))))),
	ForAll([x], Not(Or(var37(x), var6(x), Not(var119(x))))),
	ForAll([x], Not(Or(Not(var152(x)), Not(var58(x)), Not(var56(x))))),
	ForAll([x], Not(Or(var39(x), var26(x), var158(x)))),
	ForAll([x], Not(Or(Not(var25(x)), Not(var121(x)), var178(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), Or(var182(x), Not(var214(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var12(x1), Not(var23(x1))), var134(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var59(x1), Or(Not(var190(x)), Not(var217(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var220(x1)), Or(var55(x), var114(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var111(x1)), Not(var76(x1))), var4(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var167(x1)), Or(var1(x), Not(var117(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var89(x1), Or(Not(var47(x)), var125(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var181(x1), Or(var198(x), Not(var15(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var94(x1)), Not(var107(x1))), var46(x))))),
	ForAll([x], Not(Or(Not(var62(x)), Not(var20(x)), var157(x), Not(var78(x))))),
	ForAll([x], Not(Or(var54(x), Not(var14(x)), Not(var186(x)), Not(var196(x))))),
	ForAll([x], Not(Or(Not(var159(x)), Not(var184(x)), var194(x), var84(x)))),
	ForAll([x], Not(Or(Not(var72(x)), Not(var44(x)), var93(x), var173(x)))),
	ForAll([x], Not(Or(var238(x), var139(x), var154(x), var112(x)))),
	ForAll([x], Not(Or(var22(x), Not(var200(x)), Not(var11(x)), Not(var63(x))))),
	ForAll([x], Not(Or(var179(x), var53(x), var87(x), var21(x)))),
	ForAll([x], Not(Or(Not(var145(x)), Not(var241(x)), Not(var216(x)), var77(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var237(x1), Or(Not(var206(x)), Not(var116(x)), Not(var109(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var43(x1), Not(var17(x1)), Not(var85(x1))), var31(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var244(x1), Not(var61(x1))), Or(Not(var91(x)), Not(var2(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var185(x1)), Not(var172(x1))), Or(Not(var136(x)), Not(var138(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var41(x1)), Or(var50(x), Not(var3(x)), var240(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var52(x1), var150(x1), Not(var24(x1))), Not(var247(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var146(x1), Or(Not(var32(x)), var13(x), var168(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var204(x1), Not(var235(x1))), Or(Not(var187(x)), Not(var71(x)))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
