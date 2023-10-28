from z3 import *

Object = DeclareSort('Object')

var216 = Function('var216', Object, BoolSort())
var485 = Function('var485', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var498 = Function('var498', Object, BoolSort())
var469 = Function('var469', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var479 = Function('var479', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var497 = Function('var497', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var447 = Function('var447', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var460 = Function('var460', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var427 = Function('var427', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var412 = Function('var412', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var378 = Function('var378', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var493 = Function('var493', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var324 = Function('var324', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var465 = Function('var465', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var494 = Function('var494', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var496 = Function('var496', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var463 = Function('var463', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var418 = Function('var418', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var462 = Function('var462', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var455 = Function('var455', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var440 = Function('var440', Object, BoolSort())
var404 = Function('var404', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var468 = Function('var468', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var377 = Function('var377', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var487 = Function('var487', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var459 = Function('var459', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var492 = Function('var492', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var390 = Function('var390', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var449 = Function('var449', Object, BoolSort())
var486 = Function('var486', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var444 = Function('var444', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var371 = Function('var371', Object, BoolSort())
var432 = Function('var432', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var467 = Function('var467', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var409 = Function('var409', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var495 = Function('var495', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var478 = Function('var478', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var475 = Function('var475', Object, BoolSort())
var454 = Function('var454', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var436 = Function('var436', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var406 = Function('var406', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var474 = Function('var474', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var448 = Function('var448', Object, BoolSort())
var476 = Function('var476', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var424 = Function('var424', Object, BoolSort())
var395 = Function('var395', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var306 = Function('var306', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var488 = Function('var488', Object, BoolSort())
var477 = Function('var477', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var349 = Function('var349', Object, BoolSort())
var410 = Function('var410', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var216(x), var485(x)))),
	ForAll([x], Not(Or(var85(x), var126(x)))),
	ForAll([x], Not(Or(Not(var353(x)), Not(var304(x))))),
	ForAll([x], Not(Or(var337(x), Not(var61(x))))),
	ForAll([x], Not(Or(var387(x), var28(x)))),
	ForAll([x], Not(Or(Not(var56(x)), Not(var12(x))))),
	ForAll([x], Not(Or(Not(var498(x)), var469(x)))),
	ForAll([x], Not(Or(var35(x), var479(x)))),
	ForAll([x], Not(Or(Not(var113(x)), var346(x)))),
	ForAll([x], Not(Or(var298(x), var9(x)))),
	ForAll([x], Not(Or(var38(x), Not(var15(x))))),
	ForAll([x], Not(Or(var400(x), Not(var27(x))))),
	ForAll([x], Not(Or(var284(x), var332(x)))),
	ForAll([x], Not(Or(Not(var106(x)), var4(x)))),
	ForAll([x], Not(Or(Not(var36(x)), Not(var94(x))))),
	ForAll([x], Not(Or(Not(var393(x)), Not(var90(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), Not(var43(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var294(x1), var110(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var104(x1), var65(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var98(x1)), Not(var278(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var102(x1), var363(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var131(x1), var119(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var114(x1)), Not(var70(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var83(x1), Not(var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var497(x1)), var123(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var253(x1), Not(var380(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var289(x1)), Not(var327(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var447(x1)), var236(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var20(x1)), Not(var460(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var82(x1), var60(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var45(x1), Not(var293(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var133(x1)), Not(var57(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var49(x1)), Not(var24(x)))))),
	ForAll([x], Not(Or(var107(x), var187(x), Not(var84(x))))),
	ForAll([x], Not(Or(var295(x), var5(x), Not(var179(x))))),
	ForAll([x], Not(Or(var32(x), Not(var129(x)), Not(var192(x))))),
	ForAll([x], Not(Or(var25(x), Not(var154(x)), Not(var67(x))))),
	ForAll([x], Not(Or(var2(x), Not(var268(x)), var21(x)))),
	ForAll([x], Not(Or(Not(var55(x)), Not(var263(x)), Not(var220(x))))),
	ForAll([x], Not(Or(Not(var427(x)), var14(x), var412(x)))),
	ForAll([x], Not(Or(Not(var93(x)), Not(var120(x)), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var200(x)), var78(x), Not(var13(x))))),
	ForAll([x], Not(Or(var161(x), var378(x), Not(var191(x))))),
	ForAll([x], Not(Or(Not(var63(x)), var384(x), var125(x)))),
	ForAll([x], Not(Or(Not(var493(x)), var64(x), var163(x)))),
	ForAll([x], Not(Or(Not(var324(x)), Not(var184(x)), var465(x)))),
	ForAll([x], Not(Or(var30(x), var494(x), Not(var128(x))))),
	ForAll([x], Not(Or(Not(var496(x)), var31(x), var23(x)))),
	ForAll([x], Not(Or(Not(var6(x)), Not(var58(x)), var244(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var11(x1)), Or(var96(x), var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var359(x1)), var210(x1)), Not(var325(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var46(x1), Or(var370(x), var176(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var251(x1), Or(var247(x), var219(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var240(x1)), Not(var59(x1))), Not(var89(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var73(x1), Not(var193(x1))), var310(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var463(x1), var399(x1)), var285(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var7(x1)), Or(Not(var122(x)), var51(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var188(x1), Not(var283(x1))), Not(var52(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var87(x1)), var196(x1)), Not(var48(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var418(x1), Or(Not(var144(x)), Not(var462(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var223(x1), Not(var100(x1))), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var314(x1), Not(var103(x1))), Not(var75(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var464(x1), Or(Not(var17(x)), Not(var136(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var99(x1), Or(Not(var34(x)), Not(var382(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var92(x1), Or(var209(x), var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var190(x1), Not(var39(x1))), Not(var142(x)))))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var455(x)), Not(var132(x)), Not(var338(x))))),
	ForAll([x], Not(Or(Not(var205(x)), var141(x), Not(var69(x)), var41(x)))),
	ForAll([x], Not(Or(var18(x), Not(var440(x)), Not(var404(x)), Not(var168(x))))),
	ForAll([x], Not(Or(var261(x), var468(x), Not(var66(x)), var91(x)))),
	ForAll([x], Not(Or(var112(x), Not(var130(x)), Not(var134(x)), var117(x)))),
	ForAll([x], Not(Or(Not(var80(x)), Not(var260(x)), Not(var377(x)), Not(var388(x))))),
	ForAll([x], Not(Or(var487(x), Not(var159(x)), var19(x), var33(x)))),
	ForAll([x], Not(Or(Not(var1(x)), var71(x), var72(x), Not(var459(x))))),
	ForAll([x], Not(Or(var111(x), var53(x), Not(var492(x)), var315(x)))),
	ForAll([x], Not(Or(var42(x), var76(x), var109(x), Not(var300(x))))),
	ForAll([x], Not(Or(Not(var101(x)), var108(x), Not(var86(x)), Not(var390(x))))),
	ForAll([x], Not(Or(Not(var312(x)), Not(var140(x)), var173(x), var449(x)))),
	ForAll([x], Not(Or(Not(var486(x)), Not(var231(x)), var415(x), Not(var444(x))))),
	ForAll([x], Not(Or(var211(x), var371(x), var432(x), var197(x)))),
	ForAll([x], Not(Or(var150(x), Not(var10(x)), var297(x), var105(x)))),
	ForAll([x], Not(Or(Not(var137(x)), Not(var467(x)), var171(x), Not(var77(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var164(x1)), Or(var121(x), var409(x), var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var79(x1), Or(Not(var185(x)), Not(var26(x)), Not(var116(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var189(x1)), Not(var198(x1)), var322(x1)), var495(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var115(x1)), Or(var343(x), var227(x), Not(var480(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var478(x1), var74(x1)), Or(var199(x), var169(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var320(x1), Or(var81(x), var271(x), Not(var475(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var454(x1)), Or(var237(x), Not(var381(x)), var436(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var143(x1), var239(x1), Not(var258(x1))), Not(var273(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var280(x1), Or(Not(var328(x)), var62(x), Not(var172(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var406(x1)), Or(Not(var8(x)), Not(var3(x)), var474(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var357(x1), var448(x1)), Or(Not(var476(x)), Not(var124(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var394(x1)), Or(Not(var361(x)), Not(var29(x)), Not(var54(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var326(x1), Not(var342(x1))), Or(Not(var151(x)), Not(var375(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var424(x1), Not(var395(x1)), Not(var181(x1))), Not(var334(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var306(x1)), var165(x1), var44(x1)), Not(var97(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var127(x1), Not(var488(x1)), var477(x1)), var152(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var139(x1), var249(x1), var50(x1)), var118(x))))),
	ForAll([x], Not(Or(Not(var349(x)), Not(var410(x)), var95(x))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
