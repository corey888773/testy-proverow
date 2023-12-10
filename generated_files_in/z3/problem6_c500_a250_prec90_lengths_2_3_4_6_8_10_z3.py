from z3 import *

Object = DeclareSort('Object')

var120 = Function('var120', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms0 = [
	ForAll([x], Not(Or(var120(x), var224(x)))),
	ForAll([x], Not(Or(Not(var166(x)), Not(var10(x))))),
	ForAll([x], Not(Or(Not(var213(x)), Not(var128(x))))),
	ForAll([x], Not(Or(Not(var201(x)), Not(var58(x))))),
	ForAll([x], Not(Or(Not(var140(x)), var156(x)))),
	ForAll([x], Not(Or(var117(x), var222(x)))),
	ForAll([x], Not(Or(var31(x), var120(x)))),
	ForAll([x], Not(Or(Not(var123(x)), var249(x)))),
	ForAll([x], Not(Or(var241(x), var244(x)))),
	ForAll([x], Not(Or(Not(var49(x)), var162(x)))),
	ForAll([x], Not(Or(Not(var68(x)), Not(var197(x))))),
	ForAll([x], Not(Or(var20(x), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var139(x)), var14(x)))),
	ForAll([x], Not(Or(Not(var232(x)), Not(var191(x))))),
	ForAll([x], Not(Or(Not(var27(x)), var231(x)))),
	ForAll([x], Not(Or(Not(var208(x)), var103(x)))),
	ForAll([x], Not(Or(var6(x), Not(var59(x))))),
	ForAll([x], Not(Or(var176(x), var87(x)))),
	ForAll([x], Not(Or(Not(var66(x)), var216(x)))),
	ForAll([x], Not(Or(Not(var162(x)), Not(var205(x))))),
	ForAll([x], Not(Or(Not(var159(x)), var146(x)))),
	ForAll([x], Not(Or(Not(var106(x)), Not(var100(x))))),
	ForAll([x], Not(Or(Not(var107(x)), Not(var55(x))))),
	ForAll([x], Not(Or(Not(var145(x)), Not(var224(x))))),
	ForAll([x], Not(Or(var5(x), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var242(x)), var63(x)))),
	ForAll([x], Not(Or(Not(var115(x)), var210(x)))),
	ForAll([x], Not(Or(Not(var169(x)), var131(x)))),
	ForAll([x], Not(Or(var108(x), Not(var115(x))))),
	ForAll([x], Not(Or(Not(var222(x)), Not(var24(x))))),
	ForAll([x], Not(Or(var104(x), var221(x)))),
	ForAll([x], Not(Or(var193(x), Not(var226(x))))),
	ForAll([x], Not(Or(var230(x), var122(x)))),
	ForAll([x], Not(Or(Not(var171(x)), var223(x)))),
	ForAll([x], Not(Or(var175(x), Not(var191(x))))),
	ForAll([x], Not(Or(var239(x), Not(var181(x))))),
	ForAll([x], Not(Or(Not(var128(x)), Not(var64(x))))),
	ForAll([x], Not(Or(Not(var62(x)), Not(var92(x))))),
	ForAll([x], Not(Or(var24(x), var38(x)))),
	ForAll([x], Not(Or(Not(var19(x)), Not(var5(x))))),
	ForAll([x], Not(Or(var211(x), Not(var201(x))))),
	ForAll([x], Not(Or(Not(var97(x)), Not(var13(x))))),
	ForAll([x], Not(Or(var152(x), var129(x)))),
	ForAll([x], Not(Or(var146(x), Not(var29(x))))),
	ForAll([x], Not(Or(var104(x), var215(x)))),
	ForAll([x], Not(Or(Not(var69(x)), Not(var206(x))))),
	ForAll([x], Not(Or(Not(var155(x)), Not(var79(x))))),
	ForAll([x], Not(Or(var100(x), Not(var41(x))))),
	ForAll([x], Not(Or(var53(x), var20(x)))),
	ForAll([x], Not(Or(var54(x), var81(x)))),
	ForAll([x], Not(Or(var19(x), Not(var67(x))))),
	ForAll([x], Not(Or(var100(x), Not(var9(x))))),
	ForAll([x], Not(Or(var188(x), Not(var210(x))))),
	ForAll([x], Not(Or(var208(x), var220(x)))),
	ForAll([x], Not(Or(Not(var163(x)), Not(var244(x))))),
	ForAll([x], Not(Or(Not(var64(x)), Not(var15(x))))),
	ForAll([x], Not(Or(Not(var47(x)), var94(x)))),
	ForAll([x], Not(Or(var5(x), var24(x)))),
	ForAll([x], Not(Or(var201(x), Not(var216(x))))),
	ForAll([x], Not(Or(Not(var74(x)), var143(x)))),
	ForAll([x], Not(Or(Not(var170(x)), var98(x)))),
	ForAll([x], Not(Or(var122(x), Not(var117(x))))),
	ForAll([x], Not(Or(var213(x), Not(var25(x))))),
	ForAll([x], Not(Or(Not(var176(x)), Not(var59(x))))),
	ForAll([x], Not(Or(Not(var243(x)), var29(x)))),
	ForAll([x], Not(Or(Not(var184(x)), var170(x)))),
	ForAll([x], Not(Or(var144(x), var39(x)))),
	ForAll([x], Not(Or(Not(var170(x)), Not(var242(x))))),
	ForAll([x], Not(Or(Not(var94(x)), var167(x)))),
	ForAll([x], Not(Or(var16(x), var56(x)))),
	ForAll([x], Not(Or(var158(x), Not(var63(x))))),
	ForAll([x], Not(Or(var233(x), Not(var214(x))))),
	ForAll([x], Not(Or(Not(var143(x)), Not(var248(x))))),
	ForAll([x], Not(Or(Not(var196(x)), Not(var232(x))))),
	ForAll([x], Not(Or(Not(var188(x)), var36(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var108(x1), Not(var137(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var216(x1)), Not(var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var37(x1)), var177(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var247(x1), var229(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var126(x1), var42(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var96(x1)), Not(var186(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var179(x1)), Not(var40(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var43(x1)), var110(x))))),
	ForAll([x], Not(Or(var135(x), var141(x), Not(var51(x))))),
	ForAll([x], Not(Or(var204(x), Not(var229(x)), Not(var162(x))))),
	ForAll([x], Not(Or(Not(var98(x)), Not(var129(x)), var43(x)))),
	ForAll([x], Not(Or(var245(x), var172(x), var234(x)))),
	ForAll([x], Not(Or(Not(var171(x)), var200(x), var139(x)))),
	ForAll([x], Not(Or(Not(var79(x)), var236(x), Not(var233(x))))),
	ForAll([x], Not(Or(var94(x), Not(var155(x)), Not(var232(x))))),
	ForAll([x], Not(Or(Not(var197(x)), var195(x), var3(x)))),
	ForAll([x], Not(Or(Not(var50(x)), var155(x), Not(var152(x))))),
	ForAll([x], Not(Or(Not(var206(x)), var166(x), Not(var64(x))))),
	ForAll([x], Not(Or(var160(x), Not(var182(x)), var81(x)))),
	ForAll([x], Not(Or(Not(var43(x)), var215(x), var86(x)))),
	ForAll([x], Not(Or(Not(var234(x)), var49(x), var158(x)))),
	ForAll([x], Not(Or(Not(var85(x)), Not(var45(x)), Not(var111(x))))),
	ForAll([x], Not(Or(Not(var5(x)), Not(var146(x)), var79(x)))),
	ForAll([x], Not(Or(Not(var220(x)), Not(var24(x)), Not(var198(x))))),
	ForAll([x], Not(Or(var205(x), var5(x), Not(var27(x))))),
	ForAll([x], Not(Or(Not(var192(x)), var72(x), var195(x)))),
	ForAll([x], Not(Or(var139(x), var192(x), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var157(x)), Not(var59(x)), var113(x)))),
	ForAll([x], Not(Or(var6(x), Not(var164(x)), var150(x)))),
	ForAll([x], Not(Or(var114(x), Not(var124(x)), var82(x)))),
	ForAll([x], Not(Or(var164(x), Not(var205(x)), Not(var198(x))))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var76(x)), Not(var239(x))))),
	ForAll([x], Not(Or(var242(x), Not(var6(x)), Not(var103(x))))),
	ForAll([x], Not(Or(Not(var220(x)), var110(x), Not(var26(x))))),
	ForAll([x], Not(Or(var160(x), var84(x), Not(var39(x))))),
	ForAll([x], Not(Or(Not(var133(x)), var96(x), var206(x)))),
	ForAll([x], Not(Or(Not(var34(x)), var58(x), Not(var198(x))))),
	ForAll([x], Not(Or(var36(x), var139(x), var60(x)))),
	ForAll([x], Not(Or(var191(x), var104(x), var46(x)))),
	ForAll([x], Not(Or(Not(var108(x)), Not(var237(x)), var200(x)))),
	ForAll([x], Not(Or(Not(var214(x)), Not(var100(x)), Not(var54(x))))),
	ForAll([x], Not(Or(var232(x), Not(var209(x)), Not(var213(x))))),
	ForAll([x], Not(Or(Not(var91(x)), var164(x), var27(x)))),
	ForAll([x], Not(Or(var8(x), Not(var14(x)), var170(x)))),
	ForAll([x], Not(Or(Not(var177(x)), Not(var27(x)), var84(x)))),
	ForAll([x], Not(Or(Not(var52(x)), Not(var10(x)), Not(var71(x))))),
	ForAll([x], Not(Or(Not(var41(x)), Not(var29(x)), var78(x)))),
	ForAll([x], Not(Or(Not(var201(x)), var50(x), var171(x)))),
	ForAll([x], Not(Or(Not(var223(x)), Not(var82(x)), Not(var54(x))))),
	ForAll([x], Not(Or(var250(x), Not(var211(x)), Not(var199(x))))),
	ForAll([x], Not(Or(Not(var56(x)), Not(var163(x)), var238(x)))),
	ForAll([x], Not(Or(var89(x), Not(var115(x)), var242(x)))),
	ForAll([x], Not(Or(Not(var97(x)), Not(var9(x)), Not(var126(x))))),
	ForAll([x], Not(Or(Not(var236(x)), var214(x), var154(x)))),
	ForAll([x], Not(Or(Not(var191(x)), Not(var104(x)), var111(x)))),
	ForAll([x], Not(Or(Not(var86(x)), Not(var38(x)), Not(var201(x))))),
	ForAll([x], Not(Or(Not(var212(x)), var77(x), var71(x)))),
	ForAll([x], Not(Or(var66(x), Not(var225(x)), Not(var91(x))))),
	ForAll([x], Not(Or(var111(x), var170(x), Not(var36(x))))),
	ForAll([x], Not(Or(var82(x), Not(var143(x)), var144(x)))),
	ForAll([x], Not(Or(Not(var242(x)), var12(x), var223(x)))),
	ForAll([x], Not(Or(var64(x), Not(var192(x)), Not(var96(x))))),
	ForAll([x], Not(Or(var131(x), var215(x), var85(x)))),
	ForAll([x], Not(Or(var67(x), Not(var81(x)), Not(var105(x))))),
	ForAll([x], Not(Or(Not(var6(x)), var135(x), Not(var157(x))))),
	ForAll([x], Not(Or(var142(x), Not(var204(x)), Not(var166(x))))),
	ForAll([x], Not(Or(var241(x), Not(var120(x)), var158(x)))),
	ForAll([x], Not(Or(var130(x), Not(var140(x)), var205(x)))),
	ForAll([x], Not(Or(var53(x), var86(x), var103(x)))),
	ForAll([x], Not(Or(Not(var112(x)), Not(var88(x)), Not(var140(x))))),
	ForAll([x], Not(Or(var183(x), Not(var243(x)), Not(var79(x))))),
	ForAll([x], Not(Or(Not(var101(x)), var198(x), Not(var162(x))))),
	ForAll([x], Not(Or(Not(var123(x)), Not(var223(x)), var184(x)))),
	ForAll([x], Not(Or(var155(x), Not(var95(x)), var69(x)))),
	ForAll([x], Not(Or(var8(x), Not(var145(x)), var202(x)))),
	ForAll([x], Not(Or(Not(var21(x)), var37(x), Not(var154(x))))),
	ForAll([x], Not(Or(Not(var32(x)), var240(x), Not(var145(x))))),
	ForAll([x], Not(Or(var10(x), var202(x), var206(x)))),
	ForAll([x], Not(Or(Not(var147(x)), Not(var34(x)), Not(var246(x))))),
	ForAll([x], Not(Or(Not(var148(x)), Not(var65(x)), var216(x)))),
	ForAll([x], Not(Or(Not(var71(x)), Not(var1(x)), Not(var25(x))))),
	ForAll([x], Not(Or(Not(var125(x)), var40(x), Not(var54(x))))),
	ForAll([x], Not(Or(var189(x), var235(x), var28(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var232(x1), Or(var24(x), Not(var172(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var63(x1)), var73(x1)), var133(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var111(x1), Not(var189(x1))), var156(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var105(x1)), var3(x1)), var173(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var61(x1), var10(x1)), Not(var224(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var101(x1)), Or(Not(var49(x)), var250(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var50(x1)), Not(var123(x1))), Not(var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var122(x1), var29(x1)), var196(x))))),
	ForAll([x], Not(Or(Not(var234(x)), var249(x), var3(x), var150(x)))),
	ForAll([x], Not(Or(var135(x), var19(x), Not(var27(x)), var49(x)))),
	ForAll([x], Not(Or(Not(var245(x)), Not(var168(x)), var26(x), var25(x)))),
	ForAll([x], Not(Or(var116(x), var220(x), Not(var208(x)), var99(x)))),
	ForAll([x], Not(Or(var96(x), var166(x), Not(var106(x)), var235(x)))),
	ForAll([x], Not(Or(var141(x), Not(var129(x)), Not(var238(x)), Not(var167(x))))),
	ForAll([x], Not(Or(Not(var181(x)), var106(x), var135(x), Not(var129(x))))),
	ForAll([x], Not(Or(var77(x), var29(x), Not(var95(x)), Not(var131(x))))),
	ForAll([x], Not(Or(Not(var147(x)), var164(x), Not(var77(x)), Not(var41(x))))),
	ForAll([x], Not(Or(Not(var62(x)), Not(var64(x)), var119(x), var26(x)))),
	ForAll([x], Not(Or(Not(var60(x)), Not(var209(x)), Not(var16(x)), Not(var89(x))))),
	ForAll([x], Not(Or(Not(var184(x)), Not(var193(x)), var43(x), var239(x)))),
	ForAll([x], Not(Or(Not(var141(x)), Not(var112(x)), var150(x), var145(x)))),
	ForAll([x], Not(Or(var196(x), var66(x), var135(x), Not(var24(x))))),
	ForAll([x], Not(Or(Not(var240(x)), Not(var122(x)), var243(x), Not(var139(x))))),
	ForAll([x], Not(Or(Not(var163(x)), Not(var196(x)), var117(x), var106(x)))),
	ForAll([x], Not(Or(Not(var27(x)), var225(x), Not(var65(x)), Not(var179(x))))),
	ForAll([x], Not(Or(Not(var246(x)), var218(x), Not(var21(x)), Not(var27(x))))),
	ForAll([x], Not(Or(var74(x), var135(x), Not(var46(x)), var141(x)))),
	ForAll([x], Not(Or(var57(x), Not(var38(x)), Not(var28(x)), Not(var194(x))))),
	ForAll([x], Not(Or(Not(var223(x)), var199(x), Not(var198(x)), var158(x)))),
	ForAll([x], Not(Or(Not(var58(x)), Not(var110(x)), var181(x), var240(x)))),
	ForAll([x], Not(Or(var51(x), Not(var83(x)), Not(var46(x)), var144(x)))),
	ForAll([x], Not(Or(Not(var250(x)), var19(x), var58(x), var215(x)))),
	ForAll([x], Not(Or(Not(var95(x)), var221(x), Not(var233(x)), var241(x)))),
	ForAll([x], Not(Or(var2(x), Not(var184(x)), Not(var165(x)), Not(var120(x))))),
	ForAll([x], Not(Or(Not(var197(x)), Not(var124(x)), Not(var167(x)), Not(var55(x))))),
	ForAll([x], Not(Or(Not(var56(x)), Not(var66(x)), var240(x), Not(var34(x))))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var234(x)), Not(var83(x)), Not(var130(x))))),
	ForAll([x], Not(Or(Not(var11(x)), var97(x), var131(x), var233(x)))),
	ForAll([x], Not(Or(var55(x), var100(x), Not(var249(x)), var90(x)))),
	ForAll([x], Not(Or(Not(var147(x)), var174(x), var204(x), var54(x)))),
	ForAll([x], Not(Or(var15(x), Not(var196(x)), Not(var12(x)), var138(x)))),
	ForAll([x], Not(Or(Not(var166(x)), var7(x), Not(var92(x)), Not(var139(x))))),
	ForAll([x], Not(Or(Not(var222(x)), var236(x), Not(var16(x)), var76(x)))),
	ForAll([x], Not(Or(var35(x), var171(x), var113(x), Not(var50(x))))),
	ForAll([x], Not(Or(var223(x), Not(var31(x)), Not(var131(x)), var193(x)))),
	ForAll([x], Not(Or(var67(x), Not(var153(x)), Not(var138(x)), var80(x)))),
	ForAll([x], Not(Or(Not(var61(x)), Not(var167(x)), Not(var53(x)), var174(x)))),
	ForAll([x], Not(Or(Not(var151(x)), var247(x), Not(var209(x)), var129(x)))),
	ForAll([x], Not(Or(Not(var134(x)), var243(x), Not(var52(x)), Not(var215(x))))),
	ForAll([x], Not(Or(var126(x), Not(var236(x)), var71(x), var11(x)))),
	ForAll([x], Not(Or(Not(var82(x)), var6(x), Not(var205(x)), var5(x)))),
	ForAll([x], Not(Or(var196(x), var193(x), Not(var202(x)), var181(x)))),
	ForAll([x], Not(Or(var145(x), Not(var205(x)), Not(var169(x)), var111(x)))),
	ForAll([x], Not(Or(var63(x), var190(x), var71(x), var199(x)))),
	ForAll([x], Not(Or(var146(x), var88(x), Not(var210(x)), Not(var181(x))))),
	ForAll([x], Not(Or(var151(x), var163(x), Not(var108(x)), var210(x)))),
	ForAll([x], Not(Or(Not(var38(x)), Not(var202(x)), var81(x), var46(x)))),
	ForAll([x], Not(Or(var226(x), var174(x), Not(var248(x)), var61(x)))),
	ForAll([x], Not(Or(var181(x), var44(x), var213(x), var129(x)))),
	ForAll([x], Not(Or(var41(x), Not(var181(x)), var67(x), var52(x)))),
	ForAll([x], Not(Or(var25(x), var79(x), Not(var29(x)), Not(var160(x))))),
	ForAll([x], Not(Or(var30(x), Not(var165(x)), Not(var121(x)), var181(x)))),
	ForAll([x], Not(Or(var119(x), Not(var23(x)), var8(x), Not(var230(x))))),
	ForAll([x], Not(Or(Not(var197(x)), Not(var171(x)), Not(var226(x)), var14(x)))),
	ForAll([x], Not(Or(Not(var83(x)), var115(x), var118(x), var180(x)))),
	ForAll([x], Not(Or(Not(var10(x)), Not(var114(x)), var52(x), var56(x)))),
	ForAll([x], Not(Or(var121(x), var77(x), Not(var150(x)), Not(var53(x))))),
	ForAll([x], Not(Or(var56(x), Not(var209(x)), Not(var173(x)), var66(x)))),
	ForAll([x], Not(Or(Not(var16(x)), Not(var226(x)), Not(var149(x)), Not(var221(x))))),
	ForAll([x], Not(Or(Not(var106(x)), Not(var193(x)), var136(x), Not(var201(x))))),
	ForAll([x], Not(Or(Not(var137(x)), var80(x), var32(x), var61(x)))),
	ForAll([x], Not(Or(Not(var239(x)), var176(x), var96(x), Not(var108(x))))),
	ForAll([x], Not(Or(var224(x), var35(x), var227(x), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var112(x)), Not(var147(x)), Not(var178(x)), var29(x)))),
	ForAll([x], Not(Or(var86(x), var242(x), Not(var24(x)), Not(var167(x))))),
	ForAll([x], Not(Or(Not(var39(x)), Not(var200(x)), var45(x), var92(x)))),
	ForAll([x], Not(Or(Not(var22(x)), Not(var98(x)), Not(var90(x)), var233(x)))),
	ForAll([x], Not(Or(Not(var58(x)), Not(var148(x)), var227(x), var165(x)))),
	ForAll([x], Not(Or(Not(var207(x)), Not(var143(x)), Not(var72(x)), var157(x)))),
	ForAll([x], Not(Or(var223(x), Not(var2(x)), Not(var189(x)), var190(x)))),
	ForAll([x], Not(Or(Not(var167(x)), var26(x), var192(x), Not(var19(x))))),
	ForAll([x], Not(Or(var240(x), var109(x), var48(x), Not(var126(x))))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var25(x)), Not(var132(x)), Not(var219(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var119(x1)), Or(var19(x), var216(x), Not(var167(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var163(x1)), var231(x1), var60(x1)), Not(var89(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var120(x1), Or(var34(x), Not(var229(x)), var191(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var93(x1)), var118(x1), var60(x1)), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var172(x1)), Not(var173(x1))), Or(Not(var229(x)), Not(var104(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var177(x1)), Or(Not(var28(x)), var169(x), var33(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var143(x1), var7(x1)), Or(var87(x), Not(var36(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var112(x1), var247(x1), Not(var116(x1))), Not(var117(x)))))),
	ForAll([x], Not(Or(Not(var156(x)), Not(var105(x)), Not(var113(x)), var137(x), var33(x), Not(var9(x))))),
	ForAll([x], Not(Or(var50(x), var57(x), Not(var81(x)), Not(var93(x)), var32(x), Not(var196(x))))),
	ForAll([x], Not(Or(Not(var167(x)), var240(x), Not(var213(x)), Not(var121(x)), Not(var235(x)), var88(x)))),
	ForAll([x], Not(Or(var207(x), var166(x), Not(var60(x)), Not(var249(x)), Not(var235(x)), Not(var35(x))))),
	ForAll([x], Not(Or(var224(x), Not(var115(x)), var164(x), Not(var95(x)), var75(x), var21(x)))),
	ForAll([x], Not(Or(Not(var87(x)), var186(x), Not(var16(x)), Not(var118(x)), var104(x), var120(x)))),
	ForAll([x], Not(Or(Not(var161(x)), var178(x), var135(x), Not(var166(x)), var98(x), Not(var236(x))))),
	ForAll([x], Not(Or(var215(x), var65(x), Not(var230(x)), var56(x), Not(var35(x)), Not(var198(x))))),
	ForAll([x], Not(Or(var59(x), var235(x), Not(var183(x)), var101(x), Not(var98(x)), var217(x)))),
	ForAll([x], Not(Or(var59(x), Not(var6(x)), Not(var196(x)), Not(var21(x)), Not(var126(x)), var15(x)))),
	ForAll([x], Not(Or(Not(var76(x)), var138(x), var131(x), var223(x), var79(x), var92(x)))),
	ForAll([x], Not(Or(var121(x), var5(x), var219(x), Not(var236(x)), var222(x), Not(var126(x))))),
	ForAll([x], Not(Or(var216(x), Not(var66(x)), Not(var108(x)), Not(var237(x)), Not(var72(x)), Not(var121(x))))),
	ForAll([x], Not(Or(Not(var130(x)), Not(var227(x)), Not(var20(x)), Not(var241(x)), Not(var156(x)), var143(x)))),
	ForAll([x], Not(Or(Not(var196(x)), var218(x), var9(x), var14(x), var217(x), Not(var80(x))))),
	ForAll([x], Not(Or(Not(var226(x)), Not(var166(x)), Not(var188(x)), Not(var221(x)), Not(var182(x)), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var243(x)), var237(x), var130(x), var202(x), Not(var176(x)), Not(var198(x))))),
	ForAll([x], Not(Or(Not(var9(x)), Not(var243(x)), Not(var33(x)), Not(var135(x)), var215(x), var67(x)))),
	ForAll([x], Not(Or(Not(var219(x)), var165(x), Not(var46(x)), var161(x), Not(var175(x)), var61(x)))),
	ForAll([x], Not(Or(var239(x), var129(x), Not(var225(x)), var36(x), var219(x), var110(x)))),
	ForAll([x], Not(Or(Not(var148(x)), Not(var157(x)), var111(x), var128(x), Not(var215(x)), Not(var122(x))))),
	ForAll([x], Not(Or(var192(x), Not(var184(x)), Not(var199(x)), var230(x), var134(x), var11(x)))),
	ForAll([x], Not(Or(Not(var66(x)), var86(x), Not(var135(x)), var38(x), var143(x), var208(x)))),
	ForAll([x], Not(Or(var204(x), Not(var4(x)), Not(var18(x)), Not(var135(x)), Not(var154(x)), var2(x)))),
	ForAll([x], Not(Or(Not(var171(x)), Not(var131(x)), Not(var116(x)), Not(var35(x)), var66(x), Not(var249(x))))),
	ForAll([x], Not(Or(Not(var60(x)), var240(x), Not(var30(x)), var3(x), Not(var61(x)), Not(var167(x))))),
	ForAll([x], Not(Or(var232(x), var213(x), var15(x), Not(var184(x)), Not(var229(x)), var19(x)))),
	ForAll([x], Not(Or(var151(x), var24(x), var92(x), var16(x), var230(x), var164(x)))),
	ForAll([x], Not(Or(var221(x), var143(x), var96(x), Not(var229(x)), Not(var23(x)), Not(var68(x))))),
	ForAll([x], Not(Or(Not(var209(x)), Not(var192(x)), Not(var97(x)), Not(var223(x)), var109(x), Not(var152(x))))),
	ForAll([x], Not(Or(Not(var1(x)), Not(var41(x)), var200(x), Not(var157(x)), Not(var194(x)), Not(var230(x))))),
	ForAll([x], Not(Or(Not(var142(x)), var199(x), Not(var21(x)), Not(var79(x)), var20(x), var39(x)))),
	ForAll([x], Not(Or(Not(var199(x)), var175(x), var219(x), Not(var241(x)), Not(var113(x)), Not(var249(x))))),
	ForAll([x], Not(Or(Not(var20(x)), Not(var109(x)), Not(var124(x)), var97(x), var153(x), var219(x)))),
	ForAll([x], Not(Or(Not(var197(x)), var104(x), var123(x), var7(x), var188(x), var15(x)))),
	ForAll([x], Not(Or(Not(var39(x)), var63(x), Not(var119(x)), Not(var11(x)), var214(x), var73(x)))),
	ForAll([x], Not(Or(var167(x), Not(var90(x)), Not(var250(x)), var234(x), var223(x), Not(var123(x))))),
	ForAll([x], Not(Or(Not(var41(x)), var78(x), var208(x), Not(var44(x)), Not(var4(x)), Not(var94(x))))),
	ForAll([x], Not(Or(Not(var163(x)), var47(x), Not(var103(x)), var51(x), var55(x), Not(var40(x))))),
	ForAll([x], Not(Or(var72(x), Not(var43(x)), var1(x), var15(x), Not(var152(x)), Not(var202(x))))),
	ForAll([x], Not(Or(var61(x), Not(var18(x)), var102(x), var4(x), var168(x), var22(x)))),
	ForAll([x], Not(Or(var202(x), Not(var64(x)), Not(var6(x)), Not(var61(x)), Not(var171(x)), var97(x)))),
	ForAll([x], Not(Or(Not(var201(x)), var33(x), Not(var215(x)), Not(var187(x)), Not(var206(x)), Not(var242(x))))),
	ForAll([x], Not(Or(var77(x), var224(x), Not(var233(x)), var237(x), var183(x), Not(var232(x))))),
	ForAll([x], Not(Or(var8(x), Not(var239(x)), Not(var50(x)), var167(x), var170(x), var196(x)))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var98(x)), var224(x), Not(var187(x)), var242(x), var168(x)))),
	ForAll([x], Not(Or(var243(x), var58(x), var31(x), Not(var34(x)), var145(x), Not(var108(x))))),
	ForAll([x], Not(Or(Not(var202(x)), var26(x), Not(var141(x)), var52(x), Not(var3(x)), var115(x)))),
	ForAll([x], Not(Or(Not(var229(x)), Not(var135(x)), var194(x), var215(x), Not(var167(x)), var88(x)))),
	ForAll([x], Not(Or(var198(x), var222(x), Not(var103(x)), var21(x), var181(x), Not(var46(x))))),
	ForAll([x], Not(Or(Not(var141(x)), var15(x), var22(x), var36(x), Not(var13(x)), Not(var163(x))))),
	ForAll([x], Not(Or(var114(x), Not(var95(x)), var120(x), Not(var184(x)), var154(x), Not(var239(x))))),
	ForAll([x], Not(Or(Not(var68(x)), Not(var72(x)), var69(x), Not(var245(x)), Not(var102(x)), var123(x)))),
	ForAll([x], Not(Or(var246(x), var36(x), Not(var37(x)), var248(x), var231(x), var200(x)))),
	ForAll([x], Not(Or(Not(var85(x)), var228(x), Not(var229(x)), var143(x), Not(var67(x)), Not(var119(x))))),
	ForAll([x], Not(Or(var164(x), var131(x), Not(var3(x)), var62(x), var124(x), var133(x)))),
	ForAll([x], Not(Or(Not(var11(x)), var96(x), var99(x), var75(x), Not(var56(x)), Not(var242(x))))),
	ForAll([x], Not(Or(Not(var92(x)), Not(var232(x)), Not(var171(x)), var87(x), Not(var140(x)), Not(var240(x))))),
	ForAll([x], Not(Or(Not(var188(x)), var3(x), Not(var123(x)), var239(x), var157(x), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var48(x)), Not(var139(x)), var26(x), Not(var244(x)), Not(var206(x)), Not(var191(x))))),
	ForAll([x], Not(Or(Not(var107(x)), var58(x), Not(var121(x)), var226(x), Not(var212(x)), Not(var131(x))))),
	ForAll([x], Not(Or(var166(x), Not(var141(x)), var145(x), var66(x), Not(var183(x)), var106(x)))),
	ForAll([x], Not(Or(var52(x), Not(var108(x)), Not(var15(x)), var25(x), var166(x), Not(var240(x))))),
	ForAll([x], Not(Or(var200(x), Not(var187(x)), Not(var171(x)), Not(var27(x)), Not(var91(x)), var16(x)))),
	ForAll([x], Not(Or(var46(x), Not(var205(x)), Not(var111(x)), var212(x), Not(var38(x)), Not(var76(x))))),
	ForAll([x], Not(Or(var116(x), Not(var153(x)), var196(x), var69(x), var132(x), var75(x)))),
	ForAll([x], Not(Or(var93(x), Not(var249(x)), Not(var226(x)), var151(x), Not(var208(x)), Not(var209(x))))),
	ForAll([x], Not(Or(var187(x), var119(x), Not(var126(x)), var250(x), Not(var100(x)), Not(var142(x))))),
	ForAll([x], Not(Or(Not(var94(x)), Not(var136(x)), var130(x), Not(var249(x)), Not(var216(x)), Not(var85(x))))),
	ForAll([x], Not(Or(Not(var159(x)), var157(x), var49(x), Not(var220(x)), var188(x), var1(x)))),
	ForAll([x], Not(Or(Not(var238(x)), var19(x), Not(var239(x)), Not(var234(x)), Not(var214(x)), var128(x)))),
	ForAll([x], Not(Or(var58(x), Not(var221(x)), var136(x), Not(var179(x)), Not(var106(x)), Not(var197(x))))),
	ForAll([x], Not(Or(Not(var249(x)), var182(x), var120(x), Not(var63(x)), Not(var51(x)), Not(var111(x))))),
	ForAll([x], Not(Or(Not(var222(x)), Not(var201(x)), Not(var168(x)), Not(var157(x)), Not(var151(x)), Not(var245(x))))),
	ForAll([x], Not(Or(var128(x), Not(var39(x)), Not(var86(x)), Not(var175(x)), var221(x), var209(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var172(x1)), Not(var218(x1)), var18(x1), var237(x1)), Or(var248(x), var85(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var10(x1)), var16(x1), Not(var222(x1))), Or(var108(x), var89(x), Not(var198(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var216(x1), var49(x1), Not(var63(x1))), Or(Not(var192(x)), Not(var228(x)), var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var236(x1), Not(var189(x1)), Not(var123(x1)), var153(x1), var99(x1)), var184(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var140(x1)), Not(var131(x1)), Not(var184(x1))), Or(var22(x), Not(var91(x)), Not(var94(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var50(x1), var80(x1), var156(x1), var164(x1)), Or(var2(x), Not(var160(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var97(x1), Not(var231(x1))), Or(var205(x), var232(x), Not(var136(x)), Not(var2(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var185(x1), Or(var232(x), Not(var195(x)), Not(var14(x)), Not(var54(x)), Not(var56(x))))))),
	ForAll([x], Not(Or(Not(var189(x)), var146(x), var234(x), var86(x), Not(var139(x)), Not(var136(x)), var80(x), Not(var168(x))))),
	ForAll([x], Not(Or(var104(x), Not(var12(x)), Not(var151(x)), var51(x), var232(x), var141(x), Not(var119(x)), Not(var195(x))))),
	ForAll([x], Not(Or(var152(x), var46(x), var218(x), var44(x), var64(x), Not(var165(x)), Not(var153(x)), var50(x)))),
	ForAll([x], Not(Or(Not(var209(x)), Not(var130(x)), var202(x), var154(x), Not(var229(x)), Not(var65(x)), Not(var121(x)), var3(x)))),
	ForAll([x], Not(Or(var204(x), Not(var216(x)), var247(x), var237(x), var179(x), var19(x), Not(var152(x)), Not(var180(x))))),
	ForAll([x], Not(Or(var161(x), Not(var7(x)), var170(x), var234(x), var130(x), Not(var208(x)), Not(var116(x)), var79(x)))),
	ForAll([x], Not(Or(Not(var119(x)), Not(var249(x)), var15(x), Not(var246(x)), var232(x), Not(var65(x)), Not(var223(x)), Not(var129(x))))),
	ForAll([x], Not(Or(var160(x), Not(var240(x)), var76(x), Not(var165(x)), Not(var32(x)), var109(x), Not(var178(x)), Not(var218(x))))),
	ForAll([x], Not(Or(var73(x), var194(x), Not(var231(x)), Not(var12(x)), var135(x), Not(var158(x)), Not(var173(x)), var32(x)))),
	ForAll([x], Not(Or(var39(x), var176(x), var161(x), var206(x), var54(x), Not(var29(x)), var223(x), Not(var205(x))))),
	ForAll([x], Not(Or(var143(x), Not(var48(x)), Not(var104(x)), Not(var214(x)), Not(var31(x)), Not(var153(x)), Not(var183(x)), var51(x)))),
	ForAll([x], Not(Or(Not(var215(x)), var37(x), var99(x), Not(var69(x)), Not(var189(x)), var243(x), Not(var6(x)), var47(x)))),
	ForAll([x], Not(Or(var156(x), Not(var22(x)), Not(var174(x)), Not(var140(x)), var78(x), Not(var40(x)), var211(x), var27(x)))),
	ForAll([x], Not(Or(var247(x), var209(x), var162(x), var238(x), var173(x), Not(var92(x)), Not(var87(x)), var192(x)))),
	ForAll([x], Not(Or(var208(x), var9(x), var185(x), var169(x), Not(var85(x)), Not(var1(x)), Not(var213(x)), var116(x)))),
	ForAll([x], Not(Or(Not(var75(x)), Not(var204(x)), Not(var225(x)), Not(var27(x)), var205(x), var139(x), Not(var111(x)), Not(var9(x))))),
	ForAll([x], Not(Or(Not(var202(x)), Not(var235(x)), var30(x), var131(x), Not(var239(x)), Not(var134(x)), var175(x), Not(var232(x))))),
	ForAll([x], Not(Or(Not(var35(x)), var15(x), Not(var75(x)), Not(var8(x)), var237(x), Not(var113(x)), Not(var216(x)), var31(x)))),
	ForAll([x], Not(Or(Not(var191(x)), Not(var149(x)), Not(var157(x)), var224(x), var139(x), var90(x), Not(var70(x)), var209(x)))),
	ForAll([x], Not(Or(var157(x), Not(var114(x)), var79(x), var202(x), Not(var169(x)), Not(var84(x)), Not(var242(x)), Not(var72(x))))),
	ForAll([x], Not(Or(Not(var210(x)), Not(var12(x)), Not(var162(x)), var104(x), var8(x), Not(var105(x)), var238(x), var137(x)))),
	ForAll([x], Not(Or(var160(x), Not(var236(x)), var32(x), var81(x), Not(var152(x)), var115(x), Not(var250(x)), Not(var222(x))))),
	ForAll([x], Not(Or(Not(var55(x)), var31(x), var13(x), Not(var140(x)), var214(x), Not(var236(x)), var70(x), var22(x)))),
	ForAll([x], Not(Or(Not(var127(x)), var227(x), var75(x), var103(x), Not(var58(x)), var32(x), var232(x), var115(x)))),
	ForAll([x], Not(Or(Not(var134(x)), var212(x), var225(x), Not(var22(x)), var119(x), var125(x), var21(x), var241(x)))),
	ForAll([x], Not(Or(var126(x), Not(var110(x)), Not(var189(x)), Not(var250(x)), Not(var10(x)), Not(var166(x)), var96(x), var105(x)))),
	ForAll([x], Not(Or(var13(x), Not(var128(x)), Not(var32(x)), Not(var135(x)), Not(var208(x)), Not(var76(x)), Not(var200(x)), var97(x)))),
	ForAll([x], Not(Or(Not(var12(x)), Not(var122(x)), var246(x), Not(var101(x)), Not(var156(x)), Not(var210(x)), Not(var140(x)), Not(var160(x))))),
	ForAll([x], Not(Or(var223(x), Not(var128(x)), var158(x), Not(var196(x)), var232(x), Not(var122(x)), Not(var53(x)), var243(x)))),
	ForAll([x], Not(Or(var178(x), Not(var89(x)), Not(var182(x)), var84(x), Not(var237(x)), var225(x), Not(var247(x)), Not(var90(x))))),
	ForAll([x], Not(Or(Not(var236(x)), Not(var52(x)), var203(x), Not(var148(x)), Not(var117(x)), Not(var5(x)), var86(x), var175(x)))),
	ForAll([x], Not(Or(Not(var193(x)), var249(x), Not(var238(x)), Not(var47(x)), var43(x), var119(x), var173(x), var18(x)))),
	ForAll([x], Not(Or(var75(x), Not(var18(x)), Not(var73(x)), var67(x), var40(x), Not(var208(x)), var153(x), var72(x)))),
	ForAll([x], Not(Or(var36(x), Not(var77(x)), var79(x), var133(x), var83(x), Not(var183(x)), var205(x), Not(var151(x))))),
	ForAll([x], Not(Or(var7(x), var103(x), Not(var243(x)), Not(var164(x)), var123(x), Not(var163(x)), Not(var175(x)), var90(x)))),
	ForAll([x], Not(Or(Not(var168(x)), var133(x), Not(var77(x)), Not(var51(x)), var1(x), Not(var116(x)), Not(var74(x)), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var33(x)), var151(x), var209(x), Not(var194(x)), Not(var45(x)), Not(var121(x)), var60(x), var139(x)))),
	ForAll([x], Not(Or(Not(var161(x)), Not(var198(x)), var22(x), Not(var95(x)), Not(var128(x)), Not(var131(x)), Not(var15(x)), var146(x)))),
	ForAll([x], Not(Or(Not(var76(x)), Not(var64(x)), var81(x), var191(x), var9(x), Not(var221(x)), Not(var80(x)), var67(x)))),
	ForAll([x], Not(Or(Not(var197(x)), var193(x), var186(x), Not(var69(x)), var238(x), Not(var74(x)), Not(var51(x)), Not(var191(x))))),
	ForAll([x], Not(Or(Not(var2(x)), var236(x), var137(x), var89(x), Not(var78(x)), var246(x), var240(x), Not(var74(x))))),
	ForAll([x], Not(Or(var30(x), Not(var169(x)), var174(x), var244(x), var43(x), var148(x), Not(var140(x)), var124(x)))),
	ForAll([x], Not(Or(Not(var42(x)), var221(x), Not(var24(x)), Not(var170(x)), var26(x), var150(x), var203(x), Not(var104(x))))),
	ForAll([x], Not(Or(Not(var70(x)), Not(var139(x)), Not(var50(x)), Not(var149(x)), var45(x), var217(x), var138(x), Not(var117(x))))),
	ForAll([x], Not(Or(var141(x), var129(x), Not(var40(x)), Not(var160(x)), Not(var25(x)), Not(var108(x)), Not(var177(x)), var52(x)))),
	ForAll([x], Not(Or(var5(x), var42(x), Not(var127(x)), var188(x), var151(x), Not(var150(x)), Not(var153(x)), Not(var122(x))))),
	ForAll([x], Not(Or(Not(var146(x)), Not(var224(x)), var9(x), var125(x), var108(x), var244(x), Not(var87(x)), Not(var180(x))))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var99(x)), var190(x), Not(var249(x)), Not(var119(x)), Not(var232(x)), var95(x), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var76(x)), var49(x), var93(x), Not(var52(x)), Not(var86(x)), var46(x), var190(x), Not(var124(x))))),
	ForAll([x], Not(Or(var187(x), var212(x), Not(var97(x)), Not(var127(x)), Not(var70(x)), Not(var249(x)), Not(var215(x)), Not(var231(x))))),
	ForAll([x], Not(Or(Not(var140(x)), Not(var8(x)), Not(var15(x)), var45(x), Not(var34(x)), var12(x), var155(x), var74(x)))),
	ForAll([x], Not(Or(Not(var18(x)), Not(var207(x)), Not(var2(x)), Not(var21(x)), var53(x), var51(x), var175(x), var137(x)))),
	ForAll([x], Not(Or(Not(var70(x)), var84(x), var78(x), Not(var86(x)), Not(var221(x)), var87(x), var219(x), var231(x)))),
	ForAll([x], Not(Or(var225(x), var239(x), Not(var208(x)), var17(x), Not(var115(x)), var247(x), var232(x), var101(x)))),
	ForAll([x], Not(Or(Not(var136(x)), Not(var202(x)), var203(x), var179(x), var208(x), Not(var56(x)), Not(var235(x)), var102(x)))),
	ForAll([x], Not(Or(Not(var32(x)), var30(x), var230(x), Not(var21(x)), Not(var190(x)), var170(x), Not(var23(x)), var114(x)))),
	ForAll([x], Not(Or(Not(var90(x)), var75(x), var126(x), var4(x), Not(var154(x)), var91(x), Not(var110(x)), Not(var244(x))))),
	ForAll([x], Not(Or(Not(var15(x)), var137(x), var132(x), Not(var231(x)), Not(var160(x)), var37(x), var130(x), Not(var144(x))))),
	ForAll([x], Not(Or(var211(x), var155(x), var80(x), var17(x), var63(x), var9(x), Not(var172(x)), var49(x)))),
	ForAll([x], Not(Or(var230(x), Not(var101(x)), var17(x), Not(var164(x)), var245(x), Not(var178(x)), var14(x), var127(x)))),
	ForAll([x], Not(Or(var79(x), var204(x), Not(var239(x)), Not(var4(x)), Not(var47(x)), var90(x), var38(x), var22(x)))),
	ForAll([x], Not(Or(Not(var88(x)), Not(var76(x)), Not(var65(x)), var179(x), var239(x), Not(var87(x)), var225(x), var153(x)))),
	ForAll([x], Not(Or(Not(var156(x)), Not(var117(x)), Not(var237(x)), var111(x), var228(x), Not(var216(x)), var22(x), Not(var126(x))))),
	ForAll([x], Not(Or(Not(var171(x)), Not(var4(x)), var164(x), var77(x), var37(x), Not(var232(x)), var221(x), var148(x)))),
	ForAll([x], Not(Or(Not(var100(x)), Not(var84(x)), Not(var67(x)), Not(var46(x)), var191(x), var151(x), Not(var11(x)), var217(x)))),
	ForAll([x], Not(Or(Not(var82(x)), var203(x), Not(var136(x)), var169(x), Not(var119(x)), Not(var200(x)), var4(x), var8(x)))),
	ForAll([x], Not(Or(Not(var25(x)), Not(var233(x)), var232(x), Not(var112(x)), Not(var213(x)), var151(x), var60(x), Not(var54(x))))),
	ForAll([x], Not(Or(Not(var173(x)), var217(x), Not(var189(x)), Not(var51(x)), Not(var125(x)), var32(x), var42(x), var79(x)))),
	ForAll([x], Not(Or(Not(var98(x)), Not(var73(x)), var28(x), Not(var195(x)), Not(var140(x)), Not(var186(x)), Not(var63(x)), var145(x)))),
	ForAll([x], Not(Or(var217(x), var194(x), Not(var61(x)), var197(x), var26(x), var68(x), Not(var107(x)), Not(var147(x))))),
	ForAll([x], Not(Or(var209(x), var102(x), Not(var65(x)), Not(var152(x)), Not(var79(x)), Not(var67(x)), Not(var25(x)), var34(x)))),
	ForAll([x], Not(Or(var229(x), var210(x), Not(var21(x)), Not(var225(x)), var245(x), Not(var213(x)), Not(var168(x)), var55(x)))),
	ForAll([x], Not(Or(Not(var25(x)), var36(x), var33(x), var132(x), var80(x), Not(var208(x)), var14(x), Not(var187(x))))),
	ForAll([x], Not(Or(Not(var245(x)), Not(var74(x)), var180(x), var237(x), Not(var53(x)), Not(var31(x)), var230(x), Not(var150(x))))),
	ForAll([x], Not(Or(Not(var133(x)), Not(var31(x)), Not(var24(x)), Not(var215(x)), Not(var9(x)), Not(var59(x)), var249(x), var129(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var101(x1), var6(x1)), Or(Not(var115(x)), var104(x), Not(var131(x)), Not(var21(x)), var22(x), var179(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var182(x1), Not(var174(x1)), var241(x1)), Or(Not(var61(x)), var82(x), var67(x), Not(var80(x)), var78(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var245(x1), Not(var169(x1)), var239(x1)), Or(var76(x), var13(x), Not(var149(x)), var90(x), var146(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var15(x1), var17(x1), var159(x1)), Or(var162(x), Not(var207(x)), var228(x), Not(var85(x)), Not(var182(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var89(x1), Not(var90(x1)), var120(x1), var225(x1)), Or(Not(var113(x)), var130(x), Not(var218(x)), Not(var3(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var44(x1)), Not(var142(x1)), var70(x1), var36(x1), Not(var133(x1)), Not(var117(x1))), Or(var72(x), var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var224(x1)), Not(var85(x1)), var49(x1), var102(x1), Not(var140(x1)), var109(x1), var48(x1)), Not(var200(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var162(x1), var245(x1), var80(x1), var81(x1), Not(var199(x1)), Not(var11(x1)), var41(x1)), Not(var189(x)))))),
	ForAll([x], Not(Or(var16(x), Not(var210(x)), Not(var159(x)), Not(var119(x)), var54(x), Not(var60(x)), var218(x), var223(x), Not(var24(x)), Not(var149(x))))),
	ForAll([x], Not(Or(var234(x), var75(x), var155(x), Not(var169(x)), var196(x), var202(x), Not(var153(x)), var124(x), var100(x), Not(var55(x))))),
	ForAll([x], Not(Or(var225(x), var158(x), var150(x), var133(x), var110(x), Not(var90(x)), var119(x), Not(var217(x)), Not(var164(x)), Not(var6(x))))),
	ForAll([x], Not(Or(var105(x), var173(x), Not(var250(x)), Not(var35(x)), Not(var197(x)), Not(var141(x)), Not(var78(x)), var235(x), var152(x), var149(x)))),
	ForAll([x], Not(Or(Not(var67(x)), var213(x), var233(x), var184(x), var176(x), Not(var30(x)), Not(var158(x)), var250(x), Not(var106(x)), var153(x)))),
	ForAll([x], Not(Or(Not(var244(x)), Not(var170(x)), Not(var81(x)), Not(var234(x)), Not(var109(x)), Not(var115(x)), var185(x), Not(var114(x)), Not(var62(x)), var156(x)))),
	ForAll([x], Not(Or(var97(x), Not(var26(x)), Not(var228(x)), var63(x), Not(var58(x)), Not(var223(x)), Not(var156(x)), Not(var151(x)), var171(x), Not(var47(x))))),
	ForAll([x], Not(Or(Not(var50(x)), Not(var37(x)), var18(x), Not(var185(x)), var9(x), Not(var158(x)), Not(var41(x)), var205(x), var155(x), Not(var96(x))))),
	ForAll([x], Not(Or(Not(var233(x)), var235(x), Not(var22(x)), var248(x), var93(x), var112(x), Not(var202(x)), Not(var218(x)), Not(var125(x)), var161(x)))),
	ForAll([x], Not(Or(Not(var140(x)), var157(x), Not(var152(x)), var95(x), Not(var13(x)), Not(var216(x)), Not(var70(x)), var240(x), var90(x), var186(x)))),
	ForAll([x], Not(Or(Not(var36(x)), var249(x), Not(var172(x)), Not(var191(x)), Not(var210(x)), Not(var2(x)), Not(var42(x)), Not(var208(x)), Not(var178(x)), Not(var179(x))))),
	ForAll([x], Not(Or(Not(var103(x)), Not(var138(x)), Not(var85(x)), var136(x), var144(x), var3(x), Not(var216(x)), var130(x), Not(var208(x)), var131(x)))),
	ForAll([x], Not(Or(var168(x), var21(x), var167(x), Not(var54(x)), var202(x), var235(x), Not(var244(x)), Not(var222(x)), Not(var100(x)), var135(x)))),
	ForAll([x], Not(Or(Not(var226(x)), Not(var159(x)), Not(var13(x)), var79(x), var176(x), Not(var5(x)), var123(x), Not(var213(x)), var112(x), Not(var244(x))))),
	ForAll([x], Not(Or(Not(var145(x)), Not(var136(x)), Not(var215(x)), Not(var67(x)), var11(x), var24(x), Not(var146(x)), var164(x), Not(var95(x)), Not(var7(x))))),
	ForAll([x], Not(Or(var228(x), Not(var183(x)), var132(x), var9(x), var118(x), var184(x), var150(x), Not(var181(x)), var191(x), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var225(x)), var58(x), var202(x), Not(var126(x)), Not(var249(x)), var175(x), Not(var172(x)), Not(var32(x)), Not(var100(x)), var80(x)))),
	ForAll([x], Not(Or(Not(var69(x)), var163(x), var77(x), Not(var5(x)), Not(var204(x)), Not(var35(x)), var48(x), var43(x), var198(x), Not(var142(x))))),
	ForAll([x], Not(Or(Not(var73(x)), Not(var239(x)), var131(x), var207(x), Not(var249(x)), var11(x), Not(var47(x)), var181(x), Not(var40(x)), var12(x)))),
	ForAll([x], Not(Or(var244(x), var158(x), var92(x), Not(var75(x)), Not(var127(x)), Not(var12(x)), Not(var149(x)), var31(x), var3(x), Not(var35(x))))),
	ForAll([x], Not(Or(var217(x), Not(var37(x)), var244(x), var203(x), Not(var58(x)), var42(x), Not(var99(x)), Not(var218(x)), Not(var159(x)), Not(var241(x))))),
	ForAll([x], Not(Or(Not(var76(x)), var196(x), var140(x), Not(var150(x)), Not(var238(x)), Not(var179(x)), Not(var2(x)), Not(var63(x)), var244(x), var199(x)))),
	ForAll([x], Not(Or(var45(x), var39(x), Not(var30(x)), Not(var57(x)), Not(var141(x)), Not(var197(x)), Not(var23(x)), Not(var244(x)), Not(var70(x)), var41(x)))),
	ForAll([x], Not(Or(var245(x), Not(var111(x)), var41(x), Not(var205(x)), Not(var14(x)), var114(x), Not(var181(x)), Not(var142(x)), Not(var28(x)), Not(var247(x))))),
	ForAll([x], Not(Or(var194(x), Not(var240(x)), Not(var241(x)), Not(var245(x)), Not(var153(x)), Not(var228(x)), var119(x), Not(var69(x)), var192(x), var35(x)))),
	ForAll([x], Not(Or(var146(x), Not(var16(x)), var63(x), Not(var202(x)), var36(x), var180(x), Not(var155(x)), Not(var13(x)), var120(x), Not(var93(x))))),
	ForAll([x], Not(Or(Not(var119(x)), Not(var49(x)), var107(x), var243(x), Not(var122(x)), var234(x), var222(x), var48(x), Not(var90(x)), Not(var199(x))))),
	ForAll([x], Not(Or(Not(var35(x)), var5(x), Not(var86(x)), Not(var231(x)), var133(x), var112(x), Not(var58(x)), var33(x), Not(var90(x)), var55(x)))),
	ForAll([x], Not(Or(var113(x), Not(var124(x)), var125(x), var187(x), Not(var101(x)), var13(x), var29(x), var48(x), var133(x), var219(x)))),
	ForAll([x], Not(Or(var53(x), Not(var22(x)), Not(var40(x)), Not(var161(x)), var118(x), Not(var45(x)), Not(var201(x)), var4(x), var175(x), Not(var174(x))))),
	ForAll([x], Not(Or(var37(x), var170(x), var200(x), Not(var155(x)), Not(var114(x)), var115(x), var143(x), var131(x), var106(x), var241(x)))),
	ForAll([x], Not(Or(var90(x), Not(var123(x)), Not(var199(x)), var236(x), var101(x), var196(x), var100(x), Not(var51(x)), Not(var228(x)), Not(var172(x))))),
	ForAll([x], Not(Or(Not(var117(x)), Not(var193(x)), Not(var129(x)), var229(x), Not(var63(x)), var228(x), Not(var12(x)), Not(var138(x)), var71(x), var172(x)))),
	ForAll([x], Not(Or(var229(x), Not(var3(x)), var231(x), var182(x), var123(x), Not(var122(x)), Not(var74(x)), var84(x), var170(x), var247(x)))),
	ForAll([x], Not(Or(Not(var194(x)), Not(var38(x)), Not(var70(x)), var219(x), var88(x), var161(x), var185(x), var22(x), var58(x), Not(var136(x))))),
	ForAll([x], Not(Or(var103(x), var6(x), var244(x), Not(var183(x)), Not(var50(x)), var173(x), Not(var241(x)), var21(x), var188(x), var182(x)))),
	ForAll([x], Not(Or(Not(var230(x)), Not(var64(x)), var17(x), Not(var189(x)), Not(var27(x)), Not(var153(x)), var143(x), var236(x), Not(var55(x)), var124(x)))),
	ForAll([x], Not(Or(var207(x), var94(x), Not(var39(x)), var238(x), Not(var141(x)), Not(var140(x)), Not(var7(x)), var64(x), var162(x), var151(x)))),
	ForAll([x], Not(Or(var187(x), Not(var112(x)), var118(x), var22(x), var43(x), Not(var37(x)), Not(var71(x)), var63(x), var136(x), Not(var94(x))))),
	ForAll([x], Not(Or(var11(x), var189(x), var168(x), var180(x), Not(var226(x)), Not(var106(x)), Not(var175(x)), var76(x), Not(var33(x)), var139(x)))),
	ForAll([x], Not(Or(var245(x), Not(var125(x)), var130(x), var35(x), var161(x), Not(var127(x)), var28(x), Not(var47(x)), var14(x), var29(x)))),
	ForAll([x], Not(Or(Not(var157(x)), Not(var145(x)), var67(x), Not(var13(x)), var41(x), var81(x), Not(var73(x)), var184(x), var204(x), var208(x)))),
	ForAll([x], Not(Or(Not(var13(x)), var212(x), Not(var12(x)), var131(x), Not(var63(x)), Not(var27(x)), var203(x), Not(var243(x)), Not(var224(x)), Not(var135(x))))),
	ForAll([x], Not(Or(Not(var196(x)), Not(var12(x)), var63(x), var167(x), var27(x), var69(x), Not(var26(x)), var24(x), Not(var158(x)), var163(x)))),
	ForAll([x], Not(Or(Not(var90(x)), Not(var128(x)), var77(x), var206(x), Not(var243(x)), Not(var158(x)), Not(var130(x)), Not(var76(x)), var168(x), var38(x)))),
	ForAll([x], Not(Or(var145(x), var87(x), var125(x), var231(x), var164(x), Not(var246(x)), Not(var81(x)), Not(var57(x)), Not(var117(x)), Not(var147(x))))),
	ForAll([x], Not(Or(var208(x), Not(var150(x)), var141(x), var149(x), Not(var126(x)), Not(var187(x)), Not(var10(x)), var61(x), Not(var182(x)), var94(x)))),
	ForAll([x], Not(Or(Not(var201(x)), var212(x), var53(x), var181(x), var93(x), var166(x), Not(var190(x)), var160(x), Not(var129(x)), var33(x)))),
	ForAll([x], Not(Or(var180(x), Not(var116(x)), Not(var195(x)), var72(x), var182(x), Not(var174(x)), var184(x), Not(var194(x)), Not(var230(x)), Not(var119(x))))),
	ForAll([x], Not(Or(Not(var130(x)), var58(x), var19(x), var107(x), Not(var38(x)), Not(var30(x)), var217(x), Not(var190(x)), var16(x), Not(var134(x))))),
	ForAll([x], Not(Or(Not(var227(x)), var138(x), Not(var19(x)), Not(var51(x)), Not(var96(x)), Not(var26(x)), Not(var74(x)), Not(var238(x)), var123(x), var224(x)))),
	ForAll([x], Not(Or(Not(var142(x)), Not(var50(x)), Not(var217(x)), var107(x), Not(var7(x)), var74(x), var17(x), Not(var47(x)), var241(x), Not(var60(x))))),
	ForAll([x], Not(Or(Not(var48(x)), Not(var33(x)), var206(x), Not(var54(x)), var66(x), Not(var101(x)), Not(var127(x)), var141(x), var118(x), Not(var95(x))))),
	ForAll([x], Not(Or(var71(x), Not(var250(x)), var25(x), Not(var8(x)), var240(x), Not(var84(x)), Not(var107(x)), Not(var5(x)), var187(x), var199(x)))),
	ForAll([x], Not(Or(var56(x), Not(var38(x)), Not(var196(x)), var141(x), Not(var70(x)), var15(x), var184(x), Not(var247(x)), var108(x), var12(x)))),
	ForAll([x], Not(Or(var73(x), Not(var38(x)), Not(var130(x)), var70(x), Not(var125(x)), var138(x), var174(x), Not(var210(x)), var200(x), var203(x)))),
	ForAll([x], Not(Or(Not(var132(x)), var89(x), Not(var118(x)), var112(x), Not(var159(x)), Not(var13(x)), Not(var41(x)), Not(var138(x)), var101(x), var32(x)))),
	ForAll([x], Not(Or(Not(var247(x)), Not(var225(x)), var68(x), var116(x), Not(var134(x)), var69(x), Not(var122(x)), var133(x), Not(var190(x)), var143(x)))),
	ForAll([x], Not(Or(Not(var96(x)), var226(x), Not(var82(x)), var214(x), var215(x), var178(x), var97(x), Not(var163(x)), var40(x), Not(var165(x))))),
	ForAll([x], Not(Or(Not(var146(x)), var140(x), Not(var51(x)), Not(var212(x)), var153(x), Not(var152(x)), Not(var45(x)), var182(x), Not(var247(x)), var28(x)))),
	ForAll([x], Not(Or(var98(x), var217(x), Not(var30(x)), Not(var93(x)), var162(x), var95(x), Not(var2(x)), var31(x), var131(x), Not(var181(x))))),
	ForAll([x], Not(Or(Not(var46(x)), Not(var169(x)), var191(x), Not(var12(x)), var198(x), Not(var62(x)), var95(x), Not(var148(x)), var43(x), var98(x)))),
	ForAll([x], Not(Or(var165(x), Not(var38(x)), Not(var53(x)), Not(var103(x)), Not(var10(x)), Not(var152(x)), var250(x), Not(var189(x)), Not(var236(x)), Not(var35(x))))),
	ForAll([x], Not(Or(Not(var167(x)), Not(var62(x)), var80(x), var71(x), Not(var46(x)), Not(var155(x)), Not(var61(x)), var214(x), var215(x), var37(x)))),
	ForAll([x], Not(Or(Not(var243(x)), var73(x), var164(x), Not(var88(x)), Not(var226(x)), Not(var170(x)), Not(var52(x)), Not(var49(x)), var166(x), var214(x)))),
	ForAll([x], Not(Or(Not(var1(x)), Not(var222(x)), Not(var237(x)), var136(x), var202(x), Not(var223(x)), var111(x), var103(x), Not(var64(x)), var198(x)))),
	ForAll([x], Not(Or(Not(var145(x)), Not(var173(x)), var168(x), Not(var88(x)), var176(x), Not(var150(x)), var39(x), Not(var197(x)), Not(var147(x)), var234(x)))),
	ForAll([x], Not(Or(Not(var25(x)), Not(var75(x)), var146(x), var123(x), Not(var180(x)), var151(x), Not(var105(x)), Not(var157(x)), var229(x), Not(var237(x))))),
	ForAll([x], Not(Or(var146(x), var154(x), Not(var204(x)), Not(var213(x)), var141(x), var28(x), var170(x), var41(x), var236(x), Not(var174(x))))),
	ForAll([x], Not(Or(var133(x), Not(var225(x)), Not(var118(x)), Not(var200(x)), Not(var89(x)), var126(x), Not(var196(x)), Not(var95(x)), var70(x), Not(var25(x))))),
	ForAll([x], Not(Or(Not(var20(x)), Not(var173(x)), var186(x), var213(x), var101(x), var68(x), Not(var217(x)), Not(var94(x)), Not(var54(x)), Not(var227(x))))),
	ForAll([x], Not(Or(var224(x), var220(x), var24(x), Not(var104(x)), var21(x), Not(var180(x)), Not(var179(x)), Not(var59(x)), Not(var39(x)), Not(var208(x))))),
	ForAll([x], Not(Or(Not(var213(x)), Not(var86(x)), var141(x), var101(x), Not(var158(x)), var187(x), Not(var50(x)), Not(var202(x)), Not(var186(x)), var123(x)))),
	ForAll([x], Not(Or(var225(x), Not(var250(x)), var23(x), var236(x), var150(x), var77(x), Not(var98(x)), var207(x), Not(var85(x)), var231(x)))),
	ForAll([x], Not(Or(var105(x), var170(x), Not(var165(x)), Not(var39(x)), Not(var121(x)), Not(var244(x)), Not(var128(x)), var144(x), var82(x), Not(var149(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var44(x1), Or(Not(var61(x)), Not(var96(x)), var184(x), Not(var39(x)), Not(var186(x)), var154(x), Not(var6(x)), var115(x), Not(var153(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var146(x1), var243(x1)), Or(var52(x), var145(x), var114(x), Not(var216(x)), Not(var37(x)), var34(x), var7(x), Not(var246(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var1(x1)), Not(var151(x1)), Not(var228(x1)), var198(x1)), Or(Not(var158(x)), var136(x), Not(var133(x)), Not(var17(x)), var245(x), Not(var59(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var66(x1)), var28(x1), Not(var50(x1)), var38(x1), Not(var90(x1)), Not(var51(x1)), var213(x1), Not(var145(x1))), Or(Not(var226(x)), Not(var122(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var237(x1)), Not(var66(x1)), var41(x1), Not(var186(x1)), var27(x1), var133(x1)), Or(var118(x), var165(x), Not(var221(x)), Not(var77(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var20(x1)), Not(var145(x1)), Not(var199(x1))), Or(var249(x), Not(var137(x)), Not(var165(x)), Not(var123(x)), Not(var100(x)), var215(x), var63(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var146(x1), Not(var185(x1)), Not(var184(x1)), var64(x1), var172(x1)), Or(var58(x), Not(var147(x)), var151(x), var248(x), Not(var125(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var183(x1)), Not(var188(x1)), Not(var239(x1)), Not(var42(x1)), Not(var10(x1)), Not(var46(x1))), Or(var199(x), Not(var233(x)), var153(x), Not(var206(x))))))),
	ForAll([x], Not(Or(Not(var10(x)), var44(x), var73(x), Not(var229(x)), var174(x), var9(x), var84(x), Not(var244(x))))),
	ForAll([x], Not(Or(Not(var136(x)), var164(x), var11(x), var110(x))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms0)
print(s.check())
print(s.statistics())
