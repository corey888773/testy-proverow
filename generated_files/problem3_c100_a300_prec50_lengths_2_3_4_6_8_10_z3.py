from z3 import *

Object = DeclareSort('Object')

var91 = Function('var91', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var91(x)), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var4(x)), Not(var13(x))))),
	ForAll([x], Not(Or(var73(x), var86(x)))),
	ForAll([x], Not(Or(Not(var163(x)), var85(x)))),
	ForAll([x], Not(Or(var205(x), Not(var2(x))))),
	ForAll([x], Not(Or(var200(x), var78(x)))),
	ForAll([x], Not(Or(var265(x), var168(x)))),
	ForAll([x], Not(Or(Not(var96(x)), var60(x)))),
	ForAll([x], Not(Or(var132(x), Not(var31(x))))),
	ForAll([x], Not(Or(var275(x), var35(x)))),
	ForAll([x], Not(Or(Not(var68(x)), var52(x)))),
	ForAll([x], Not(Or(var148(x), var161(x)))),
	ForAll([x], Not(Or(Not(var115(x)), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var207(x)), Not(var36(x))))),
	ForAll([x], Not(Or(var177(x), Not(var216(x))))),
	ForAll([x], Not(Or(Not(var169(x)), Not(var14(x))))),
	ForAll([x], Not(Or(Not(var234(x)), Not(var249(x))))),
	ForAll([x], Not(Or(var137(x), var61(x)))),
	ForAll([x], Not(Or(var26(x), Not(var185(x))))),
	ForAll([x], Not(Or(Not(var39(x)), var261(x)))),
	ForAll([x], Not(Or(var55(x), var175(x)))),
	ForAll([x], Not(Or(var204(x), Not(var294(x))))),
	ForAll([x], Not(Or(var125(x), Not(var202(x))))),
	ForAll([x], Not(Or(Not(var77(x)), Not(var80(x))))),
	ForAll([x], Not(Or(Not(var192(x)), var179(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var6(x1)), Not(var51(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var180(x1), var130(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var75(x1)), Not(var100(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var139(x1)), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var135(x1)), Not(var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var38(x1)), var40(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var17(x1), Not(var154(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var232(x1), Not(var15(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var141(x1)), var164(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var158(x1), Not(var193(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var165(x1)), Not(var129(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var19(x1)), Not(var58(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var20(x1), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var106(x1), var82(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var155(x1), Not(var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var37(x1), var199(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var5(x1), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), var145(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var133(x1)), Not(var242(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var43(x1)), var94(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var248(x1)), Not(var33(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var257(x1)), Not(var65(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var166(x1)), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var118(x1), Not(var70(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var41(x1), Not(var268(x)))))),
	ForAll([x], Not(Or(var29(x), var98(x), var167(x)))),
	ForAll([x], Not(Or(Not(var290(x)), var143(x), Not(var49(x))))),
	ForAll([x], Not(Or(Not(var231(x)), Not(var66(x)), var195(x)))),
	ForAll([x], Not(Or(var79(x), var121(x), Not(var110(x))))),
	ForAll([x], Not(Or(var123(x), Not(var291(x)), var278(x)))),
	ForAll([x], Not(Or(var197(x), Not(var134(x)), Not(var236(x))))),
	ForAll([x], Not(Or(var50(x), var72(x), var260(x)))),
	ForAll([x], Not(Or(var7(x), var101(x), var9(x)))),
	ForAll([x], Not(Or(var157(x), Not(var104(x)), Not(var140(x))))),
	ForAll([x], Not(Or(Not(var244(x)), var152(x), var286(x)))),
	ForAll([x], Not(Or(Not(var93(x)), var126(x), var90(x)))),
	ForAll([x], Not(Or(var186(x), var22(x), Not(var281(x))))),
	ForAll([x], Not(Or(Not(var144(x)), Not(var138(x)), Not(var32(x))))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var57(x)), Not(var150(x))))),
	ForAll([x], Not(Or(Not(var114(x)), var111(x), var64(x)))),
	ForAll([x], Not(Or(var235(x), Not(var16(x)), var187(x)))),
	ForAll([x], Not(Or(Not(var153(x)), var214(x), Not(var279(x))))),
	ForAll([x], Not(Or(Not(var99(x)), Not(var271(x)), var62(x)))),
	ForAll([x], Not(Or(Not(var116(x)), var63(x), var300(x)))),
	ForAll([x], Not(Or(Not(var245(x)), Not(var142(x)), Not(var11(x))))),
	ForAll([x], Not(Or(var97(x), var151(x), var131(x)))),
	ForAll([x], Not(Or(var292(x), Not(var149(x)), var10(x)))),
	ForAll([x], Not(Or(var89(x), var117(x), var109(x)))),
	ForAll([x], Not(Or(var34(x), var222(x), Not(var107(x))))),
	ForAll([x], Not(Or(var251(x), Not(var120(x)), Not(var124(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var160(x1), Or(Not(var105(x)), Not(var188(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var102(x1)), var298(x1)), var219(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var226(x1)), var136(x1)), Not(var47(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var127(x1), Not(var128(x1))), var172(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), Or(Not(var81(x)), Not(var42(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var220(x1), var159(x1)), var54(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var25(x1)), var297(x1)), Not(var239(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var113(x1)), Not(var122(x1))), var273(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var227(x1)), Or(Not(var84(x)), Not(var284(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var256(x1), Or(var46(x), var156(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var95(x1)), Or(Not(var162(x)), var287(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var92(x1)), Not(var299(x1))), var212(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var48(x1)), Or(Not(var87(x)), var71(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var184(x1), Or(var253(x), Not(var241(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var224(x1)), Not(var191(x1))), var223(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var213(x1)), Or(Not(var56(x)), var146(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var59(x1), Not(var218(x1))), var18(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var210(x1)), Or(Not(var3(x)), var264(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), Or(Not(var12(x)), var147(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var53(x1), var119(x1)), Not(var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var27(x1), Or(Not(var209(x)), Not(var233(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var208(x1)), var174(x1)), Not(var285(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var194(x1), Or(var108(x), Not(var83(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var103(x1), Or(var201(x), Not(var263(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var112(x1)), Or(var69(x), Not(var28(x)))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
