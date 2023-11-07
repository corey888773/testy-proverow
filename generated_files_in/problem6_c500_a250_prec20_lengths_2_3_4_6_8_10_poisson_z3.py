from z3 import *

Object = DeclareSort('Object')

var118 = Function('var118', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(var118(x))),
	ForAll([x], Not(Not(var173(x)))),
	ForAll([x], Not(Not(var162(x)))),
	ForAll([x], Not(var17(x))),
	ForAll([x], Not(var115(x))),
	ForAll([x], Not(var51(x))),
	ForAll([x], Not(var122(x))),
	ForAll([x], Not(Not(var135(x)))),
	ForAll([x], Not(Not(var20(x)))),
	ForAll([x], Not(Not(var78(x)))),
	ForAll([x], Not(Not(var82(x)))),
	Exists([x], Not(var169(x))),
	Exists([x], Not(var63(x))),
	Exists([x], var171(x)),
	Exists([x], var39(x)),
	Exists([x], var138(x)),
	Exists([x], Not(var93(x))),
	Exists([x], var217(x)),
	Exists([x], Not(var96(x))),
	Exists([x], Not(var169(x))),
	Exists([x], var29(x)),
	Exists([x], Not(var172(x))),
	Exists([x], var111(x)),
	Exists([x], Not(var108(x))),
	Exists([x], var160(x)),
	Exists([x], Not(var177(x))),
	Exists([x], Not(var168(x))),
	Exists([x], var11(x)),
	Exists([x], Not(var43(x))),
	Exists([x], var30(x)),
	Exists([x], var26(x)),
	Exists([x], var243(x)),
	Exists([x], var213(x)),
	Exists([x], Not(var230(x))),
	Exists([x], Not(var127(x))),
	Exists([x], Not(var62(x))),
	Exists([x], Not(var32(x))),
	Exists([x], var33(x)),
	Exists([x], Not(var22(x))),
	Exists([x], var35(x)),
	Exists([x], Not(var74(x))),
	Exists([x], Not(var104(x))),
	Exists([x], Not(var60(x))),
	Exists([x], Not(var12(x))),
	Exists([x], Not(var137(x))),
	Exists([x], var208(x)),
	Exists([x], var1(x)),
	Exists([x], var80(x)),
	Exists([x], var228(x)),
	Exists([x], Not(var60(x))),
	Exists([x], Not(var49(x))),
	Exists([x], var3(x)),
	Exists([x], var108(x)),
	ForAll([x], Not(Or(var243(x), Not(var114(x))))),
	ForAll([x], Not(Or(Not(var55(x)), Not(var39(x))))),
	ForAll([x], Not(Or(Not(var40(x)), var217(x)))),
	ForAll([x], Not(Or(Not(var114(x)), Not(var218(x))))),
	ForAll([x], Not(Or(Not(var89(x)), Not(var245(x))))),
	ForAll([x], Not(Or(Not(var228(x)), Not(var167(x))))),
	ForAll([x], Not(Or(Not(var107(x)), Not(var55(x))))),
	ForAll([x], Not(Or(var144(x), Not(var148(x))))),
	ForAll([x], Not(Or(var156(x), Not(var223(x))))),
	ForAll([x], Not(Or(var53(x), var140(x)))),
	ForAll([x], Not(Or(var67(x), var132(x)))),
	ForAll([x], Not(Or(var178(x), var174(x)))),
	ForAll([x], Not(Or(var200(x), var101(x)))),
	ForAll([x], Not(Or(var87(x), Not(var68(x))))),
	ForAll([x], Not(Or(Not(var136(x)), var146(x)))),
	ForAll([x], Not(Or(var47(x), var55(x)))),
	ForAll([x], Not(Or(Not(var230(x)), var36(x)))),
	ForAll([x], Not(Or(var179(x), Not(var149(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), Not(var62(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var233(x1), var250(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var169(x1), var164(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var176(x1)), Not(var78(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), Not(var61(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var228(x1)), Not(var107(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var106(x1)), Not(var89(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var119(x1)), Not(var235(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var97(x1), var206(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), var144(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var25(x1)), var152(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var226(x1)), var171(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var23(x1), Not(var187(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var158(x1), var52(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var120(x1)), var203(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var188(x1)), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var67(x1), var12(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var130(x1), var126(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var22(x1), Not(var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), var77(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var67(x1), var240(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var79(x1)), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var144(x1)), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var35(x1), Not(var204(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var181(x1), var65(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var209(x1), Not(var78(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var238(x1), Not(var213(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var63(x1), Not(var147(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var240(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var51(x1), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var10(x1), Not(var141(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var137(x1)), var197(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var49(x1), var88(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var164(x1), var162(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var72(x1)), Not(var89(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var231(x1)), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var230(x1), var43(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var232(x1), var104(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var93(x1), Not(var153(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var47(x1)), var36(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var85(x1)), Not(var215(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var75(x1)), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var39(x1)), var197(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var191(x1), var222(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var250(x1)), var113(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var231(x1)), var155(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var72(x1), var239(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var186(x1)), Not(var38(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var59(x1), var96(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var142(x1), var34(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var203(x1), Not(var104(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var207(x1)), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var226(x1), var158(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var40(x1)), var132(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var109(x1), var42(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var80(x1)), var51(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var156(x1)), Not(var223(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var204(x1)), var139(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var142(x1), var210(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var79(x1), Not(var110(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var21(x1)), var211(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var83(x1), var218(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var63(x1), var97(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var83(x1)), var234(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var169(x1)), Not(var150(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var41(x1)), Not(var53(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var202(x1), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), var26(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var41(x1), Not(var54(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var217(x1), var228(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var127(x1), var165(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var158(x1), Not(var137(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var136(x1), var34(x))))),
	ForAll([x], Not(Or(Not(var73(x)), var63(x), var39(x)))),
	ForAll([x], Not(Or(var107(x), Not(var224(x)), Not(var70(x))))),
	ForAll([x], Not(Or(Not(var64(x)), var135(x), var21(x)))),
	ForAll([x], Not(Or(var162(x), var143(x), Not(var191(x))))),
	ForAll([x], Not(Or(var48(x), var110(x), var73(x)))),
	ForAll([x], Not(Or(Not(var205(x)), var96(x), var233(x)))),
	ForAll([x], Not(Or(Not(var165(x)), var62(x), var178(x)))),
	ForAll([x], Not(Or(Not(var123(x)), var172(x), var110(x)))),
	ForAll([x], Not(Or(var30(x), var103(x), var211(x)))),
	ForAll([x], Not(Or(var17(x), var206(x), var69(x)))),
	ForAll([x], Not(Or(var39(x), Not(var233(x)), Not(var58(x))))),
	ForAll([x], Not(Or(Not(var156(x)), Not(var224(x)), Not(var100(x))))),
	ForAll([x], Not(Or(var33(x), var170(x), var231(x)))),
	ForAll([x], Not(Or(var98(x), var221(x), Not(var237(x))))),
	ForAll([x], Not(Or(Not(var187(x)), Not(var149(x)), Not(var137(x))))),
	ForAll([x], Not(Or(Not(var89(x)), Not(var20(x)), Not(var178(x))))),
	ForAll([x], Not(Or(Not(var69(x)), var171(x), Not(var93(x))))),
	ForAll([x], Not(Or(var158(x), Not(var141(x)), Not(var57(x))))),
	ForAll([x], Not(Or(var96(x), var6(x), Not(var93(x))))),
	ForAll([x], Not(Or(Not(var12(x)), var88(x), Not(var217(x))))),
	ForAll([x], Not(Or(Not(var219(x)), Not(var207(x)), var200(x)))),
	ForAll([x], Not(Or(var202(x), var179(x), var50(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var138(x1), Or(Not(var182(x)), Not(var250(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var57(x1), Or(Not(var122(x)), var249(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var173(x1)), var126(x1)), Not(var195(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var176(x1)), var35(x1)), Not(var48(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var216(x1), var118(x1)), var1(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var132(x1), Or(var97(x), Not(var163(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var78(x1)), Or(Not(var176(x)), Not(var27(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var230(x1)), Or(Not(var2(x)), Not(var147(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var239(x1)), Or(var68(x), var221(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var154(x1)), Or(Not(var149(x)), Not(var202(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var68(x1)), Not(var185(x1))), var58(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var245(x1)), Or(Not(var118(x)), var57(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var242(x1), Or(Not(var222(x)), Not(var164(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var6(x1)), Not(var28(x1))), var246(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var86(x1)), var242(x1)), var245(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var42(x1)), Or(Not(var244(x)), var213(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var189(x1)), Or(var130(x), Not(var128(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var69(x1), Not(var25(x1))), var18(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var45(x1)), var156(x1)), Not(var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var102(x1), var103(x1)), var127(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var147(x1)), Or(Not(var143(x)), Not(var65(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var71(x1), Not(var212(x1))), Not(var121(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var220(x1), Not(var54(x1))), Not(var211(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var138(x1)), var210(x1)), Not(var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var199(x1)), Or(Not(var240(x)), Not(var87(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var156(x1), Or(var121(x), Not(var175(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var216(x1)), Or(var31(x), Not(var228(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var188(x1), Or(var20(x), Not(var212(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var26(x1), Or(var233(x), Not(var13(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var204(x1)), Not(var131(x1))), Not(var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var246(x1)), Or(var198(x), Not(var204(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var248(x1)), var85(x1)), Not(var159(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var223(x1)), Or(Not(var179(x)), var249(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var69(x1), var233(x1)), Not(var108(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var158(x1)), Not(var157(x1))), var52(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var180(x1)), Not(var9(x1))), Not(var143(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var167(x1), var136(x1)), Not(var181(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var91(x1), var140(x1)), var131(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var221(x1), var233(x1)), Not(var51(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var141(x1), Or(Not(var211(x)), var94(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var119(x1), Not(var30(x1))), var99(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var246(x1), Or(var231(x), var83(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var166(x1), var237(x1)), Not(var181(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var225(x1), var65(x1)), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var151(x1)), var201(x1)), Not(var230(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var184(x1)), Not(var105(x1))), var4(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var163(x1), var229(x1)), Not(var128(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var249(x1), Not(var137(x1))), var165(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var44(x1), Or(var223(x), var26(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var227(x1)), var157(x1)), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var71(x1), Or(var6(x), Not(var64(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var105(x1), Or(Not(var57(x)), var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var155(x1), var149(x1)), Not(var199(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var110(x1)), Or(var214(x), var133(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var117(x1)), Or(var189(x), Not(var65(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var126(x1)), var15(x1)), var137(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var238(x1)), Or(Not(var82(x)), var123(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var91(x1)), Or(var77(x), Not(var94(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var74(x1), Not(var61(x1))), Not(var105(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var182(x1)), Not(var90(x1))), var72(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var211(x1), Not(var97(x1))), Not(var74(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var145(x1)), Not(var226(x1))), var90(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var14(x1)), Not(var129(x1))), Not(var180(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var96(x1), Not(var59(x1))), Not(var204(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var165(x1)), Or(var130(x), Not(var138(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var187(x1), var22(x1)), Not(var238(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var179(x1), Not(var45(x1))), Not(var146(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var116(x1), Or(Not(var199(x)), var33(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var15(x1), Or(Not(var87(x)), var244(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Or(Not(var218(x)), Not(var100(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var103(x1)), Not(var218(x1))), var209(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var105(x1), Or(Not(var240(x)), var195(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var231(x1), Or(var171(x), var139(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var54(x1), Not(var152(x1))), var240(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var180(x1), Not(var215(x1))), Not(var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var54(x1)), Or(var85(x), Not(var128(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var75(x1)), var230(x1)), var107(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var169(x1)), var85(x1)), Not(var133(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var121(x1), Or(Not(var43(x)), Not(var159(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var5(x1), Not(var22(x1))), var46(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var192(x1)), Not(var157(x1))), Not(var229(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var228(x1), Not(var137(x1))), Not(var169(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var179(x1), Not(var140(x1))), Not(var133(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var167(x1)), Or(Not(var79(x)), Not(var94(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var200(x1), Not(var244(x1))), Not(var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var18(x1), Not(var44(x1))), Not(var77(x)))))),
	ForAll([x], Not(Or(var132(x), var60(x), Not(var27(x)), var103(x)))),
	ForAll([x], Not(Or(var41(x), var132(x), var73(x), Not(var232(x))))),
	ForAll([x], Not(Or(Not(var22(x)), Not(var202(x)), var188(x), var16(x)))),
	ForAll([x], Not(Or(Not(var152(x)), Not(var146(x)), Not(var17(x)), var37(x)))),
	ForAll([x], Not(Or(var14(x), var71(x), Not(var237(x)), Not(var241(x))))),
	ForAll([x], Not(Or(Not(var229(x)), var206(x), Not(var201(x)), var87(x)))),
	ForAll([x], Not(Or(Not(var182(x)), var39(x), var58(x), Not(var16(x))))),
	ForAll([x], Not(Or(var18(x), var197(x), Not(var4(x)), var153(x)))),
	ForAll([x], Not(Or(Not(var193(x)), Not(var225(x)), var173(x), Not(var65(x))))),
	ForAll([x], Not(Or(Not(var180(x)), var36(x), var181(x), var171(x)))),
	ForAll([x], Not(Or(var77(x), var166(x), var194(x), var233(x)))),
	ForAll([x], Not(Or(Not(var162(x)), var194(x), var206(x), Not(var148(x))))),
	ForAll([x], Not(Or(Not(var225(x)), Not(var125(x)), Not(var198(x)), var226(x)))),
	ForAll([x], Not(Or(Not(var56(x)), Not(var236(x)), Not(var206(x)), Not(var123(x))))),
	ForAll([x], Not(Or(var150(x), Not(var169(x)), Not(var186(x)), Not(var250(x))))),
	ForAll([x], Not(Or(var187(x), var20(x), Not(var62(x)), var117(x)))),
	ForAll([x], Not(Or(var30(x), Not(var201(x)), Not(var88(x)), var180(x)))),
	ForAll([x], Not(Or(Not(var66(x)), var40(x), Not(var71(x)), Not(var33(x))))),
	ForAll([x], Not(Or(Not(var225(x)), var245(x), var117(x), var162(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var139(x1), Or(Not(var201(x)), var148(x), Not(var37(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var123(x1), Or(var15(x), Not(var167(x)), var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), Not(var28(x1))), Or(Not(var153(x)), var83(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var106(x1), var181(x1)), Or(var42(x), Not(var138(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var84(x1), Or(var28(x), Not(var211(x)), var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var72(x1), var204(x1)), Or(Not(var24(x)), Not(var219(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var55(x1)), Not(var97(x1)), var105(x1)), Not(var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var129(x1)), var186(x1), var214(x1)), var172(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var69(x1), Not(var107(x1))), Or(var66(x), var53(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var77(x1)), Or(Not(var15(x)), var62(x), var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var114(x1)), Or(Not(var67(x)), Not(var3(x)), Not(var244(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var23(x1)), Not(var229(x1)), Not(var144(x1))), var128(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var152(x1)), var65(x1)), Or(var58(x), Not(var180(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var165(x1), Not(var10(x1)), var158(x1)), var126(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var124(x1)), Not(var100(x1)), var196(x1)), Not(var114(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var14(x1)), Not(var121(x1))), Or(Not(var148(x)), var138(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var74(x1), var100(x1)), Or(Not(var73(x)), Not(var126(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var38(x1)), Or(var59(x), var232(x), Not(var176(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var4(x1)), var16(x1)), Or(var149(x), Not(var200(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var6(x1), Or(var20(x), var228(x), var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var177(x1), Or(Not(var47(x)), Not(var185(x)), var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var149(x1), Or(var16(x), Not(var5(x)), Not(var212(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var165(x1), Or(Not(var111(x)), Not(var62(x)), Not(var229(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var13(x1), Or(Not(var183(x)), Not(var68(x)), var119(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var54(x1), Or(var49(x), Not(var197(x)), var56(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var231(x1)), var212(x1)), Or(var5(x), var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var246(x1), Or(Not(var250(x)), var111(x), var186(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var110(x1)), Or(var104(x), var55(x), Not(var43(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var161(x1)), Or(Not(var14(x)), Not(var203(x)), Not(var152(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var219(x1), Not(var232(x1)), Not(var76(x1))), Not(var246(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var29(x1), var178(x1)), Or(var176(x), Not(var105(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var85(x1), Not(var194(x1))), Or(Not(var122(x)), var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var92(x1), var139(x1)), Or(Not(var140(x)), var50(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var173(x1)), var145(x1), Not(var143(x1))), var176(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var125(x1)), Not(var63(x1)), var229(x1)), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var223(x1), var167(x1), Not(var66(x1))), var132(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var30(x1), Not(var234(x1))), Or(Not(var180(x)), var71(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), Or(Not(var122(x)), Not(var159(x)), var161(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var164(x1), var64(x1), Not(var240(x1))), var130(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var157(x1), Or(Not(var70(x)), var153(x), Not(var124(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var104(x1)), Not(var222(x1)), Not(var233(x1))), Not(var214(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var127(x1), var174(x1), var240(x1)), Not(var134(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var206(x1), Or(Not(var31(x)), Not(var83(x)), Not(var194(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var33(x1), Not(var224(x1)), var56(x1)), var123(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var87(x1), Or(var136(x), Not(var239(x)), var232(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var41(x1), Not(var25(x1)), Not(var116(x1))), Not(var43(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var126(x1), var242(x1), var219(x1)), Not(var92(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var128(x1)), var121(x1)), Or(Not(var139(x)), Not(var130(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var202(x1), Or(var169(x), Not(var95(x)), var58(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var76(x1)), Not(var130(x1))), Or(var188(x), Not(var173(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var224(x1)), var105(x1)), Or(Not(var213(x)), var76(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var157(x1)), Or(Not(var223(x)), Not(var220(x)), Not(var100(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var239(x1)), var223(x1), Not(var119(x1))), Not(var107(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var137(x1)), var63(x1)), Or(Not(var202(x)), var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var179(x1), Or(Not(var127(x)), Not(var51(x)), Not(var164(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var107(x1)), Not(var217(x1))), Or(Not(var6(x)), var91(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var117(x1), var145(x1)), Or(var51(x), var183(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var215(x1), var141(x1)), Or(Not(var202(x)), Not(var117(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var57(x1), var1(x1), var82(x1)), var212(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var142(x1), Or(Not(var84(x)), Not(var103(x)), var85(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var54(x1)), Not(var181(x1))), Or(var144(x), Not(var164(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var23(x1)), Not(var111(x1)), var64(x1)), var230(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var23(x1), Not(var126(x1)), Not(var85(x1))), var220(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var187(x1), Or(var21(x), Not(var51(x)), Not(var225(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var224(x1), Not(var193(x1))), Or(Not(var135(x)), var124(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var237(x1)), Not(var59(x1))), Or(Not(var220(x)), var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var26(x1)), Or(var171(x), Not(var201(x)), Not(var241(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var133(x1)), Or(var3(x), Not(var134(x)), var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var220(x1)), Or(Not(var92(x)), var149(x), Not(var155(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var53(x1)), Not(var207(x1))), Or(Not(var64(x)), Not(var70(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var143(x1)), Or(Not(var112(x)), var123(x), var126(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var22(x1)), Or(Not(var86(x)), var173(x), Not(var59(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var140(x1), Or(Not(var41(x)), var150(x), Not(var30(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var239(x1)), Or(var196(x), Not(var141(x)), var211(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var126(x1)), Not(var77(x1)), var64(x1)), var16(x))))),
	ForAll([x], Not(Or(var47(x), Not(var153(x)), var84(x), var141(x), Not(var133(x))))),
	ForAll([x], Not(Or(Not(var40(x)), var120(x), Not(var199(x)), var65(x), Not(var240(x))))),
	ForAll([x], Not(Or(var187(x), Not(var193(x)), var23(x), Not(var52(x)), var111(x)))),
	ForAll([x], Not(Or(var34(x), Not(var117(x)), Not(var8(x)), Not(var125(x)), var152(x)))),
	ForAll([x], Not(Or(Not(var167(x)), var242(x), Not(var234(x)), Not(var92(x)), var240(x)))),
	ForAll([x], Not(Or(Not(var76(x)), var67(x), Not(var100(x)), Not(var117(x)), Not(var57(x))))),
	ForAll([x], Not(Or(var69(x), Not(var102(x)), Not(var209(x)), var53(x), Not(var21(x))))),
	ForAll([x], Not(Or(var86(x), Not(var21(x)), Not(var177(x)), var76(x), var149(x)))),
	ForAll([x], Not(Or(var202(x), var104(x), var108(x), Not(var139(x)), var96(x)))),
	ForAll([x], Not(Or(Not(var108(x)), Not(var10(x)), Not(var87(x)), var236(x), var234(x)))),
	ForAll([x], Not(Or(var35(x), Not(var15(x)), var94(x), var182(x), var96(x)))),
	ForAll([x], Not(Or(Not(var163(x)), Not(var31(x)), var173(x), Not(var40(x)), Not(var166(x))))),
	ForAll([x], Not(Or(var130(x), var114(x), Not(var90(x)), Not(var156(x)), var145(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var89(x1)), Or(var102(x), Not(var72(x)), var195(x), Not(var14(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var74(x1)), Or(Not(var249(x)), var178(x), var126(x), var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var190(x1), var99(x1), var201(x1)), Or(Not(var48(x)), var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var71(x1)), var56(x1)), Or(Not(var49(x)), Not(var78(x)), Not(var246(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var94(x1)), var183(x1), var99(x1), Not(var142(x1))), var246(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var196(x1), Not(var150(x1))), Or(Not(var3(x)), Not(var182(x)), Not(var51(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var149(x1)), Not(var138(x1)), Not(var41(x1)), Not(var201(x1))), Not(var147(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var115(x1), Not(var191(x1)), Not(var174(x1))), Or(Not(var74(x)), var203(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var2(x1), var169(x1), Not(var147(x1))), Or(Not(var92(x)), var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var25(x1)), Not(var18(x1))), Or(Not(var105(x)), Not(var203(x)), Not(var148(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var138(x1)), Or(Not(var176(x)), var195(x), Not(var218(x)), Not(var225(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var208(x1)), var238(x1), Not(var53(x1)), Not(var237(x1))), var87(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var177(x1), Or(Not(var205(x)), Not(var117(x)), Not(var199(x)), Not(var119(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var175(x1)), var227(x1), Not(var92(x1)), Not(var235(x1))), Not(var128(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var121(x1), var194(x1), var90(x1)), Or(var10(x), Not(var80(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var106(x1), Or(var196(x), Not(var179(x)), Not(var132(x)), var59(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var100(x1)), var225(x1)), Or(var49(x), Not(var116(x)), var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var152(x1), var176(x1), var128(x1)), Or(var195(x), Not(var229(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var25(x1)), var31(x1), Not(var47(x1)), var149(x1)), Not(var223(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var30(x1)), var179(x1), var201(x1)), Or(var13(x), Not(var78(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var124(x1)), var241(x1), var84(x1), Not(var136(x1))), var33(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var68(x1)), Or(Not(var111(x)), var138(x), var101(x), Not(var10(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var177(x1), Or(Not(var79(x)), var30(x), Not(var147(x)), var226(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var129(x1)), Not(var82(x1)), var208(x1), var182(x1)), var180(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var128(x1)), Not(var83(x1))), Or(Not(var191(x)), var205(x), Not(var190(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var89(x1)), var225(x1), Not(var205(x1)), var147(x1)), Not(var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var153(x1)), Not(var137(x1))), Or(Not(var191(x)), var92(x), var4(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var123(x1), var28(x1)), Or(var193(x), Not(var132(x)), Not(var184(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var139(x1)), var157(x1)), Or(Not(var147(x)), var242(x), var228(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var187(x1), Or(Not(var42(x)), Not(var92(x)), var214(x), var208(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var192(x1), var108(x1)), Or(Not(var115(x)), Not(var213(x)), Not(var207(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var107(x1)), var148(x1), Not(var75(x1)), var170(x1)), var68(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var4(x1)), Not(var187(x1)), var180(x1)), Or(var135(x), var139(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var55(x1), Not(var84(x1))), Or(var129(x), var163(x), var123(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var183(x1), var189(x1), var35(x1), Not(var162(x1))), var34(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var199(x1), var245(x1), Not(var69(x1)), Not(var150(x1))), Not(var181(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var120(x1)), var199(x1), Not(var189(x1)), var94(x1)), var184(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var137(x1)), var143(x1), var162(x1)), Or(var202(x), var232(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var73(x1), var15(x1), Not(var174(x1))), Or(var250(x), var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var92(x1), Or(Not(var69(x)), Not(var55(x)), var87(x), var205(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var66(x1), Not(var147(x1)), var98(x1), Not(var35(x1))), var211(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var64(x1)), Or(var88(x), var1(x), var92(x), var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var100(x1)), Or(var162(x), Not(var148(x)), Not(var159(x)), var209(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var43(x1)), var179(x1), Not(var66(x1))), Or(Not(var126(x)), Not(var103(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var219(x1), var6(x1)), Or(Not(var163(x)), Not(var90(x)), var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var135(x1)), Or(Not(var26(x)), Not(var35(x)), Not(var183(x)), var41(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var233(x1)), Not(var68(x1)), Not(var186(x1))), Or(var199(x), Not(var182(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var226(x1), Or(var136(x), Not(var132(x)), var130(x), var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var36(x1)), Not(var215(x1)), Not(var67(x1))), Or(var35(x), var134(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var147(x1)), var41(x1)), Or(var203(x), Not(var223(x)), Not(var196(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var169(x1), Not(var143(x1)), var182(x1), Not(var72(x1))), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var223(x1), var47(x1), var31(x1), var141(x1)), var104(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var166(x1), Or(Not(var12(x)), var117(x), Not(var170(x)), Not(var134(x))))))),
	ForAll([x], Not(Or(Not(var69(x)), Not(var143(x)), var198(x), var155(x), var27(x), Not(var220(x))))),
	ForAll([x], Not(Or(Not(var79(x)), Not(var60(x)), var30(x), var149(x), var235(x), Not(var107(x))))),
	ForAll([x], Not(Or(var232(x), Not(var218(x)), var35(x), Not(var113(x)), Not(var36(x)), var111(x)))),
	ForAll([x], Not(Or(Not(var14(x)), Not(var142(x)), Not(var193(x)), var201(x), var9(x), Not(var239(x))))),
	ForAll([x], Not(Or(Not(var133(x)), var226(x), Not(var90(x)), Not(var42(x)), Not(var59(x)), var37(x)))),
	ForAll([x], Not(Or(var50(x), Not(var187(x)), Not(var67(x)), var182(x), Not(var51(x)), var146(x)))),
	ForAll([x], Not(Or(var176(x), var103(x), Not(var45(x)), var80(x), var247(x), Not(var127(x))))),
	ForAll([x], Not(Or(var235(x), Not(var163(x)), var129(x), Not(var120(x)), var136(x), var178(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var202(x1), var158(x1), Not(var131(x1)), Not(var97(x1))), Or(Not(var244(x)), Not(var163(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var204(x1), var198(x1), var52(x1), var236(x1), Not(var38(x1))), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var204(x1), Not(var38(x1))), Or(Not(var36(x)), var51(x), var31(x), var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var105(x1), var44(x1), var109(x1), var243(x1), var41(x1)), Not(var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var36(x1), Or(var29(x), Not(var78(x)), Not(var115(x)), Not(var130(x)), var112(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var131(x1)), Or(var155(x), var126(x), Not(var13(x)), var75(x), var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var114(x1), Not(var24(x1))), Or(Not(var195(x)), var231(x), Not(var59(x)), var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var107(x1), var60(x1)), Or(Not(var44(x)), var117(x), Not(var200(x)), Not(var33(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var153(x1)), var41(x1)), Or(var68(x), var16(x), Not(var243(x)), var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var7(x1), Not(var44(x1)), Not(var77(x1))), Or(Not(var217(x)), var153(x), Not(var124(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var96(x1)), Not(var237(x1)), var132(x1), Not(var193(x1)), Not(var122(x1))), Not(var94(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var93(x1), Or(var155(x), var5(x), Not(var136(x)), Not(var71(x)), Not(var88(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var64(x1)), Not(var219(x1))), Or(Not(var240(x)), var160(x), Not(var79(x)), Not(var41(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var197(x1), Not(var188(x1)), var113(x1), Not(var149(x1))), Or(Not(var15(x)), var5(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var76(x1), Or(var46(x), Not(var138(x)), var196(x), Not(var199(x)), var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var8(x1), Not(var117(x1)), var24(x1)), Or(Not(var49(x)), Not(var82(x)), var52(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var106(x1), var40(x1), Not(var108(x1)), Not(var184(x1))), Or(var56(x), Not(var11(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var172(x1), var86(x1)), Or(var248(x), Not(var36(x)), var184(x), var209(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var213(x1)), Or(var232(x), var18(x), Not(var139(x)), Not(var59(x)), var83(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var182(x1)), var245(x1), var107(x1), Not(var180(x1))), Or(var211(x), var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var106(x1)), var214(x1), Not(var97(x1)), var223(x1), Not(var93(x1))), var30(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var164(x1), Not(var133(x1)), Not(var74(x1)), Not(var128(x1))), Or(Not(var33(x)), var185(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var250(x1)), Or(Not(var118(x)), var89(x), Not(var111(x)), var239(x), Not(var121(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var33(x1), Not(var26(x1)), var169(x1)), Or(Not(var243(x)), Not(var127(x)), var154(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var215(x1)), var198(x1), var187(x1)), Or(var231(x), var135(x), Not(var162(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var243(x1)), Not(var185(x1)), var9(x1), Not(var236(x1))), Or(var232(x), var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var136(x1)), var240(x1), Not(var167(x1))), Or(Not(var70(x)), var189(x), var148(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var72(x1), var105(x1)), Or(Not(var48(x)), var195(x), Not(var233(x)), var102(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var224(x1), var134(x1), Not(var106(x1)), Not(var144(x1)), Not(var202(x1))), var245(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var232(x1)), Or(var47(x), var21(x), Not(var48(x)), Not(var165(x)), Not(var222(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var164(x1), var197(x1), Not(var155(x1))), Or(Not(var193(x)), Not(var56(x)), var206(x)))))),
	ForAll([x], Not(Or(Not(var247(x)), var165(x), Not(var160(x)), var136(x), Not(var225(x)), Not(var46(x)), Not(var23(x))))),
	ForAll([x], Not(Or(var12(x), Not(var91(x)), Not(var109(x)), var169(x), Not(var50(x)), var59(x), Not(var107(x))))),
	ForAll([x], Not(Or(Not(var200(x)), Not(var95(x)), Not(var117(x)), var35(x), Not(var11(x)), var14(x), Not(var228(x))))),
	ForAll([x], Not(Or(var159(x), Not(var206(x)), Not(var181(x)), var33(x), Not(var128(x)), Not(var10(x)), var110(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var214(x1)), Or(var220(x), Not(var178(x)), var157(x), var139(x), Not(var67(x)), Not(var4(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var193(x1)), Or(var149(x), Not(var148(x)), var166(x), Not(var60(x)), var98(x), var169(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var49(x1)), Not(var19(x1)), var224(x1), var117(x1)), Or(Not(var185(x)), var178(x), Not(var250(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var1(x1), Not(var60(x1)), var117(x1), var116(x1), Not(var24(x1)), Not(var160(x1))), Not(var197(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var50(x1)), var197(x1), var234(x1), Not(var122(x1)), Not(var227(x1))), Or(Not(var132(x)), var145(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var181(x1), var184(x1), var13(x1), var198(x1), var155(x1), var166(x1)), Not(var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var28(x1)), var34(x1)), Or(var196(x), Not(var58(x)), Not(var190(x)), var63(x), Not(var187(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var84(x1), var154(x1), Not(var250(x1)), Not(var39(x1)), Not(var72(x1))), Or(Not(var8(x)), var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var102(x1)), var65(x1), var187(x1), Not(var125(x1))), Or(var93(x), Not(var152(x)), Not(var191(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var72(x1)), var71(x1), var62(x1), var203(x1), Not(var247(x1))), Or(var20(x), Not(var241(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var51(x1)), Not(var117(x1)), var165(x1), Not(var211(x1)), var143(x1)), Or(var177(x), Not(var87(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var115(x1)), var52(x1), var35(x1), var67(x1), Not(var241(x1))), Or(Not(var98(x)), Not(var63(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var81(x1)), var227(x1), Not(var248(x1)), var189(x1)), Or(Not(var67(x)), var88(x), var213(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var121(x1), Not(var194(x1))), Or(var33(x), var210(x), var243(x), Not(var181(x)), Not(var11(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var180(x1), Not(var53(x1)), Not(var169(x1)), var10(x1)), Or(Not(var218(x)), Not(var155(x)), Not(var160(x))))))),
	ForAll([x], Not(Or(var54(x), var35(x), var48(x), Not(var116(x)), var12(x), var188(x), var122(x), var247(x)))),
	ForAll([x], Not(Or(var71(x), Not(var138(x)), var137(x), Not(var90(x)), var1(x), Not(var8(x)), var57(x), Not(var215(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var153(x1), Not(var79(x1))), Or(var236(x), var182(x), Not(var9(x)), var163(x), Not(var25(x)), Not(var205(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var114(x1), Or(Not(var10(x)), Not(var90(x)), Not(var111(x)), var27(x), var187(x), var69(x), Not(var240(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var94(x1), Not(var28(x1)), Not(var23(x1)), Not(var114(x1)), var46(x1), var103(x1), Not(var91(x1))), var146(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var213(x1)), Or(var158(x), Not(var188(x)), var48(x), Not(var225(x)), Not(var49(x)), Not(var12(x)), Not(var52(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), Not(var190(x1))), Or(var209(x), var135(x), var95(x), var35(x), var242(x), Not(var235(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var55(x1), Not(var23(x1)), var13(x1), var131(x1)), Or(Not(var138(x)), var228(x), Not(var219(x)), var40(x)))))),
	ForAll([x], Not(Or(Not(var228(x)), var196(x), var81(x), Not(var91(x)), var126(x), var49(x), Not(var78(x)), var66(x), Not(var190(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var181(x1), Not(var227(x1)), Not(var166(x1)), Not(var120(x1)), var66(x1)), Or(var113(x), Not(var138(x)), Not(var37(x)), Not(var41(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var159(x1)), var190(x1), Not(var213(x1)), Not(var235(x1)), Not(var54(x1))), Or(Not(var93(x)), Not(var53(x)), var136(x), var112(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var250(x1)), var1(x1), var103(x1), Not(var171(x1)), Not(var70(x1)), var158(x1)), Or(var234(x), var31(x), var202(x), var19(x)))))),
	ForAll([x], Not(Or(Not(var123(x)), Not(var231(x)), var146(x), Not(var41(x)), var110(x), Not(var34(x))))),
	ForAll([x], Not(Or(Not(var9(x)), var134(x)))),
	ForAll([x], Not(Or(var97(x), var73(x), Not(var217(x)), var210(x)))),
	ForAll([x], Not(Or(Not(var111(x)), Not(var186(x)), var29(x), var82(x), Not(var35(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var138(x1)), Or(var156(x), Not(var229(x)), Not(var18(x))))))),
	Exists([x], Not(var203(x))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var12(x1), Not(var78(x1))), Or(var90(x), Not(var225(x)), Not(var222(x)), var235(x)))))),
	Exists([x], var48(x)),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var156(x1), Not(var184(x1)), var155(x1), Not(var7(x1))), Or(var77(x), Not(var226(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var144(x1)), var68(x1)), Or(Not(var114(x)), Not(var72(x)), Not(var23(x)), var220(x), var170(x), Not(var217(x)), Not(var250(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var132(x1), Not(var68(x1)), Not(var227(x1)), var43(x1)), Or(var57(x), Not(var245(x)), var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var146(x1)), Not(var165(x1)), Not(var109(x1))), Not(var206(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var242(x1)), var8(x1), var2(x1), Not(var13(x1)), Not(var184(x1)), var152(x1), Not(var223(x1))), Not(var201(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var246(x1)), Or(var22(x), var134(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var198(x1), var241(x1), var14(x1)), var129(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var92(x1)), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var21(x1), Or(var151(x), Not(var215(x)), var203(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
