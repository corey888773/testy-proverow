from z3 import *

Object = DeclareSort('Object')

var393 = Function('var393', Object, BoolSort())
var401 = Function('var401', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var435 = Function('var435', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var589 = Function('var589', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var367 = Function('var367', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var539 = Function('var539', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var511 = Function('var511', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var362 = Function('var362', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var500 = Function('var500', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var269 = Function('var269', Object, BoolSort())
var385 = Function('var385', Object, BoolSort())
var309 = Function('var309', Object, BoolSort())
var483 = Function('var483', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var546 = Function('var546', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var575 = Function('var575', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var470 = Function('var470', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var540 = Function('var540', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var545 = Function('var545', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var495 = Function('var495', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var576 = Function('var576', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var551 = Function('var551', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var438 = Function('var438', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var501 = Function('var501', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var333 = Function('var333', Object, BoolSort())
var499 = Function('var499', Object, BoolSort())
var348 = Function('var348', Object, BoolSort())
var578 = Function('var578', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var446 = Function('var446', Object, BoolSort())
var564 = Function('var564', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var536 = Function('var536', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var515 = Function('var515', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var553 = Function('var553', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var404 = Function('var404', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var296 = Function('var296', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var335 = Function('var335', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var462 = Function('var462', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var571 = Function('var571', Object, BoolSort())
var475 = Function('var475', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var493 = Function('var493', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var354 = Function('var354', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var425 = Function('var425', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var522 = Function('var522', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var481 = Function('var481', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var351 = Function('var351', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var595 = Function('var595', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var403 = Function('var403', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var577 = Function('var577', Object, BoolSort())
var486 = Function('var486', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var430 = Function('var430', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var426 = Function('var426', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var377 = Function('var377', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var569 = Function('var569', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var581 = Function('var581', Object, BoolSort())
var460 = Function('var460', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var543 = Function('var543', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var302 = Function('var302', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var570 = Function('var570', Object, BoolSort())
var519 = Function('var519', Object, BoolSort())
var336 = Function('var336', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var356 = Function('var356', Object, BoolSort())
var509 = Function('var509', Object, BoolSort())
var432 = Function('var432', Object, BoolSort())
var316 = Function('var316', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var550 = Function('var550', Object, BoolSort())
var529 = Function('var529', Object, BoolSort())
var586 = Function('var586', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var533 = Function('var533', Object, BoolSort())
var531 = Function('var531', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var448 = Function('var448', Object, BoolSort())
var440 = Function('var440', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var323 = Function('var323', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var457 = Function('var457', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var405 = Function('var405', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var431 = Function('var431', Object, BoolSort())
var454 = Function('var454', Object, BoolSort())
var588 = Function('var588', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var574 = Function('var574', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var555 = Function('var555', Object, BoolSort())
var422 = Function('var422', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var471 = Function('var471', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var453 = Function('var453', Object, BoolSort())
var490 = Function('var490', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var458 = Function('var458', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var372 = Function('var372', Object, BoolSort())
var308 = Function('var308', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var306 = Function('var306', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var467 = Function('var467', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var587 = Function('var587', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var566 = Function('var566', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var461 = Function('var461', Object, BoolSort())
var477 = Function('var477', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var449 = Function('var449', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var482 = Function('var482', Object, BoolSort())
var591 = Function('var591', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var582 = Function('var582', Object, BoolSort())
var439 = Function('var439', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var340 = Function('var340', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var516 = Function('var516', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var599 = Function('var599', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var465 = Function('var465', Object, BoolSort())
var530 = Function('var530', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var532 = Function('var532', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var313 = Function('var313', Object, BoolSort())
var407 = Function('var407', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var535 = Function('var535', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var485 = Function('var485', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var379 = Function('var379', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var416 = Function('var416', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var474 = Function('var474', Object, BoolSort())
var488 = Function('var488', Object, BoolSort())
var386 = Function('var386', Object, BoolSort())
var496 = Function('var496', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var517 = Function('var517', Object, BoolSort())
var565 = Function('var565', Object, BoolSort())
var411 = Function('var411', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var390 = Function('var390', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var406 = Function('var406', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var561 = Function('var561', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var324 = Function('var324', Object, BoolSort())
var429 = Function('var429', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var596 = Function('var596', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var307 = Function('var307', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var562 = Function('var562', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var452 = Function('var452', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var478 = Function('var478', Object, BoolSort())
var423 = Function('var423', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var276 = Function('var276', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var364 = Function('var364', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var318 = Function('var318', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var479 = Function('var479', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var556 = Function('var556', Object, BoolSort())
var518 = Function('var518', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var350 = Function('var350', Object, BoolSort())
var520 = Function('var520', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var443 = Function('var443', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var525 = Function('var525', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var491 = Function('var491', Object, BoolSort())
var584 = Function('var584', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var472 = Function('var472', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var421 = Function('var421', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var567 = Function('var567', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var413 = Function('var413', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var427 = Function('var427', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var317 = Function('var317', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var450 = Function('var450', Object, BoolSort())
var559 = Function('var559', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var492 = Function('var492', Object, BoolSort())
var560 = Function('var560', Object, BoolSort())
var408 = Function('var408', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var349 = Function('var349', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var393(x)), var401(x)))),
	ForAll([x], Not(Or(var200(x), Not(var208(x))))),
	ForAll([x], Not(Or(var211(x), var435(x)))),
	ForAll([x], Not(Or(var36(x), Not(var10(x))))),
	ForAll([x], Not(Or(Not(var168(x)), Not(var589(x))))),
	ForAll([x], Not(Or(Not(var125(x)), Not(var367(x))))),
	ForAll([x], Not(Or(var143(x), Not(var539(x))))),
	ForAll([x], Not(Or(var135(x), Not(var67(x))))),
	ForAll([x], Not(Or(var247(x), Not(var387(x))))),
	ForAll([x], Not(Or(var310(x), Not(var120(x))))),
	ForAll([x], Not(Or(var511(x), Not(var271(x))))),
	ForAll([x], Not(Or(var203(x), var362(x)))),
	ForAll([x], Not(Or(var217(x), var95(x)))),
	ForAll([x], Not(Or(var238(x), var500(x)))),
	ForAll([x], Not(Or(Not(var169(x)), var269(x)))),
	ForAll([x], Not(Or(var385(x), Not(var309(x))))),
	ForAll([x], Not(Or(var483(x), Not(var248(x))))),
	ForAll([x], Not(Or(var546(x), var345(x)))),
	ForAll([x], Not(Or(var575(x), Not(var130(x))))),
	ForAll([x], Not(Or(Not(var122(x)), Not(var105(x))))),
	ForAll([x], Not(Or(Not(var394(x)), Not(var353(x))))),
	ForAll([x], Not(Or(Not(var150(x)), var221(x)))),
	ForAll([x], Not(Or(Not(var282(x)), Not(var325(x))))),
	ForAll([x], Not(Or(var8(x), Not(var270(x))))),
	ForAll([x], Not(Or(Not(var28(x)), var40(x)))),
	ForAll([x], Not(Or(var151(x), var470(x)))),
	ForAll([x], Not(Or(Not(var123(x)), Not(var234(x))))),
	ForAll([x], Not(Or(var78(x), var76(x)))),
	ForAll([x], Not(Or(Not(var263(x)), var266(x)))),
	ForAll([x], Not(Or(var230(x), var540(x)))),
	ForAll([x], Not(Or(Not(var233(x)), Not(var192(x))))),
	ForAll([x], Not(Or(Not(var545(x)), var61(x)))),
	ForAll([x], Not(Or(Not(var7(x)), var415(x)))),
	ForAll([x], Not(Or(var89(x), Not(var495(x))))),
	ForAll([x], Not(Or(var58(x), var21(x)))),
	ForAll([x], Not(Or(var210(x), Not(var193(x))))),
	ForAll([x], Not(Or(var576(x), Not(var11(x))))),
	ForAll([x], Not(Or(Not(var332(x)), var103(x)))),
	ForAll([x], Not(Or(Not(var86(x)), var231(x)))),
	ForAll([x], Not(Or(var305(x), Not(var53(x))))),
	ForAll([x], Not(Or(Not(var222(x)), Not(var85(x))))),
	ForAll([x], Not(Or(Not(var137(x)), Not(var303(x))))),
	ForAll([x], Not(Or(Not(var329(x)), var145(x)))),
	ForAll([x], Not(Or(Not(var344(x)), var551(x)))),
	ForAll([x], Not(Or(var300(x), var77(x)))),
	ForAll([x], Not(Or(var35(x), Not(var438(x))))),
	ForAll([x], Not(Or(Not(var359(x)), var287(x)))),
	ForAll([x], Not(Or(var3(x), var501(x)))),
	ForAll([x], Not(Or(Not(var185(x)), var33(x)))),
	ForAll([x], Not(Or(Not(var333(x)), var499(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var348(x1)), Not(var578(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var292(x1), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var56(x1)), Not(var446(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var564(x1), var357(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var256(x1)), Not(var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), var298(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var536(x1)), var286(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var24(x1)), Not(var6(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var515(x1)), Not(var283(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var176(x1)), var146(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var156(x1), Not(var553(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var347(x1), var179(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var404(x1)), var90(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var257(x1)), var213(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var296(x1), Not(var80(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var237(x1), Not(var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), Not(var100(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var319(x1), var335(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var361(x1)), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var142(x1)), Not(var106(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var139(x1)), var63(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), var9(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var50(x1)), Not(var462(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var241(x1), Not(var290(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var16(x1), Not(var173(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var167(x1), var571(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var475(x1), var71(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var299(x1)), Not(var170(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var493(x1), var304(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var202(x1)), Not(var224(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var226(x1), var354(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var199(x1)), Not(var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var228(x1)), Not(var152(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var166(x1)), Not(var171(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var119(x1), var191(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var187(x1)), var184(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var74(x1)), Not(var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var425(x1), Not(var250(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var225(x1)), var37(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var25(x1), Not(var338(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var215(x1)), Not(var268(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var34(x1), var1(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var522(x1), Not(var178(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var481(x1), var126(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var147(x1)), Not(var255(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var351(x1)), var180(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var321(x1), var264(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var12(x1)), var118(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var148(x1)), var595(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var301(x1)), var403(x))))),
	ForAll([x], Not(Or(Not(var246(x)), Not(var280(x)), Not(var209(x))))),
	ForAll([x], Not(Or(var189(x), Not(var190(x)), Not(var136(x))))),
	ForAll([x], Not(Or(Not(var297(x)), Not(var577(x)), Not(var486(x))))),
	ForAll([x], Not(Or(var236(x), Not(var62(x)), Not(var165(x))))),
	ForAll([x], Not(Or(Not(var194(x)), var339(x), var55(x)))),
	ForAll([x], Not(Or(Not(var430(x)), Not(var75(x)), var121(x)))),
	ForAll([x], Not(Or(var426(x), Not(var157(x)), var377(x)))),
	ForAll([x], Not(Or(var399(x), Not(var569(x)), Not(var201(x))))),
	ForAll([x], Not(Or(var204(x), Not(var360(x)), var181(x)))),
	ForAll([x], Not(Or(var84(x), Not(var581(x)), var460(x)))),
	ForAll([x], Not(Or(var107(x), Not(var543(x)), var45(x)))),
	ForAll([x], Not(Or(var253(x), Not(var302(x)), var326(x)))),
	ForAll([x], Not(Or(Not(var73(x)), Not(var158(x)), Not(var59(x))))),
	ForAll([x], Not(Or(var267(x), Not(var261(x)), Not(var64(x))))),
	ForAll([x], Not(Or(var570(x), Not(var519(x)), var336(x)))),
	ForAll([x], Not(Or(Not(var182(x)), var356(x), Not(var509(x))))),
	ForAll([x], Not(Or(var432(x), var316(x), Not(var19(x))))),
	ForAll([x], Not(Or(Not(var330(x)), Not(var244(x)), Not(var550(x))))),
	ForAll([x], Not(Or(Not(var529(x)), var586(x), Not(var65(x))))),
	ForAll([x], Not(Or(var108(x), Not(var533(x)), var531(x)))),
	ForAll([x], Not(Or(Not(var54(x)), Not(var448(x)), Not(var440(x))))),
	ForAll([x], Not(Or(Not(var291(x)), Not(var341(x)), Not(var219(x))))),
	ForAll([x], Not(Or(var113(x), Not(var381(x)), Not(var323(x))))),
	ForAll([x], Not(Or(var252(x), var457(x), var69(x)))),
	ForAll([x], Not(Or(var198(x), var60(x), Not(var265(x))))),
	ForAll([x], Not(Or(Not(var149(x)), Not(var97(x)), Not(var101(x))))),
	ForAll([x], Not(Or(Not(var405(x)), Not(var232(x)), var164(x)))),
	ForAll([x], Not(Or(Not(var431(x)), Not(var454(x)), Not(var588(x))))),
	ForAll([x], Not(Or(var172(x), var574(x), Not(var312(x))))),
	ForAll([x], Not(Or(Not(var346(x)), Not(var96(x)), Not(var188(x))))),
	ForAll([x], Not(Or(Not(var249(x)), Not(var555(x)), Not(var422(x))))),
	ForAll([x], Not(Or(Not(var82(x)), var44(x), var471(x)))),
	ForAll([x], Not(Or(var99(x), var279(x), var240(x)))),
	ForAll([x], Not(Or(var453(x), var490(x), var132(x)))),
	ForAll([x], Not(Or(var93(x), var205(x), Not(var175(x))))),
	ForAll([x], Not(Or(var458(x), var72(x), Not(var235(x))))),
	ForAll([x], Not(Or(Not(var214(x)), Not(var262(x)), Not(var372(x))))),
	ForAll([x], Not(Or(Not(var308(x)), var110(x), var23(x)))),
	ForAll([x], Not(Or(Not(var254(x)), Not(var17(x)), var52(x)))),
	ForAll([x], Not(Or(var160(x), Not(var141(x)), Not(var285(x))))),
	ForAll([x], Not(Or(var306(x), Not(var343(x)), Not(var467(x))))),
	ForAll([x], Not(Or(Not(var57(x)), var138(x), var154(x)))),
	ForAll([x], Not(Or(Not(var272(x)), var223(x), var48(x)))),
	ForAll([x], Not(Or(var18(x), Not(var587(x)), Not(var337(x))))),
	ForAll([x], Not(Or(var129(x), Not(var384(x)), var314(x)))),
	ForAll([x], Not(Or(var14(x), var566(x), var43(x)))),
	ForAll([x], Not(Or(Not(var117(x)), Not(var461(x)), var477(x)))),
	ForAll([x], Not(Or(Not(var124(x)), Not(var218(x)), var449(x)))),
	ForAll([x], Not(Or(Not(var320(x)), var482(x), Not(var591(x))))),
	ForAll([x], Not(Or(Not(var183(x)), var582(x), var439(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var207(x1), Or(Not(var128(x)), Not(var251(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var355(x1)), var13(x1)), Not(var328(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var340(x1), Or(var358(x), Not(var516(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var196(x1)), Or(var599(x), Not(var383(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var15(x1), var275(x1)), Not(var465(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var530(x1), var27(x1)), var46(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var532(x1), var277(x1)), var216(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var313(x1)), var407(x1)), Not(var81(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var535(x1), Not(var51(x1))), var186(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var485(x1), Not(var334(x1))), var352(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var258(x1), Or(Not(var259(x)), Not(var379(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var109(x1)), Not(var162(x1))), var79(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var416(x1), Or(var116(x), Not(var133(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var47(x1)), var474(x1)), Not(var488(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var386(x1)), Not(var496(x1))), Not(var245(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var517(x1)), Or(Not(var565(x)), var411(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var206(x1), Or(var363(x), var239(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var390(x1), Or(var115(x), var243(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var153(x1), var39(x1)), Not(var406(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var140(x1)), Or(var561(x), Not(var30(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var324(x1), Not(var429(x1))), var284(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var464(x1), Not(var31(x1))), Not(var163(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var161(x1), Or(var596(x), var112(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var331(x1), Or(Not(var104(x)), Not(var307(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var38(x1)), Or(Not(var562(x)), var127(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var295(x1)), Or(var452(x), Not(var98(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var274(x1)), var478(x1)), Not(var423(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var260(x1), Or(var91(x), Not(var83(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var276(x1), Or(var288(x), Not(var20(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var380(x1), var281(x1)), var131(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var327(x1)), Or(Not(var315(x)), Not(var144(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var364(x1)), Or(Not(var229(x)), var480(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var212(x1), Or(var94(x), var318(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var5(x1), Or(Not(var197(x)), var114(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var479(x1), var382(x1)), Not(var26(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var195(x1)), Not(var102(x1))), var556(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var518(x1), Or(var92(x), Not(var342(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var350(x1)), Or(var520(x), Not(var242(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var443(x1)), Or(Not(var22(x)), Not(var525(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var220(x1)), Not(var66(x1))), Not(var491(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var584(x1)), Or(var32(x), Not(var2(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var472(x1)), Or(var177(x), Not(var421(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var49(x1), var567(x1)), Not(var227(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var413(x1)), Not(var289(x1))), Not(var155(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var427(x1)), Not(var159(x1))), Not(var311(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var317(x1), Not(var278(x1))), var450(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var559(x1), var134(x1)), var273(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var492(x1)), var560(x1)), var408(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var293(x1), Or(var366(x), Not(var294(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var322(x1)), Or(var87(x), var349(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
