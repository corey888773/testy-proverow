from z3 import *

Object = DeclareSort('Object')

var186 = Function('var186', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var276 = Function('var276', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var186(x)), var47(x)))),
	ForAll([x], Not(Or(var159(x), var299(x)))),
	ForAll([x], Not(Or(var291(x), Not(var1(x))))),
	ForAll([x], Not(Or(Not(var103(x)), Not(var146(x))))),
	ForAll([x], Not(Or(Not(var160(x)), Not(var162(x))))),
	ForAll([x], Not(Or(var13(x), var233(x)))),
	ForAll([x], Not(Or(Not(var36(x)), Not(var17(x))))),
	ForAll([x], Not(Or(var276(x), Not(var14(x))))),
	ForAll([x], Not(Or(Not(var6(x)), var167(x)))),
	ForAll([x], Not(Or(Not(var144(x)), var266(x)))),
	ForAll([x], Not(Or(var32(x), var217(x)))),
	ForAll([x], Not(Or(var99(x), Not(var169(x))))),
	ForAll([x], Not(Or(var65(x), Not(var264(x))))),
	ForAll([x], Not(Or(Not(var195(x)), Not(var34(x))))),
	ForAll([x], Not(Or(var118(x), var234(x)))),
	ForAll([x], Not(Or(var84(x), Not(var85(x))))),
	ForAll([x], Not(Or(var194(x), Not(var121(x))))),
	ForAll([x], Not(Or(var168(x), Not(var139(x))))),
	ForAll([x], Not(Or(Not(var226(x)), var241(x)))),
	ForAll([x], Not(Or(var161(x), Not(var71(x))))),
	ForAll([x], Not(Or(var122(x), var142(x)))),
	ForAll([x], Not(Or(var54(x), var184(x)))),
	ForAll([x], Not(Or(var155(x), var218(x)))),
	ForAll([x], Not(Or(var175(x), var210(x)))),
	ForAll([x], Not(Or(var172(x), Not(var219(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var88(x1), Not(var281(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var110(x1), Not(var268(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var73(x1)), var77(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var209(x1)), Not(var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var246(x1)), var288(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var93(x1)), Not(var4(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var242(x1), Not(var35(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var108(x1), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var78(x1)), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var124(x1), var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var15(x1)), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var86(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var69(x1)), var18(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var252(x1)), var57(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var19(x1)), var171(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var166(x1)), Not(var38(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var145(x1), var119(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var138(x1)), Not(var289(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var63(x1), var40(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var22(x1)), var260(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var30(x1), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), var89(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var37(x1)), Not(var208(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var102(x1)), Not(var53(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), var29(x))))),
	ForAll([x], Not(Or(var76(x), Not(var5(x)), var43(x)))),
	ForAll([x], Not(Or(var183(x), var114(x), Not(var64(x))))),
	ForAll([x], Not(Or(var83(x), Not(var133(x)), Not(var170(x))))),
	ForAll([x], Not(Or(var80(x), Not(var158(x)), Not(var58(x))))),
	ForAll([x], Not(Or(var163(x), var75(x), Not(var202(x))))),
	ForAll([x], Not(Or(var11(x), Not(var200(x)), Not(var23(x))))),
	ForAll([x], Not(Or(Not(var235(x)), var26(x), Not(var56(x))))),
	ForAll([x], Not(Or(var182(x), var177(x), Not(var150(x))))),
	ForAll([x], Not(Or(Not(var127(x)), var91(x), var247(x)))),
	ForAll([x], Not(Or(Not(var294(x)), var94(x), var109(x)))),
	ForAll([x], Not(Or(Not(var107(x)), Not(var28(x)), Not(var25(x))))),
	ForAll([x], Not(Or(var62(x), var149(x), Not(var265(x))))),
	ForAll([x], Not(Or(var153(x), var222(x), var46(x)))),
	ForAll([x], Not(Or(var117(x), Not(var100(x)), var293(x)))),
	ForAll([x], Not(Or(Not(var187(x)), Not(var74(x)), var42(x)))),
	ForAll([x], Not(Or(var20(x), var261(x), Not(var55(x))))),
	ForAll([x], Not(Or(var180(x), Not(var231(x)), var152(x)))),
	ForAll([x], Not(Or(var128(x), Not(var298(x)), Not(var192(x))))),
	ForAll([x], Not(Or(var82(x), var285(x), var31(x)))),
	ForAll([x], Not(Or(Not(var52(x)), Not(var156(x)), Not(var140(x))))),
	ForAll([x], Not(Or(var151(x), var199(x), Not(var106(x))))),
	ForAll([x], Not(Or(Not(var10(x)), var259(x), var136(x)))),
	ForAll([x], Not(Or(Not(var130(x)), var173(x), var95(x)))),
	ForAll([x], Not(Or(var148(x), Not(var243(x)), var101(x)))),
	ForAll([x], Not(Or(var137(x), var70(x), var224(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var92(x1), Not(var250(x1))), var203(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var98(x1)), var220(x1)), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var61(x1)), var253(x1)), Not(var141(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var164(x1)), Not(var39(x1))), var254(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var87(x1), Or(Not(var131(x)), Not(var271(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var113(x1), Or(Not(var116(x)), var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var181(x1), var176(x1)), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var179(x1)), Not(var97(x1))), var174(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var112(x1)), Or(var111(x), Not(var165(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var227(x1)), var120(x1)), Not(var129(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var225(x1)), Or(var215(x), var125(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var295(x1)), Not(var178(x1))), Not(var157(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var267(x1), Or(Not(var90(x)), var59(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var255(x1), Or(var67(x), var143(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var263(x1)), Or(Not(var104(x)), var258(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var72(x1)), Not(var205(x1))), var191(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var51(x1), Or(var115(x), Not(var132(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var68(x1), var290(x1)), Not(var33(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var123(x1)), Not(var9(x1))), var79(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var81(x1), var211(x1)), var213(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var134(x1)), Or(Not(var66(x)), var105(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var96(x1), Or(var24(x), Not(var12(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var3(x1), Not(var21(x1))), var190(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var147(x1), Or(Not(var41(x)), var135(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var126(x1), Not(var154(x1))), var185(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
