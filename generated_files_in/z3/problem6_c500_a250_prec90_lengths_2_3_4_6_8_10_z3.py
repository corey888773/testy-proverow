from z3 import *

Object = DeclareSort('Object')

var243 = Function('var243', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var243(x), var201(x)))),
	ForAll([x], Not(Or(var211(x), var18(x)))),
	ForAll([x], Not(Or(var115(x), var121(x)))),
	ForAll([x], Not(Or(var22(x), Not(var195(x))))),
	ForAll([x], Not(Or(Not(var194(x)), Not(var172(x))))),
	ForAll([x], Not(Or(Not(var136(x)), Not(var158(x))))),
	ForAll([x], Not(Or(var18(x), var25(x)))),
	ForAll([x], Not(Or(Not(var163(x)), Not(var47(x))))),
	ForAll([x], Not(Or(Not(var211(x)), var162(x)))),
	ForAll([x], Not(Or(Not(var48(x)), var74(x)))),
	ForAll([x], Not(Or(var81(x), Not(var39(x))))),
	ForAll([x], Not(Or(var111(x), var29(x)))),
	ForAll([x], Not(Or(Not(var186(x)), Not(var99(x))))),
	ForAll([x], Not(Or(Not(var40(x)), Not(var84(x))))),
	ForAll([x], Not(Or(Not(var95(x)), Not(var240(x))))),
	ForAll([x], Not(Or(var115(x), Not(var60(x))))),
	ForAll([x], Not(Or(var232(x), Not(var206(x))))),
	ForAll([x], Not(Or(Not(var189(x)), var12(x)))),
	ForAll([x], Not(Or(var185(x), var200(x)))),
	ForAll([x], Not(Or(var166(x), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var117(x)), var15(x)))),
	ForAll([x], Not(Or(var13(x), var131(x)))),
	ForAll([x], Not(Or(var70(x), Not(var146(x))))),
	ForAll([x], Not(Or(Not(var68(x)), Not(var243(x))))),
	ForAll([x], Not(Or(var75(x), Not(var100(x))))),
	ForAll([x], Not(Or(var10(x), var124(x)))),
	ForAll([x], Not(Or(var40(x), var24(x)))),
	ForAll([x], Not(Or(var19(x), var247(x)))),
	ForAll([x], Not(Or(Not(var195(x)), var194(x)))),
	ForAll([x], Not(Or(var121(x), Not(var233(x))))),
	ForAll([x], Not(Or(var106(x), Not(var6(x))))),
	ForAll([x], Not(Or(var128(x), Not(var34(x))))),
	ForAll([x], Not(Or(var182(x), var212(x)))),
	ForAll([x], Not(Or(Not(var75(x)), Not(var3(x))))),
	ForAll([x], Not(Or(var248(x), var86(x)))),
	ForAll([x], Not(Or(var157(x), var226(x)))),
	ForAll([x], Not(Or(var24(x), var41(x)))),
	ForAll([x], Not(Or(Not(var154(x)), Not(var1(x))))),
	ForAll([x], Not(Or(var141(x), var238(x)))),
	ForAll([x], Not(Or(Not(var248(x)), var36(x)))),
	ForAll([x], Not(Or(Not(var45(x)), Not(var249(x))))),
	ForAll([x], Not(Or(Not(var91(x)), var206(x)))),
	ForAll([x], Not(Or(var247(x), Not(var4(x))))),
	ForAll([x], Not(Or(var35(x), Not(var74(x))))),
	ForAll([x], Not(Or(var164(x), Not(var126(x))))),
	ForAll([x], Not(Or(Not(var235(x)), Not(var220(x))))),
	ForAll([x], Not(Or(Not(var66(x)), var195(x)))),
	ForAll([x], Not(Or(Not(var20(x)), var211(x)))),
	ForAll([x], Not(Or(var11(x), var110(x)))),
	ForAll([x], Not(Or(Not(var105(x)), var249(x)))),
	ForAll([x], Not(Or(var1(x), Not(var123(x))))),
	ForAll([x], Not(Or(Not(var232(x)), var249(x)))),
	ForAll([x], Not(Or(Not(var236(x)), Not(var37(x))))),
	ForAll([x], Not(Or(var81(x), Not(var64(x))))),
	ForAll([x], Not(Or(var146(x), Not(var50(x))))),
	ForAll([x], Not(Or(Not(var208(x)), Not(var11(x))))),
	ForAll([x], Not(Or(var112(x), var46(x)))),
	ForAll([x], Not(Or(var36(x), Not(var213(x))))),
	ForAll([x], Not(Or(var234(x), Not(var4(x))))),
	ForAll([x], Not(Or(Not(var34(x)), Not(var153(x))))),
	ForAll([x], Not(Or(Not(var1(x)), Not(var84(x))))),
	ForAll([x], Not(Or(var231(x), var29(x)))),
	ForAll([x], Not(Or(Not(var48(x)), var123(x)))),
	ForAll([x], Not(Or(Not(var128(x)), var82(x)))),
	ForAll([x], Not(Or(var214(x), Not(var60(x))))),
	ForAll([x], Not(Or(var104(x), var156(x)))),
	ForAll([x], Not(Or(var35(x), var40(x)))),
	ForAll([x], Not(Or(Not(var213(x)), Not(var234(x))))),
	ForAll([x], Not(Or(Not(var100(x)), var193(x)))),
	ForAll([x], Not(Or(Not(var92(x)), Not(var20(x))))),
	ForAll([x], Not(Or(var212(x), var206(x)))),
	ForAll([x], Not(Or(var14(x), var64(x)))),
	ForAll([x], Not(Or(var77(x), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var50(x)), Not(var164(x))))),
	ForAll([x], Not(Or(var110(x), Not(var66(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var56(x1), var91(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var96(x1)), Not(var67(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var150(x1), Not(var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var143(x1), var100(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var249(x1)), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var52(x1), Not(var36(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var136(x1), var170(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var172(x1), var126(x))))),
	ForAll([x], Not(Or(Not(var166(x)), Not(var223(x)), Not(var117(x))))),
	ForAll([x], Not(Or(var29(x), Not(var77(x)), var101(x)))),
	ForAll([x], Not(Or(var18(x), var123(x), Not(var170(x))))),
	ForAll([x], Not(Or(var237(x), var82(x), var186(x)))),
	ForAll([x], Not(Or(Not(var66(x)), var247(x), var3(x)))),
	ForAll([x], Not(Or(Not(var127(x)), Not(var1(x)), Not(var248(x))))),
	ForAll([x], Not(Or(var136(x), var63(x), Not(var182(x))))),
	ForAll([x], Not(Or(var130(x), Not(var180(x)), Not(var43(x))))),
	ForAll([x], Not(Or(Not(var16(x)), Not(var136(x)), var153(x)))),
	ForAll([x], Not(Or(Not(var238(x)), Not(var160(x)), var22(x)))),
	ForAll([x], Not(Or(Not(var99(x)), var223(x), var53(x)))),
	ForAll([x], Not(Or(var143(x), var230(x), Not(var40(x))))),
	ForAll([x], Not(Or(var80(x), var153(x), Not(var90(x))))),
	ForAll([x], Not(Or(var14(x), Not(var175(x)), var219(x)))),
	ForAll([x], Not(Or(var61(x), Not(var76(x)), var83(x)))),
	ForAll([x], Not(Or(Not(var162(x)), var32(x), Not(var53(x))))),
	ForAll([x], Not(Or(var130(x), Not(var37(x)), Not(var101(x))))),
	ForAll([x], Not(Or(var90(x), var35(x), var111(x)))),
	ForAll([x], Not(Or(Not(var28(x)), Not(var35(x)), Not(var151(x))))),
	ForAll([x], Not(Or(Not(var25(x)), var122(x), var37(x)))),
	ForAll([x], Not(Or(var110(x), var168(x), var6(x)))),
	ForAll([x], Not(Or(var155(x), Not(var18(x)), Not(var180(x))))),
	ForAll([x], Not(Or(var24(x), Not(var6(x)), Not(var117(x))))),
	ForAll([x], Not(Or(var120(x), Not(var55(x)), var83(x)))),
	ForAll([x], Not(Or(var98(x), Not(var167(x)), Not(var13(x))))),
	ForAll([x], Not(Or(var101(x), var95(x), Not(var52(x))))),
	ForAll([x], Not(Or(var16(x), Not(var29(x)), Not(var157(x))))),
	ForAll([x], Not(Or(var165(x), var156(x), Not(var36(x))))),
	ForAll([x], Not(Or(Not(var110(x)), Not(var109(x)), Not(var105(x))))),
	ForAll([x], Not(Or(Not(var82(x)), Not(var194(x)), Not(var10(x))))),
	ForAll([x], Not(Or(var202(x), Not(var221(x)), Not(var80(x))))),
	ForAll([x], Not(Or(var7(x), Not(var128(x)), Not(var98(x))))),
	ForAll([x], Not(Or(Not(var105(x)), Not(var74(x)), var55(x)))),
	ForAll([x], Not(Or(Not(var181(x)), var134(x), Not(var96(x))))),
	ForAll([x], Not(Or(Not(var229(x)), var47(x), Not(var233(x))))),
	ForAll([x], Not(Or(Not(var119(x)), var249(x), var7(x)))),
	ForAll([x], Not(Or(var175(x), var37(x), var178(x)))),
	ForAll([x], Not(Or(Not(var131(x)), Not(var31(x)), Not(var93(x))))),
	ForAll([x], Not(Or(var151(x), var34(x), var235(x)))),
	ForAll([x], Not(Or(Not(var145(x)), var172(x), Not(var94(x))))),
	ForAll([x], Not(Or(var114(x), var174(x), Not(var3(x))))),
	ForAll([x], Not(Or(Not(var83(x)), var213(x), Not(var105(x))))),
	ForAll([x], Not(Or(Not(var98(x)), var225(x), var209(x)))),
	ForAll([x], Not(Or(var13(x), Not(var146(x)), var112(x)))),
	ForAll([x], Not(Or(var83(x), var139(x), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var79(x)), var8(x), var183(x)))),
	ForAll([x], Not(Or(Not(var236(x)), var216(x), var59(x)))),
	ForAll([x], Not(Or(Not(var99(x)), var42(x), var130(x)))),
	ForAll([x], Not(Or(Not(var143(x)), Not(var97(x)), var150(x)))),
	ForAll([x], Not(Or(var160(x), Not(var2(x)), var177(x)))),
	ForAll([x], Not(Or(var12(x), var138(x), Not(var125(x))))),
	ForAll([x], Not(Or(Not(var87(x)), var62(x), var40(x)))),
	ForAll([x], Not(Or(Not(var60(x)), Not(var76(x)), var190(x)))),
	ForAll([x], Not(Or(var200(x), Not(var208(x)), var77(x)))),
	ForAll([x], Not(Or(var85(x), var31(x), Not(var144(x))))),
	ForAll([x], Not(Or(var245(x), Not(var195(x)), Not(var196(x))))),
	ForAll([x], Not(Or(Not(var61(x)), Not(var8(x)), Not(var154(x))))),
	ForAll([x], Not(Or(Not(var79(x)), var147(x), Not(var21(x))))),
	ForAll([x], Not(Or(Not(var68(x)), var57(x), var143(x)))),
	ForAll([x], Not(Or(var194(x), var94(x), var243(x)))),
	ForAll([x], Not(Or(var48(x), var240(x), Not(var206(x))))),
	ForAll([x], Not(Or(Not(var3(x)), Not(var16(x)), var65(x)))),
	ForAll([x], Not(Or(var69(x), var6(x), Not(var170(x))))),
	ForAll([x], Not(Or(Not(var132(x)), var226(x), Not(var221(x))))),
	ForAll([x], Not(Or(var240(x), Not(var105(x)), var235(x)))),
	ForAll([x], Not(Or(Not(var206(x)), Not(var86(x)), Not(var51(x))))),
	ForAll([x], Not(Or(var134(x), var247(x), var182(x)))),
	ForAll([x], Not(Or(var226(x), Not(var70(x)), var48(x)))),
	ForAll([x], Not(Or(var145(x), Not(var73(x)), var124(x)))),
	ForAll([x], Not(Or(Not(var16(x)), var188(x), var2(x)))),
	ForAll([x], Not(Or(var214(x), var104(x), Not(var32(x))))),
	ForAll([x], Not(Or(Not(var106(x)), Not(var237(x)), Not(var199(x))))),
	ForAll([x], Not(Or(var97(x), Not(var82(x)), Not(var90(x))))),
	ForAll([x], Not(Or(var35(x), Not(var231(x)), Not(var143(x))))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var127(x)), var102(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var172(x1), Or(Not(var139(x)), var103(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var183(x1)), Or(var28(x), Not(var229(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var234(x1)), Or(var166(x), var130(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var177(x1), Or(Not(var11(x)), Not(var66(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var234(x1)), Or(var58(x), var240(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var145(x1), var107(x1)), var216(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var38(x1), Or(var64(x), var244(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var54(x1), Or(Not(var119(x)), Not(var102(x))))))),
	ForAll([x], Not(Or(Not(var211(x)), Not(var144(x)), var65(x), var204(x)))),
	ForAll([x], Not(Or(var249(x), var76(x), Not(var66(x)), Not(var106(x))))),
	ForAll([x], Not(Or(Not(var69(x)), Not(var137(x)), Not(var124(x)), Not(var192(x))))),
	ForAll([x], Not(Or(Not(var112(x)), var94(x), var124(x), var18(x)))),
	ForAll([x], Not(Or(Not(var245(x)), var117(x), var142(x), Not(var162(x))))),
	ForAll([x], Not(Or(var36(x), var154(x), var32(x), var206(x)))),
	ForAll([x], Not(Or(var146(x), var69(x), Not(var158(x)), Not(var238(x))))),
	ForAll([x], Not(Or(var63(x), Not(var137(x)), var238(x), var223(x)))),
	ForAll([x], Not(Or(var146(x), var81(x), var50(x), var104(x)))),
	ForAll([x], Not(Or(var192(x), var52(x), var72(x), var242(x)))),
	ForAll([x], Not(Or(var182(x), Not(var32(x)), Not(var11(x)), var235(x)))),
	ForAll([x], Not(Or(Not(var79(x)), Not(var157(x)), var220(x), Not(var174(x))))),
	ForAll([x], Not(Or(var173(x), var58(x), Not(var28(x)), Not(var71(x))))),
	ForAll([x], Not(Or(var60(x), Not(var205(x)), Not(var95(x)), var57(x)))),
	ForAll([x], Not(Or(var215(x), var40(x), Not(var48(x)), var43(x)))),
	ForAll([x], Not(Or(Not(var107(x)), var159(x), Not(var54(x)), Not(var81(x))))),
	ForAll([x], Not(Or(var125(x), Not(var226(x)), Not(var9(x)), var93(x)))),
	ForAll([x], Not(Or(var83(x), Not(var65(x)), var177(x), Not(var11(x))))),
	ForAll([x], Not(Or(var191(x), var126(x), var217(x), Not(var78(x))))),
	ForAll([x], Not(Or(var62(x), var33(x), var46(x), Not(var170(x))))),
	ForAll([x], Not(Or(var146(x), var41(x), Not(var122(x)), Not(var60(x))))),
	ForAll([x], Not(Or(Not(var28(x)), Not(var52(x)), Not(var142(x)), Not(var226(x))))),
	ForAll([x], Not(Or(Not(var186(x)), Not(var9(x)), var123(x), Not(var175(x))))),
	ForAll([x], Not(Or(Not(var60(x)), var6(x), Not(var161(x)), Not(var220(x))))),
	ForAll([x], Not(Or(var137(x), var102(x), Not(var84(x)), var230(x)))),
	ForAll([x], Not(Or(var248(x), Not(var208(x)), Not(var197(x)), var103(x)))),
	ForAll([x], Not(Or(Not(var91(x)), Not(var222(x)), var25(x), Not(var16(x))))),
	ForAll([x], Not(Or(var118(x), var227(x), var241(x), Not(var91(x))))),
	ForAll([x], Not(Or(var1(x), var113(x), Not(var152(x)), var145(x)))),
	ForAll([x], Not(Or(Not(var160(x)), Not(var16(x)), Not(var214(x)), Not(var5(x))))),
	ForAll([x], Not(Or(Not(var162(x)), var98(x), var173(x), var67(x)))),
	ForAll([x], Not(Or(var78(x), Not(var130(x)), Not(var164(x)), var240(x)))),
	ForAll([x], Not(Or(Not(var12(x)), var179(x), Not(var149(x)), var235(x)))),
	ForAll([x], Not(Or(Not(var146(x)), var249(x), Not(var202(x)), var94(x)))),
	ForAll([x], Not(Or(Not(var19(x)), Not(var203(x)), Not(var228(x)), var162(x)))),
	ForAll([x], Not(Or(var183(x), var167(x), var196(x), Not(var153(x))))),
	ForAll([x], Not(Or(Not(var42(x)), Not(var165(x)), var219(x), var73(x)))),
	ForAll([x], Not(Or(Not(var35(x)), Not(var198(x)), Not(var26(x)), var74(x)))),
	ForAll([x], Not(Or(var76(x), var201(x), var122(x), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var140(x)), var91(x), Not(var162(x)), Not(var212(x))))),
	ForAll([x], Not(Or(Not(var127(x)), Not(var209(x)), var226(x), var13(x)))),
	ForAll([x], Not(Or(Not(var9(x)), Not(var123(x)), var21(x), Not(var162(x))))),
	ForAll([x], Not(Or(Not(var223(x)), var247(x), var236(x), Not(var229(x))))),
	ForAll([x], Not(Or(var105(x), Not(var26(x)), var126(x), Not(var83(x))))),
	ForAll([x], Not(Or(Not(var26(x)), var156(x), var77(x), var5(x)))),
	ForAll([x], Not(Or(var136(x), Not(var69(x)), var163(x), Not(var53(x))))),
	ForAll([x], Not(Or(var157(x), Not(var164(x)), Not(var11(x)), Not(var105(x))))),
	ForAll([x], Not(Or(var43(x), var70(x), Not(var34(x)), var158(x)))),
	ForAll([x], Not(Or(var156(x), Not(var31(x)), Not(var250(x)), var243(x)))),
	ForAll([x], Not(Or(Not(var146(x)), Not(var49(x)), var10(x), Not(var8(x))))),
	ForAll([x], Not(Or(var207(x), var155(x), var30(x), var8(x)))),
	ForAll([x], Not(Or(var149(x), var91(x), Not(var79(x)), var182(x)))),
	ForAll([x], Not(Or(var241(x), var81(x), var170(x), Not(var113(x))))),
	ForAll([x], Not(Or(var249(x), var222(x), Not(var14(x)), Not(var33(x))))),
	ForAll([x], Not(Or(Not(var173(x)), Not(var187(x)), Not(var117(x)), Not(var127(x))))),
	ForAll([x], Not(Or(var146(x), var13(x), Not(var20(x)), Not(var190(x))))),
	ForAll([x], Not(Or(var195(x), Not(var111(x)), var157(x), var68(x)))),
	ForAll([x], Not(Or(var90(x), Not(var97(x)), var60(x), Not(var144(x))))),
	ForAll([x], Not(Or(Not(var6(x)), var22(x), Not(var245(x)), Not(var89(x))))),
	ForAll([x], Not(Or(var187(x), var162(x), Not(var165(x)), Not(var143(x))))),
	ForAll([x], Not(Or(var87(x), Not(var15(x)), var219(x), Not(var130(x))))),
	ForAll([x], Not(Or(var104(x), var233(x), var244(x), Not(var213(x))))),
	ForAll([x], Not(Or(Not(var51(x)), Not(var219(x)), Not(var106(x)), var249(x)))),
	ForAll([x], Not(Or(var93(x), var55(x), Not(var107(x)), Not(var69(x))))),
	ForAll([x], Not(Or(var111(x), Not(var5(x)), Not(var3(x)), Not(var180(x))))),
	ForAll([x], Not(Or(Not(var206(x)), Not(var196(x)), var10(x), Not(var197(x))))),
	ForAll([x], Not(Or(var175(x), var245(x), Not(var79(x)), Not(var159(x))))),
	ForAll([x], Not(Or(Not(var8(x)), Not(var188(x)), Not(var26(x)), Not(var182(x))))),
	ForAll([x], Not(Or(Not(var80(x)), Not(var189(x)), var31(x), var169(x)))),
	ForAll([x], Not(Or(var66(x), Not(var217(x)), Not(var191(x)), var58(x)))),
	ForAll([x], Not(Or(var151(x), var203(x), Not(var162(x)), Not(var82(x))))),
	ForAll([x], Not(Or(var43(x), var152(x), Not(var112(x)), var149(x)))),
	ForAll([x], Not(Or(Not(var188(x)), var159(x), var30(x), var120(x)))),
	ForAll([x], Not(Or(Not(var112(x)), Not(var208(x)), var169(x), Not(var220(x))))),
	ForAll([x], Not(Or(var218(x), var46(x), Not(var109(x)), var39(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var169(x1), Not(var137(x1))), Or(Not(var7(x)), Not(var196(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var222(x1), Not(var6(x1)), var216(x1)), Not(var237(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var139(x1)), var71(x1)), Or(var72(x), Not(var60(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var101(x1)), Not(var228(x1))), Or(var180(x), var130(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var158(x1)), var26(x1)), Or(var201(x), var144(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var153(x1), Not(var175(x1)), var16(x1)), Not(var163(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var225(x1), var158(x1), Not(var227(x1))), var146(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var150(x1)), var89(x1)), Or(var77(x), var240(x)))))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var24(x)), var5(x), Not(var45(x)), var115(x), var88(x)))),
	ForAll([x], Not(Or(var24(x), var198(x), Not(var209(x)), Not(var180(x)), Not(var47(x)), Not(var144(x))))),
	ForAll([x], Not(Or(var139(x), Not(var123(x)), var222(x), var153(x), var92(x), Not(var172(x))))),
	ForAll([x], Not(Or(Not(var1(x)), var204(x), var55(x), Not(var188(x)), var103(x), var34(x)))),
	ForAll([x], Not(Or(var178(x), Not(var160(x)), Not(var158(x)), Not(var215(x)), var156(x), var242(x)))),
	ForAll([x], Not(Or(Not(var224(x)), var42(x), var130(x), var168(x), var86(x), Not(var150(x))))),
	ForAll([x], Not(Or(var80(x), Not(var124(x)), var199(x), Not(var56(x)), Not(var144(x)), Not(var216(x))))),
	ForAll([x], Not(Or(Not(var171(x)), Not(var223(x)), Not(var95(x)), Not(var46(x)), Not(var248(x)), Not(var123(x))))),
	ForAll([x], Not(Or(Not(var123(x)), Not(var78(x)), var158(x), Not(var244(x)), Not(var195(x)), Not(var210(x))))),
	ForAll([x], Not(Or(Not(var106(x)), Not(var13(x)), Not(var156(x)), Not(var133(x)), var124(x), Not(var36(x))))),
	ForAll([x], Not(Or(Not(var71(x)), Not(var140(x)), Not(var46(x)), Not(var133(x)), var203(x), Not(var58(x))))),
	ForAll([x], Not(Or(var181(x), Not(var172(x)), Not(var42(x)), var163(x), var22(x), Not(var231(x))))),
	ForAll([x], Not(Or(var217(x), Not(var234(x)), var186(x), Not(var213(x)), var138(x), var19(x)))),
	ForAll([x], Not(Or(Not(var93(x)), var23(x), var33(x), Not(var184(x)), var224(x), Not(var14(x))))),
	ForAll([x], Not(Or(Not(var73(x)), var170(x), Not(var207(x)), Not(var223(x)), var136(x), Not(var69(x))))),
	ForAll([x], Not(Or(Not(var227(x)), var201(x), var11(x), var130(x), Not(var68(x)), var192(x)))),
	ForAll([x], Not(Or(var241(x), Not(var164(x)), Not(var10(x)), var205(x), var157(x), Not(var42(x))))),
	ForAll([x], Not(Or(var16(x), var8(x), var162(x), Not(var108(x)), var35(x), var83(x)))),
	ForAll([x], Not(Or(Not(var244(x)), var156(x), var65(x), Not(var233(x)), var103(x), var123(x)))),
	ForAll([x], Not(Or(Not(var82(x)), Not(var200(x)), Not(var83(x)), var52(x), Not(var25(x)), Not(var47(x))))),
	ForAll([x], Not(Or(Not(var231(x)), Not(var234(x)), var93(x), var79(x), Not(var113(x)), Not(var71(x))))),
	ForAll([x], Not(Or(Not(var232(x)), var41(x), var26(x), var197(x), var141(x), Not(var58(x))))),
	ForAll([x], Not(Or(var53(x), Not(var92(x)), var59(x), var162(x), Not(var54(x)), var5(x)))),
	ForAll([x], Not(Or(var136(x), var193(x), Not(var97(x)), var225(x), var221(x), Not(var3(x))))),
	ForAll([x], Not(Or(var51(x), var127(x), var42(x), Not(var202(x)), Not(var82(x)), Not(var138(x))))),
	ForAll([x], Not(Or(Not(var248(x)), Not(var204(x)), var200(x), var235(x), var103(x), Not(var112(x))))),
	ForAll([x], Not(Or(Not(var174(x)), var131(x), var212(x), var68(x), var124(x), var250(x)))),
	ForAll([x], Not(Or(var88(x), var244(x), Not(var159(x)), var235(x), Not(var226(x)), var12(x)))),
	ForAll([x], Not(Or(Not(var17(x)), var225(x), var32(x), Not(var41(x)), Not(var190(x)), var217(x)))),
	ForAll([x], Not(Or(Not(var36(x)), Not(var58(x)), Not(var53(x)), Not(var249(x)), var39(x), var197(x)))),
	ForAll([x], Not(Or(Not(var143(x)), Not(var201(x)), var217(x), var90(x), Not(var178(x)), var16(x)))),
	ForAll([x], Not(Or(Not(var154(x)), Not(var75(x)), Not(var165(x)), var57(x), var136(x), Not(var222(x))))),
	ForAll([x], Not(Or(Not(var85(x)), var11(x), Not(var166(x)), var25(x), Not(var65(x)), Not(var82(x))))),
	ForAll([x], Not(Or(var108(x), var234(x), Not(var158(x)), Not(var113(x)), var167(x), var36(x)))),
	ForAll([x], Not(Or(Not(var216(x)), var153(x), Not(var117(x)), Not(var46(x)), Not(var195(x)), Not(var84(x))))),
	ForAll([x], Not(Or(Not(var87(x)), var136(x), var65(x), var194(x), var150(x), var183(x)))),
	ForAll([x], Not(Or(Not(var152(x)), var206(x), var230(x), Not(var10(x)), var154(x), var77(x)))),
	ForAll([x], Not(Or(var102(x), var128(x), Not(var138(x)), var166(x), Not(var246(x)), Not(var111(x))))),
	ForAll([x], Not(Or(var239(x), var173(x), Not(var25(x)), Not(var175(x)), Not(var155(x)), Not(var188(x))))),
	ForAll([x], Not(Or(var38(x), Not(var223(x)), var239(x), Not(var209(x)), Not(var211(x)), Not(var113(x))))),
	ForAll([x], Not(Or(var25(x), var152(x), var26(x), Not(var118(x)), var20(x), Not(var194(x))))),
	ForAll([x], Not(Or(var232(x), Not(var42(x)), var82(x), Not(var207(x)), Not(var66(x)), Not(var224(x))))),
	ForAll([x], Not(Or(var246(x), Not(var148(x)), var232(x), var213(x), Not(var182(x)), var229(x)))),
	ForAll([x], Not(Or(Not(var86(x)), Not(var238(x)), Not(var184(x)), var218(x), var128(x), Not(var151(x))))),
	ForAll([x], Not(Or(var65(x), var92(x), Not(var101(x)), var37(x), Not(var103(x)), var230(x)))),
	ForAll([x], Not(Or(var238(x), var32(x), Not(var70(x)), Not(var95(x)), Not(var196(x)), var168(x)))),
	ForAll([x], Not(Or(var202(x), Not(var95(x)), Not(var190(x)), Not(var68(x)), var143(x), var212(x)))),
	ForAll([x], Not(Or(Not(var84(x)), var168(x), Not(var194(x)), Not(var61(x)), var53(x), var35(x)))),
	ForAll([x], Not(Or(var174(x), Not(var51(x)), Not(var8(x)), Not(var70(x)), Not(var66(x)), var243(x)))),
	ForAll([x], Not(Or(var133(x), Not(var74(x)), Not(var44(x)), Not(var78(x)), Not(var100(x)), var9(x)))),
	ForAll([x], Not(Or(var241(x), var23(x), var94(x), var113(x), Not(var66(x)), var62(x)))),
	ForAll([x], Not(Or(var42(x), Not(var64(x)), Not(var68(x)), var100(x), var109(x), Not(var157(x))))),
	ForAll([x], Not(Or(var235(x), Not(var136(x)), var81(x), var168(x), var221(x), Not(var193(x))))),
	ForAll([x], Not(Or(var120(x), var198(x), var51(x), Not(var186(x)), Not(var126(x)), Not(var222(x))))),
	ForAll([x], Not(Or(Not(var101(x)), var185(x), Not(var203(x)), Not(var75(x)), var86(x), var211(x)))),
	ForAll([x], Not(Or(var126(x), Not(var192(x)), var136(x), Not(var52(x)), var202(x), var60(x)))),
	ForAll([x], Not(Or(Not(var169(x)), Not(var237(x)), Not(var19(x)), Not(var93(x)), Not(var85(x)), Not(var48(x))))),
	ForAll([x], Not(Or(var41(x), var178(x), var185(x), Not(var12(x)), var65(x), Not(var219(x))))),
	ForAll([x], Not(Or(Not(var64(x)), Not(var23(x)), var89(x), var153(x), Not(var15(x)), var97(x)))),
	ForAll([x], Not(Or(Not(var26(x)), Not(var164(x)), Not(var84(x)), Not(var82(x)), Not(var167(x)), Not(var80(x))))),
	ForAll([x], Not(Or(var211(x), Not(var200(x)), var215(x), var122(x), var180(x), Not(var88(x))))),
	ForAll([x], Not(Or(var27(x), var138(x), var242(x), Not(var152(x)), var50(x), Not(var148(x))))),
	ForAll([x], Not(Or(var52(x), Not(var136(x)), var5(x), Not(var83(x)), var49(x), Not(var32(x))))),
	ForAll([x], Not(Or(Not(var154(x)), var168(x), Not(var211(x)), var107(x), var237(x), Not(var82(x))))),
	ForAll([x], Not(Or(var80(x), var102(x), var174(x), Not(var163(x)), var244(x), Not(var108(x))))),
	ForAll([x], Not(Or(var231(x), Not(var18(x)), Not(var153(x)), Not(var53(x)), Not(var144(x)), var158(x)))),
	ForAll([x], Not(Or(var77(x), Not(var123(x)), var11(x), var78(x), Not(var23(x)), Not(var54(x))))),
	ForAll([x], Not(Or(var8(x), Not(var24(x)), Not(var65(x)), Not(var237(x)), var121(x), var166(x)))),
	ForAll([x], Not(Or(Not(var61(x)), var144(x), var25(x), var38(x), var147(x), var69(x)))),
	ForAll([x], Not(Or(var113(x), var81(x), Not(var128(x)), var55(x), Not(var191(x)), Not(var224(x))))),
	ForAll([x], Not(Or(Not(var29(x)), var82(x), Not(var13(x)), var173(x), var239(x), var248(x)))),
	ForAll([x], Not(Or(Not(var124(x)), var81(x), var76(x), Not(var217(x)), var92(x), var32(x)))),
	ForAll([x], Not(Or(Not(var101(x)), Not(var237(x)), Not(var183(x)), var156(x), var45(x), var206(x)))),
	ForAll([x], Not(Or(var244(x), var191(x), Not(var113(x)), Not(var136(x)), var164(x), var178(x)))),
	ForAll([x], Not(Or(Not(var70(x)), var35(x), var239(x), var42(x), var88(x), Not(var94(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var42(x1)), Not(var134(x1))), Or(var212(x), Not(var179(x)), var50(x), var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var192(x1), Not(var165(x1))), Or(Not(var55(x)), var195(x), Not(var114(x)), var120(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var186(x1), Or(Not(var107(x)), var158(x), var100(x), Not(var239(x)), var201(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var187(x1), var243(x1)), Or(Not(var94(x)), var132(x), var158(x), var92(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var180(x1)), Or(Not(var85(x)), Not(var166(x)), Not(var134(x)), Not(var25(x)), Not(var44(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var101(x1), var208(x1), var8(x1), var7(x1)), Or(Not(var132(x)), Not(var137(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var200(x1)), Or(var177(x), Not(var124(x)), Not(var131(x)), Not(var144(x)), var80(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var220(x1), Not(var137(x1))), Or(var55(x), var88(x), Not(var68(x)), Not(var62(x))))))),
	ForAll([x], Not(Or(var211(x), var32(x), Not(var174(x)), Not(var231(x)), Not(var175(x)), Not(var243(x)), var142(x), var86(x)))),
	ForAll([x], Not(Or(Not(var199(x)), var97(x), Not(var36(x)), Not(var50(x)), var74(x), var246(x), Not(var118(x)), var166(x)))),
	ForAll([x], Not(Or(var72(x), var233(x), var62(x), Not(var238(x)), var131(x), Not(var34(x)), Not(var222(x)), var211(x)))),
	ForAll([x], Not(Or(Not(var165(x)), var71(x), Not(var138(x)), var62(x), Not(var166(x)), var173(x), var180(x), var17(x)))),
	ForAll([x], Not(Or(Not(var64(x)), var131(x), var221(x), Not(var120(x)), var133(x), Not(var105(x)), Not(var229(x)), var20(x)))),
	ForAll([x], Not(Or(var95(x), var115(x), var211(x), var220(x), var174(x), var55(x), var44(x), var189(x)))),
	ForAll([x], Not(Or(Not(var237(x)), Not(var16(x)), var250(x), Not(var198(x)), var77(x), var98(x), Not(var93(x)), var10(x)))),
	ForAll([x], Not(Or(var198(x), var152(x), var217(x), var101(x), Not(var6(x)), Not(var151(x)), Not(var108(x)), var74(x)))),
	ForAll([x], Not(Or(Not(var214(x)), var120(x), var153(x), var65(x), var61(x), var168(x), var75(x), Not(var6(x))))),
	ForAll([x], Not(Or(Not(var52(x)), var250(x), Not(var160(x)), Not(var90(x)), Not(var187(x)), var8(x), var169(x), Not(var197(x))))),
	ForAll([x], Not(Or(Not(var112(x)), var70(x), Not(var94(x)), var78(x), Not(var238(x)), Not(var48(x)), var84(x), var137(x)))),
	ForAll([x], Not(Or(var234(x), Not(var176(x)), Not(var108(x)), var160(x), Not(var42(x)), var141(x), Not(var110(x)), var233(x)))),
	ForAll([x], Not(Or(Not(var100(x)), Not(var42(x)), var24(x), Not(var181(x)), var247(x), Not(var9(x)), var14(x), Not(var116(x))))),
	ForAll([x], Not(Or(Not(var180(x)), var113(x), var192(x), var238(x), Not(var91(x)), Not(var174(x)), Not(var158(x)), var109(x)))),
	ForAll([x], Not(Or(var32(x), var106(x), var222(x), var131(x), Not(var111(x)), Not(var9(x)), var110(x), Not(var168(x))))),
	ForAll([x], Not(Or(var9(x), Not(var240(x)), Not(var5(x)), var163(x), Not(var195(x)), var25(x), Not(var49(x)), var189(x)))),
	ForAll([x], Not(Or(Not(var137(x)), var192(x), Not(var187(x)), Not(var8(x)), var126(x), var244(x), var53(x), var169(x)))),
	ForAll([x], Not(Or(Not(var100(x)), var179(x), Not(var85(x)), var87(x), Not(var164(x)), var55(x), Not(var17(x)), Not(var221(x))))),
	ForAll([x], Not(Or(var207(x), var48(x), var201(x), var67(x), var28(x), var8(x), Not(var177(x)), Not(var161(x))))),
	ForAll([x], Not(Or(Not(var103(x)), Not(var154(x)), Not(var23(x)), var106(x), var117(x), Not(var198(x)), Not(var76(x)), Not(var174(x))))),
	ForAll([x], Not(Or(Not(var219(x)), Not(var79(x)), Not(var11(x)), var167(x), var122(x), Not(var206(x)), Not(var9(x)), var228(x)))),
	ForAll([x], Not(Or(var250(x), var223(x), var224(x), Not(var10(x)), Not(var229(x)), Not(var179(x)), var96(x), Not(var6(x))))),
	ForAll([x], Not(Or(var212(x), var172(x), var222(x), Not(var148(x)), var63(x), Not(var142(x)), var66(x), var150(x)))),
	ForAll([x], Not(Or(Not(var75(x)), Not(var58(x)), Not(var132(x)), Not(var31(x)), Not(var237(x)), var62(x), Not(var105(x)), Not(var134(x))))),
	ForAll([x], Not(Or(Not(var73(x)), var249(x), var122(x), Not(var223(x)), Not(var129(x)), var45(x), var210(x), Not(var132(x))))),
	ForAll([x], Not(Or(Not(var174(x)), var129(x), var44(x), Not(var198(x)), Not(var190(x)), var14(x), var163(x), Not(var41(x))))),
	ForAll([x], Not(Or(var54(x), Not(var78(x)), Not(var174(x)), Not(var3(x)), Not(var75(x)), Not(var182(x)), var22(x), var14(x)))),
	ForAll([x], Not(Or(var243(x), Not(var113(x)), var24(x), var107(x), var31(x), var98(x), Not(var185(x)), var106(x)))),
	ForAll([x], Not(Or(var75(x), var132(x), var98(x), var21(x), var129(x), var170(x), Not(var24(x)), var30(x)))),
	ForAll([x], Not(Or(var7(x), var2(x), var64(x), var75(x), Not(var163(x)), Not(var234(x)), Not(var67(x)), Not(var60(x))))),
	ForAll([x], Not(Or(var97(x), var203(x), Not(var134(x)), var54(x), var47(x), Not(var80(x)), var237(x), Not(var139(x))))),
	ForAll([x], Not(Or(Not(var195(x)), Not(var24(x)), Not(var87(x)), var9(x), var98(x), var143(x), Not(var167(x)), Not(var21(x))))),
	ForAll([x], Not(Or(Not(var58(x)), Not(var29(x)), var101(x), Not(var109(x)), Not(var16(x)), Not(var30(x)), var182(x), var237(x)))),
	ForAll([x], Not(Or(var34(x), var192(x), var50(x), var131(x), var130(x), var123(x), var168(x), Not(var43(x))))),
	ForAll([x], Not(Or(var60(x), Not(var157(x)), var228(x), Not(var24(x)), Not(var183(x)), var32(x), var84(x), Not(var205(x))))),
	ForAll([x], Not(Or(Not(var13(x)), var95(x), var11(x), Not(var181(x)), Not(var19(x)), var170(x), Not(var217(x)), Not(var148(x))))),
	ForAll([x], Not(Or(Not(var150(x)), Not(var70(x)), Not(var224(x)), Not(var204(x)), var24(x), var31(x), Not(var97(x)), var100(x)))),
	ForAll([x], Not(Or(Not(var224(x)), var114(x), Not(var215(x)), Not(var48(x)), Not(var10(x)), var165(x), var64(x), Not(var189(x))))),
	ForAll([x], Not(Or(var207(x), var31(x), var165(x), Not(var100(x)), Not(var184(x)), Not(var177(x)), var32(x), var38(x)))),
	ForAll([x], Not(Or(Not(var83(x)), Not(var67(x)), Not(var111(x)), var171(x), var37(x), Not(var41(x)), var33(x), var21(x)))),
	ForAll([x], Not(Or(Not(var38(x)), Not(var239(x)), var57(x), var182(x), Not(var147(x)), var214(x), var40(x), Not(var207(x))))),
	ForAll([x], Not(Or(var32(x), var144(x), var215(x), Not(var2(x)), Not(var51(x)), var188(x), Not(var243(x)), var190(x)))),
	ForAll([x], Not(Or(Not(var57(x)), Not(var204(x)), var86(x), var172(x), var154(x), Not(var203(x)), var217(x), Not(var249(x))))),
	ForAll([x], Not(Or(var96(x), Not(var200(x)), var171(x), var71(x), Not(var98(x)), var86(x), var53(x), var160(x)))),
	ForAll([x], Not(Or(var107(x), var201(x), var38(x), var135(x), Not(var88(x)), var28(x), Not(var176(x)), var117(x)))),
	ForAll([x], Not(Or(var230(x), var1(x), var69(x), var226(x), Not(var52(x)), Not(var123(x)), Not(var48(x)), var133(x)))),
	ForAll([x], Not(Or(Not(var45(x)), var169(x), var80(x), var102(x), Not(var11(x)), var123(x), var126(x), Not(var3(x))))),
	ForAll([x], Not(Or(Not(var114(x)), Not(var232(x)), var216(x), var112(x), var101(x), Not(var96(x)), Not(var175(x)), Not(var205(x))))),
	ForAll([x], Not(Or(var205(x), Not(var61(x)), Not(var193(x)), var40(x), Not(var98(x)), var142(x), Not(var92(x)), Not(var60(x))))),
	ForAll([x], Not(Or(Not(var13(x)), Not(var1(x)), var82(x), Not(var50(x)), Not(var192(x)), var174(x), var15(x), var110(x)))),
	ForAll([x], Not(Or(Not(var91(x)), var80(x), var15(x), var64(x), var35(x), Not(var65(x)), Not(var151(x)), Not(var164(x))))),
	ForAll([x], Not(Or(var14(x), var168(x), var176(x), Not(var37(x)), Not(var117(x)), Not(var61(x)), Not(var210(x)), Not(var72(x))))),
	ForAll([x], Not(Or(Not(var94(x)), var44(x), Not(var171(x)), var164(x), Not(var40(x)), Not(var139(x)), Not(var33(x)), Not(var178(x))))),
	ForAll([x], Not(Or(Not(var204(x)), Not(var166(x)), var76(x), Not(var112(x)), var133(x), var43(x), Not(var129(x)), var91(x)))),
	ForAll([x], Not(Or(var230(x), Not(var181(x)), Not(var83(x)), Not(var19(x)), var29(x), var76(x), var249(x), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var97(x)), Not(var191(x)), var79(x), Not(var37(x)), Not(var47(x)), Not(var165(x)), Not(var166(x)), var220(x)))),
	ForAll([x], Not(Or(Not(var217(x)), Not(var78(x)), Not(var95(x)), Not(var147(x)), var68(x), Not(var239(x)), Not(var77(x)), Not(var143(x))))),
	ForAll([x], Not(Or(Not(var172(x)), var85(x), var161(x), var166(x), Not(var211(x)), Not(var81(x)), Not(var212(x)), Not(var70(x))))),
	ForAll([x], Not(Or(var134(x), var171(x), Not(var186(x)), Not(var66(x)), var162(x), var34(x), Not(var41(x)), var148(x)))),
	ForAll([x], Not(Or(var182(x), var66(x), Not(var70(x)), var183(x), var144(x), var235(x), Not(var147(x)), var34(x)))),
	ForAll([x], Not(Or(var162(x), var247(x), Not(var93(x)), Not(var9(x)), Not(var108(x)), var202(x), var36(x), Not(var182(x))))),
	ForAll([x], Not(Or(var202(x), Not(var119(x)), var198(x), Not(var52(x)), var38(x), var50(x), var32(x), var87(x)))),
	ForAll([x], Not(Or(Not(var242(x)), var9(x), var86(x), var177(x), Not(var220(x)), Not(var2(x)), var45(x), var146(x)))),
	ForAll([x], Not(Or(var215(x), Not(var103(x)), Not(var53(x)), var209(x), Not(var212(x)), var18(x), Not(var1(x)), Not(var162(x))))),
	ForAll([x], Not(Or(Not(var72(x)), Not(var96(x)), var236(x), var95(x), Not(var218(x)), var35(x), Not(var182(x)), Not(var68(x))))),
	ForAll([x], Not(Or(var171(x), var79(x), var135(x), Not(var208(x)), Not(var117(x)), var134(x), var175(x), Not(var81(x))))),
	ForAll([x], Not(Or(var135(x), var9(x), Not(var68(x)), var44(x), Not(var208(x)), Not(var187(x)), Not(var69(x)), Not(var107(x))))),
	ForAll([x], Not(Or(Not(var212(x)), Not(var156(x)), Not(var186(x)), var119(x), var42(x), var177(x), var221(x), var69(x)))),
	ForAll([x], Not(Or(Not(var205(x)), Not(var224(x)), Not(var197(x)), var58(x), Not(var75(x)), Not(var227(x)), Not(var165(x)), Not(var95(x))))),
	ForAll([x], Not(Or(var180(x), var103(x), var114(x), Not(var242(x)), var217(x), Not(var241(x)), Not(var153(x)), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var214(x)), var136(x), var117(x), var99(x), var52(x), Not(var156(x)), var81(x), var78(x)))),
	ForAll([x], Not(Or(Not(var26(x)), var29(x), Not(var197(x)), Not(var208(x)), var177(x), var134(x), Not(var244(x)), Not(var109(x))))),
	ForAll([x], Not(Or(var114(x), var85(x), var134(x), var11(x), Not(var69(x)), Not(var1(x)), Not(var237(x)), Not(var102(x))))),
	ForAll([x], Not(Or(var101(x), Not(var6(x)), Not(var53(x)), var90(x), var185(x), Not(var247(x)), var227(x), var140(x)))),
	ForAll([x], Not(Or(var86(x), Not(var72(x)), Not(var114(x)), Not(var231(x)), var45(x), var187(x), var241(x), Not(var152(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var115(x1), var193(x1), Not(var140(x1)), Not(var76(x1))), Or(var22(x), Not(var131(x)), Not(var35(x)), var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var118(x1)), Not(var128(x1)), var240(x1)), Or(Not(var58(x)), var230(x), Not(var202(x)), var132(x), Not(var213(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var209(x1)), Or(var205(x), var249(x), var195(x), Not(var73(x)), var168(x), var107(x), Not(var50(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var18(x1), var57(x1), var178(x1), Not(var59(x1))), Or(Not(var11(x)), var49(x), Not(var209(x)), Not(var239(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var215(x1), var73(x1), Not(var191(x1)), Not(var40(x1)), Not(var122(x1)), var29(x1)), Or(var241(x), Not(var65(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var134(x1), Not(var4(x1)), var165(x1), var91(x1), Not(var205(x1))), Or(var93(x), var61(x), var129(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var96(x1), Not(var143(x1)), Not(var9(x1)), var224(x1), Not(var66(x1)), var13(x1)), Or(Not(var233(x)), var44(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var203(x1)), Not(var188(x1))), Or(var56(x), Not(var101(x)), Not(var73(x)), var197(x), Not(var156(x)), var239(x)))))),
	ForAll([x], Not(Or(var148(x), var174(x), Not(var33(x)), var110(x), var5(x), var129(x), var41(x), Not(var73(x)), var37(x), Not(var224(x))))),
	ForAll([x], Not(Or(Not(var106(x)), Not(var101(x)), Not(var223(x)), var140(x), Not(var204(x)), var236(x), Not(var119(x)), Not(var51(x)), var72(x), var9(x)))),
	ForAll([x], Not(Or(Not(var121(x)), Not(var56(x)), Not(var142(x)), Not(var150(x)), var214(x), var3(x), Not(var122(x)), Not(var140(x)), var183(x), var11(x)))),
	ForAll([x], Not(Or(Not(var221(x)), var31(x), var241(x), Not(var44(x)), var77(x), var226(x), var247(x), var91(x), Not(var114(x)), var119(x)))),
	ForAll([x], Not(Or(Not(var9(x)), var99(x), var138(x), var65(x), Not(var121(x)), Not(var133(x)), Not(var34(x)), var64(x), Not(var95(x)), var42(x)))),
	ForAll([x], Not(Or(var227(x), Not(var72(x)), Not(var194(x)), var147(x), var181(x), var160(x), Not(var75(x)), var123(x), Not(var42(x)), var83(x)))),
	ForAll([x], Not(Or(var36(x), Not(var165(x)), var223(x), Not(var112(x)), Not(var57(x)), var44(x), Not(var237(x)), var213(x), Not(var92(x)), var152(x)))),
	ForAll([x], Not(Or(Not(var25(x)), Not(var9(x)), Not(var170(x)), var122(x), var232(x), Not(var245(x)), var243(x), var175(x), Not(var22(x)), Not(var3(x))))),
	ForAll([x], Not(Or(Not(var114(x)), Not(var196(x)), Not(var84(x)), Not(var212(x)), Not(var115(x)), var22(x), Not(var3(x)), Not(var157(x)), Not(var30(x)), var171(x)))),
	ForAll([x], Not(Or(var224(x), Not(var159(x)), Not(var232(x)), Not(var243(x)), Not(var106(x)), Not(var155(x)), Not(var107(x)), Not(var196(x)), Not(var108(x)), var189(x)))),
	ForAll([x], Not(Or(Not(var199(x)), Not(var244(x)), Not(var143(x)), Not(var177(x)), Not(var153(x)), var231(x), var218(x), Not(var79(x)), Not(var42(x)), Not(var201(x))))),
	ForAll([x], Not(Or(Not(var244(x)), var190(x), Not(var226(x)), var67(x), Not(var5(x)), Not(var69(x)), Not(var140(x)), var159(x), Not(var187(x)), Not(var242(x))))),
	ForAll([x], Not(Or(var114(x), var170(x), var102(x), Not(var182(x)), var68(x), var29(x), var153(x), Not(var168(x)), var137(x), Not(var213(x))))),
	ForAll([x], Not(Or(Not(var172(x)), var72(x), var216(x), Not(var116(x)), Not(var181(x)), var244(x), var25(x), Not(var224(x)), Not(var23(x)), var180(x)))),
	ForAll([x], Not(Or(Not(var203(x)), Not(var100(x)), var193(x), Not(var98(x)), Not(var26(x)), var217(x), Not(var102(x)), var13(x), Not(var233(x)), Not(var120(x))))),
	ForAll([x], Not(Or(var133(x), Not(var91(x)), var196(x), Not(var59(x)), var161(x), Not(var67(x)), Not(var70(x)), Not(var69(x)), var242(x), var238(x)))),
	ForAll([x], Not(Or(var212(x), Not(var76(x)), Not(var228(x)), Not(var207(x)), Not(var217(x)), Not(var131(x)), var111(x), var145(x), Not(var153(x)), Not(var46(x))))),
	ForAll([x], Not(Or(var62(x), var193(x), Not(var134(x)), Not(var122(x)), var179(x), Not(var205(x)), Not(var79(x)), var65(x), Not(var143(x)), Not(var187(x))))),
	ForAll([x], Not(Or(Not(var163(x)), var209(x), var118(x), Not(var149(x)), Not(var95(x)), Not(var100(x)), var53(x), var201(x), var245(x), var135(x)))),
	ForAll([x], Not(Or(Not(var119(x)), Not(var37(x)), Not(var27(x)), Not(var5(x)), var86(x), Not(var181(x)), var155(x), Not(var174(x)), var64(x), Not(var101(x))))),
	ForAll([x], Not(Or(var3(x), var73(x), var170(x), var188(x), Not(var202(x)), Not(var197(x)), Not(var186(x)), var132(x), Not(var95(x)), Not(var69(x))))),
	ForAll([x], Not(Or(Not(var219(x)), var161(x), Not(var103(x)), var172(x), var49(x), var176(x), var247(x), Not(var213(x)), Not(var5(x)), var174(x)))),
	ForAll([x], Not(Or(var226(x), Not(var224(x)), Not(var62(x)), var24(x), Not(var110(x)), Not(var155(x)), var141(x), Not(var73(x)), var19(x), Not(var206(x))))),
	ForAll([x], Not(Or(Not(var240(x)), var46(x), var17(x), Not(var115(x)), var200(x), var9(x), Not(var8(x)), var104(x), var127(x), var54(x)))),
	ForAll([x], Not(Or(Not(var81(x)), Not(var160(x)), Not(var56(x)), Not(var226(x)), var146(x), var249(x), var214(x), Not(var32(x)), var139(x), Not(var105(x))))),
	ForAll([x], Not(Or(var99(x), var5(x), var66(x), var217(x), Not(var121(x)), var189(x), var102(x), var192(x), var11(x), var220(x)))),
	ForAll([x], Not(Or(var235(x), var161(x), Not(var2(x)), var151(x), var192(x), var163(x), Not(var204(x)), Not(var191(x)), var19(x), Not(var82(x))))),
	ForAll([x], Not(Or(var172(x), Not(var61(x)), var161(x), var110(x), var213(x), Not(var45(x)), Not(var73(x)), Not(var223(x)), Not(var15(x)), var184(x)))),
	ForAll([x], Not(Or(Not(var33(x)), Not(var162(x)), Not(var9(x)), Not(var209(x)), Not(var237(x)), var221(x), Not(var46(x)), Not(var123(x)), Not(var60(x)), var120(x)))),
	ForAll([x], Not(Or(var37(x), Not(var118(x)), var39(x), var15(x), Not(var192(x)), Not(var55(x)), Not(var165(x)), var155(x), Not(var108(x)), Not(var195(x))))),
	ForAll([x], Not(Or(var67(x), Not(var2(x)), Not(var9(x)), var63(x), Not(var125(x)), Not(var230(x)), Not(var234(x)), var138(x), Not(var3(x)), Not(var134(x))))),
	ForAll([x], Not(Or(var21(x), Not(var22(x)), var218(x), var250(x), var157(x), var130(x), Not(var6(x)), var88(x), var64(x), Not(var198(x))))),
	ForAll([x], Not(Or(var91(x), Not(var95(x)), Not(var203(x)), var188(x), var68(x), Not(var106(x)), Not(var204(x)), var141(x), Not(var220(x)), var58(x)))),
	ForAll([x], Not(Or(var198(x), var99(x), var13(x), Not(var163(x)), Not(var127(x)), Not(var6(x)), Not(var203(x)), Not(var147(x)), var67(x), Not(var226(x))))),
	ForAll([x], Not(Or(var45(x), var3(x), var124(x), Not(var241(x)), var56(x), var237(x), Not(var132(x)), Not(var108(x)), Not(var218(x)), var32(x)))),
	ForAll([x], Not(Or(Not(var111(x)), Not(var238(x)), var44(x), Not(var92(x)), var83(x), var1(x), Not(var249(x)), Not(var40(x)), var19(x), Not(var89(x))))),
	ForAll([x], Not(Or(Not(var31(x)), var160(x), var195(x), Not(var183(x)), var155(x), var233(x), var110(x), Not(var128(x)), var235(x), var60(x)))),
	ForAll([x], Not(Or(Not(var27(x)), Not(var248(x)), Not(var219(x)), Not(var6(x)), var125(x), var152(x), Not(var111(x)), Not(var110(x)), Not(var2(x)), var107(x)))),
	ForAll([x], Not(Or(var137(x), var26(x), var209(x), var72(x), var43(x), Not(var236(x)), var154(x), Not(var216(x)), Not(var144(x)), Not(var123(x))))),
	ForAll([x], Not(Or(Not(var174(x)), var171(x), Not(var229(x)), Not(var246(x)), var126(x), Not(var49(x)), var62(x), var45(x), Not(var9(x)), var154(x)))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var188(x)), Not(var167(x)), Not(var99(x)), var71(x), Not(var57(x)), Not(var50(x)), var128(x), Not(var162(x)), var32(x)))),
	ForAll([x], Not(Or(var208(x), Not(var114(x)), var238(x), Not(var211(x)), Not(var218(x)), Not(var213(x)), var197(x), var2(x), var58(x), Not(var40(x))))),
	ForAll([x], Not(Or(var11(x), Not(var130(x)), var38(x), var127(x), Not(var128(x)), Not(var242(x)), var73(x), var125(x), Not(var244(x)), Not(var72(x))))),
	ForAll([x], Not(Or(Not(var212(x)), var13(x), var238(x), Not(var24(x)), var236(x), var54(x), Not(var224(x)), var49(x), Not(var91(x)), Not(var107(x))))),
	ForAll([x], Not(Or(var214(x), var145(x), Not(var82(x)), Not(var8(x)), Not(var226(x)), var183(x), Not(var62(x)), Not(var181(x)), Not(var84(x)), var234(x)))),
	ForAll([x], Not(Or(var240(x), var4(x), Not(var112(x)), var115(x), var6(x), Not(var45(x)), var161(x), var206(x), var105(x), var143(x)))),
	ForAll([x], Not(Or(Not(var234(x)), var179(x), Not(var124(x)), Not(var58(x)), Not(var148(x)), var102(x), Not(var12(x)), Not(var165(x)), var158(x), var6(x)))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var211(x)), var133(x), Not(var66(x)), var186(x), var235(x), var175(x), Not(var173(x)), Not(var55(x)), var205(x)))),
	ForAll([x], Not(Or(Not(var151(x)), Not(var57(x)), Not(var153(x)), Not(var69(x)), var182(x), var8(x), var221(x), Not(var35(x)), var195(x), var102(x)))),
	ForAll([x], Not(Or(Not(var130(x)), var140(x), var9(x), var81(x), var185(x), Not(var44(x)), var225(x), Not(var240(x)), var40(x), var91(x)))),
	ForAll([x], Not(Or(var69(x), Not(var162(x)), Not(var78(x)), Not(var134(x)), Not(var161(x)), var206(x), var151(x), var209(x), var236(x), Not(var113(x))))),
	ForAll([x], Not(Or(Not(var6(x)), var96(x), Not(var21(x)), var238(x), var171(x), Not(var151(x)), var107(x), var20(x), var143(x), Not(var58(x))))),
	ForAll([x], Not(Or(Not(var212(x)), Not(var87(x)), Not(var92(x)), var58(x), var240(x), var158(x), var222(x), var24(x), Not(var188(x)), var235(x)))),
	ForAll([x], Not(Or(Not(var17(x)), var114(x), Not(var20(x)), Not(var221(x)), Not(var65(x)), Not(var110(x)), var43(x), Not(var157(x)), Not(var5(x)), var177(x)))),
	ForAll([x], Not(Or(Not(var235(x)), Not(var225(x)), Not(var157(x)), var180(x), Not(var182(x)), var104(x), var211(x), var102(x), var14(x), var124(x)))),
	ForAll([x], Not(Or(Not(var206(x)), Not(var26(x)), Not(var145(x)), Not(var105(x)), var181(x), var131(x), var68(x), var41(x), Not(var102(x)), var189(x)))),
	ForAll([x], Not(Or(Not(var132(x)), var122(x), var250(x), Not(var82(x)), var157(x), var149(x), var178(x), var38(x), var41(x), var87(x)))),
	ForAll([x], Not(Or(Not(var59(x)), var63(x), var189(x), var1(x), Not(var169(x)), var84(x), var86(x), Not(var183(x)), Not(var40(x)), var177(x)))),
	ForAll([x], Not(Or(Not(var134(x)), var180(x), Not(var248(x)), Not(var95(x)), Not(var22(x)), var153(x), Not(var33(x)), var36(x), Not(var15(x)), var240(x)))),
	ForAll([x], Not(Or(Not(var225(x)), var240(x), var98(x), var211(x), var54(x), var12(x), var53(x), Not(var201(x)), Not(var134(x)), var204(x)))),
	ForAll([x], Not(Or(Not(var92(x)), Not(var122(x)), var78(x), var90(x), var226(x), Not(var69(x)), Not(var186(x)), var115(x), Not(var139(x)), Not(var53(x))))),
	ForAll([x], Not(Or(Not(var21(x)), Not(var190(x)), var49(x), var68(x), var234(x), var23(x), Not(var241(x)), Not(var28(x)), Not(var27(x)), Not(var65(x))))),
	ForAll([x], Not(Or(var27(x), var223(x), Not(var54(x)), Not(var140(x)), var198(x), var143(x), Not(var189(x)), Not(var185(x)), var170(x), Not(var236(x))))),
	ForAll([x], Not(Or(var74(x), var47(x), var189(x), Not(var37(x)), Not(var5(x)), Not(var111(x)), Not(var225(x)), Not(var77(x)), Not(var119(x)), var27(x)))),
	ForAll([x], Not(Or(var15(x), Not(var177(x)), Not(var2(x)), Not(var72(x)), var169(x), Not(var37(x)), Not(var74(x)), Not(var77(x)), Not(var97(x)), Not(var39(x))))),
	ForAll([x], Not(Or(Not(var103(x)), var129(x), var223(x), var249(x), Not(var142(x)), Not(var36(x)), var165(x), Not(var168(x)), var196(x), var81(x)))),
	ForAll([x], Not(Or(var147(x), var157(x), var170(x), var192(x), Not(var65(x)), Not(var206(x)), var43(x), Not(var208(x)), Not(var197(x)), var67(x)))),
	ForAll([x], Not(Or(var195(x), var21(x), Not(var151(x)), var250(x), var139(x), var158(x), var52(x), var146(x), Not(var118(x)), Not(var22(x))))),
	ForAll([x], Not(Or(var200(x), Not(var108(x)), Not(var14(x)), Not(var225(x)), var131(x), var94(x), var150(x), var27(x), Not(var38(x)), Not(var91(x))))),
	ForAll([x], Not(Or(Not(var65(x)), Not(var114(x)), var89(x), Not(var126(x)), var33(x), Not(var118(x)), Not(var204(x)), Not(var229(x)), var97(x), var116(x)))),
	ForAll([x], Not(Or(Not(var15(x)), Not(var45(x)), var25(x), Not(var188(x)), Not(var210(x)), Not(var132(x)), Not(var147(x)), var44(x), var159(x), Not(var215(x))))),
	ForAll([x], Not(Or(var39(x), var203(x), var217(x), Not(var236(x)), Not(var12(x)), var207(x), var106(x), Not(var147(x)), var19(x), Not(var211(x))))),
	ForAll([x], Not(Or(var230(x), Not(var27(x)), var161(x), var47(x), var180(x), var38(x), Not(var234(x)), var178(x), Not(var82(x)), var242(x)))),
	ForAll([x], Not(Or(Not(var32(x)), Not(var198(x)), Not(var99(x)), Not(var176(x)), Not(var115(x)), var19(x), var229(x), Not(var238(x)), var83(x), var95(x)))),
	ForAll([x], Not(Or(var191(x), Not(var64(x)), Not(var24(x)), var132(x), var206(x), Not(var100(x)), Not(var33(x)), Not(var169(x)), Not(var29(x)), Not(var231(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var108(x1)), Or(var199(x), var149(x), Not(var8(x)), Not(var193(x)), var23(x), Not(var226(x)), var165(x), var232(x), var200(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var177(x1)), Not(var1(x1)), Not(var14(x1))), Or(Not(var51(x)), var144(x), var59(x), var187(x), Not(var79(x)), var142(x), Not(var134(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var152(x1)), var194(x1)), Or(Not(var175(x)), var103(x), Not(var3(x)), var50(x), var124(x), Not(var201(x)), Not(var218(x)), var230(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var49(x1), Not(var225(x1)), var211(x1), var63(x1), Not(var121(x1))), Or(Not(var209(x)), var135(x), Not(var66(x)), Not(var14(x)), var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var140(x1), var242(x1), var238(x1), var187(x1), var37(x1), Not(var68(x1)), Not(var61(x1))), Or(var204(x), var59(x), var185(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var37(x1), var121(x1), var202(x1), var16(x1), Not(var136(x1)), Not(var125(x1))), Or(Not(var171(x)), var98(x), var58(x), Not(var137(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var164(x1)), Not(var237(x1)), Not(var70(x1)), Not(var194(x1))), Or(var119(x), var227(x), Not(var242(x)), Not(var48(x)), Not(var188(x)), Not(var87(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var196(x1)), Not(var92(x1))), Or(Not(var77(x)), var62(x), Not(var134(x)), Not(var214(x)), Not(var233(x)), var42(x), var56(x), Not(var14(x))))))),
	ForAll([x], Not(Or(var165(x), Not(var161(x)), Not(var163(x)), var108(x)))),
	ForAll([x], Not(Or(Not(var152(x)), var90(x), var3(x), var73(x))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())