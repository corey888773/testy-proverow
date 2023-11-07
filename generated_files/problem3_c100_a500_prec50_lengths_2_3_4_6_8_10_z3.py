from z3 import *

Object = DeclareSort('Object')

var12 = Function('var12', Object, BoolSort())
var493 = Function('var493', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var309 = Function('var309', Object, BoolSort())
var414 = Function('var414', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var425 = Function('var425', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var402 = Function('var402', Object, BoolSort())
var445 = Function('var445', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var465 = Function('var465', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var458 = Function('var458', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var439 = Function('var439', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var469 = Function('var469', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var307 = Function('var307', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var385 = Function('var385', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var354 = Function('var354', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var435 = Function('var435', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var429 = Function('var429', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var491 = Function('var491', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var472 = Function('var472', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var420 = Function('var420', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var392 = Function('var392', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var356 = Function('var356', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var444 = Function('var444', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var483 = Function('var483', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var419 = Function('var419', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var386 = Function('var386', Object, BoolSort())
var424 = Function('var424', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var448 = Function('var448', Object, BoolSort())
var411 = Function('var411', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var308 = Function('var308', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var492 = Function('var492', Object, BoolSort())
var473 = Function('var473', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var324 = Function('var324', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var276 = Function('var276', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var389 = Function('var389', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var349 = Function('var349', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var269 = Function('var269', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var431 = Function('var431', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var416 = Function('var416', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var441 = Function('var441', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var484 = Function('var484', Object, BoolSort())
var409 = Function('var409', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var468 = Function('var468', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var395 = Function('var395', Object, BoolSort())
var466 = Function('var466', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var432 = Function('var432', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var437 = Function('var437', Object, BoolSort())
var440 = Function('var440', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var449 = Function('var449', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var350 = Function('var350', Object, BoolSort())
var487 = Function('var487', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var442 = Function('var442', Object, BoolSort())
var433 = Function('var433', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var457 = Function('var457', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var443 = Function('var443', Object, BoolSort())
var403 = Function('var403', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var410 = Function('var410', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var378 = Function('var378', Object, BoolSort())
var498 = Function('var498', Object, BoolSort())
var391 = Function('var391', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var12(x), var493(x)))),
	ForAll([x], Not(Or(var337(x), Not(var338(x))))),
	ForAll([x], Not(Or(var84(x), var309(x)))),
	ForAll([x], Not(Or(Not(var414(x)), var147(x)))),
	ForAll([x], Not(Or(var71(x), var200(x)))),
	ForAll([x], Not(Or(Not(var300(x)), var211(x)))),
	ForAll([x], Not(Or(Not(var213(x)), Not(var54(x))))),
	ForAll([x], Not(Or(Not(var3(x)), Not(var253(x))))),
	ForAll([x], Not(Or(Not(var384(x)), Not(var158(x))))),
	ForAll([x], Not(Or(var105(x), Not(var339(x))))),
	ForAll([x], Not(Or(var188(x), Not(var86(x))))),
	ForAll([x], Not(Or(Not(var425(x)), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var343(x)), var222(x)))),
	ForAll([x], Not(Or(Not(var122(x)), var156(x)))),
	ForAll([x], Not(Or(var402(x), var445(x)))),
	ForAll([x], Not(Or(var52(x), Not(var26(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), Not(var81(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var241(x1), Not(var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var216(x1)), Not(var465(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var2(x1)), var458(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var228(x1)), Not(var439(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var108(x1), Not(var321(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var17(x1)), Not(var23(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var47(x1), Not(var469(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var180(x1), Not(var322(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var62(x1)), var69(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var307(x1), Not(var231(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var18(x1)), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var320(x1), Not(var268(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var100(x1)), Not(var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var326(x1)), var385(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var65(x1), var354(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var43(x1)), var294(x))))),
	ForAll([x], Not(Or(var1(x), Not(var283(x)), Not(var7(x))))),
	ForAll([x], Not(Or(Not(var8(x)), var166(x), var175(x)))),
	ForAll([x], Not(Or(Not(var15(x)), Not(var256(x)), var435(x)))),
	ForAll([x], Not(Or(Not(var168(x)), var24(x), var92(x)))),
	ForAll([x], Not(Or(Not(var49(x)), var202(x), var243(x)))),
	ForAll([x], Not(Or(var464(x), var109(x), var429(x)))),
	ForAll([x], Not(Or(var38(x), Not(var282(x)), Not(var16(x))))),
	ForAll([x], Not(Or(Not(var39(x)), var45(x), Not(var14(x))))),
	ForAll([x], Not(Or(var61(x), var198(x), var103(x)))),
	ForAll([x], Not(Or(var491(x), var4(x), var118(x)))),
	ForAll([x], Not(Or(var51(x), Not(var189(x)), var42(x)))),
	ForAll([x], Not(Or(Not(var472(x)), var157(x), var60(x)))),
	ForAll([x], Not(Or(var13(x), Not(var66(x)), var264(x)))),
	ForAll([x], Not(Or(var57(x), Not(var280(x)), var328(x)))),
	ForAll([x], Not(Or(var97(x), Not(var46(x)), var82(x)))),
	ForAll([x], Not(Or(var346(x), Not(var6(x)), Not(var420(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var87(x1)), Not(var195(x1))), Not(var77(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var289(x1), var25(x1)), Not(var50(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var392(x1)), Not(var37(x1))), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var237(x1)), Or(var98(x), var247(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var64(x1), Or(Not(var298(x)), var299(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var41(x1), Or(Not(var197(x)), Not(var11(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var356(x1)), Or(Not(var63(x)), var444(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var262(x1)), Not(var89(x1))), var203(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var483(x1), Or(Not(var244(x)), Not(var36(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var419(x1)), Or(Not(var107(x)), var246(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var162(x1), Not(var374(x1))), Not(var329(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var386(x1), Or(Not(var424(x)), var277(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var58(x1)), Or(var273(x), var448(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var411(x1), var67(x1)), var56(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var292(x1), Not(var143(x1))), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var139(x1)), Or(Not(var93(x)), var227(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var242(x1), Not(var111(x1))), var72(x))))),
	ForAll([x], Not(Or(var5(x), Not(var34(x)), var74(x), Not(var308(x))))),
	ForAll([x], Not(Or(var20(x), Not(var492(x)), Not(var473(x)), Not(var263(x))))),
	ForAll([x], Not(Or(Not(var9(x)), var310(x), var40(x), Not(var236(x))))),
	ForAll([x], Not(Or(Not(var480(x)), var324(x), var10(x), var342(x)))),
	ForAll([x], Not(Or(var31(x), var73(x), Not(var68(x)), var55(x)))),
	ForAll([x], Not(Or(var305(x), Not(var276(x)), var21(x), var116(x)))),
	ForAll([x], Not(Or(Not(var389(x)), var96(x), var104(x), var53(x)))),
	ForAll([x], Not(Or(var314(x), var349(x), var274(x), Not(var91(x))))),
	ForAll([x], Not(Or(Not(var281(x)), var269(x), Not(var265(x)), Not(var431(x))))),
	ForAll([x], Not(Or(var330(x), var221(x), Not(var399(x)), Not(var101(x))))),
	ForAll([x], Not(Or(Not(var120(x)), Not(var301(x)), Not(var279(x)), Not(var266(x))))),
	ForAll([x], Not(Or(Not(var59(x)), var387(x), var35(x), Not(var416(x))))),
	ForAll([x], Not(Or(Not(var334(x)), Not(var78(x)), Not(var383(x)), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var28(x)), var441(x), var245(x), Not(var484(x))))),
	ForAll([x], Not(Or(var409(x), Not(var248(x)), Not(var150(x)), var415(x)))),
	ForAll([x], Not(Or(Not(var27(x)), Not(var79(x)), var177(x), Not(var70(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var179(x1)), Not(var366(x1)), Not(var332(x1))), var382(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var138(x1)), Not(var102(x1)), var468(x1)), Not(var217(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var193(x1), Not(var214(x1)), Not(var395(x1))), var466(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var255(x1), Or(Not(var99(x)), Not(var80(x)), var341(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var191(x1), var432(x1), var95(x1)), var186(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var152(x1), Not(var125(x1)), var380(x1)), Not(var75(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var393(x1)), var30(x1), var437(x1)), var440(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var400(x1)), var130(x1)), Or(var90(x), var173(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var361(x1)), var449(x1), Not(var83(x1))), var226(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var149(x1)), var94(x1), Not(var345(x1))), var350(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var487(x1)), Or(var344(x), var442(x), var433(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var184(x1), var331(x1), var209(x1)), var325(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var363(x1), Or(Not(var457(x)), Not(var181(x)), Not(var443(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var403(x1), Not(var151(x1)), Not(var85(x1))), Not(var136(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var234(x1), var32(x1)), Or(var368(x), Not(var210(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var397(x1), Not(var119(x1)), Not(var33(x1))), var410(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var148(x1)), Not(var370(x1)), var182(x1)), var106(x))))),
	ForAll([x], Not(Or(Not(var194(x)), Not(var378(x)), Not(var498(x)), var391(x))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
