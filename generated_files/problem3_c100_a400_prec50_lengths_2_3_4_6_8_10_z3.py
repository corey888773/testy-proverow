from z3 import *

Object = DeclareSort('Object')

var306 = Function('var306', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var362 = Function('var362', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var356 = Function('var356', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var369 = Function('var369', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var309 = Function('var309', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var392 = Function('var392', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var376 = Function('var376', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var269 = Function('var269', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var365 = Function('var365', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var351 = Function('var351', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var296 = Function('var296', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var348 = Function('var348', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var379 = Function('var379', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var371 = Function('var371', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var373 = Function('var373', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var306(x), Not(var33(x))))),
	ForAll([x], Not(Or(var16(x), var274(x)))),
	ForAll([x], Not(Or(var74(x), var17(x)))),
	ForAll([x], Not(Or(var70(x), Not(var370(x))))),
	ForAll([x], Not(Or(Not(var320(x)), var85(x)))),
	ForAll([x], Not(Or(var40(x), var132(x)))),
	ForAll([x], Not(Or(Not(var248(x)), Not(var25(x))))),
	ForAll([x], Not(Or(Not(var101(x)), Not(var357(x))))),
	ForAll([x], Not(Or(var62(x), var207(x)))),
	ForAll([x], Not(Or(Not(var65(x)), Not(var262(x))))),
	ForAll([x], Not(Or(Not(var50(x)), var226(x)))),
	ForAll([x], Not(Or(Not(var96(x)), Not(var359(x))))),
	ForAll([x], Not(Or(Not(var287(x)), Not(var71(x))))),
	ForAll([x], Not(Or(Not(var115(x)), var82(x)))),
	ForAll([x], Not(Or(var144(x), Not(var59(x))))),
	ForAll([x], Not(Or(var48(x), Not(var64(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var164(x1), Not(var272(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var347(x1), Not(var27(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var173(x1), Not(var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var152(x1)), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var203(x1), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var133(x1)), Not(var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var154(x1)), var131(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var104(x1), Not(var245(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), var236(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var141(x1)), Not(var214(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var54(x1)), Not(var178(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Not(var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var103(x1)), Not(var305(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var196(x1), var91(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), var26(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var107(x1)), Not(var69(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var360(x1)), var21(x))))),
	ForAll([x], Not(Or(Not(var128(x)), var114(x), var87(x)))),
	ForAll([x], Not(Or(Not(var161(x)), var125(x), Not(var165(x))))),
	ForAll([x], Not(Or(Not(var182(x)), var29(x), Not(var258(x))))),
	ForAll([x], Not(Or(var143(x), Not(var201(x)), var38(x)))),
	ForAll([x], Not(Or(Not(var221(x)), var282(x), Not(var32(x))))),
	ForAll([x], Not(Or(Not(var220(x)), Not(var147(x)), Not(var148(x))))),
	ForAll([x], Not(Or(Not(var75(x)), Not(var127(x)), var22(x)))),
	ForAll([x], Not(Or(var119(x), var241(x), Not(var95(x))))),
	ForAll([x], Not(Or(Not(var126(x)), Not(var10(x)), Not(var151(x))))),
	ForAll([x], Not(Or(Not(var23(x)), Not(var108(x)), var362(x)))),
	ForAll([x], Not(Or(var39(x), var229(x), var117(x)))),
	ForAll([x], Not(Or(Not(var227(x)), Not(var67(x)), var6(x)))),
	ForAll([x], Not(Or(var37(x), Not(var116(x)), Not(var169(x))))),
	ForAll([x], Not(Or(var129(x), var293(x), Not(var53(x))))),
	ForAll([x], Not(Or(Not(var34(x)), var113(x), Not(var294(x))))),
	ForAll([x], Not(Or(Not(var180(x)), var98(x), var118(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var329(x1)), Not(var123(x1))), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var338(x1)), var42(x1)), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var217(x1)), var73(x1)), Not(var80(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var170(x1)), var92(x1)), var160(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var46(x1)), Not(var84(x1))), var35(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var52(x1)), Or(Not(var137(x)), var356(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var197(x1)), Or(var124(x), Not(var111(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var246(x1)), var41(x1)), var146(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var304(x1)), Not(var51(x1))), Not(var102(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var150(x1), var18(x1)), var5(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var369(x1)), var138(x1)), var234(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var270(x1)), Or(var136(x), Not(var88(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var72(x1), var135(x1)), Not(var309(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var200(x1)), Not(var45(x1))), var322(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var76(x1)), Or(Not(var63(x)), Not(var19(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var168(x1)), Or(Not(var183(x)), var261(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var120(x1), Or(Not(var343(x)), Not(var264(x))))))),
	ForAll([x], Not(Or(Not(var310(x)), var157(x), var172(x), var142(x)))),
	ForAll([x], Not(Or(Not(var266(x)), Not(var330(x)), Not(var166(x)), Not(var89(x))))),
	ForAll([x], Not(Or(Not(var171(x)), var8(x), var289(x), Not(var273(x))))),
	ForAll([x], Not(Or(Not(var212(x)), Not(var175(x)), Not(var225(x)), var20(x)))),
	ForAll([x], Not(Or(Not(var83(x)), var185(x), var392(x), Not(var174(x))))),
	ForAll([x], Not(Or(Not(var109(x)), Not(var121(x)), var122(x), Not(var167(x))))),
	ForAll([x], Not(Or(var163(x), Not(var15(x)), Not(var99(x)), var90(x)))),
	ForAll([x], Not(Or(Not(var331(x)), Not(var247(x)), Not(var235(x)), var105(x)))),
	ForAll([x], Not(Or(Not(var134(x)), var363(x), var253(x), var376(x)))),
	ForAll([x], Not(Or(Not(var78(x)), var288(x), var162(x), Not(var312(x))))),
	ForAll([x], Not(Or(var68(x), var327(x), var337(x), var13(x)))),
	ForAll([x], Not(Or(var269(x), var176(x), var106(x), Not(var81(x))))),
	ForAll([x], Not(Or(var344(x), var206(x), var159(x), var222(x)))),
	ForAll([x], Not(Or(var208(x), Not(var321(x)), Not(var393(x)), Not(var366(x))))),
	ForAll([x], Not(Or(var368(x), var355(x), Not(var388(x)), var139(x)))),
	ForAll([x], Not(Or(var100(x), Not(var145(x)), var202(x), Not(var77(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var314(x1), var365(x1), var193(x1)), var94(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var291(x1)), Not(var358(x1))), Or(Not(var140(x)), var49(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var213(x1)), Or(var44(x), var374(x), var179(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var177(x1), Or(var297(x), var28(x), var228(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var110(x1), var181(x1), Not(var56(x1))), Not(var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var36(x1)), Not(var351(x1))), Or(var97(x), var397(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var295(x1), Not(var3(x1))), Or(Not(var155(x)), var280(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var375(x1)), var232(x1)), Or(var209(x), var198(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var231(x1), Not(var153(x1)), Not(var319(x1))), Not(var237(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var210(x1), Or(Not(var184(x)), Not(var382(x)), Not(var296(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var86(x1), Not(var112(x1))), Or(var342(x), Not(var353(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var255(x1), Not(var348(x1)), Not(var219(x1))), Not(var57(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var55(x1)), Or(Not(var303(x)), var379(x), var211(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var130(x1), var58(x1), Not(var7(x1))), var286(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var79(x1)), Or(Not(var192(x)), var149(x), var371(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var43(x1), Not(var61(x1))), Or(Not(var156(x)), var47(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var373(x1)), var93(x1)), Or(var278(x), var9(x)))))),
	ForAll([x], Not(Or(Not(var345(x)), var12(x))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
