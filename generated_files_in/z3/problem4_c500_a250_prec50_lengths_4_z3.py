from z3 import *

Object = DeclareSort('Object')

var90 = Function('var90', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms0 = [
	ForAll([x], Not(Or(var90(x), var148(x), var9(x), Not(var120(x))))),
	ForAll([x], Not(Or(Not(var15(x)), var239(x), var60(x), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var129(x)), Not(var69(x)), var97(x), var57(x)))),
	ForAll([x], Not(Or(var173(x), Not(var76(x)), Not(var165(x)), var186(x)))),
	ForAll([x], Not(Or(var49(x), var12(x), var115(x), Not(var85(x))))),
	ForAll([x], Not(Or(Not(var90(x)), Not(var79(x)), Not(var225(x)), Not(var17(x))))),
	ForAll([x], Not(Or(var235(x), Not(var14(x)), Not(var238(x)), var163(x)))),
	ForAll([x], Not(Or(var117(x), Not(var182(x)), Not(var229(x)), Not(var179(x))))),
	ForAll([x], Not(Or(Not(var158(x)), var29(x), Not(var190(x)), var161(x)))),
	ForAll([x], Not(Or(Not(var104(x)), var86(x), Not(var58(x)), var91(x)))),
	ForAll([x], Not(Or(var200(x), Not(var97(x)), var229(x), Not(var89(x))))),
	ForAll([x], Not(Or(Not(var57(x)), var139(x), Not(var179(x)), var70(x)))),
	ForAll([x], Not(Or(var154(x), var17(x), Not(var205(x)), Not(var195(x))))),
	ForAll([x], Not(Or(var115(x), Not(var97(x)), var131(x), Not(var102(x))))),
	ForAll([x], Not(Or(var14(x), var45(x), Not(var43(x)), Not(var109(x))))),
	ForAll([x], Not(Or(var8(x), Not(var82(x)), Not(var94(x)), Not(var86(x))))),
	ForAll([x], Not(Or(var193(x), var157(x), Not(var198(x)), var147(x)))),
	ForAll([x], Not(Or(Not(var135(x)), var107(x), var52(x), var4(x)))),
	ForAll([x], Not(Or(Not(var105(x)), Not(var248(x)), var39(x), var59(x)))),
	ForAll([x], Not(Or(Not(var199(x)), Not(var250(x)), Not(var180(x)), Not(var219(x))))),
	ForAll([x], Not(Or(var76(x), var106(x), Not(var210(x)), var177(x)))),
	ForAll([x], Not(Or(var165(x), var235(x), var239(x), var160(x)))),
	ForAll([x], Not(Or(Not(var21(x)), Not(var240(x)), var172(x), Not(var148(x))))),
	ForAll([x], Not(Or(Not(var187(x)), Not(var163(x)), var167(x), Not(var211(x))))),
	ForAll([x], Not(Or(Not(var151(x)), Not(var250(x)), Not(var128(x)), Not(var6(x))))),
	ForAll([x], Not(Or(Not(var126(x)), var230(x), Not(var151(x)), Not(var40(x))))),
	ForAll([x], Not(Or(Not(var156(x)), var250(x), Not(var20(x)), var122(x)))),
	ForAll([x], Not(Or(var23(x), var113(x), Not(var166(x)), var232(x)))),
	ForAll([x], Not(Or(var173(x), var53(x), Not(var118(x)), Not(var5(x))))),
	ForAll([x], Not(Or(var199(x), var89(x), Not(var150(x)), Not(var56(x))))),
	ForAll([x], Not(Or(Not(var147(x)), Not(var150(x)), var130(x), Not(var139(x))))),
	ForAll([x], Not(Or(Not(var131(x)), var177(x), Not(var33(x)), Not(var157(x))))),
	ForAll([x], Not(Or(Not(var220(x)), var134(x), var138(x), Not(var45(x))))),
	ForAll([x], Not(Or(var105(x), Not(var76(x)), var49(x), Not(var46(x))))),
	ForAll([x], Not(Or(Not(var91(x)), Not(var11(x)), Not(var55(x)), Not(var163(x))))),
	ForAll([x], Not(Or(var186(x), Not(var36(x)), var105(x), var49(x)))),
	ForAll([x], Not(Or(Not(var141(x)), Not(var51(x)), Not(var146(x)), Not(var25(x))))),
	ForAll([x], Not(Or(Not(var231(x)), Not(var137(x)), var40(x), Not(var42(x))))),
	ForAll([x], Not(Or(Not(var18(x)), var46(x), Not(var174(x)), var51(x)))),
	ForAll([x], Not(Or(var62(x), Not(var52(x)), Not(var63(x)), Not(var184(x))))),
	ForAll([x], Not(Or(Not(var68(x)), Not(var57(x)), var113(x), Not(var24(x))))),
	ForAll([x], Not(Or(var222(x), Not(var37(x)), Not(var228(x)), Not(var144(x))))),
	ForAll([x], Not(Or(Not(var12(x)), Not(var92(x)), var189(x), Not(var169(x))))),
	ForAll([x], Not(Or(Not(var170(x)), var218(x), Not(var198(x)), var84(x)))),
	ForAll([x], Not(Or(var82(x), Not(var148(x)), Not(var90(x)), var51(x)))),
	ForAll([x], Not(Or(var43(x), Not(var238(x)), var205(x), var180(x)))),
	ForAll([x], Not(Or(var163(x), var192(x), Not(var159(x)), Not(var21(x))))),
	ForAll([x], Not(Or(var189(x), Not(var84(x)), Not(var193(x)), var42(x)))),
	ForAll([x], Not(Or(Not(var6(x)), var183(x), var37(x), Not(var217(x))))),
	ForAll([x], Not(Or(Not(var127(x)), var13(x), var146(x), Not(var156(x))))),
	ForAll([x], Not(Or(Not(var40(x)), var4(x), Not(var249(x)), var26(x)))),
	ForAll([x], Not(Or(Not(var80(x)), Not(var101(x)), var79(x), var28(x)))),
	ForAll([x], Not(Or(Not(var194(x)), Not(var218(x)), var173(x), Not(var235(x))))),
	ForAll([x], Not(Or(Not(var153(x)), var6(x), Not(var182(x)), var233(x)))),
	ForAll([x], Not(Or(var52(x), var198(x), Not(var88(x)), Not(var120(x))))),
	ForAll([x], Not(Or(var9(x), Not(var76(x)), Not(var112(x)), Not(var235(x))))),
	ForAll([x], Not(Or(var111(x), var14(x), var82(x), var231(x)))),
	ForAll([x], Not(Or(var5(x), var38(x), Not(var212(x)), Not(var136(x))))),
	ForAll([x], Not(Or(Not(var230(x)), Not(var83(x)), var167(x), Not(var5(x))))),
	ForAll([x], Not(Or(Not(var179(x)), var55(x), var99(x), Not(var82(x))))),
	ForAll([x], Not(Or(Not(var105(x)), var198(x), Not(var56(x)), Not(var116(x))))),
	ForAll([x], Not(Or(var45(x), Not(var46(x)), var96(x), var196(x)))),
	ForAll([x], Not(Or(Not(var160(x)), Not(var213(x)), var33(x), Not(var134(x))))),
	ForAll([x], Not(Or(Not(var79(x)), Not(var180(x)), Not(var240(x)), var214(x)))),
	ForAll([x], Not(Or(var175(x), var15(x), Not(var85(x)), var31(x)))),
	ForAll([x], Not(Or(Not(var245(x)), var109(x), Not(var88(x)), Not(var203(x))))),
	ForAll([x], Not(Or(Not(var129(x)), Not(var150(x)), var80(x), Not(var120(x))))),
	ForAll([x], Not(Or(var223(x), var65(x), Not(var162(x)), Not(var233(x))))),
	ForAll([x], Not(Or(Not(var102(x)), var67(x), var21(x), Not(var6(x))))),
	ForAll([x], Not(Or(var190(x), Not(var66(x)), Not(var242(x)), var135(x)))),
	ForAll([x], Not(Or(var223(x), var233(x), Not(var242(x)), var238(x)))),
	ForAll([x], Not(Or(var248(x), var106(x), Not(var12(x)), Not(var216(x))))),
	ForAll([x], Not(Or(Not(var189(x)), Not(var185(x)), var91(x), var192(x)))),
	ForAll([x], Not(Or(Not(var155(x)), Not(var218(x)), Not(var38(x)), Not(var222(x))))),
	ForAll([x], Not(Or(var64(x), var197(x), Not(var240(x)), Not(var33(x))))),
	ForAll([x], Not(Or(Not(var18(x)), var165(x), Not(var54(x)), Not(var209(x))))),
	ForAll([x], Not(Or(Not(var218(x)), Not(var200(x)), var99(x), var144(x)))),
	ForAll([x], Not(Or(Not(var179(x)), Not(var177(x)), Not(var240(x)), Not(var183(x))))),
	ForAll([x], Not(Or(var161(x), Not(var128(x)), Not(var149(x)), var210(x)))),
	ForAll([x], Not(Or(var133(x), Not(var99(x)), Not(var141(x)), var85(x)))),
	ForAll([x], Not(Or(var137(x), var226(x), Not(var193(x)), Not(var158(x))))),
	ForAll([x], Not(Or(var178(x), var197(x), Not(var230(x)), var186(x)))),
	ForAll([x], Not(Or(var22(x), Not(var110(x)), Not(var58(x)), var139(x)))),
	ForAll([x], Not(Or(var129(x), Not(var107(x)), Not(var212(x)), Not(var199(x))))),
	ForAll([x], Not(Or(var206(x), var96(x), Not(var183(x)), Not(var230(x))))),
	ForAll([x], Not(Or(var126(x), var117(x), var207(x), var153(x)))),
	ForAll([x], Not(Or(Not(var164(x)), Not(var240(x)), Not(var248(x)), Not(var26(x))))),
	ForAll([x], Not(Or(Not(var99(x)), var221(x), Not(var246(x)), var109(x)))),
	ForAll([x], Not(Or(Not(var242(x)), var158(x), Not(var215(x)), var95(x)))),
	ForAll([x], Not(Or(var177(x), var163(x), Not(var187(x)), Not(var157(x))))),
	ForAll([x], Not(Or(var102(x), var213(x), Not(var131(x)), Not(var85(x))))),
	ForAll([x], Not(Or(Not(var109(x)), var77(x), var131(x), Not(var169(x))))),
	ForAll([x], Not(Or(var243(x), var211(x), Not(var196(x)), var138(x)))),
	ForAll([x], Not(Or(var2(x), Not(var30(x)), Not(var34(x)), Not(var221(x))))),
	ForAll([x], Not(Or(Not(var73(x)), Not(var84(x)), var86(x), Not(var135(x))))),
	ForAll([x], Not(Or(var168(x), var116(x), Not(var213(x)), var33(x)))),
	ForAll([x], Not(Or(Not(var136(x)), var40(x), Not(var235(x)), var239(x)))),
	ForAll([x], Not(Or(Not(var13(x)), var149(x), var228(x), var93(x)))),
	ForAll([x], Not(Or(Not(var200(x)), Not(var65(x)), var105(x), Not(var228(x))))),
	ForAll([x], Not(Or(var244(x), Not(var49(x)), var4(x), Not(var13(x))))),
	ForAll([x], Not(Or(var175(x), var242(x), var149(x), var108(x)))),
	ForAll([x], Not(Or(var167(x), Not(var233(x)), var44(x), Not(var19(x))))),
	ForAll([x], Not(Or(var1(x), var142(x), var138(x), var169(x)))),
	ForAll([x], Not(Or(Not(var167(x)), var104(x), var52(x), Not(var166(x))))),
	ForAll([x], Not(Or(Not(var117(x)), Not(var24(x)), Not(var126(x)), Not(var99(x))))),
	ForAll([x], Not(Or(Not(var149(x)), var73(x), var245(x), Not(var213(x))))),
	ForAll([x], Not(Or(Not(var134(x)), var208(x), var101(x), var161(x)))),
	ForAll([x], Not(Or(Not(var181(x)), var6(x), var221(x), var24(x)))),
	ForAll([x], Not(Or(var227(x), var73(x), var53(x), var9(x)))),
	ForAll([x], Not(Or(var70(x), Not(var2(x)), var162(x), var240(x)))),
	ForAll([x], Not(Or(var241(x), Not(var87(x)), var186(x), Not(var26(x))))),
	ForAll([x], Not(Or(var110(x), var168(x), var112(x), Not(var10(x))))),
	ForAll([x], Not(Or(Not(var136(x)), Not(var165(x)), Not(var73(x)), var161(x)))),
	ForAll([x], Not(Or(var95(x), Not(var222(x)), Not(var183(x)), var238(x)))),
	ForAll([x], Not(Or(var157(x), Not(var181(x)), var142(x), Not(var204(x))))),
	ForAll([x], Not(Or(Not(var33(x)), var36(x), var68(x), Not(var199(x))))),
	ForAll([x], Not(Or(var34(x), Not(var239(x)), Not(var242(x)), Not(var162(x))))),
	ForAll([x], Not(Or(Not(var38(x)), var73(x), Not(var76(x)), var122(x)))),
	ForAll([x], Not(Or(var147(x), var233(x), var42(x), var205(x)))),
	ForAll([x], Not(Or(var9(x), var136(x), Not(var63(x)), Not(var112(x))))),
	ForAll([x], Not(Or(var87(x), var56(x), var45(x), var155(x)))),
	ForAll([x], Not(Or(Not(var248(x)), var137(x), var86(x), var238(x)))),
	ForAll([x], Not(Or(var87(x), Not(var128(x)), var195(x), var243(x)))),
	ForAll([x], Not(Or(var109(x), var238(x), var248(x), var199(x)))),
	ForAll([x], Not(Or(var21(x), Not(var89(x)), Not(var55(x)), var193(x)))),
	ForAll([x], Not(Or(var202(x), var43(x), var48(x), Not(var238(x))))),
	ForAll([x], Not(Or(Not(var82(x)), Not(var76(x)), Not(var106(x)), var158(x)))),
	ForAll([x], Not(Or(Not(var9(x)), Not(var129(x)), Not(var147(x)), Not(var12(x))))),
	ForAll([x], Not(Or(Not(var222(x)), var87(x), Not(var72(x)), Not(var157(x))))),
	ForAll([x], Not(Or(var234(x), var135(x), Not(var166(x)), var86(x)))),
	ForAll([x], Not(Or(Not(var56(x)), var187(x), var138(x), var129(x)))),
	ForAll([x], Not(Or(Not(var174(x)), Not(var215(x)), var11(x), Not(var109(x))))),
	ForAll([x], Not(Or(Not(var183(x)), var69(x), var231(x), var228(x)))),
	ForAll([x], Not(Or(Not(var200(x)), var24(x), Not(var227(x)), var184(x)))),
	ForAll([x], Not(Or(var141(x), Not(var56(x)), Not(var65(x)), var215(x)))),
	ForAll([x], Not(Or(Not(var159(x)), var15(x), Not(var126(x)), var196(x)))),
	ForAll([x], Not(Or(var20(x), Not(var202(x)), var42(x), Not(var58(x))))),
	ForAll([x], Not(Or(var219(x), Not(var165(x)), Not(var86(x)), var104(x)))),
	ForAll([x], Not(Or(var196(x), Not(var228(x)), Not(var134(x)), Not(var222(x))))),
	ForAll([x], Not(Or(var195(x), Not(var142(x)), Not(var98(x)), Not(var138(x))))),
	ForAll([x], Not(Or(Not(var238(x)), Not(var16(x)), Not(var77(x)), Not(var172(x))))),
	ForAll([x], Not(Or(var178(x), Not(var182(x)), var9(x), var196(x)))),
	ForAll([x], Not(Or(Not(var92(x)), Not(var204(x)), var196(x), Not(var28(x))))),
	ForAll([x], Not(Or(var220(x), var250(x), var4(x), var130(x)))),
	ForAll([x], Not(Or(var16(x), Not(var34(x)), var66(x), var228(x)))),
	ForAll([x], Not(Or(var225(x), Not(var176(x)), var149(x), var89(x)))),
	ForAll([x], Not(Or(Not(var78(x)), Not(var50(x)), var181(x), var62(x)))),
	ForAll([x], Not(Or(Not(var81(x)), var72(x), var122(x), var110(x)))),
	ForAll([x], Not(Or(var91(x), Not(var113(x)), Not(var226(x)), Not(var160(x))))),
	ForAll([x], Not(Or(Not(var178(x)), var244(x), Not(var95(x)), var5(x)))),
	ForAll([x], Not(Or(var191(x), Not(var240(x)), var69(x), var178(x)))),
	ForAll([x], Not(Or(Not(var169(x)), var234(x), var65(x), var205(x)))),
	ForAll([x], Not(Or(var183(x), var154(x), Not(var82(x)), Not(var75(x))))),
	ForAll([x], Not(Or(var202(x), var119(x), Not(var217(x)), var28(x)))),
	ForAll([x], Not(Or(Not(var50(x)), var136(x), var114(x), Not(var182(x))))),
	ForAll([x], Not(Or(var223(x), var106(x), var236(x), var135(x)))),
	ForAll([x], Not(Or(Not(var169(x)), var123(x), var220(x), var95(x)))),
	ForAll([x], Not(Or(var215(x), var226(x), var4(x), var106(x)))),
	ForAll([x], Not(Or(var85(x), Not(var248(x)), var74(x), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var225(x)), var128(x), var163(x), Not(var6(x))))),
	ForAll([x], Not(Or(var70(x), var120(x), var134(x), var28(x)))),
	ForAll([x], Not(Or(var100(x), var242(x), var7(x), Not(var81(x))))),
	ForAll([x], Not(Or(var116(x), Not(var131(x)), var181(x), Not(var224(x))))),
	ForAll([x], Not(Or(Not(var127(x)), Not(var24(x)), var141(x), var201(x)))),
	ForAll([x], Not(Or(Not(var51(x)), var218(x), Not(var182(x)), Not(var53(x))))),
	ForAll([x], Not(Or(var218(x), Not(var140(x)), Not(var66(x)), Not(var70(x))))),
	ForAll([x], Not(Or(var60(x), Not(var52(x)), Not(var156(x)), var126(x)))),
	ForAll([x], Not(Or(Not(var118(x)), var97(x), Not(var48(x)), var220(x)))),
	ForAll([x], Not(Or(var122(x), var183(x), var233(x), var6(x)))),
	ForAll([x], Not(Or(Not(var250(x)), var23(x), Not(var242(x)), var193(x)))),
	ForAll([x], Not(Or(Not(var1(x)), Not(var191(x)), var68(x), var24(x)))),
	ForAll([x], Not(Or(Not(var45(x)), var219(x), Not(var106(x)), var149(x)))),
	ForAll([x], Not(Or(Not(var150(x)), var88(x), Not(var1(x)), var213(x)))),
	ForAll([x], Not(Or(Not(var199(x)), var3(x), var5(x), Not(var24(x))))),
	ForAll([x], Not(Or(var139(x), Not(var119(x)), var28(x), var216(x)))),
	ForAll([x], Not(Or(Not(var30(x)), var122(x), var152(x), Not(var18(x))))),
	ForAll([x], Not(Or(var142(x), Not(var75(x)), var206(x), Not(var121(x))))),
	ForAll([x], Not(Or(Not(var169(x)), var250(x), var171(x), var173(x)))),
	ForAll([x], Not(Or(Not(var158(x)), var88(x), var38(x), var132(x)))),
	ForAll([x], Not(Or(var129(x), var88(x), var20(x), var184(x)))),
	ForAll([x], Not(Or(var171(x), Not(var223(x)), Not(var219(x)), var199(x)))),
	ForAll([x], Not(Or(Not(var75(x)), var242(x), Not(var235(x)), var13(x)))),
	ForAll([x], Not(Or(var187(x), var250(x), var9(x), Not(var244(x))))),
	ForAll([x], Not(Or(Not(var51(x)), Not(var22(x)), Not(var88(x)), Not(var165(x))))),
	ForAll([x], Not(Or(Not(var105(x)), var64(x), var215(x), var95(x)))),
	ForAll([x], Not(Or(var41(x), var234(x), Not(var208(x)), var87(x)))),
	ForAll([x], Not(Or(Not(var234(x)), Not(var232(x)), Not(var178(x)), var139(x)))),
	ForAll([x], Not(Or(var149(x), Not(var103(x)), var31(x), var21(x)))),
	ForAll([x], Not(Or(var45(x), Not(var46(x)), var41(x), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var182(x)), Not(var59(x)), var50(x), Not(var1(x))))),
	ForAll([x], Not(Or(var29(x), var34(x), Not(var37(x)), var55(x)))),
	ForAll([x], Not(Or(Not(var100(x)), var79(x), Not(var188(x)), Not(var234(x))))),
	ForAll([x], Not(Or(var241(x), var137(x), Not(var212(x)), Not(var219(x))))),
	ForAll([x], Not(Or(Not(var84(x)), Not(var141(x)), Not(var189(x)), var242(x)))),
	ForAll([x], Not(Or(var193(x), Not(var224(x)), var33(x), Not(var196(x))))),
	ForAll([x], Not(Or(Not(var38(x)), Not(var35(x)), Not(var93(x)), var192(x)))),
	ForAll([x], Not(Or(var68(x), var134(x), var167(x), Not(var30(x))))),
	ForAll([x], Not(Or(var244(x), Not(var169(x)), var45(x), Not(var181(x))))),
	ForAll([x], Not(Or(Not(var63(x)), var99(x), Not(var204(x)), var117(x)))),
	ForAll([x], Not(Or(var202(x), var238(x), var73(x), var39(x)))),
	ForAll([x], Not(Or(var189(x), var17(x), var117(x), Not(var90(x))))),
	ForAll([x], Not(Or(var93(x), var174(x), Not(var138(x)), var39(x)))),
	ForAll([x], Not(Or(Not(var249(x)), Not(var127(x)), var113(x), var160(x)))),
	ForAll([x], Not(Or(Not(var44(x)), Not(var138(x)), var153(x), Not(var207(x))))),
	ForAll([x], Not(Or(var196(x), Not(var74(x)), Not(var149(x)), Not(var173(x))))),
	ForAll([x], Not(Or(Not(var121(x)), Not(var166(x)), var99(x), Not(var150(x))))),
	ForAll([x], Not(Or(Not(var60(x)), var95(x), Not(var99(x)), Not(var87(x))))),
	ForAll([x], Not(Or(Not(var110(x)), Not(var101(x)), Not(var119(x)), Not(var130(x))))),
	ForAll([x], Not(Or(var65(x), Not(var34(x)), var39(x), var30(x)))),
	ForAll([x], Not(Or(Not(var42(x)), Not(var208(x)), Not(var235(x)), Not(var8(x))))),
	ForAll([x], Not(Or(Not(var72(x)), Not(var210(x)), var132(x), Not(var167(x))))),
	ForAll([x], Not(Or(Not(var192(x)), var54(x), Not(var38(x)), var90(x)))),
	ForAll([x], Not(Or(Not(var132(x)), Not(var165(x)), var210(x), var189(x)))),
	ForAll([x], Not(Or(var62(x), Not(var34(x)), var169(x), var103(x)))),
	ForAll([x], Not(Or(var179(x), Not(var183(x)), var212(x), Not(var220(x))))),
	ForAll([x], Not(Or(var118(x), var114(x), Not(var102(x)), var84(x)))),
	ForAll([x], Not(Or(Not(var156(x)), var182(x), Not(var175(x)), Not(var57(x))))),
	ForAll([x], Not(Or(Not(var141(x)), var159(x), var171(x), Not(var84(x))))),
	ForAll([x], Not(Or(var70(x), Not(var235(x)), Not(var120(x)), Not(var178(x))))),
	ForAll([x], Not(Or(Not(var238(x)), Not(var215(x)), Not(var60(x)), var77(x)))),
	ForAll([x], Not(Or(var41(x), var51(x), var34(x), var210(x)))),
	ForAll([x], Not(Or(Not(var241(x)), var201(x), var74(x), var40(x)))),
	ForAll([x], Not(Or(var192(x), var145(x), Not(var10(x)), Not(var35(x))))),
	ForAll([x], Not(Or(var142(x), Not(var228(x)), Not(var216(x)), Not(var6(x))))),
	ForAll([x], Not(Or(Not(var97(x)), var230(x), Not(var37(x)), Not(var72(x))))),
	ForAll([x], Not(Or(Not(var126(x)), Not(var162(x)), Not(var161(x)), var186(x)))),
	ForAll([x], Not(Or(Not(var240(x)), var224(x), Not(var132(x)), Not(var193(x))))),
	ForAll([x], Not(Or(Not(var175(x)), Not(var71(x)), Not(var181(x)), Not(var167(x))))),
	ForAll([x], Not(Or(Not(var67(x)), Not(var168(x)), Not(var72(x)), var95(x)))),
	ForAll([x], Not(Or(Not(var207(x)), Not(var110(x)), var87(x), var126(x)))),
	ForAll([x], Not(Or(var199(x), Not(var14(x)), Not(var16(x)), Not(var12(x))))),
	ForAll([x], Not(Or(var27(x), Not(var46(x)), var202(x), Not(var136(x))))),
	ForAll([x], Not(Or(Not(var48(x)), Not(var30(x)), var193(x), Not(var224(x))))),
	ForAll([x], Not(Or(Not(var51(x)), Not(var172(x)), var173(x), Not(var177(x))))),
	ForAll([x], Not(Or(Not(var112(x)), Not(var126(x)), var106(x), var41(x)))),
	ForAll([x], Not(Or(var239(x), var222(x), Not(var215(x)), var242(x)))),
	ForAll([x], Not(Or(var33(x), Not(var198(x)), Not(var62(x)), Not(var28(x))))),
	ForAll([x], Not(Or(var112(x), var157(x), Not(var244(x)), var33(x)))),
	ForAll([x], Not(Or(Not(var213(x)), Not(var176(x)), Not(var148(x)), Not(var209(x))))),
	ForAll([x], Not(Or(var151(x), var123(x), var14(x), Not(var21(x))))),
	ForAll([x], Not(Or(Not(var53(x)), var110(x), Not(var86(x)), var144(x)))),
	ForAll([x], Not(Or(var147(x), Not(var32(x)), Not(var175(x)), var13(x)))),
	ForAll([x], Not(Or(Not(var98(x)), var186(x), var115(x), var182(x)))),
	ForAll([x], Not(Or(var168(x), var3(x), var239(x), var130(x)))),
	ForAll([x], Not(Or(Not(var160(x)), Not(var41(x)), var118(x), var16(x)))),
	ForAll([x], Not(Or(var62(x), var63(x), Not(var243(x)), Not(var135(x))))),
	ForAll([x], Not(Or(var245(x), var134(x), var192(x), Not(var198(x))))),
	ForAll([x], Not(Or(var98(x), Not(var116(x)), Not(var44(x)), Not(var141(x))))),
	ForAll([x], Not(Or(Not(var43(x)), var99(x), var198(x), Not(var209(x))))),
	ForAll([x], Not(Or(var87(x), var124(x), Not(var11(x)), Not(var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var116(x1)), var171(x1)), Or(var122(x), var215(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var31(x1)), Or(var110(x), Not(var223(x)), var172(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var149(x1)), Not(var2(x1)), var195(x1)), Not(var150(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var7(x1), Not(var94(x1)), Not(var13(x1))), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var34(x1), var83(x1)), Or(Not(var3(x)), Not(var117(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var200(x1)), var174(x1)), Or(Not(var48(x)), Not(var156(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var226(x1), var157(x1)), Or(var199(x), var247(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var11(x1), Not(var22(x1)), var250(x1)), Not(var146(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var85(x1), var80(x1), Not(var167(x1))), Not(var114(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var168(x1)), var75(x1)), Or(var95(x), Not(var105(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var212(x1), Or(var70(x), Not(var188(x)), Not(var128(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var199(x1), var196(x1)), Or(var59(x), var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), Or(var119(x), Not(var215(x)), Not(var250(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var32(x1)), var88(x1)), Or(Not(var110(x)), Not(var111(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var145(x1)), Or(Not(var119(x)), var19(x), Not(var49(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var98(x1)), Not(var130(x1))), Or(Not(var94(x)), var193(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var17(x1), Or(Not(var44(x)), Not(var19(x)), Not(var107(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var188(x1), Or(Not(var204(x)), var27(x), var218(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), Or(var243(x), Not(var59(x)), Not(var175(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var123(x1), var163(x1), Not(var190(x1))), var193(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var250(x1), var111(x1), Not(var190(x1))), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var124(x1), Or(var121(x), var26(x), Not(var117(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var128(x1)), Or(Not(var175(x)), var148(x), Not(var34(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var154(x1)), Not(var248(x1))), Or(var159(x), var148(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), Or(Not(var173(x)), Not(var205(x)), var79(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var17(x1)), var141(x1)), Or(Not(var160(x)), Not(var13(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var135(x1), var199(x1), Not(var62(x1))), Not(var215(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var54(x1), Not(var65(x1))), Or(var59(x), var132(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var22(x1)), Not(var86(x1))), Or(var183(x), var119(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var179(x1)), Or(var142(x), var70(x), var84(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var6(x1)), var207(x1)), Or(Not(var175(x)), Not(var214(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var79(x1), var37(x1), Not(var4(x1))), var65(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var6(x1)), Not(var112(x1))), Or(var104(x), var135(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var169(x1)), Not(var102(x1))), Or(Not(var125(x)), Not(var85(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var231(x1)), var150(x1)), Or(var168(x), var97(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var146(x1)), Or(var105(x), Not(var69(x)), Not(var73(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var44(x1), Or(var70(x), Not(var40(x)), Not(var73(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var232(x1)), var135(x1), Not(var23(x1))), var191(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var192(x1), Or(var229(x), var135(x), Not(var247(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var116(x1)), var47(x1), var173(x1)), Not(var234(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var246(x1), Not(var91(x1))), Or(Not(var88(x)), var214(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var151(x1), var69(x1), var145(x1)), var170(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var84(x1)), Not(var172(x1))), Or(var146(x), Not(var53(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var150(x1)), Or(var27(x), Not(var17(x)), var110(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var9(x1), var213(x1), Not(var190(x1))), var61(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var210(x1), Or(var219(x), Not(var36(x)), Not(var130(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var212(x1)), Or(var76(x), Not(var158(x)), var160(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var48(x1), Not(var206(x1))), Or(Not(var227(x)), Not(var90(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var27(x1)), Not(var100(x1))), Or(var59(x), var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var11(x1), Not(var246(x1)), Not(var173(x1))), Not(var200(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var50(x1)), Not(var190(x1))), Or(Not(var220(x)), var246(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var41(x1)), var200(x1)), Or(Not(var249(x)), Not(var78(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var89(x1), Not(var130(x1))), Or(var159(x), var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var28(x1)), var214(x1)), Or(var98(x), Not(var65(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var130(x1)), Not(var34(x1)), Not(var240(x1))), Not(var83(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var195(x1), var122(x1)), Or(var233(x), Not(var72(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var147(x1)), Or(var234(x), var70(x), var140(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var63(x1), Or(Not(var163(x)), Not(var11(x)), var67(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var241(x1), Or(var8(x), Not(var177(x)), Not(var18(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var97(x1), var90(x1), Not(var153(x1))), var211(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Or(Not(var93(x)), Not(var189(x)), var236(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var199(x1), Not(var167(x1)), var230(x1)), Not(var149(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var210(x1), Not(var242(x1))), Or(var228(x), var221(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var22(x1)), Or(var84(x), var159(x), var154(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var166(x1), Not(var175(x1))), Or(var203(x), var240(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var21(x1)), var106(x1)), Or(Not(var166(x)), var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var244(x1)), var160(x1), Not(var178(x1))), Not(var197(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var84(x1)), Not(var200(x1))), Or(var185(x), Not(var213(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), Or(var159(x), var44(x), var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var190(x1), var76(x1), var228(x1)), var233(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var161(x1)), Or(var72(x), Not(var176(x)), var222(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var249(x1)), var212(x1)), Or(Not(var41(x)), Not(var188(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var109(x1)), Or(var123(x), Not(var97(x)), var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var54(x1)), Or(Not(var217(x)), var210(x), Not(var153(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var70(x1), Not(var214(x1))), Or(var116(x), Not(var211(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var50(x1)), var218(x1)), Or(Not(var151(x)), var199(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var109(x1), Not(var245(x1))), Or(var150(x), Not(var118(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var76(x1)), Or(Not(var62(x)), Not(var97(x)), Not(var211(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var140(x1), Not(var156(x1)), var47(x1)), var158(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var107(x1), Not(var215(x1))), Or(var197(x), Not(var196(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var43(x1), var155(x1)), Or(Not(var44(x)), var226(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var234(x1)), var249(x1), Not(var208(x1))), var179(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), Or(var128(x), Not(var249(x)), var107(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var75(x1)), Not(var124(x1)), var47(x1)), var96(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var155(x1)), Not(var222(x1))), Or(var59(x), Not(var99(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var6(x1)), Or(Not(var69(x)), Not(var14(x)), Not(var142(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var135(x1)), Not(var188(x1)), Not(var34(x1))), var184(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var213(x1), var231(x1), var138(x1)), Not(var246(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var128(x1)), var73(x1), var118(x1)), Not(var242(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var222(x1)), Or(Not(var8(x)), Not(var18(x)), var170(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var173(x1)), Not(var140(x1))), Or(var155(x), Not(var230(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var113(x1), Or(Not(var93(x)), var60(x), Not(var57(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var28(x1)), Not(var64(x1)), var85(x1)), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var45(x1), Not(var120(x1)), Not(var77(x1))), var200(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var141(x1)), Not(var210(x1))), Or(var104(x), var171(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var181(x1), Or(Not(var18(x)), Not(var29(x)), Not(var164(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var183(x1)), Or(Not(var249(x)), Not(var208(x)), Not(var45(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var160(x1), Not(var52(x1))), Or(var219(x), var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var118(x1), var46(x1)), Or(var8(x), Not(var82(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var245(x1)), Not(var210(x1))), Or(var230(x), Not(var223(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var123(x1)), var190(x1)), Or(Not(var236(x)), var126(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var45(x1)), var74(x1), Not(var164(x1))), Not(var245(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var18(x1), var75(x1), Not(var210(x1))), var245(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var127(x1), var63(x1)), Or(var91(x), var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var176(x1), var190(x1)), Or(Not(var94(x)), Not(var28(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var249(x1)), Or(var60(x), Not(var24(x)), var157(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var172(x1), var49(x1), Not(var243(x1))), Not(var163(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var206(x1)), Not(var227(x1))), Or(Not(var111(x)), var117(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var67(x1), Not(var48(x1)), Not(var125(x1))), var54(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var64(x1), Not(var24(x1))), Or(var89(x), var130(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var70(x1), Not(var234(x1))), Or(Not(var192(x)), var53(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var207(x1), Not(var57(x1)), var91(x1)), var124(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var152(x1), var13(x1), var192(x1)), var240(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var116(x1)), Or(var236(x), var205(x), Not(var97(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var41(x1), Or(Not(var190(x)), Not(var240(x)), Not(var232(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var212(x1)), var111(x1), Not(var128(x1))), Not(var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var76(x1)), Not(var16(x1)), Not(var219(x1))), Not(var225(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var145(x1)), Not(var48(x1)), var156(x1)), var172(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var128(x1)), Or(Not(var114(x)), Not(var139(x)), var113(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var113(x1), Not(var177(x1))), Or(Not(var237(x)), Not(var211(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var233(x1), var154(x1)), Or(Not(var83(x)), var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var240(x1), var218(x1), Not(var2(x1))), Not(var76(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var144(x1), Or(var19(x), Not(var138(x)), var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var72(x1), Not(var84(x1))), Or(Not(var136(x)), Not(var162(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var169(x1)), var183(x1)), Or(Not(var13(x)), var228(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var87(x1), Not(var250(x1))), Or(var102(x), Not(var170(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var105(x1)), var178(x1)), Or(var234(x), var232(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var8(x1), var125(x1)), Or(Not(var154(x)), Not(var13(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var1(x1), Not(var186(x1)), var127(x1)), Not(var235(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var241(x1)), var16(x1), var11(x1)), var37(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Or(Not(var176(x)), var50(x), Not(var191(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var92(x1), var32(x1)), Or(var10(x), var201(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var183(x1), var33(x1), Not(var46(x1))), Not(var244(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var228(x1), Or(var60(x), var25(x), Not(var108(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var74(x1)), Or(Not(var35(x)), var231(x), Not(var10(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var37(x1), Or(var101(x), Not(var112(x)), Not(var131(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var169(x1)), var179(x1), var55(x1)), Not(var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var194(x1)), Not(var121(x1))), Or(var134(x), Not(var43(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var151(x1), var76(x1)), Or(var117(x), Not(var49(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var37(x1), Or(var168(x), var229(x), Not(var79(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var10(x1), Not(var191(x1)), Not(var37(x1))), Not(var98(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var235(x1), var86(x1), var156(x1)), var91(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var73(x1)), Not(var41(x1))), Or(var121(x), var132(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var149(x1)), Or(var161(x), Not(var66(x)), Not(var244(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var145(x1), Or(var225(x), var64(x), Not(var11(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var246(x1), Not(var70(x1))), Or(Not(var166(x)), var141(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var18(x1)), Or(var147(x), Not(var54(x)), var194(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var117(x1), var167(x1), Not(var72(x1))), var246(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var165(x1), var25(x1)), Or(Not(var31(x)), var44(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var66(x1)), Not(var230(x1)), Not(var226(x1))), var210(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var178(x1)), Not(var88(x1)), var54(x1)), var105(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var150(x1), Not(var250(x1)), Not(var160(x1))), Not(var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var23(x1)), Or(Not(var141(x)), var18(x), Not(var76(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var87(x1)), Not(var141(x1))), Or(var98(x), var177(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var10(x1), Or(var63(x), Not(var54(x)), Not(var79(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), Or(var124(x), Not(var110(x)), Not(var227(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var211(x1), Or(Not(var93(x)), var180(x), var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var36(x1), var148(x1)), Or(var163(x), Not(var24(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var86(x1), Not(var138(x1)), Not(var41(x1))), Not(var162(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), Or(Not(var228(x)), Not(var221(x)), Not(var184(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var107(x1)), Not(var44(x1)), Not(var83(x1))), var81(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var93(x1)), Not(var31(x1)), Not(var151(x1))), Not(var108(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var101(x1), Or(Not(var47(x)), Not(var249(x)), Not(var223(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var135(x1), Not(var4(x1))), Or(Not(var177(x)), Not(var202(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var107(x1), var51(x1), Not(var137(x1))), Not(var216(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var131(x1)), var212(x1)), Or(var197(x), Not(var62(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var139(x1), Not(var117(x1)), Not(var16(x1))), Not(var126(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var135(x1), var33(x1)), Or(var170(x), Not(var119(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var173(x1), Or(Not(var191(x)), var18(x), var89(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var34(x1)), Or(var60(x), var27(x), Not(var185(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Or(var137(x), Not(var143(x)), var49(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var82(x1), var130(x1)), Or(Not(var170(x)), var138(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var164(x1)), var203(x1), Not(var216(x1))), var195(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var1(x1), Not(var160(x1))), Or(var138(x), var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var54(x1), Not(var26(x1))), Or(Not(var69(x)), var215(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var105(x1), Not(var11(x1))), Or(Not(var50(x)), var84(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var14(x1)), Not(var168(x1)), Not(var224(x1))), Not(var108(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var65(x1)), Or(Not(var220(x)), Not(var131(x)), var36(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var42(x1)), var185(x1)), Or(Not(var163(x)), Not(var4(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var164(x1)), Not(var157(x1))), Or(Not(var45(x)), Not(var99(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var82(x1), Not(var239(x1)), Not(var133(x1))), Not(var59(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var173(x1)), Or(var48(x), var10(x), var67(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var69(x1)), var199(x1)), Or(Not(var231(x)), Not(var230(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var92(x1), Or(var220(x), Not(var157(x)), var208(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var102(x1), Or(Not(var8(x)), Not(var168(x)), Not(var55(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var162(x1), Or(Not(var49(x)), var211(x), Not(var242(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var95(x1), Or(var67(x), Not(var242(x)), var51(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var119(x1)), Or(var108(x), var212(x), var215(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var1(x1), var13(x1), var130(x1)), Not(var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var21(x1), var193(x1)), Or(var222(x), var154(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var79(x1)), Or(var214(x), var128(x), Not(var74(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var199(x1)), var57(x1), var155(x1)), Not(var151(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var72(x1), var213(x1)), Or(var92(x), Not(var106(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var159(x1), var240(x1)), Or(Not(var235(x)), Not(var76(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Or(var182(x), var134(x), Not(var4(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var68(x1)), Or(Not(var96(x)), var162(x), Not(var238(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var168(x1)), var8(x1), var211(x1)), var181(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var144(x1)), Or(Not(var187(x)), Not(var88(x)), Not(var225(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var3(x1), Not(var7(x1)), var195(x1)), var203(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), Or(Not(var229(x)), var165(x), var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var150(x1)), Not(var124(x1))), Or(var141(x), Not(var189(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var129(x1)), Not(var20(x1))), Or(var40(x), var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var48(x1)), Not(var154(x1))), Or(Not(var157(x)), var231(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var249(x1)), var133(x1)), Or(var94(x), Not(var136(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var11(x1)), Not(var116(x1))), Or(var141(x), var117(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var51(x1), Not(var216(x1))), Or(Not(var98(x)), Not(var179(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var116(x1), Or(Not(var202(x)), var194(x), var248(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var245(x1)), Or(Not(var99(x)), var236(x), Not(var31(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var95(x1), var90(x1)), Or(Not(var13(x)), Not(var43(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var139(x1), var227(x1), Not(var248(x1))), Not(var117(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var223(x1), Not(var91(x1))), Or(Not(var191(x)), var171(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var222(x1), Not(var131(x1)), var138(x1)), Not(var197(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), Or(var172(x), var189(x), var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var143(x1)), var8(x1), var177(x1)), var225(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Or(var52(x), Not(var35(x)), Not(var163(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var243(x1)), Or(Not(var207(x)), var105(x), Not(var172(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var90(x1), Not(var103(x1)), Not(var52(x1))), var155(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var135(x1)), Or(var133(x), var214(x), Not(var166(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var156(x1), var166(x1), var26(x1)), var122(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var103(x1)), Or(var57(x), var7(x), Not(var107(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var55(x1)), var97(x1)), Or(var25(x), Not(var115(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var47(x1), var176(x1), Not(var72(x1))), var243(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var173(x1)), Or(var204(x), Not(var165(x)), Not(var199(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var213(x1), Not(var28(x1))), Or(var37(x), Not(var201(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var227(x1), Or(var207(x), var195(x), Not(var16(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var229(x1), var35(x1)), Or(Not(var186(x)), var244(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var140(x1)), Or(var154(x), var135(x), var9(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var78(x1), Not(var13(x1)), var189(x1)), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var243(x1)), Not(var52(x1))), Or(Not(var192(x)), var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var11(x1)), Or(var172(x), var19(x), var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var245(x1), Not(var160(x1))), Or(var243(x), var230(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var113(x1), Not(var235(x1)), var142(x1)), Not(var243(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var247(x1), Not(var105(x1)), Not(var10(x1))), var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var217(x1)), Or(var37(x), var82(x), var152(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var216(x1)), Or(var152(x), Not(var35(x)), Not(var154(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var240(x1)), Or(var174(x), var101(x), var143(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var247(x1)), var150(x1)), Or(Not(var238(x)), var208(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var87(x1)), var67(x1), Not(var35(x1))), Not(var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var111(x1), Or(Not(var142(x)), Not(var238(x)), var194(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var248(x1)), var221(x1), var71(x1)), var93(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var216(x1)), Not(var5(x1))), Or(Not(var185(x)), var241(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var66(x1), var26(x1), Not(var165(x1))), Not(var35(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var172(x1), Not(var31(x1)), var142(x1)), Not(var36(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var222(x1)), Or(Not(var20(x)), var3(x), var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var125(x1), Or(var186(x), var10(x), var235(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var105(x1), Or(Not(var55(x)), var9(x), Not(var131(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var172(x1), Not(var60(x1)), Not(var33(x1))), Not(var48(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var162(x1)), Or(Not(var38(x)), var5(x), Not(var131(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var58(x1), Or(Not(var85(x)), Not(var120(x)), Not(var124(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var158(x1), var170(x1)), Or(var162(x), Not(var6(x)))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms0)
print(s.check())
print(s.statistics())
