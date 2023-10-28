from z3 import *

Object = DeclareSort('Object')

var35 = Function('var35', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var396 = Function('var396', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var340 = Function('var340', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var395 = Function('var395', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var335 = Function('var335', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var372 = Function('var372', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var364 = Function('var364', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var318 = Function('var318', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var308 = Function('var308', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var369 = Function('var369', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var377 = Function('var377', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var307 = Function('var307', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var302 = Function('var302', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var365 = Function('var365', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var323 = Function('var323', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var35(x)), var31(x)))),
	ForAll([x], Not(Or(var155(x), Not(var184(x))))),
	ForAll([x], Not(Or(var341(x), Not(var53(x))))),
	ForAll([x], Not(Or(var6(x), var299(x)))),
	ForAll([x], Not(Or(var164(x), Not(var192(x))))),
	ForAll([x], Not(Or(Not(var169(x)), var42(x)))),
	ForAll([x], Not(Or(var157(x), Not(var108(x))))),
	ForAll([x], Not(Or(Not(var68(x)), var47(x)))),
	ForAll([x], Not(Or(Not(var51(x)), Not(var397(x))))),
	ForAll([x], Not(Or(Not(var244(x)), Not(var241(x))))),
	ForAll([x], Not(Or(var142(x), Not(var396(x))))),
	ForAll([x], Not(Or(var91(x), var40(x)))),
	ForAll([x], Not(Or(Not(var5(x)), Not(var20(x))))),
	ForAll([x], Not(Or(Not(var340(x)), var139(x)))),
	ForAll([x], Not(Or(var291(x), Not(var117(x))))),
	ForAll([x], Not(Or(Not(var93(x)), Not(var160(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var79(x1)), Not(var10(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var33(x1), var134(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var395(x1), Not(var161(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var335(x1), Not(var137(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var72(x1), var125(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var12(x1)), Not(var290(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var167(x1)), Not(var181(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var180(x1)), var168(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var55(x1)), var133(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var100(x1)), Not(var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Not(var345(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), Not(var28(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var222(x1)), Not(var103(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var293(x1), var281(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var21(x1)), Not(var135(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var81(x1), Not(var52(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var78(x1)), var110(x))))),
	ForAll([x], Not(Or(Not(var76(x)), var92(x), var90(x)))),
	ForAll([x], Not(Or(var38(x), Not(var56(x)), Not(var120(x))))),
	ForAll([x], Not(Or(var319(x), Not(var95(x)), var151(x)))),
	ForAll([x], Not(Or(Not(var300(x)), var46(x), var372(x)))),
	ForAll([x], Not(Or(var172(x), var248(x), var382(x)))),
	ForAll([x], Not(Or(Not(var179(x)), var251(x), Not(var311(x))))),
	ForAll([x], Not(Or(Not(var364(x)), var63(x), var75(x)))),
	ForAll([x], Not(Or(Not(var85(x)), Not(var153(x)), Not(var399(x))))),
	ForAll([x], Not(Or(var97(x), Not(var318(x)), var375(x)))),
	ForAll([x], Not(Or(var255(x), var69(x), Not(var343(x))))),
	ForAll([x], Not(Or(Not(var150(x)), Not(var158(x)), Not(var145(x))))),
	ForAll([x], Not(Or(var9(x), var177(x), Not(var338(x))))),
	ForAll([x], Not(Or(Not(var282(x)), Not(var171(x)), var124(x)))),
	ForAll([x], Not(Or(var163(x), Not(var7(x)), Not(var394(x))))),
	ForAll([x], Not(Or(Not(var331(x)), var272(x), var8(x)))),
	ForAll([x], Not(Or(Not(var3(x)), var57(x), var11(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var118(x1), Or(Not(var25(x)), Not(var127(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var36(x1)), Or(var370(x), var253(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var58(x1), var99(x1)), var210(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var352(x1), var73(x1)), Not(var326(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var67(x1), Or(Not(var149(x)), var227(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var45(x1), Not(var152(x1))), var176(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var18(x1)), Not(var126(x1))), var156(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var111(x1), Or(var94(x), var198(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var22(x1), Not(var60(x1))), var143(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var366(x1), Not(var277(x1))), var16(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var140(x1), Or(Not(var183(x)), Not(var325(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var284(x1), Or(var304(x), var74(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var292(x1), Or(Not(var223(x)), Not(var129(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var114(x1), Or(Not(var44(x)), var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var112(x1), var144(x1)), var26(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var196(x1), Or(Not(var84(x)), var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var1(x1)), var101(x1)), Not(var109(x)))))),
	ForAll([x], Not(Or(var173(x), var54(x), var104(x), Not(var238(x))))),
	ForAll([x], Not(Or(var342(x), var64(x), Not(var128(x)), var228(x)))),
	ForAll([x], Not(Or(var224(x), Not(var24(x)), var65(x), Not(var59(x))))),
	ForAll([x], Not(Or(Not(var355(x)), Not(var257(x)), var130(x), var19(x)))),
	ForAll([x], Not(Or(Not(var141(x)), Not(var295(x)), var136(x), var87(x)))),
	ForAll([x], Not(Or(Not(var146(x)), var374(x), var213(x), Not(var32(x))))),
	ForAll([x], Not(Or(Not(var246(x)), var193(x), var170(x), Not(var199(x))))),
	ForAll([x], Not(Or(Not(var363(x)), var88(x), var50(x), var201(x)))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var43(x)), Not(var154(x)), var368(x)))),
	ForAll([x], Not(Or(Not(var308(x)), Not(var49(x)), var361(x), var131(x)))),
	ForAll([x], Not(Or(Not(var98(x)), Not(var132(x)), Not(var71(x)), Not(var122(x))))),
	ForAll([x], Not(Or(var256(x), var15(x), var83(x), Not(var369(x))))),
	ForAll([x], Not(Or(var267(x), Not(var377(x)), Not(var174(x)), var207(x)))),
	ForAll([x], Not(Or(var185(x), Not(var27(x)), Not(var165(x)), Not(var216(x))))),
	ForAll([x], Not(Or(Not(var119(x)), var231(x), Not(var148(x)), Not(var80(x))))),
	ForAll([x], Not(Or(var113(x), var77(x), var225(x), var86(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var307(x1), var381(x1)), Or(var106(x), var286(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var82(x1)), Not(var357(x1)), Not(var29(x1))), var37(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var287(x1), Or(var138(x), var360(x), var302(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var62(x1), var321(x1), var105(x1)), var203(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var166(x1), var240(x1), var365(x1)), Not(var297(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var400(x1)), Not(var23(x1))), Or(var147(x), var115(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var187(x1)), Or(Not(var13(x)), Not(var314(x)), var41(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var285(x1)), Not(var221(x1))), Or(Not(var388(x)), var188(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var275(x1), Not(var262(x1))), Or(var358(x), Not(var116(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var89(x1)), var327(x1)), Or(var301(x), var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var175(x1)), var48(x1), Not(var189(x1))), Not(var347(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var30(x1)), Not(var212(x1)), Not(var159(x1))), var182(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), Or(var123(x), var178(x), var288(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var4(x1)), Not(var298(x1)), var339(x1)), var61(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var162(x1)), Not(var121(x1))), Or(Not(var344(x)), Not(var209(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var204(x1)), Or(var259(x), var202(x), Not(var323(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var320(x1)), Or(Not(var328(x)), Not(var329(x)), Not(var107(x))))))),
	ForAll([x], Not(Or(Not(var102(x)), var359(x), Not(var252(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
