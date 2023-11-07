from z3 import *

Object = DeclareSort('Object')

var130 = Function('var130', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var130(x)), var70(x)))),
	ForAll([x], Not(Or(var2(x), Not(var187(x))))),
	ForAll([x], Not(Or(var38(x), var32(x)))),
	ForAll([x], Not(Or(var122(x), Not(var59(x))))),
	ForAll([x], Not(Or(Not(var24(x)), var72(x)))),
	ForAll([x], Not(Or(Not(var185(x)), Not(var44(x))))),
	ForAll([x], Not(Or(var80(x), Not(var3(x))))),
	ForAll([x], Not(Or(var13(x), Not(var82(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var231(x1), var87(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var36(x1), Not(var129(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var46(x1), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var176(x1)), Not(var12(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var16(x1)), var159(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var6(x1)), Not(var27(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var101(x1)), var139(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), var14(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var145(x1)), Not(var73(x)))))),
	ForAll([x], Not(Or(Not(var182(x)), Not(var116(x)), Not(var33(x))))),
	ForAll([x], Not(Or(var108(x), var5(x), var67(x)))),
	ForAll([x], Not(Or(var31(x), var8(x), Not(var54(x))))),
	ForAll([x], Not(Or(Not(var25(x)), var47(x), Not(var125(x))))),
	ForAll([x], Not(Or(Not(var71(x)), var4(x), Not(var53(x))))),
	ForAll([x], Not(Or(var52(x), Not(var55(x)), Not(var20(x))))),
	ForAll([x], Not(Or(Not(var69(x)), var35(x), var168(x)))),
	ForAll([x], Not(Or(Not(var163(x)), var57(x), var126(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), Or(Not(var208(x)), Not(var121(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var162(x1)), Not(var49(x1))), var248(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var29(x1)), Not(var91(x1))), var15(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var241(x1), Or(var219(x), Not(var23(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), Or(var229(x), Not(var115(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var58(x1), Not(var75(x1))), var95(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var64(x1)), Or(var179(x), var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var167(x1)), Or(Not(var131(x)), Not(var188(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var246(x1)), var45(x1)), Not(var66(x)))))),
	ForAll([x], Not(Or(var63(x), var137(x), var56(x), Not(var186(x))))),
	ForAll([x], Not(Or(var40(x), var81(x), var184(x), Not(var174(x))))),
	ForAll([x], Not(Or(var164(x), var61(x), Not(var76(x)), var157(x)))),
	ForAll([x], Not(Or(Not(var22(x)), Not(var113(x)), var217(x), var223(x)))),
	ForAll([x], Not(Or(var18(x), var194(x), var111(x), var240(x)))),
	ForAll([x], Not(Or(var34(x), var39(x), var65(x), Not(var21(x))))),
	ForAll([x], Not(Or(var155(x), var102(x), Not(var11(x)), Not(var41(x))))),
	ForAll([x], Not(Or(Not(var197(x)), Not(var244(x)), var243(x), var42(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var98(x1), var84(x1)), Or(var48(x), Not(var152(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var7(x1)), Or(var26(x), Not(var112(x)), Not(var51(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var242(x1)), var119(x1)), Or(Not(var128(x)), Not(var203(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var28(x1)), Or(Not(var142(x)), Not(var214(x)), var43(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var212(x1)), var109(x1)), Or(Not(var10(x)), Not(var62(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var1(x1), Not(var151(x1))), Or(var103(x), Not(var89(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var37(x1)), var19(x1), Not(var17(x1))), Not(var85(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var86(x1)), Or(Not(var9(x)), Not(var198(x)), var232(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
