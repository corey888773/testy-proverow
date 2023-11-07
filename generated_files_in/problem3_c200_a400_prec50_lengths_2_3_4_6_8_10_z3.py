from z3 import *

Object = DeclareSort('Object')

var322 = Function('var322', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var356 = Function('var356', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var302 = Function('var302', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var317 = Function('var317', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var377 = Function('var377', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var369 = Function('var369', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var376 = Function('var376', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var269 = Function('var269', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var373 = Function('var373', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var350 = Function('var350', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var349 = Function('var349', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var386 = Function('var386', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var306 = Function('var306', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var378 = Function('var378', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var309 = Function('var309', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var367 = Function('var367', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var276 = Function('var276', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var296 = Function('var296', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var316 = Function('var316', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var354 = Function('var354', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var379 = Function('var379', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var372 = Function('var372', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var395 = Function('var395', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var313 = Function('var313', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var318 = Function('var318', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var398 = Function('var398', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var307 = Function('var307', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var335 = Function('var335', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var391 = Function('var391', Object, BoolSort())
var362 = Function('var362', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var333 = Function('var333', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var371 = Function('var371', Object, BoolSort())
var336 = Function('var336', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var365 = Function('var365', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var348 = Function('var348', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var323 = Function('var323', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var392 = Function('var392', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var389 = Function('var389', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var396 = Function('var396', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var308 = Function('var308', Object, BoolSort())
var340 = Function('var340', Object, BoolSort())
var351 = Function('var351', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var364 = Function('var364', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var385 = Function('var385', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var390 = Function('var390', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var324 = Function('var324', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var322(x), Not(var200(x))))),
	ForAll([x], Not(Or(Not(var374(x)), Not(var109(x))))),
	ForAll([x], Not(Or(Not(var319(x)), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var169(x)), Not(var91(x))))),
	ForAll([x], Not(Or(Not(var39(x)), var42(x)))),
	ForAll([x], Not(Or(Not(var89(x)), var64(x)))),
	ForAll([x], Not(Or(var291(x), var127(x)))),
	ForAll([x], Not(Or(var328(x), Not(var220(x))))),
	ForAll([x], Not(Or(var394(x), Not(var28(x))))),
	ForAll([x], Not(Or(var356(x), Not(var100(x))))),
	ForAll([x], Not(Or(Not(var102(x)), var18(x)))),
	ForAll([x], Not(Or(Not(var302(x)), Not(var70(x))))),
	ForAll([x], Not(Or(Not(var165(x)), var48(x)))),
	ForAll([x], Not(Or(var246(x), var65(x)))),
	ForAll([x], Not(Or(Not(var43(x)), Not(var255(x))))),
	ForAll([x], Not(Or(var112(x), var21(x)))),
	ForAll([x], Not(Or(Not(var387(x)), var66(x)))),
	ForAll([x], Not(Or(var297(x), var317(x)))),
	ForAll([x], Not(Or(var9(x), Not(var208(x))))),
	ForAll([x], Not(Or(var149(x), Not(var60(x))))),
	ForAll([x], Not(Or(Not(var156(x)), Not(var377(x))))),
	ForAll([x], Not(Or(var128(x), Not(var20(x))))),
	ForAll([x], Not(Or(Not(var90(x)), var214(x)))),
	ForAll([x], Not(Or(var17(x), var369(x)))),
	ForAll([x], Not(Or(var63(x), Not(var273(x))))),
	ForAll([x], Not(Or(Not(var376(x)), var49(x)))),
	ForAll([x], Not(Or(var178(x), Not(var269(x))))),
	ForAll([x], Not(Or(var321(x), Not(var164(x))))),
	ForAll([x], Not(Or(var373(x), Not(var157(x))))),
	ForAll([x], Not(Or(var218(x), Not(var34(x))))),
	ForAll([x], Not(Or(var350(x), var272(x)))),
	ForAll([x], Not(Or(var120(x), var230(x)))),
	ForAll([x], Not(Or(var236(x), var55(x)))),
	ForAll([x], Not(Or(Not(var380(x)), Not(var188(x))))),
	ForAll([x], Not(Or(Not(var225(x)), var349(x)))),
	ForAll([x], Not(Or(Not(var281(x)), Not(var168(x))))),
	ForAll([x], Not(Or(Not(var352(x)), Not(var368(x))))),
	ForAll([x], Not(Or(var116(x), var182(x)))),
	ForAll([x], Not(Or(Not(var223(x)), var250(x)))),
	ForAll([x], Not(Or(Not(var138(x)), var267(x)))),
	ForAll([x], Not(Or(Not(var201(x)), var211(x)))),
	ForAll([x], Not(Or(Not(var92(x)), var177(x)))),
	ForAll([x], Not(Or(Not(var199(x)), var337(x)))),
	ForAll([x], Not(Or(var386(x), var77(x)))),
	ForAll([x], Not(Or(Not(var33(x)), var245(x)))),
	ForAll([x], Not(Or(var132(x), var342(x)))),
	ForAll([x], Not(Or(var361(x), var115(x)))),
	ForAll([x], Not(Or(Not(var332(x)), Not(var306(x))))),
	ForAll([x], Not(Or(Not(var113(x)), var125(x)))),
	ForAll([x], Not(Or(var186(x), Not(var378(x))))),
	ForAll([x], Not(Or(var86(x), Not(var95(x))))),
	ForAll([x], Not(Or(Not(var110(x)), Not(var263(x))))),
	ForAll([x], Not(Or(var23(x), Not(var79(x))))),
	ForAll([x], Not(Or(Not(var161(x)), Not(var256(x))))),
	ForAll([x], Not(Or(var111(x), Not(var69(x))))),
	ForAll([x], Not(Or(Not(var181(x)), Not(var53(x))))),
	ForAll([x], Not(Or(var24(x), var108(x)))),
	ForAll([x], Not(Or(var249(x), var232(x)))),
	ForAll([x], Not(Or(Not(var309(x)), var139(x)))),
	ForAll([x], Not(Or(var84(x), Not(var367(x))))),
	ForAll([x], Not(Or(Not(var195(x)), var56(x)))),
	ForAll([x], Not(Or(var276(x), Not(var270(x))))),
	ForAll([x], Not(Or(Not(var104(x)), Not(var248(x))))),
	ForAll([x], Not(Or(Not(var197(x)), Not(var206(x))))),
	ForAll([x], Not(Or(var82(x), var107(x)))),
	ForAll([x], Not(Or(Not(var397(x)), var298(x)))),
	ForAll([x], Not(Or(Not(var152(x)), var217(x)))),
	ForAll([x], Not(Or(Not(var10(x)), var271(x)))),
	ForAll([x], Not(Or(var296(x), Not(var325(x))))),
	ForAll([x], Not(Or(var283(x), Not(var131(x))))),
	ForAll([x], Not(Or(var222(x), Not(var78(x))))),
	ForAll([x], Not(Or(Not(var286(x)), var316(x)))),
	ForAll([x], Not(Or(Not(var334(x)), Not(var221(x))))),
	ForAll([x], Not(Or(var163(x), Not(var173(x))))),
	ForAll([x], Not(Or(var354(x), var264(x)))),
	ForAll([x], Not(Or(Not(var15(x)), Not(var251(x))))),
	ForAll([x], Not(Or(Not(var19(x)), var299(x)))),
	ForAll([x], Not(Or(var240(x), var329(x)))),
	ForAll([x], Not(Or(Not(var189(x)), Not(var282(x))))),
	ForAll([x], Not(Or(Not(var375(x)), Not(var80(x))))),
	ForAll([x], Not(Or(Not(var134(x)), var159(x)))),
	ForAll([x], Not(Or(Not(var150(x)), Not(var160(x))))),
	ForAll([x], Not(Or(var260(x), var52(x)))),
	ForAll([x], Not(Or(Not(var93(x)), var301(x)))),
	ForAll([x], Not(Or(var36(x), var205(x)))),
	ForAll([x], Not(Or(var379(x), var330(x)))),
	ForAll([x], Not(Or(var278(x), var372(x)))),
	ForAll([x], Not(Or(var265(x), Not(var174(x))))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var58(x))))),
	ForAll([x], Not(Or(var148(x), var144(x)))),
	ForAll([x], Not(Or(Not(var94(x)), Not(var209(x))))),
	ForAll([x], Not(Or(Not(var14(x)), Not(var11(x))))),
	ForAll([x], Not(Or(var26(x), Not(var254(x))))),
	ForAll([x], Not(Or(Not(var280(x)), Not(var381(x))))),
	ForAll([x], Not(Or(var180(x), var194(x)))),
	ForAll([x], Not(Or(var192(x), var311(x)))),
	ForAll([x], Not(Or(var341(x), var136(x)))),
	ForAll([x], Not(Or(var46(x), Not(var395(x))))),
	ForAll([x], Not(Or(var105(x), var6(x)))),
	ForAll([x], Not(Or(Not(var103(x)), Not(var83(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var253(x1), var370(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var117(x1), Not(var300(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var122(x1)), var5(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var171(x1)), var313(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var358(x1), Not(var239(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var88(x1)), var114(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var261(x1)), var124(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var50(x1)), var304(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var72(x1)), var187(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var12(x1), Not(var44(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var268(x1)), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var184(x1)), Not(var142(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var85(x1)), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var226(x1), Not(var318(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var288(x1), Not(var315(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var310(x1), var400(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var398(x1)), Not(var87(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var345(x1)), var275(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var237(x1), var98(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var284(x1)), Not(var129(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var224(x1), Not(var204(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var277(x1)), var290(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var235(x1), Not(var353(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var179(x1)), var393(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var307(x1), Not(var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var76(x1)), Not(var143(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var193(x1), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var146(x1)), Not(var258(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var7(x1), Not(var198(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var339(x1), var335(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var293(x1)), Not(var135(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var155(x1), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var25(x1)), var391(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var362(x1), Not(var347(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var59(x1), var247(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var162(x1)), var303(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var216(x1), var71(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var233(x1), var137(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var252(x1)), var145(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var383(x1)), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var121(x1)), var314(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var62(x1), Not(var333(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var96(x1), Not(var238(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var8(x1), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var266(x1)), Not(var234(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), var176(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var371(x1)), var336(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), var203(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var365(x1)), Not(var170(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var166(x1), var241(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var279(x1)), Not(var262(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var305(x1)), Not(var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var172(x1), Not(var348(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var123(x1), Not(var190(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var382(x1)), Not(var40(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var323(x1)), Not(var196(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var207(x1)), Not(var147(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var326(x1)), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var360(x1), var126(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var384(x1), Not(var259(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var101(x1)), var215(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var61(x1), var320(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var338(x1), Not(var229(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var185(x1), Not(var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var57(x1), Not(var231(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var392(x1)), var99(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var389(x1)), Not(var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var344(x1)), Not(var359(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var287(x1), var396(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var141(x1)), var285(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var191(x1), var167(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var74(x1), var388(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var154(x1), Not(var35(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var54(x1)), Not(var331(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var274(x1)), var210(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var343(x1)), Not(var81(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var242(x1)), Not(var308(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var340(x1), Not(var351(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var257(x1), var13(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var75(x1)), Not(var355(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var366(x1), Not(var32(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var228(x1), Not(var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var289(x1)), Not(var294(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var140(x1)), var295(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var364(x1)), var119(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var73(x1)), var51(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var151(x1), var213(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var202(x1)), Not(var97(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var399(x1), var219(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var244(x1)), Not(var346(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var4(x1), Not(var385(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var153(x1), Not(var357(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var212(x1), var390(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var41(x1)), Not(var38(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var130(x1)), var106(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var324(x1)), Not(var183(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var227(x1)), Not(var118(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var327(x1), Not(var133(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var363(x1), Not(var312(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var292(x1)), var175(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
