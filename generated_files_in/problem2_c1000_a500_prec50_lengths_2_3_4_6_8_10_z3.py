from z3 import *

Object = DeclareSort('Object')

var136 = Function('var136', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var494 = Function('var494', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var475 = Function('var475', Object, BoolSort())
var479 = Function('var479', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var498 = Function('var498', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var443 = Function('var443', Object, BoolSort())
var497 = Function('var497', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var335 = Function('var335', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var410 = Function('var410', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var417 = Function('var417', Object, BoolSort())
var406 = Function('var406', Object, BoolSort())
var448 = Function('var448', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var465 = Function('var465', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var466 = Function('var466', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var317 = Function('var317', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var395 = Function('var395', Object, BoolSort())
var369 = Function('var369', Object, BoolSort())
var452 = Function('var452', Object, BoolSort())
var421 = Function('var421', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var336 = Function('var336', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var458 = Function('var458', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var386 = Function('var386', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var340 = Function('var340', Object, BoolSort())
var356 = Function('var356', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var373 = Function('var373', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var378 = Function('var378', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var409 = Function('var409', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var493 = Function('var493', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var318 = Function('var318', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var446 = Function('var446', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var392 = Function('var392', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var348 = Function('var348', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var371 = Function('var371', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var491 = Function('var491', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var413 = Function('var413', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var405 = Function('var405', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var429 = Function('var429', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var470 = Function('var470', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var483 = Function('var483', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var436 = Function('var436', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var377 = Function('var377', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var425 = Function('var425', Object, BoolSort())
var324 = Function('var324', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var426 = Function('var426', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var488 = Function('var488', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var431 = Function('var431', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var316 = Function('var316', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var481 = Function('var481', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var490 = Function('var490', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var364 = Function('var364', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var403 = Function('var403', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var390 = Function('var390', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var367 = Function('var367', Object, BoolSort())
var351 = Function('var351', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var420 = Function('var420', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var404 = Function('var404', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var418 = Function('var418', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var323 = Function('var323', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var365 = Function('var365', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var313 = Function('var313', Object, BoolSort())
var430 = Function('var430', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var419 = Function('var419', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var379 = Function('var379', Object, BoolSort())
var496 = Function('var496', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var439 = Function('var439', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var454 = Function('var454', Object, BoolSort())
var437 = Function('var437', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var269 = Function('var269', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var385 = Function('var385', Object, BoolSort())
var407 = Function('var407', Object, BoolSort())
var438 = Function('var438', Object, BoolSort())
var354 = Function('var354', Object, BoolSort())
var416 = Function('var416', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var442 = Function('var442', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var445 = Function('var445', Object, BoolSort())
var349 = Function('var349', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var457 = Function('var457', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var499 = Function('var499', Object, BoolSort())
var456 = Function('var456', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var372 = Function('var372', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var309 = Function('var309', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var447 = Function('var447', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var492 = Function('var492', Object, BoolSort())
var486 = Function('var486', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var307 = Function('var307', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var500 = Function('var500', Object, BoolSort())
var489 = Function('var489', Object, BoolSort())
var408 = Function('var408', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var432 = Function('var432', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var450 = Function('var450', Object, BoolSort())
var391 = Function('var391', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var402 = Function('var402', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var473 = Function('var473', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var462 = Function('var462', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var460 = Function('var460', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var435 = Function('var435', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var495 = Function('var495', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var449 = Function('var449', Object, BoolSort())
var440 = Function('var440', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var362 = Function('var362', Object, BoolSort())
var459 = Function('var459', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var308 = Function('var308', Object, BoolSort())
var401 = Function('var401', Object, BoolSort())
var424 = Function('var424', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var467 = Function('var467', Object, BoolSort())
var398 = Function('var398', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var376 = Function('var376', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var302 = Function('var302', Object, BoolSort())
var412 = Function('var412', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var478 = Function('var478', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var276 = Function('var276', Object, BoolSort())
var463 = Function('var463', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var350 = Function('var350', Object, BoolSort())
var451 = Function('var451', Object, BoolSort())
var411 = Function('var411', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var423 = Function('var423', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var414 = Function('var414', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var476 = Function('var476', Object, BoolSort())
var444 = Function('var444', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var441 = Function('var441', Object, BoolSort())
var455 = Function('var455', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var471 = Function('var471', Object, BoolSort())
var469 = Function('var469', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var434 = Function('var434', Object, BoolSort())
var487 = Function('var487', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var484 = Function('var484', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var433 = Function('var433', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var474 = Function('var474', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var389 = Function('var389', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var427 = Function('var427', Object, BoolSort())
var468 = Function('var468', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var396 = Function('var396', Object, BoolSort())
var485 = Function('var485', Object, BoolSort())
var296 = Function('var296', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var472 = Function('var472', Object, BoolSort())
var422 = Function('var422', Object, BoolSort())
var461 = Function('var461', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var306 = Function('var306', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var453 = Function('var453', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var477 = Function('var477', Object, BoolSort())
var333 = Function('var333', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var482 = Function('var482', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var428 = Function('var428', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Not(var136(x)))),
	ForAll([x], Not(Not(var320(x)))),
	ForAll([x], Not(var144(x))),
	ForAll([x], Not(Not(var113(x)))),
	ForAll([x], Not(var213(x))),
	ForAll([x], Not(var494(x))),
	ForAll([x], Not(Not(var94(x)))),
	ForAll([x], Not(Not(var105(x)))),
	ForAll([x], Not(Not(var368(x)))),
	ForAll([x], Not(Not(var178(x)))),
	ForAll([x], Not(var360(x))),
	ForAll([x], Not(var475(x))),
	ForAll([x], Not(Not(var479(x)))),
	ForAll([x], Not(Not(var155(x)))),
	ForAll([x], Not(Not(var498(x)))),
	ForAll([x], Not(var380(x))),
	ForAll([x], Not(var7(x))),
	ForAll([x], Not(Not(var443(x)))),
	ForAll([x], Not(var497(x))),
	ForAll([x], Not(var380(x))),
	ForAll([x], Not(var382(x))),
	ForAll([x], Not(Not(var223(x)))),
	ForAll([x], Not(var45(x))),
	ForAll([x], Not(Not(var329(x)))),
	ForAll([x], Not(Not(var335(x)))),
	ForAll([x], Not(var360(x))),
	ForAll([x], Not(var98(x))),
	ForAll([x], Not(Not(var410(x)))),
	ForAll([x], Not(var278(x))),
	ForAll([x], Not(var28(x))),
	ForAll([x], Not(var417(x))),
	ForAll([x], Not(var406(x))),
	ForAll([x], Not(var448(x))),
	ForAll([x], Not(var293(x))),
	ForAll([x], Not(var268(x))),
	ForAll([x], Not(Not(var7(x)))),
	ForAll([x], Not(Not(var40(x)))),
	ForAll([x], Not(Not(var283(x)))),
	ForAll([x], Not(var253(x))),
	ForAll([x], Not(var6(x))),
	ForAll([x], Not(Not(var160(x)))),
	ForAll([x], Not(var465(x))),
	ForAll([x], Not(var92(x))),
	ForAll([x], Not(var92(x))),
	ForAll([x], Not(Not(var14(x)))),
	ForAll([x], Not(var282(x))),
	ForAll([x], Not(var466(x))),
	ForAll([x], Not(var84(x))),
	ForAll([x], Not(Not(var11(x)))),
	ForAll([x], Not(Not(var317(x)))),
	ForAll([x], Not(Not(var258(x)))),
	ForAll([x], Not(Not(var69(x)))),
	ForAll([x], Not(Not(var23(x)))),
	Exists([x], var332(x)),
	Exists([x], Not(var40(x))),
	Exists([x], Not(var78(x))),
	Exists([x], var363(x)),
	Exists([x], Not(var144(x))),
	Exists([x], var92(x)),
	Exists([x], Not(var167(x))),
	Exists([x], var317(x)),
	Exists([x], var395(x)),
	Exists([x], Not(var369(x))),
	Exists([x], var452(x)),
	Exists([x], var421(x)),
	Exists([x], Not(var268(x))),
	Exists([x], Not(var370(x))),
	Exists([x], var336(x)),
	Exists([x], Not(var40(x))),
	Exists([x], var202(x)),
	Exists([x], var116(x)),
	Exists([x], Not(var282(x))),
	Exists([x], var458(x)),
	Exists([x], var368(x)),
	Exists([x], Not(var271(x))),
	Exists([x], Not(var204(x))),
	Exists([x], Not(var384(x))),
	Exists([x], Not(var3(x))),
	Exists([x], Not(var386(x))),
	Exists([x], Not(var288(x))),
	Exists([x], var45(x)),
	Exists([x], Not(var448(x))),
	Exists([x], Not(var340(x))),
	Exists([x], var356(x)),
	Exists([x], Not(var150(x))),
	Exists([x], var120(x)),
	Exists([x], Not(var373(x))),
	Exists([x], var257(x)),
	Exists([x], var368(x)),
	Exists([x], Not(var245(x))),
	Exists([x], Not(var158(x))),
	Exists([x], var191(x)),
	Exists([x], var186(x)),
	Exists([x], var7(x)),
	Exists([x], Not(var378(x))),
	Exists([x], var395(x)),
	Exists([x], Not(var75(x))),
	Exists([x], var409(x)),
	Exists([x], var290(x)),
	Exists([x], Not(var194(x))),
	Exists([x], var341(x)),
	Exists([x], Not(var65(x))),
	Exists([x], Not(var274(x))),
	Exists([x], var493(x)),
	Exists([x], var12(x)),
	Exists([x], var318(x)),
	ForAll([x], Not(Or(Not(var249(x)), var97(x)))),
	ForAll([x], Not(Or(var498(x), var33(x)))),
	ForAll([x], Not(Or(Not(var54(x)), var66(x)))),
	ForAll([x], Not(Or(var130(x), var388(x)))),
	ForAll([x], Not(Or(var195(x), Not(var29(x))))),
	ForAll([x], Not(Or(var85(x), var305(x)))),
	ForAll([x], Not(Or(var190(x), Not(var452(x))))),
	ForAll([x], Not(Or(Not(var43(x)), Not(var123(x))))),
	ForAll([x], Not(Or(var143(x), Not(var274(x))))),
	ForAll([x], Not(Or(Not(var270(x)), var202(x)))),
	ForAll([x], Not(Or(var236(x), var446(x)))),
	ForAll([x], Not(Or(Not(var475(x)), var380(x)))),
	ForAll([x], Not(Or(Not(var17(x)), var392(x)))),
	ForAll([x], Not(Or(var131(x), Not(var253(x))))),
	ForAll([x], Not(Or(Not(var348(x)), Not(var42(x))))),
	ForAll([x], Not(Or(var80(x), var41(x)))),
	ForAll([x], Not(Or(var284(x), Not(var179(x))))),
	ForAll([x], Not(Or(var56(x), var371(x)))),
	ForAll([x], Not(Or(Not(var61(x)), var175(x)))),
	ForAll([x], Not(Or(Not(var126(x)), var154(x)))),
	ForAll([x], Not(Or(var119(x), Not(var358(x))))),
	ForAll([x], Not(Or(Not(var198(x)), var218(x)))),
	ForAll([x], Not(Or(Not(var47(x)), var283(x)))),
	ForAll([x], Not(Or(var109(x), Not(var42(x))))),
	ForAll([x], Not(Or(var491(x), var48(x)))),
	ForAll([x], Not(Or(Not(var7(x)), Not(var15(x))))),
	ForAll([x], Not(Or(Not(var263(x)), var310(x)))),
	ForAll([x], Not(Or(Not(var74(x)), var340(x)))),
	ForAll([x], Not(Or(Not(var493(x)), Not(var381(x))))),
	ForAll([x], Not(Or(var242(x), Not(var413(x))))),
	ForAll([x], Not(Or(Not(var226(x)), Not(var126(x))))),
	ForAll([x], Not(Or(var178(x), var66(x)))),
	ForAll([x], Not(Or(var131(x), var121(x)))),
	ForAll([x], Not(Or(Not(var227(x)), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var51(x)), Not(var93(x))))),
	ForAll([x], Not(Or(Not(var98(x)), var493(x)))),
	ForAll([x], Not(Or(var160(x), Not(var378(x))))),
	ForAll([x], Not(Or(var405(x), var200(x)))),
	ForAll([x], Not(Or(Not(var165(x)), Not(var17(x))))),
	ForAll([x], Not(Or(var56(x), Not(var180(x))))),
	ForAll([x], Not(Or(Not(var17(x)), Not(var186(x))))),
	ForAll([x], Not(Or(Not(var465(x)), var162(x)))),
	ForAll([x], Not(Or(var76(x), Not(var328(x))))),
	ForAll([x], Not(Or(Not(var41(x)), var151(x)))),
	ForAll([x], Not(Or(Not(var47(x)), Not(var183(x))))),
	ForAll([x], Not(Or(Not(var318(x)), Not(var125(x))))),
	ForAll([x], Not(Or(Not(var429(x)), Not(var48(x))))),
	ForAll([x], Not(Or(var405(x), Not(var301(x))))),
	ForAll([x], Not(Or(Not(var87(x)), var199(x)))),
	ForAll([x], Not(Or(var180(x), var327(x)))),
	ForAll([x], Not(Or(var84(x), Not(var67(x))))),
	ForAll([x], Not(Or(Not(var270(x)), Not(var89(x))))),
	ForAll([x], Not(Or(Not(var48(x)), var470(x)))),
	ForAll([x], Not(Or(Not(var300(x)), Not(var180(x))))),
	ForAll([x], Not(Or(var226(x), var483(x)))),
	ForAll([x], Not(Or(Not(var378(x)), Not(var357(x))))),
	ForAll([x], Not(Or(var157(x), Not(var301(x))))),
	ForAll([x], Not(Or(var39(x), Not(var436(x))))),
	ForAll([x], Not(Or(Not(var69(x)), Not(var74(x))))),
	ForAll([x], Not(Or(var158(x), Not(var209(x))))),
	ForAll([x], Not(Or(var53(x), Not(var318(x))))),
	ForAll([x], Not(Or(Not(var65(x)), var58(x)))),
	ForAll([x], Not(Or(var168(x), var413(x)))),
	ForAll([x], Not(Or(Not(var265(x)), Not(var290(x))))),
	ForAll([x], Not(Or(var227(x), Not(var113(x))))),
	ForAll([x], Not(Or(Not(var213(x)), Not(var25(x))))),
	ForAll([x], Not(Or(var68(x), Not(var271(x))))),
	ForAll([x], Not(Or(var377(x), Not(var75(x))))),
	ForAll([x], Not(Or(var334(x), Not(var425(x))))),
	ForAll([x], Not(Or(var324(x), var46(x)))),
	ForAll([x], Not(Or(var153(x), Not(var319(x))))),
	ForAll([x], Not(Or(var465(x), Not(var240(x))))),
	ForAll([x], Not(Or(var87(x), Not(var465(x))))),
	ForAll([x], Not(Or(var263(x), Not(var426(x))))),
	ForAll([x], Not(Or(var56(x), Not(var124(x))))),
	ForAll([x], Not(Or(Not(var488(x)), Not(var355(x))))),
	ForAll([x], Not(Or(var310(x), Not(var431(x))))),
	ForAll([x], Not(Or(Not(var174(x)), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var316(x)), Not(var169(x))))),
	ForAll([x], Not(Or(Not(var330(x)), var321(x)))),
	ForAll([x], Not(Or(var256(x), var146(x)))),
	ForAll([x], Not(Or(Not(var361(x)), var481(x)))),
	ForAll([x], Not(Or(var88(x), var246(x)))),
	ForAll([x], Not(Or(var132(x), Not(var171(x))))),
	ForAll([x], Not(Or(Not(var214(x)), var108(x)))),
	ForAll([x], Not(Or(var291(x), Not(var31(x))))),
	ForAll([x], Not(Or(var321(x), Not(var58(x))))),
	ForAll([x], Not(Or(var490(x), var136(x)))),
	ForAll([x], Not(Or(var221(x), var301(x)))),
	ForAll([x], Not(Or(var2(x), var83(x)))),
	ForAll([x], Not(Or(var364(x), var6(x)))),
	ForAll([x], Not(Or(var364(x), Not(var348(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var91(x1), var305(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var341(x1), Not(var152(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var466(x1), var92(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var403(x1)), var206(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var145(x1)), var429(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var213(x1)), Not(var390(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var119(x1), var111(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var367(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var288(x1)), var351(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var187(x1)), Not(var192(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var397(x1), var250(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var446(x1), Not(var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var198(x1)), Not(var420(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var233(x1), var262(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var359(x1), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var143(x1)), Not(var404(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var166(x1), Not(var161(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var238(x1), var50(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var418(x1)), var73(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var64(x1), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var323(x1)), Not(var240(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var143(x1), var255(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var42(x1)), Not(var85(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var278(x1), var344(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var332(x1), Not(var331(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var365(x1)), Not(var124(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var55(x1), var313(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var11(x1)), var430(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var340(x1), var111(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var210(x1)), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var392(x1), var25(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var205(x1), Not(var168(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), Not(var6(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var213(x1)), Not(var5(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var77(x1)), Not(var419(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var240(x1), var301(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var258(x1), Not(var377(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var448(x1), Not(var132(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var297(x1), var383(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var174(x1)), Not(var379(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var491(x1)), var2(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var65(x1), var75(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var496(x1), var141(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var128(x1)), Not(var313(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var105(x1), Not(var284(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var294(x1)), Not(var120(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var64(x1), var127(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var268(x1)), var152(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var464(x1), var282(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var494(x1)), Not(var425(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var439(x1), Not(var153(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var24(x1), var37(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var194(x1), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var220(x1)), var329(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var289(x1), var371(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var40(x1)), Not(var273(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var268(x1)), var54(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var118(x1)), var454(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var317(x1)), Not(var316(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var125(x1)), Not(var437(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var132(x1)), var230(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var52(x1)), Not(var313(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var417(x1)), Not(var180(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var279(x1), var383(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var168(x1), var361(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var348(x1)), var115(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Not(var378(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var269(x1), Not(var146(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var358(x1), var265(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var448(x1)), var34(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var245(x1), var316(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), var137(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var42(x1), var436(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var160(x1), Not(var210(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var144(x1), Not(var261(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var95(x1), Not(var227(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var1(x1), Not(var234(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var437(x1), var256(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var418(x1)), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var443(x1)), var158(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var359(x1), var256(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var170(x1)), Not(var470(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var204(x1)), Not(var385(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var407(x1), Not(var379(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var124(x1), var438(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var56(x1), Not(var378(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var310(x1), var406(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var218(x1), var301(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var15(x1), var11(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var191(x1)), Not(var354(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var128(x1), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var493(x1), var416(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var35(x1)), var95(x))))),
	ForAll([x], Not(Or(Not(var63(x)), var210(x), var383(x)))),
	ForAll([x], Not(Or(var238(x), var81(x), Not(var318(x))))),
	ForAll([x], Not(Or(Not(var149(x)), Not(var90(x)), var226(x)))),
	ForAll([x], Not(Or(Not(var161(x)), var420(x), Not(var442(x))))),
	ForAll([x], Not(Or(var22(x), var445(x), Not(var328(x))))),
	ForAll([x], Not(Or(Not(var349(x)), Not(var188(x)), var224(x)))),
	ForAll([x], Not(Or(var410(x), Not(var465(x)), var81(x)))),
	ForAll([x], Not(Or(var265(x), Not(var457(x)), Not(var312(x))))),
	ForAll([x], Not(Or(var141(x), var263(x), Not(var197(x))))),
	ForAll([x], Not(Or(var499(x), Not(var456(x)), var183(x)))),
	ForAll([x], Not(Or(Not(var148(x)), var352(x), var437(x)))),
	ForAll([x], Not(Or(var379(x), Not(var237(x)), Not(var65(x))))),
	ForAll([x], Not(Or(var256(x), Not(var297(x)), var258(x)))),
	ForAll([x], Not(Or(var342(x), Not(var175(x)), var9(x)))),
	ForAll([x], Not(Or(var174(x), var351(x), var39(x)))),
	ForAll([x], Not(Or(var359(x), var379(x), var98(x)))),
	ForAll([x], Not(Or(var381(x), Not(var466(x)), var3(x)))),
	ForAll([x], Not(Or(var341(x), Not(var273(x)), var372(x)))),
	ForAll([x], Not(Or(var173(x), Not(var309(x)), Not(var77(x))))),
	ForAll([x], Not(Or(var230(x), var257(x), Not(var452(x))))),
	ForAll([x], Not(Or(var246(x), Not(var72(x)), Not(var231(x))))),
	ForAll([x], Not(Or(Not(var120(x)), var481(x), var67(x)))),
	ForAll([x], Not(Or(var169(x), var239(x), Not(var76(x))))),
	ForAll([x], Not(Or(Not(var128(x)), var68(x), Not(var174(x))))),
	ForAll([x], Not(Or(var187(x), var224(x), Not(var285(x))))),
	ForAll([x], Not(Or(var240(x), var447(x), Not(var184(x))))),
	ForAll([x], Not(Or(Not(var317(x)), Not(var267(x)), Not(var27(x))))),
	ForAll([x], Not(Or(Not(var419(x)), var406(x), Not(var165(x))))),
	ForAll([x], Not(Or(var205(x), var492(x), Not(var486(x))))),
	ForAll([x], Not(Or(var174(x), Not(var89(x)), var448(x)))),
	ForAll([x], Not(Or(Not(var96(x)), Not(var356(x)), var446(x)))),
	ForAll([x], Not(Or(var134(x), Not(var280(x)), var443(x)))),
	ForAll([x], Not(Or(Not(var457(x)), var447(x), var361(x)))),
	ForAll([x], Not(Or(var24(x), Not(var137(x)), Not(var139(x))))),
	ForAll([x], Not(Or(var1(x), Not(var312(x)), Not(var374(x))))),
	ForAll([x], Not(Or(Not(var319(x)), Not(var96(x)), Not(var307(x))))),
	ForAll([x], Not(Or(Not(var169(x)), var343(x), var241(x)))),
	ForAll([x], Not(Or(var164(x), Not(var21(x)), Not(var281(x))))),
	ForAll([x], Not(Or(var220(x), var192(x), var340(x)))),
	ForAll([x], Not(Or(Not(var291(x)), Not(var500(x)), var317(x)))),
	ForAll([x], Not(Or(var489(x), var408(x), var355(x)))),
	ForAll([x], Not(Or(var148(x), Not(var405(x)), Not(var324(x))))),
	ForAll([x], Not(Or(Not(var209(x)), Not(var72(x)), var365(x)))),
	ForAll([x], Not(Or(var335(x), var86(x), Not(var21(x))))),
	ForAll([x], Not(Or(var129(x), var281(x), var205(x)))),
	ForAll([x], Not(Or(var324(x), var217(x), Not(var432(x))))),
	ForAll([x], Not(Or(Not(var240(x)), var149(x), var105(x)))),
	ForAll([x], Not(Or(Not(var324(x)), Not(var51(x)), Not(var307(x))))),
	ForAll([x], Not(Or(var190(x), Not(var52(x)), Not(var253(x))))),
	ForAll([x], Not(Or(var432(x), Not(var232(x)), Not(var103(x))))),
	ForAll([x], Not(Or(Not(var258(x)), var187(x), Not(var450(x))))),
	ForAll([x], Not(Or(var67(x), Not(var226(x)), var335(x)))),
	ForAll([x], Not(Or(var365(x), Not(var421(x)), Not(var194(x))))),
	ForAll([x], Not(Or(Not(var324(x)), Not(var115(x)), var431(x)))),
	ForAll([x], Not(Or(Not(var499(x)), var132(x), var391(x)))),
	ForAll([x], Not(Or(Not(var216(x)), var452(x), var402(x)))),
	ForAll([x], Not(Or(Not(var261(x)), Not(var337(x)), var274(x)))),
	ForAll([x], Not(Or(var338(x), var437(x), var473(x)))),
	ForAll([x], Not(Or(var490(x), var71(x), Not(var405(x))))),
	ForAll([x], Not(Or(Not(var402(x)), Not(var214(x)), var2(x)))),
	ForAll([x], Not(Or(Not(var462(x)), Not(var144(x)), Not(var275(x))))),
	ForAll([x], Not(Or(Not(var291(x)), Not(var387(x)), var3(x)))),
	ForAll([x], Not(Or(var265(x), Not(var169(x)), var53(x)))),
	ForAll([x], Not(Or(var460(x), var371(x), var63(x)))),
	ForAll([x], Not(Or(var419(x), var464(x), var267(x)))),
	ForAll([x], Not(Or(var158(x), var432(x), var368(x)))),
	ForAll([x], Not(Or(var382(x), Not(var251(x)), var488(x)))),
	ForAll([x], Not(Or(Not(var211(x)), var435(x), var403(x)))),
	ForAll([x], Not(Or(var136(x), var57(x), Not(var495(x))))),
	ForAll([x], Not(Or(Not(var125(x)), var176(x), Not(var53(x))))),
	ForAll([x], Not(Or(Not(var449(x)), Not(var440(x)), var151(x)))),
	ForAll([x], Not(Or(var483(x), var65(x), var491(x)))),
	ForAll([x], Not(Or(var167(x), var303(x), var341(x)))),
	ForAll([x], Not(Or(Not(var69(x)), Not(var206(x)), Not(var126(x))))),
	ForAll([x], Not(Or(var290(x), Not(var417(x)), Not(var360(x))))),
	ForAll([x], Not(Or(var256(x), Not(var325(x)), var206(x)))),
	ForAll([x], Not(Or(Not(var490(x)), Not(var258(x)), Not(var488(x))))),
	ForAll([x], Not(Or(var283(x), var332(x), var199(x)))),
	ForAll([x], Not(Or(var362(x), Not(var35(x)), var111(x)))),
	ForAll([x], Not(Or(var459(x), Not(var375(x)), var71(x)))),
	ForAll([x], Not(Or(var308(x), var279(x), var209(x)))),
	ForAll([x], Not(Or(var401(x), Not(var424(x)), var437(x)))),
	ForAll([x], Not(Or(Not(var220(x)), Not(var436(x)), var148(x)))),
	ForAll([x], Not(Or(var259(x), var98(x), var243(x)))),
	ForAll([x], Not(Or(var208(x), Not(var342(x)), Not(var351(x))))),
	ForAll([x], Not(Or(Not(var106(x)), var432(x), Not(var50(x))))),
	ForAll([x], Not(Or(Not(var318(x)), Not(var161(x)), Not(var462(x))))),
	ForAll([x], Not(Or(var150(x), var7(x), Not(var388(x))))),
	ForAll([x], Not(Or(var280(x), var456(x), var460(x)))),
	ForAll([x], Not(Or(var71(x), var467(x), var419(x)))),
	ForAll([x], Not(Or(var398(x), var437(x), var24(x)))),
	ForAll([x], Not(Or(var136(x), Not(var38(x)), Not(var47(x))))),
	ForAll([x], Not(Or(Not(var382(x)), var148(x), var496(x)))),
	ForAll([x], Not(Or(Not(var406(x)), var381(x), Not(var480(x))))),
	ForAll([x], Not(Or(var114(x), Not(var431(x)), var33(x)))),
	ForAll([x], Not(Or(Not(var252(x)), Not(var304(x)), var265(x)))),
	ForAll([x], Not(Or(Not(var265(x)), Not(var392(x)), var202(x)))),
	ForAll([x], Not(Or(Not(var364(x)), var128(x), var52(x)))),
	ForAll([x], Not(Or(var317(x), var112(x), Not(var315(x))))),
	ForAll([x], Not(Or(Not(var163(x)), var150(x), Not(var246(x))))),
	ForAll([x], Not(Or(var366(x), Not(var33(x)), Not(var142(x))))),
	ForAll([x], Not(Or(var362(x), var272(x), var42(x)))),
	ForAll([x], Not(Or(Not(var339(x)), Not(var467(x)), var95(x)))),
	ForAll([x], Not(Or(Not(var304(x)), var263(x), Not(var288(x))))),
	ForAll([x], Not(Or(var376(x), Not(var18(x)), Not(var132(x))))),
	ForAll([x], Not(Or(Not(var466(x)), Not(var263(x)), var186(x)))),
	ForAll([x], Not(Or(Not(var10(x)), Not(var22(x)), var302(x)))),
	ForAll([x], Not(Or(Not(var90(x)), var95(x), Not(var364(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var412(x1)), Or(var130(x), Not(var105(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var249(x1)), Not(var361(x1))), var329(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var105(x1), Or(var182(x), Not(var402(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var154(x1)), Not(var227(x1))), Not(var478(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var246(x1), Or(var148(x), var297(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var125(x1)), Or(Not(var149(x)), Not(var54(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var194(x1), Or(var17(x), var127(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var129(x1)), var384(x1)), Not(var244(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var212(x1), Not(var165(x1))), var388(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var266(x1), Not(var431(x1))), var459(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var110(x1), Or(Not(var262(x)), var276(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var52(x1), Not(var371(x1))), var352(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var153(x1), Not(var463(x1))), Not(var462(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var323(x1), Not(var11(x1))), Not(var402(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var276(x1), Not(var337(x1))), Not(var218(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var382(x1), Or(var28(x), Not(var281(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var236(x1), Or(var249(x), Not(var382(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var28(x1)), Or(var159(x), Not(var213(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var372(x1), Or(var89(x), Not(var134(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var402(x1)), var377(x1)), Not(var350(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var391(x1)), var143(x1)), Not(var370(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var321(x1)), var451(x1)), Not(var188(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var411(x1), Or(var28(x), var184(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), Or(Not(var286(x)), Not(var393(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var446(x1)), Or(var208(x), var76(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var11(x1), Not(var419(x1))), var218(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var175(x1)), Or(Not(var99(x)), var84(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var445(x1)), var234(x1)), Not(var317(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var267(x1), var225(x1)), Not(var351(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var412(x1)), var7(x1)), var31(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var268(x1)), Or(Not(var217(x)), Not(var77(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var479(x1)), Or(Not(var234(x)), var103(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var91(x1), Not(var499(x1))), var423(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var419(x1), Or(var60(x), Not(var430(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var79(x1)), Not(var88(x1))), var174(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var117(x1), Or(var371(x), Not(var370(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var221(x1)), Or(var151(x), var20(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var104(x1), var93(x1)), var184(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var368(x1), Or(var253(x), Not(var198(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var414(x1), Or(Not(var406(x)), Not(var354(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var270(x1)), Not(var264(x1))), var8(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var291(x1)), Or(var299(x), Not(var229(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var100(x1)), Or(var271(x), Not(var494(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var253(x1), var252(x1)), Not(var315(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var383(x1)), var459(x1)), var42(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var356(x1)), var118(x1)), var187(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var476(x1)), Or(var426(x), var197(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var227(x1), var33(x1)), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var444(x1), var452(x1)), var129(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var193(x1)), Or(Not(var214(x)), var351(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var41(x1)), Not(var325(x1))), Not(var430(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var380(x1), Or(Not(var164(x)), Not(var14(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var143(x1)), var441(x1)), var395(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var89(x1)), Or(Not(var259(x)), Not(var218(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var126(x1)), var364(x1)), var483(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var455(x1)), var295(x1)), Not(var382(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var390(x1)), var322(x1)), var298(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var263(x1), Not(var471(x1))), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var469(x1), Or(var121(x), var222(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var125(x1)), Or(Not(var345(x)), Not(var286(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var86(x1), var314(x1)), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var152(x1)), var357(x1)), Not(var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var230(x1), Or(Not(var371(x)), var165(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var350(x1)), Or(var320(x), var12(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var162(x1), var208(x1)), Not(var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var51(x1)), Or(var177(x), Not(var216(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var70(x1)), Not(var246(x1))), Not(var46(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var153(x1)), Not(var140(x1))), var31(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var169(x1), var382(x1)), var351(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var110(x1)), Or(Not(var216(x)), Not(var438(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var406(x1), Or(Not(var127(x)), Not(var64(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var199(x1), Not(var148(x1))), var104(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var46(x1), Or(Not(var404(x)), Not(var418(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var62(x1)), Or(Not(var447(x)), var445(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var198(x1), var231(x1)), Not(var254(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var328(x1), Or(var355(x), Not(var234(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var290(x1), Or(Not(var60(x)), Not(var434(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var274(x1), Or(var217(x), var293(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var487(x1)), Or(Not(var348(x)), Not(var81(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var65(x1), Or(Not(var377(x)), Not(var312(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var214(x1)), var78(x1)), Not(var131(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var109(x1)), Or(Not(var419(x)), Not(var271(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var201(x1), Or(Not(var350(x)), Not(var388(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var81(x1)), Or(var309(x), var143(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var201(x1)), Or(var109(x), var480(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var452(x1), Or(var185(x), Not(var137(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var301(x1), var8(x1)), var380(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var300(x1), Or(var416(x), var363(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var89(x1)), Or(Not(var106(x)), var257(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var302(x1), Not(var194(x1))), var465(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var308(x1), Or(Not(var53(x)), Not(var426(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var345(x1), Or(Not(var243(x)), var168(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var264(x1)), Not(var192(x1))), var259(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var404(x1)), Or(var31(x), var351(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var424(x1), var277(x1)), var78(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var182(x1)), Or(var45(x), Not(var75(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var202(x1), Not(var231(x1))), var167(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var9(x1)), Not(var133(x1))), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var320(x1)), Or(Not(var141(x)), Not(var405(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var274(x1), Not(var335(x1))), var304(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var458(x1), Or(var417(x), var231(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var425(x1)), Or(Not(var499(x)), Not(var409(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var287(x1)), Or(var164(x), var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var480(x1)), Or(var176(x), var47(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var150(x1)), var406(x1)), Not(var192(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var60(x1)), var172(x1)), Not(var117(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var229(x1), var219(x1)), var113(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var414(x1), Not(var150(x1))), Not(var417(x)))))),
	ForAll([x], Not(Or(Not(var484(x)), var452(x), var328(x), var343(x)))),
	ForAll([x], Not(Or(var72(x), var51(x), var304(x), Not(var493(x))))),
	ForAll([x], Not(Or(Not(var462(x)), var282(x), Not(var425(x)), Not(var56(x))))),
	ForAll([x], Not(Or(var67(x), var74(x), Not(var37(x)), var366(x)))),
	ForAll([x], Not(Or(Not(var141(x)), var7(x), var260(x), Not(var438(x))))),
	ForAll([x], Not(Or(Not(var151(x)), var481(x), var497(x), var204(x)))),
	ForAll([x], Not(Or(var181(x), var410(x), var38(x), Not(var272(x))))),
	ForAll([x], Not(Or(Not(var92(x)), var441(x), Not(var135(x)), Not(var246(x))))),
	ForAll([x], Not(Or(Not(var52(x)), Not(var243(x)), var429(x), var354(x)))),
	ForAll([x], Not(Or(var181(x), Not(var335(x)), Not(var251(x)), var204(x)))),
	ForAll([x], Not(Or(var243(x), Not(var75(x)), var175(x), var351(x)))),
	ForAll([x], Not(Or(var282(x), var69(x), Not(var297(x)), var204(x)))),
	ForAll([x], Not(Or(var425(x), var175(x), Not(var107(x)), Not(var55(x))))),
	ForAll([x], Not(Or(Not(var455(x)), Not(var116(x)), var162(x), Not(var83(x))))),
	ForAll([x], Not(Or(var181(x), var431(x), Not(var392(x)), var111(x)))),
	ForAll([x], Not(Or(var301(x), Not(var378(x)), Not(var110(x)), var172(x)))),
	ForAll([x], Not(Or(Not(var370(x)), Not(var438(x)), Not(var483(x)), Not(var153(x))))),
	ForAll([x], Not(Or(Not(var351(x)), var433(x), var72(x), Not(var386(x))))),
	ForAll([x], Not(Or(Not(var198(x)), var237(x), var360(x), Not(var337(x))))),
	ForAll([x], Not(Or(Not(var402(x)), var34(x), Not(var112(x)), var43(x)))),
	ForAll([x], Not(Or(var17(x), var491(x), var489(x), var128(x)))),
	ForAll([x], Not(Or(Not(var488(x)), var438(x), Not(var176(x)), Not(var146(x))))),
	ForAll([x], Not(Or(Not(var103(x)), Not(var261(x)), Not(var309(x)), var58(x)))),
	ForAll([x], Not(Or(Not(var416(x)), var345(x), Not(var318(x)), var184(x)))),
	ForAll([x], Not(Or(Not(var494(x)), Not(var168(x)), Not(var186(x)), Not(var67(x))))),
	ForAll([x], Not(Or(var442(x), var376(x), Not(var58(x)), var13(x)))),
	ForAll([x], Not(Or(var256(x), Not(var123(x)), Not(var307(x)), var175(x)))),
	ForAll([x], Not(Or(Not(var429(x)), Not(var463(x)), var280(x), var115(x)))),
	ForAll([x], Not(Or(var313(x), Not(var329(x)), var283(x), var129(x)))),
	ForAll([x], Not(Or(var228(x), Not(var313(x)), var294(x), Not(var195(x))))),
	ForAll([x], Not(Or(var395(x), var137(x), Not(var18(x)), Not(var163(x))))),
	ForAll([x], Not(Or(var199(x), Not(var210(x)), var424(x), var357(x)))),
	ForAll([x], Not(Or(var491(x), var231(x), var380(x), var425(x)))),
	ForAll([x], Not(Or(Not(var164(x)), Not(var332(x)), var324(x), Not(var178(x))))),
	ForAll([x], Not(Or(Not(var93(x)), var80(x), Not(var250(x)), Not(var149(x))))),
	ForAll([x], Not(Or(Not(var326(x)), var474(x), Not(var425(x)), var479(x)))),
	ForAll([x], Not(Or(var212(x), var45(x), var123(x), var356(x)))),
	ForAll([x], Not(Or(Not(var390(x)), Not(var420(x)), var76(x), var220(x)))),
	ForAll([x], Not(Or(Not(var102(x)), Not(var435(x)), Not(var17(x)), Not(var229(x))))),
	ForAll([x], Not(Or(var266(x), var62(x), var111(x), var44(x)))),
	ForAll([x], Not(Or(var63(x), var52(x), var18(x), Not(var53(x))))),
	ForAll([x], Not(Or(var99(x), var284(x), var462(x), Not(var14(x))))),
	ForAll([x], Not(Or(Not(var212(x)), Not(var52(x)), Not(var389(x)), var85(x)))),
	ForAll([x], Not(Or(var317(x), var412(x), Not(var93(x)), Not(var123(x))))),
	ForAll([x], Not(Or(Not(var447(x)), var307(x), Not(var320(x)), var282(x)))),
	ForAll([x], Not(Or(var208(x), var3(x), var213(x), Not(var467(x))))),
	ForAll([x], Not(Or(var58(x), Not(var156(x)), Not(var62(x)), var7(x)))),
	ForAll([x], Not(Or(Not(var293(x)), Not(var427(x)), var116(x), Not(var128(x))))),
	ForAll([x], Not(Or(var299(x), Not(var102(x)), Not(var356(x)), var308(x)))),
	ForAll([x], Not(Or(Not(var326(x)), var211(x), Not(var182(x)), var43(x)))),
	ForAll([x], Not(Or(Not(var451(x)), Not(var56(x)), var143(x), var417(x)))),
	ForAll([x], Not(Or(Not(var33(x)), Not(var73(x)), var469(x), Not(var107(x))))),
	ForAll([x], Not(Or(var330(x), var341(x), var321(x), Not(var455(x))))),
	ForAll([x], Not(Or(var160(x), Not(var493(x)), Not(var252(x)), Not(var152(x))))),
	ForAll([x], Not(Or(Not(var480(x)), Not(var464(x)), var192(x), Not(var449(x))))),
	ForAll([x], Not(Or(Not(var363(x)), Not(var462(x)), var446(x), Not(var468(x))))),
	ForAll([x], Not(Or(var87(x), Not(var365(x)), var114(x), var178(x)))),
	ForAll([x], Not(Or(var450(x), var144(x), var243(x), var216(x)))),
	ForAll([x], Not(Or(var373(x), var193(x), var464(x), Not(var378(x))))),
	ForAll([x], Not(Or(Not(var192(x)), var356(x), Not(var279(x)), var257(x)))),
	ForAll([x], Not(Or(Not(var436(x)), Not(var10(x)), Not(var133(x)), var159(x)))),
	ForAll([x], Not(Or(Not(var161(x)), var352(x), var122(x), var408(x)))),
	ForAll([x], Not(Or(Not(var250(x)), Not(var154(x)), Not(var56(x)), var197(x)))),
	ForAll([x], Not(Or(Not(var52(x)), var479(x), var22(x), var491(x)))),
	ForAll([x], Not(Or(Not(var270(x)), Not(var344(x)), var177(x), var88(x)))),
	ForAll([x], Not(Or(Not(var203(x)), Not(var18(x)), var346(x), var302(x)))),
	ForAll([x], Not(Or(var39(x), var106(x), Not(var218(x)), var391(x)))),
	ForAll([x], Not(Or(Not(var278(x)), var492(x), var224(x), Not(var1(x))))),
	ForAll([x], Not(Or(var441(x), Not(var373(x)), var122(x), var437(x)))),
	ForAll([x], Not(Or(Not(var278(x)), Not(var93(x)), var17(x), var3(x)))),
	ForAll([x], Not(Or(Not(var230(x)), var350(x), Not(var362(x)), var6(x)))),
	ForAll([x], Not(Or(Not(var191(x)), Not(var169(x)), Not(var312(x)), var344(x)))),
	ForAll([x], Not(Or(Not(var377(x)), Not(var362(x)), var141(x), var451(x)))),
	ForAll([x], Not(Or(var155(x), var492(x), var176(x), Not(var319(x))))),
	ForAll([x], Not(Or(Not(var62(x)), Not(var189(x)), Not(var234(x)), Not(var435(x))))),
	ForAll([x], Not(Or(var399(x), Not(var481(x)), var490(x), var200(x)))),
	ForAll([x], Not(Or(Not(var236(x)), var386(x), var270(x), var334(x)))),
	ForAll([x], Not(Or(var110(x), var465(x), Not(var417(x)), var361(x)))),
	ForAll([x], Not(Or(Not(var261(x)), var393(x), Not(var118(x)), Not(var16(x))))),
	ForAll([x], Not(Or(var407(x), var480(x), var58(x), Not(var331(x))))),
	ForAll([x], Not(Or(Not(var33(x)), Not(var166(x)), var198(x), var5(x)))),
	ForAll([x], Not(Or(Not(var446(x)), var465(x), Not(var159(x)), var270(x)))),
	ForAll([x], Not(Or(var362(x), Not(var128(x)), Not(var65(x)), var468(x)))),
	ForAll([x], Not(Or(var77(x), Not(var426(x)), var444(x), Not(var448(x))))),
	ForAll([x], Not(Or(var55(x), var372(x), var392(x), Not(var50(x))))),
	ForAll([x], Not(Or(Not(var174(x)), var52(x), var424(x), Not(var479(x))))),
	ForAll([x], Not(Or(Not(var377(x)), Not(var236(x)), Not(var235(x)), var341(x)))),
	ForAll([x], Not(Or(var145(x), Not(var185(x)), var429(x), Not(var318(x))))),
	ForAll([x], Not(Or(var218(x), Not(var407(x)), Not(var118(x)), var474(x)))),
	ForAll([x], Not(Or(Not(var353(x)), Not(var360(x)), Not(var297(x)), var118(x)))),
	ForAll([x], Not(Or(Not(var452(x)), Not(var446(x)), Not(var388(x)), Not(var161(x))))),
	ForAll([x], Not(Or(var30(x), var114(x), Not(var275(x)), Not(var229(x))))),
	ForAll([x], Not(Or(Not(var396(x)), var485(x), var227(x), var216(x)))),
	ForAll([x], Not(Or(var164(x), Not(var432(x)), Not(var17(x)), var118(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var363(x1)), Or(Not(var105(x)), Not(var443(x)), var64(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var96(x1), Or(Not(var398(x)), var173(x), var201(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var8(x1), Or(var296(x), Not(var438(x)), Not(var152(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var285(x1), var234(x1), var480(x1)), var161(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var11(x1)), var300(x1), Not(var36(x1))), Not(var14(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var356(x1)), Not(var436(x1))), Or(var407(x), Not(var73(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var159(x1)), Or(var193(x), var47(x), var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var319(x1), Not(var377(x1)), Not(var370(x1))), Not(var297(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var379(x1), Not(var427(x1)), Not(var190(x1))), Not(var415(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var398(x1)), Not(var3(x1))), Or(var129(x), var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var163(x1), var355(x1)), Or(Not(var262(x)), var101(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var345(x1)), Or(var267(x), Not(var248(x)), Not(var490(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var430(x1), Not(var238(x1))), Or(Not(var500(x)), var372(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var289(x1), Or(var381(x), var259(x), Not(var151(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), Or(var85(x), Not(var327(x)), Not(var281(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var242(x1), Or(var76(x), var87(x), var139(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var401(x1)), var287(x1)), Or(Not(var358(x)), Not(var57(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var328(x1), var120(x1)), Or(var364(x), Not(var421(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var189(x1), Or(Not(var341(x)), Not(var363(x)), Not(var332(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var305(x1)), Not(var373(x1))), Or(var209(x), Not(var109(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var135(x1)), var113(x1), var437(x1)), var256(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var357(x1), Not(var142(x1))), Or(Not(var339(x)), var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var401(x1), Or(var402(x), Not(var270(x)), Not(var305(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var323(x1), Or(Not(var182(x)), Not(var404(x)), var245(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var152(x1)), Not(var437(x1)), Not(var350(x1))), Not(var178(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var487(x1)), var183(x1), var274(x1)), Not(var138(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var254(x1), Not(var195(x1)), Not(var9(x1))), var144(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var457(x1)), var66(x1)), Or(var215(x), Not(var175(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var450(x1)), Not(var1(x1))), Or(Not(var113(x)), var206(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var440(x1)), Not(var371(x1)), var309(x1)), Not(var123(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var169(x1)), Not(var472(x1))), Or(Not(var295(x)), Not(var212(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var470(x1)), var439(x1), Not(var422(x1))), Not(var113(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var83(x1)), Not(var440(x1))), Or(Not(var31(x)), Not(var278(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var183(x1)), Or(Not(var278(x)), Not(var232(x)), Not(var365(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var274(x1), Or(Not(var156(x)), var60(x), Not(var334(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var175(x1), Or(Not(var142(x)), Not(var173(x)), Not(var222(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var167(x1)), var451(x1), Not(var466(x1))), Not(var346(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var454(x1), Not(var93(x1)), Not(var418(x1))), var235(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var444(x1)), Or(Not(var37(x)), Not(var191(x)), Not(var344(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var371(x1)), var444(x1)), Or(var107(x), Not(var62(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var461(x1), Not(var125(x1))), Or(var364(x), var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var427(x1)), var417(x1)), Or(var65(x), Not(var15(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var113(x1), var486(x1), var389(x1)), Not(var491(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var233(x1), var425(x1), Not(var196(x1))), Not(var323(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var438(x1)), Not(var408(x1)), var256(x1)), var440(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var430(x1)), Not(var268(x1))), Or(var17(x), var15(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var132(x1), Or(var21(x), var272(x), Not(var399(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var441(x1), Or(Not(var234(x)), Not(var277(x)), Not(var409(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var236(x1), Or(var326(x), Not(var4(x)), var75(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var311(x1)), var62(x1), var338(x1)), var303(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var372(x1)), Or(Not(var217(x)), var1(x), Not(var469(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var191(x1), Not(var435(x1)), var275(x1)), Not(var239(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var303(x1), Or(Not(var343(x)), var122(x), Not(var254(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var465(x1), Or(Not(var304(x)), var462(x), Not(var124(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var232(x1), Or(Not(var18(x)), var304(x), var273(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var420(x1)), Or(Not(var96(x)), Not(var28(x)), var277(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var99(x1), Or(var195(x), var162(x), var124(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var484(x1), var161(x1)), Or(Not(var98(x)), var246(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var272(x1), Not(var304(x1))), Or(var306(x), Not(var375(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var89(x1)), var372(x1)), Or(Not(var345(x)), var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var164(x1)), Or(Not(var198(x)), Not(var448(x)), Not(var79(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var391(x1), Or(Not(var228(x)), Not(var420(x)), Not(var116(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var216(x1), Or(Not(var276(x)), var91(x), Not(var472(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var464(x1)), Or(var393(x), var463(x), Not(var479(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var157(x1)), Or(var467(x), Not(var355(x)), Not(var312(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var74(x1)), Or(Not(var253(x)), var2(x), var48(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var258(x1)), Or(Not(var53(x)), Not(var120(x)), var166(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var357(x1), Not(var345(x1))), Or(var223(x), var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var83(x1), Not(var95(x1)), var284(x1)), Not(var401(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var498(x1), Not(var26(x1))), Or(Not(var472(x)), Not(var245(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var177(x1), var101(x1), var22(x1)), Not(var364(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var492(x1)), Or(var365(x), Not(var135(x)), Not(var398(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var257(x1), Or(Not(var215(x)), Not(var8(x)), Not(var166(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var305(x1), Not(var439(x1)), Not(var240(x1))), var57(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var391(x1)), Not(var323(x1))), Or(var315(x), var245(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var219(x1)), Not(var488(x1)), Not(var162(x1))), Not(var427(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var278(x1), var27(x1), var282(x1)), var291(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var91(x1), Or(var93(x), var17(x), Not(var420(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var408(x1)), var430(x1), var3(x1)), Not(var379(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var84(x1)), Or(Not(var146(x)), var455(x), var371(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var297(x1)), var73(x1), Not(var251(x1))), Not(var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var246(x1)), var300(x1), var295(x1)), Not(var222(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var370(x1)), var390(x1), var201(x1)), var416(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var162(x1), Or(var237(x), Not(var317(x)), Not(var305(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var78(x1)), Not(var300(x1)), var88(x1)), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var405(x1)), Not(var118(x1))), Or(var126(x), Not(var299(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var152(x1)), var24(x1)), Or(Not(var117(x)), Not(var400(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var269(x1), Not(var50(x1)), var28(x1)), var116(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var257(x1), var262(x1)), Or(Not(var204(x)), Not(var338(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var453(x1), Not(var28(x1))), Or(var489(x), Not(var190(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var147(x1), Not(var483(x1))), Or(Not(var461(x)), Not(var286(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var486(x1), Or(Not(var200(x)), var381(x), var44(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var370(x1)), Not(var101(x1))), Or(var251(x), var463(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var76(x1), Or(Not(var223(x)), var407(x), var403(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var131(x1)), Not(var344(x1)), var31(x1)), Not(var113(x)))))),
	ForAll([x], Not(Or(Not(var469(x)), var315(x), Not(var40(x)), Not(var306(x)), Not(var297(x))))),
	ForAll([x], Not(Or(Not(var22(x)), Not(var498(x)), var20(x), var423(x), Not(var355(x))))),
	ForAll([x], Not(Or(Not(var421(x)), Not(var382(x)), var445(x), Not(var274(x)), var308(x)))),
	ForAll([x], Not(Or(var91(x), var453(x), Not(var89(x)), Not(var108(x)), var371(x)))),
	ForAll([x], Not(Or(Not(var346(x)), Not(var201(x)), Not(var168(x)), Not(var85(x)), Not(var368(x))))),
	ForAll([x], Not(Or(var155(x), var416(x), Not(var325(x)), Not(var217(x)), Not(var491(x))))),
	ForAll([x], Not(Or(var256(x), var316(x), var159(x), var204(x), Not(var448(x))))),
	ForAll([x], Not(Or(Not(var301(x)), Not(var177(x)), Not(var331(x)), var418(x), Not(var173(x))))),
	ForAll([x], Not(Or(Not(var415(x)), Not(var21(x)), Not(var25(x)), var481(x), var403(x)))),
	ForAll([x], Not(Or(var57(x), var321(x), Not(var273(x)), Not(var265(x)), Not(var175(x))))),
	ForAll([x], Not(Or(Not(var149(x)), Not(var54(x)), var202(x), Not(var487(x)), Not(var282(x))))),
	ForAll([x], Not(Or(var147(x), var215(x), Not(var312(x)), var37(x), Not(var104(x))))),
	ForAll([x], Not(Or(Not(var422(x)), var5(x), Not(var340(x)), var409(x), Not(var256(x))))),
	ForAll([x], Not(Or(Not(var163(x)), var377(x), var466(x), var304(x), Not(var237(x))))),
	ForAll([x], Not(Or(var101(x), var445(x), Not(var239(x)), var400(x), var250(x)))),
	ForAll([x], Not(Or(var119(x), Not(var222(x)), Not(var123(x)), Not(var92(x)), var409(x)))),
	ForAll([x], Not(Or(Not(var6(x)), Not(var381(x)), var402(x), var469(x), Not(var340(x))))),
	ForAll([x], Not(Or(Not(var370(x)), var15(x), Not(var60(x)), Not(var79(x)), Not(var292(x))))),
	ForAll([x], Not(Or(var184(x), var281(x), var491(x), Not(var469(x)), Not(var110(x))))),
	ForAll([x], Not(Or(Not(var318(x)), Not(var491(x)), var79(x), Not(var222(x)), var139(x)))),
	ForAll([x], Not(Or(var396(x), Not(var26(x)), var340(x), Not(var205(x)), Not(var327(x))))),
	ForAll([x], Not(Or(Not(var214(x)), Not(var324(x)), var343(x), var477(x), var51(x)))),
	ForAll([x], Not(Or(Not(var120(x)), var168(x), var409(x), var196(x), var158(x)))),
	ForAll([x], Not(Or(Not(var351(x)), var477(x), var7(x), var397(x), Not(var130(x))))),
	ForAll([x], Not(Or(var391(x), Not(var306(x)), Not(var453(x)), var488(x), var425(x)))),
	ForAll([x], Not(Or(var138(x), var422(x), var190(x), var316(x), var77(x)))),
	ForAll([x], Not(Or(var312(x), var189(x), Not(var151(x)), Not(var353(x)), var244(x)))),
	ForAll([x], Not(Or(Not(var333(x)), Not(var293(x)), Not(var74(x)), var283(x), Not(var433(x))))),
	ForAll([x], Not(Or(Not(var298(x)), Not(var169(x)), Not(var288(x)), Not(var364(x)), Not(var65(x))))),
	ForAll([x], Not(Or(var407(x), Not(var39(x)), var173(x), Not(var447(x)), Not(var25(x))))),
	ForAll([x], Not(Or(var272(x), var484(x), Not(var498(x)), Not(var441(x)), Not(var309(x))))),
	ForAll([x], Not(Or(Not(var320(x)), var329(x), var289(x), Not(var226(x)), Not(var54(x))))),
	ForAll([x], Not(Or(var362(x), Not(var202(x)), var188(x), Not(var331(x)), Not(var232(x))))),
	ForAll([x], Not(Or(Not(var383(x)), Not(var172(x)), var151(x), Not(var188(x)), var55(x)))),
	ForAll([x], Not(Or(var260(x), Not(var196(x)), var324(x), var189(x), var472(x)))),
	ForAll([x], Not(Or(var48(x), Not(var476(x)), var106(x), var160(x), Not(var313(x))))),
	ForAll([x], Not(Or(Not(var92(x)), var280(x), Not(var467(x)), Not(var263(x)), var219(x)))),
	ForAll([x], Not(Or(var108(x), var292(x), Not(var82(x)), var109(x), var14(x)))),
	ForAll([x], Not(Or(Not(var477(x)), var3(x), Not(var170(x)), var70(x), var332(x)))),
	ForAll([x], Not(Or(var420(x), var288(x), Not(var71(x)), var200(x), var390(x)))),
	ForAll([x], Not(Or(Not(var183(x)), var161(x), Not(var255(x)), var411(x), Not(var466(x))))),
	ForAll([x], Not(Or(var345(x), var495(x), Not(var272(x)), Not(var334(x)), var238(x)))),
	ForAll([x], Not(Or(var447(x), Not(var416(x)), var430(x), Not(var24(x)), var63(x)))),
	ForAll([x], Not(Or(var5(x), var361(x), var441(x), var446(x), var479(x)))),
	ForAll([x], Not(Or(Not(var114(x)), Not(var458(x)), var68(x), Not(var130(x)), Not(var27(x))))),
	ForAll([x], Not(Or(var113(x), var297(x), var171(x), var182(x), Not(var436(x))))),
	ForAll([x], Not(Or(var223(x), Not(var217(x)), Not(var28(x)), var215(x), Not(var13(x))))),
	ForAll([x], Not(Or(var225(x), Not(var433(x)), Not(var388(x)), Not(var80(x)), Not(var121(x))))),
	ForAll([x], Not(Or(Not(var336(x)), Not(var104(x)), Not(var96(x)), var174(x), var383(x)))),
	ForAll([x], Not(Or(Not(var465(x)), Not(var172(x)), Not(var450(x)), Not(var391(x)), Not(var203(x))))),
	ForAll([x], Not(Or(var453(x), var74(x), Not(var371(x)), Not(var104(x)), Not(var212(x))))),
	ForAll([x], Not(Or(var353(x), Not(var221(x)), var281(x), var49(x), var381(x)))),
	ForAll([x], Not(Or(var310(x), var1(x), var257(x), Not(var400(x)), Not(var274(x))))),
	ForAll([x], Not(Or(Not(var138(x)), var292(x), var163(x), var64(x), Not(var251(x))))),
	ForAll([x], Not(Or(var95(x), Not(var479(x)), var316(x), Not(var18(x)), var288(x)))),
	ForAll([x], Not(Or(Not(var491(x)), Not(var281(x)), Not(var222(x)), Not(var466(x)), var299(x)))),
	ForAll([x], Not(Or(var361(x), var158(x), Not(var167(x)), var70(x), Not(var54(x))))),
	ForAll([x], Not(Or(Not(var342(x)), var69(x), var85(x), var194(x), var84(x)))),
	ForAll([x], Not(Or(Not(var436(x)), Not(var112(x)), Not(var482(x)), var126(x), var429(x)))),
	ForAll([x], Not(Or(var290(x), Not(var159(x)), var325(x), Not(var395(x)), Not(var164(x))))),
	ForAll([x], Not(Or(var330(x), var401(x), var23(x), var164(x), Not(var426(x))))),
	ForAll([x], Not(Or(Not(var227(x)), var209(x), var457(x), var220(x), Not(var233(x))))),
	ForAll([x], Not(Or(var66(x), Not(var477(x)), Not(var122(x)), Not(var263(x)), var453(x)))),
	ForAll([x], Not(Or(var459(x), Not(var414(x)), Not(var155(x)), Not(var66(x)), var341(x)))),
	ForAll([x], Not(Or(var40(x), var98(x), Not(var466(x)), var190(x), Not(var426(x))))),
	ForAll([x], Not(Or(Not(var261(x)), var454(x), var130(x), var265(x), Not(var498(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var179(x1), var457(x1), var227(x1)), Or(Not(var134(x)), Not(var282(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var194(x1), Or(Not(var320(x)), Not(var184(x)), var103(x), Not(var119(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var350(x1)), Or(var467(x), Not(var482(x)), var213(x), Not(var120(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var214(x1)), Not(var384(x1)), var462(x1), var237(x1)), Not(var170(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var426(x1)), var286(x1), var154(x1), var97(x1)), var38(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var345(x1)), var362(x1), var224(x1), Not(var47(x1))), Not(var44(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var360(x1), Or(var81(x), var216(x), var319(x), var168(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var282(x1)), var496(x1), Not(var38(x1)), var406(x1)), var331(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var403(x1)), Or(Not(var441(x)), Not(var102(x)), var275(x), var244(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var412(x1)), Not(var387(x1)), var377(x1)), Or(Not(var162(x)), var346(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var361(x1)), var341(x1), var27(x1), var123(x1)), var207(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var430(x1)), var42(x1), Not(var285(x1))), Or(var214(x), Not(var454(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var134(x1)), var104(x1), var421(x1), Not(var31(x1))), var203(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var102(x1)), Or(Not(var202(x)), var70(x), Not(var293(x)), Not(var486(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var308(x1), Not(var25(x1)), Not(var302(x1))), Or(var85(x), var338(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var77(x1)), var233(x1), var319(x1)), Or(Not(var242(x)), Not(var491(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var485(x1), var254(x1)), Or(var379(x), Not(var223(x)), var118(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var441(x1)), var116(x1)), Or(var52(x), var392(x), Not(var338(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var225(x1), var459(x1)), Or(Not(var207(x)), Not(var347(x)), var51(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var144(x1), Not(var306(x1))), Or(var454(x), var310(x), var470(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var167(x1), var42(x1)), Or(Not(var276(x)), Not(var482(x)), var113(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var474(x1), Not(var463(x1))), Or(Not(var119(x)), Not(var328(x)), Not(var266(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var20(x1), Or(Not(var308(x)), var123(x), var223(x), var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var356(x1), var226(x1)), Or(var434(x), var469(x), Not(var82(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var338(x1)), Or(var9(x), var438(x), var119(x), var73(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var352(x1)), var435(x1), var281(x1)), Or(Not(var108(x)), Not(var490(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var254(x1), Not(var349(x1)), Not(var146(x1)), var21(x1)), var382(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var211(x1)), Or(Not(var173(x)), Not(var485(x)), Not(var196(x)), Not(var397(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var483(x1)), Or(var285(x), var226(x), Not(var162(x)), Not(var2(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var324(x1)), var207(x1)), Or(var69(x), var102(x), Not(var461(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var228(x1), Or(Not(var454(x)), Not(var419(x)), Not(var301(x)), var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var373(x1), Not(var9(x1))), Or(Not(var287(x)), Not(var113(x)), var307(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var148(x1)), var272(x1)), Or(Not(var253(x)), Not(var187(x)), var109(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var138(x1)), Not(var37(x1)), Not(var179(x1))), Or(var125(x), Not(var396(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var53(x1), Not(var344(x1)), Not(var225(x1)), var172(x1)), Not(var401(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var400(x1), Not(var493(x1)), Not(var43(x1)), var474(x1)), Not(var101(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var415(x1)), Not(var145(x1)), Not(var12(x1)), Not(var61(x1))), Not(var488(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var120(x1)), Not(var362(x1)), Not(var387(x1)), var192(x1)), Not(var126(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var441(x1)), Or(Not(var494(x)), Not(var165(x)), Not(var450(x)), var259(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var244(x1)), Or(Not(var271(x)), var478(x), Not(var182(x)), Not(var247(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var490(x1), Or(var48(x), Not(var149(x)), var72(x), var402(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var315(x1), Or(Not(var426(x)), var456(x), Not(var93(x)), Not(var434(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var291(x1)), Not(var380(x1)), Not(var229(x1))), Or(var103(x), var306(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var348(x1), var280(x1), Not(var462(x1)), Not(var413(x1))), Not(var379(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var59(x1)), Not(var51(x1))), Or(var274(x), Not(var465(x)), var262(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var41(x1)), var24(x1), var275(x1), Not(var456(x1))), Not(var309(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var383(x1), var45(x1)), Or(Not(var42(x)), var35(x), Not(var255(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var202(x1), Or(Not(var377(x)), Not(var22(x)), var184(x), Not(var381(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var19(x1), Or(var292(x), var205(x), var387(x), Not(var56(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var166(x1), var331(x1), var182(x1)), Or(var455(x), Not(var333(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var59(x1), var104(x1), Not(var226(x1))), Or(Not(var14(x)), Not(var275(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var496(x1)), Not(var366(x1)), var191(x1)), Or(Not(var460(x)), var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var421(x1), var315(x1)), Or(Not(var454(x)), var234(x), Not(var133(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var260(x1), Not(var221(x1)), Not(var335(x1))), Or(Not(var100(x)), Not(var277(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var195(x1)), Not(var243(x1)), var175(x1)), Or(Not(var53(x)), var188(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var152(x1), Or(var253(x), var428(x), var112(x), Not(var450(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var65(x1)), Or(var131(x), Not(var245(x)), Not(var412(x)), var238(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var225(x1)), Or(Not(var413(x)), Not(var16(x)), Not(var19(x)), var238(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var217(x1), Not(var452(x1)), Not(var409(x1)), Not(var251(x1))), Not(var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var165(x1), var58(x1), Not(var13(x1)), Not(var374(x1))), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var114(x1), Or(var259(x), Not(var477(x)), var87(x), var356(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var286(x1)), Not(var78(x1)), var269(x1), var134(x1)), Not(var150(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var198(x1), var292(x1), Not(var62(x1))), Or(var115(x), var101(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var422(x1)), Or(var155(x), var194(x), var205(x), Not(var302(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var243(x1), var453(x1)), Or(var141(x), var281(x), var469(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var454(x1)), var206(x1), var334(x1)), Or(var85(x), var164(x)))))),
	ForAll([x], Not(Or(var324(x), Not(var211(x)), var230(x), var431(x), var51(x), var338(x)))),
	ForAll([x], Not(Or(var312(x), Not(var98(x)), var465(x), Not(var260(x)), var453(x), Not(var256(x))))),
	ForAll([x], Not(Or(Not(var91(x)), Not(var266(x)), var315(x), var157(x), var165(x), var206(x)))),
	ForAll([x], Not(Or(Not(var312(x)), var1(x), Not(var152(x)), Not(var426(x)), Not(var464(x)), var236(x)))),
	ForAll([x], Not(Or(var6(x), var451(x), Not(var296(x)), var479(x), Not(var399(x)), var145(x)))),
	ForAll([x], Not(Or(Not(var379(x)), Not(var97(x)), Not(var184(x)), var10(x), var351(x), Not(var213(x))))),
	ForAll([x], Not(Or(var56(x), var236(x), Not(var353(x)), Not(var62(x)), var97(x), Not(var117(x))))),
	ForAll([x], Not(Or(Not(var163(x)), Not(var268(x)), Not(var125(x)), var139(x), var238(x), var314(x)))),
	ForAll([x], Not(Or(var57(x), Not(var414(x)), Not(var457(x)), var396(x), Not(var278(x)), var386(x)))),
	ForAll([x], Not(Or(var345(x), var342(x), Not(var144(x)), Not(var57(x)), Not(var271(x)), var417(x)))),
	ForAll([x], Not(Or(Not(var87(x)), var321(x), var340(x), var73(x), Not(var76(x)), Not(var322(x))))),
	ForAll([x], Not(Or(var66(x), var218(x), Not(var36(x)), Not(var306(x)), var123(x), Not(var412(x))))),
	ForAll([x], Not(Or(Not(var424(x)), var481(x), var331(x), var161(x), var427(x), Not(var231(x))))),
	ForAll([x], Not(Or(var167(x), Not(var158(x)), var99(x), Not(var290(x)), var350(x), Not(var438(x))))),
	ForAll([x], Not(Or(Not(var467(x)), var275(x), var474(x), Not(var468(x)), var458(x), var390(x)))),
	ForAll([x], Not(Or(Not(var206(x)), var328(x), Not(var90(x)), var122(x), var5(x), Not(var126(x))))),
	ForAll([x], Not(Or(Not(var68(x)), var248(x), var228(x), Not(var384(x)), var492(x), Not(var145(x))))),
	ForAll([x], Not(Or(Not(var483(x)), var252(x), Not(var468(x)), var139(x), var289(x), Not(var86(x))))),
	ForAll([x], Not(Or(var227(x), var84(x), Not(var367(x)), Not(var257(x)), var274(x), var470(x)))),
	ForAll([x], Not(Or(Not(var56(x)), Not(var45(x)), var32(x), Not(var261(x)), Not(var119(x)), Not(var459(x))))),
	ForAll([x], Not(Or(var375(x), var421(x), var87(x), Not(var270(x)), var453(x), var487(x)))),
	ForAll([x], Not(Or(var39(x), Not(var237(x)), Not(var391(x)), Not(var340(x)), Not(var96(x)), Not(var58(x))))),
	ForAll([x], Not(Or(Not(var409(x)), var477(x), var58(x), var325(x), var101(x), var172(x)))),
	ForAll([x], Not(Or(Not(var332(x)), Not(var29(x)), Not(var226(x)), Not(var454(x)), Not(var478(x)), Not(var194(x))))),
	ForAll([x], Not(Or(Not(var459(x)), Not(var306(x)), Not(var315(x)), Not(var58(x)), Not(var176(x)), var208(x)))),
	ForAll([x], Not(Or(var93(x), Not(var53(x)), Not(var394(x)), Not(var43(x)), var284(x), var266(x)))),
	ForAll([x], Not(Or(var66(x), Not(var427(x)), var61(x), var161(x), var193(x), Not(var413(x))))),
	ForAll([x], Not(Or(var429(x), var493(x), Not(var301(x)), var368(x), var468(x), Not(var36(x))))),
	ForAll([x], Not(Or(var95(x), var170(x), var357(x), Not(var47(x)), var274(x), Not(var485(x))))),
	ForAll([x], Not(Or(var374(x), var117(x), var425(x), Not(var309(x)), Not(var238(x)), var135(x)))),
	ForAll([x], Not(Or(Not(var335(x)), var53(x), var248(x), var15(x), var184(x), var67(x)))),
	ForAll([x], Not(Or(var441(x), Not(var480(x)), var284(x), var73(x), var118(x), Not(var425(x))))),
	ForAll([x], Not(Or(Not(var302(x)), Not(var312(x)), var182(x), var372(x), var150(x), Not(var248(x))))),
	ForAll([x], Not(Or(var414(x), var384(x), var287(x), Not(var164(x)), Not(var152(x)), var30(x)))),
	ForAll([x], Not(Or(var430(x), var315(x), Not(var176(x)), Not(var4(x)), var102(x), Not(var143(x))))),
	ForAll([x], Not(Or(var216(x), var444(x), Not(var266(x)), Not(var64(x)), var277(x), Not(var13(x))))),
	ForAll([x], Not(Or(Not(var483(x)), var138(x), var380(x), Not(var240(x)), var33(x), var133(x)))),
	ForAll([x], Not(Or(Not(var310(x)), Not(var292(x)), var10(x), var276(x), var433(x), Not(var204(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var426(x1), Not(var277(x1)), var405(x1)), Or(var205(x), var489(x), var240(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var348(x1)), var389(x1), var90(x1), Not(var113(x1))), Or(var79(x), Not(var84(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var229(x1), Or(Not(var376(x)), var135(x), Not(var367(x)), Not(var89(x)), Not(var374(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var301(x1), Not(var499(x1)), Not(var238(x1))), Or(Not(var175(x)), Not(var130(x)), Not(var217(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var362(x1), Not(var323(x1)), Not(var29(x1))), Or(var140(x), var145(x), var43(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var480(x1)), var370(x1), var198(x1)), Or(var234(x), var230(x), Not(var286(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var454(x1)), Or(Not(var410(x)), var76(x), var231(x), Not(var349(x)), var414(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var349(x1), Not(var429(x1)), var126(x1)), Or(var436(x), var374(x), var320(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var150(x1)), var317(x1)), Or(Not(var218(x)), Not(var174(x)), Not(var139(x)), var224(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var161(x1)), Not(var47(x1)), var226(x1)), Or(Not(var338(x)), var225(x), Not(var475(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var347(x1)), Not(var49(x1))), Or(var206(x), var104(x), var176(x), var220(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var17(x1)), Or(var238(x), var473(x), Not(var366(x)), var259(x), Not(var295(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var279(x1), Or(var465(x), Not(var495(x)), var133(x), var441(x), var159(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var388(x1), var247(x1), Not(var477(x1))), Or(Not(var377(x)), var196(x), var25(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var278(x1)), Not(var357(x1)), var292(x1), Not(var17(x1)), var260(x1)), var102(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var463(x1)), var483(x1), var283(x1)), Or(Not(var10(x)), var372(x), var320(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var253(x1), var493(x1), Not(var405(x1)), Not(var273(x1))), Or(Not(var220(x)), Not(var53(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var36(x1)), Or(Not(var45(x)), Not(var314(x)), var282(x), var353(x), Not(var7(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var103(x1), Or(Not(var471(x)), Not(var189(x)), var169(x), Not(var37(x)), var159(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var215(x1), var353(x1), Not(var392(x1))), Or(Not(var489(x)), var194(x), var442(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var277(x1), var218(x1), var458(x1), var435(x1)), Or(var198(x), Not(var293(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var473(x1), Or(Not(var484(x)), Not(var479(x)), Not(var488(x)), Not(var305(x)), var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var211(x1)), var256(x1), Not(var428(x1)), Not(var373(x1)), Not(var260(x1))), var232(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var474(x1)), var272(x1), var475(x1), Not(var432(x1))), Or(Not(var333(x)), Not(var259(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var390(x1), var296(x1), var492(x1), var362(x1)), Or(var408(x), Not(var31(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var72(x1)), Or(var122(x), var386(x), var219(x), Not(var203(x)), var334(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var82(x1), var497(x1), Not(var179(x1))), Or(var30(x), Not(var160(x)), var334(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var455(x1)), Not(var77(x1)), var483(x1), Not(var474(x1)), var257(x1)), Not(var463(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var257(x1)), Not(var269(x1)), Not(var10(x1))), Or(Not(var160(x)), Not(var233(x)), Not(var388(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var368(x1), var302(x1)), Or(Not(var397(x)), Not(var153(x)), var250(x), Not(var235(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var408(x1)), var69(x1), var400(x1), Not(var491(x1))), Or(Not(var145(x)), Not(var46(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var163(x1)), Or(Not(var287(x)), var244(x), var165(x), Not(var92(x)), var473(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var68(x1), Not(var461(x1)), Not(var447(x1))), Or(Not(var229(x)), var494(x), var85(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var147(x1), Or(Not(var190(x)), var82(x), var329(x), var64(x), Not(var392(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var259(x1), var170(x1), var8(x1)), Or(Not(var431(x)), Not(var374(x)), var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var494(x1)), var59(x1), Not(var274(x1)), var61(x1)), Or(var372(x), Not(var368(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var497(x1)), var399(x1), var199(x1)), Or(Not(var444(x)), Not(var276(x)), Not(var83(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var465(x1), var182(x1), var160(x1), Not(var19(x1)), Not(var478(x1))), var423(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var28(x1), var267(x1), Not(var176(x1)), var182(x1), var229(x1)), var324(x))))),
	ForAll([x], Not(Or(Not(var55(x)), var242(x), Not(var295(x)), var189(x), var266(x), Not(var451(x)), var220(x)))),
	ForAll([x], Not(Or(var289(x), Not(var466(x)), Not(var123(x)), Not(var317(x)), Not(var462(x)), Not(var120(x)), var78(x)))),
	ForAll([x], Not(Or(var472(x), Not(var452(x)), var263(x), Not(var365(x)), var329(x), var178(x), var474(x)))),
	ForAll([x], Not(Or(Not(var74(x)), var289(x), var177(x), Not(var308(x)), Not(var415(x)), var226(x), Not(var413(x))))),
	ForAll([x], Not(Or(Not(var75(x)), Not(var442(x)), var373(x), Not(var208(x)), var196(x), var347(x), Not(var365(x))))),
	ForAll([x], Not(Or(var11(x), var40(x), Not(var43(x)), var316(x), var469(x), Not(var126(x)), Not(var220(x))))),
	ForAll([x], Not(Or(Not(var314(x)), Not(var432(x)), Not(var163(x)), var61(x), var390(x), var37(x), Not(var288(x))))),
	ForAll([x], Not(Or(var184(x), Not(var140(x)), var396(x), var104(x), Not(var189(x)), Not(var169(x)), Not(var78(x))))),
	ForAll([x], Not(Or(var286(x), Not(var116(x)), Not(var463(x)), var253(x), Not(var323(x)), Not(var358(x)), Not(var266(x))))),
	ForAll([x], Not(Or(Not(var465(x)), Not(var269(x)), Not(var315(x)), Not(var492(x)), var499(x), Not(var268(x)), var243(x)))),
	ForAll([x], Not(Or(var97(x), var333(x), Not(var386(x)), var391(x), Not(var203(x)), var313(x), Not(var440(x))))),
	ForAll([x], Not(Or(var102(x), var437(x), Not(var429(x)), Not(var459(x)), Not(var45(x)), Not(var33(x)), var85(x)))),
	ForAll([x], Not(Or(var83(x), Not(var107(x)), Not(var492(x)), Not(var293(x)), Not(var281(x)), Not(var279(x)), var498(x)))),
	ForAll([x], Not(Or(var226(x), var13(x), var437(x), var340(x), Not(var396(x)), var352(x), var488(x)))),
	ForAll([x], Not(Or(var40(x), Not(var271(x)), var452(x), var252(x), var447(x), Not(var223(x)), Not(var10(x))))),
	ForAll([x], Not(Or(var18(x), var397(x), Not(var33(x)), var439(x), var322(x), var225(x), Not(var261(x))))),
	ForAll([x], Not(Or(var339(x), var343(x), Not(var456(x)), Not(var229(x)), Not(var345(x)), var445(x), var56(x)))),
	ForAll([x], Not(Or(var412(x), var371(x), Not(var417(x)), Not(var292(x)), var243(x), var309(x), var394(x)))),
	ForAll([x], Not(Or(Not(var138(x)), var180(x), Not(var237(x)), var434(x), var461(x), var238(x), var23(x)))),
	ForAll([x], Not(Or(Not(var141(x)), Not(var432(x)), var396(x), Not(var11(x)), var112(x), Not(var365(x)), var103(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var396(x1)), var9(x1), Not(var242(x1)), var442(x1)), Or(var155(x), var434(x), var386(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var148(x1), var184(x1)), Or(Not(var197(x)), var357(x), var312(x), var153(x), Not(var24(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var310(x1)), Or(var176(x), var481(x), var383(x), var40(x), var295(x), var7(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var138(x1)), var363(x1)), Or(var408(x), var279(x), Not(var10(x)), var218(x), var236(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var353(x1), Not(var228(x1)), var37(x1)), Or(var88(x), Not(var162(x)), Not(var54(x)), var418(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var417(x1), Not(var43(x1)), var314(x1), Not(var33(x1)), Not(var86(x1))), Or(Not(var99(x)), var368(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var268(x1), Or(Not(var35(x)), var120(x), Not(var457(x)), var290(x), Not(var159(x)), var497(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var463(x1), Not(var94(x1)), var225(x1)), Or(Not(var428(x)), Not(var25(x)), Not(var480(x)), Not(var246(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var493(x1)), Not(var433(x1))), Or(var442(x), Not(var81(x)), Not(var25(x)), Not(var112(x)), Not(var1(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var34(x1), var190(x1), Not(var418(x1)), Not(var100(x1)), Not(var300(x1))), Or(Not(var426(x)), var18(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), Or(var30(x), var488(x), Not(var80(x)), Not(var53(x)), Not(var343(x)), Not(var400(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var219(x1), Not(var234(x1))), Or(var404(x), var64(x), Not(var355(x)), Not(var16(x)), var364(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var197(x1), var77(x1), var328(x1), var163(x1)), Or(var325(x), var126(x), var88(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var467(x1)), var295(x1), var56(x1), Not(var395(x1))), Or(var479(x), Not(var105(x)), var227(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var392(x1), var415(x1), var14(x1), var100(x1)), Or(Not(var186(x)), Not(var264(x)), var327(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var292(x1), Not(var433(x1))), Or(var76(x), Not(var44(x)), Not(var480(x)), Not(var331(x)), var300(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var217(x1)), Not(var293(x1)), Not(var379(x1)), Not(var339(x1)), var248(x1)), Or(var445(x), var410(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var41(x1)), var421(x1)), Or(Not(var279(x)), var171(x), Not(var415(x)), Not(var250(x)), var245(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var191(x1), var14(x1), var456(x1), Not(var32(x1)), var259(x1)), Or(var182(x), var56(x)))))),
	ForAll([x], Not(Or(Not(var192(x)), var216(x), var145(x), var484(x), var425(x), var245(x), Not(var194(x)), var101(x)))),
	ForAll([x], Not(Or(var300(x), var457(x), var423(x), var267(x), var477(x), Not(var360(x)), Not(var348(x)), var162(x)))),
	ForAll([x], Not(Or(Not(var486(x)), var245(x), var21(x), var474(x), var383(x), var249(x), var115(x), Not(var209(x))))),
	ForAll([x], Not(Or(Not(var129(x)), Not(var238(x)), Not(var73(x)), Not(var106(x)), var354(x), Not(var198(x)), Not(var29(x)), Not(var322(x))))),
	ForAll([x], Not(Or(Not(var72(x)), var178(x), Not(var108(x)), Not(var173(x)), Not(var226(x)), var127(x), Not(var154(x)), Not(var444(x))))),
	ForAll([x], Not(Or(var248(x), Not(var445(x)), var408(x), Not(var334(x)), var132(x), var22(x), var338(x), var481(x)))),
	ForAll([x], Not(Or(Not(var397(x)), Not(var200(x)), Not(var68(x)), Not(var174(x)), var302(x), Not(var415(x)), Not(var301(x)), Not(var385(x))))),
	ForAll([x], Not(Or(Not(var436(x)), var488(x), var486(x), Not(var131(x)), Not(var91(x)), Not(var139(x)), Not(var465(x)), var106(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var352(x1), var52(x1)), Or(Not(var367(x)), var424(x), var267(x), var142(x), Not(var217(x)), var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var118(x1), Not(var399(x1)), var329(x1), Not(var71(x1)), var361(x1)), Or(Not(var45(x)), Not(var456(x)), var208(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var256(x1)), var417(x1), var103(x1), var38(x1), var244(x1), Not(var442(x1)), Not(var434(x1))), Not(var397(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var447(x1), Not(var343(x1)), var36(x1), Not(var255(x1)), var319(x1), Not(var162(x1)), var462(x1)), var185(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var473(x1), var429(x1)), Or(var474(x), Not(var252(x)), var297(x), var323(x), Not(var113(x)), var415(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var126(x1)), var53(x1), Not(var66(x1)), var315(x1), var243(x1), var118(x1), var176(x1)), var450(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var58(x1), Not(var469(x1)), Not(var126(x1)), var225(x1), var315(x1), Not(var75(x1)), Not(var337(x1))), var160(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var297(x1), Not(var157(x1)), Not(var314(x1)), var139(x1), var187(x1), var430(x1), Not(var302(x1))), var168(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var42(x1)), Not(var465(x1)), var199(x1)), Or(var325(x), Not(var321(x)), Not(var62(x)), var82(x), var307(x)))))),
	ForAll([x], Not(Or(Not(var208(x)), var133(x), Not(var199(x)), var75(x), Not(var421(x)), Not(var15(x)), Not(var161(x)), Not(var129(x)), var271(x)))),
	ForAll([x], Not(Or(var120(x), var202(x), Not(var166(x)), Not(var49(x)), var115(x), var29(x), var255(x), var325(x), var317(x)))),
	ForAll([x], Not(Or(var223(x), Not(var492(x)), Not(var232(x)), var318(x), var188(x), var130(x), Not(var261(x)), Not(var202(x)), var462(x)))),
	ForAll([x], Not(Or(Not(var132(x)), Not(var311(x)), Not(var209(x)), Not(var177(x)), var272(x), var329(x), var429(x), Not(var400(x)), Not(var353(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var417(x1)), var349(x1), Not(var405(x1)), var370(x1), var8(x1), Not(var124(x1)), var485(x1), var358(x1)), Not(var396(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var486(x1), var300(x1)), Or(Not(var382(x)), var252(x), Not(var363(x)), Not(var411(x)), Not(var7(x)), var255(x), var426(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var216(x1), Not(var106(x1))), Or(Not(var21(x)), Not(var474(x)), Not(var305(x)), var479(x), var398(x), Not(var65(x)), Not(var210(x))))))),
	ForAll([x], Not(Or(Not(var500(x)), Not(var254(x)), Not(var156(x)), Not(var293(x)), var479(x), var8(x), Not(var5(x)), var274(x), Not(var300(x)), Not(var191(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var226(x1)), Not(var366(x1)), Not(var42(x1)), Not(var374(x1)), Not(var333(x1)), Not(var290(x1)), Not(var385(x1)), Not(var110(x1))), Or(Not(var91(x)), Not(var11(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var371(x1), Or(Not(var68(x)), Not(var251(x)), Not(var123(x)), Not(var393(x)), Not(var471(x)), var248(x), var280(x), var423(x), Not(var29(x)), var271(x)))))),
	ForAll([x], Not(Or(var359(x), var164(x), Not(var171(x)), var467(x), Not(var7(x)), var362(x), Not(var54(x)), var36(x)))),
	ForAll([x], Not(Or(Not(var490(x)), var7(x), Not(var341(x)), Not(var445(x)), Not(var12(x)), var269(x), var108(x), Not(var101(x)), Not(var410(x)), var287(x), Not(var233(x))))),
	ForAll([x], Not(Or(var406(x), Not(var183(x)), Not(var402(x)), var1(x), var373(x), var447(x)))),
	ForAll([x], Not(Or(Not(var53(x)), var100(x), Not(var497(x)), var242(x), var452(x), Not(var282(x)), Not(var198(x)), var158(x), var59(x)))),
	ForAll([x], Not(Or(Not(var4(x)), var245(x), Not(var353(x)), var103(x)))),
	ForAll([x], Not(Or(var103(x), var230(x), var385(x)))),
	ForAll([x], Not(Or(var132(x), Not(var245(x)), Not(var44(x)), var274(x), Not(var109(x)), var436(x)))),
	ForAll([x], Not(Not(var237(x)))),
	ForAll([x], Not(Or(var438(x), Not(var56(x)), Not(var232(x))))),
	ForAll([x], Not(Or(Not(var363(x)), var38(x), var237(x), Not(var232(x)), Not(var105(x)), Not(var99(x)), Not(var304(x)), Not(var294(x)), Not(var357(x)), Not(var376(x)), Not(var70(x))))),
	ForAll([x], Not(Or(var146(x), var86(x), Not(var151(x)), Not(var372(x)), Not(var177(x)), var222(x), var180(x), var386(x)))),
	ForAll([x], Not(Or(Not(var174(x)), Not(var374(x)), var146(x), Not(var401(x)), var164(x), Not(var485(x)), var446(x), var258(x), var489(x), Not(var268(x))))),
	ForAll([x], Not(Not(var346(x)))),
	ForAll([x], Not(Or(var394(x), var395(x), Not(var43(x)), var6(x), Not(var472(x)), Not(var248(x)), Not(var2(x)), var279(x)))),
	ForAll([x], Not(Or(Not(var292(x)), Not(var52(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var28(x1)), Not(var86(x1))), Or(Not(var167(x)), Not(var463(x)), Not(var381(x)), Not(var201(x)), Not(var204(x)), Not(var210(x)), var118(x), var72(x), var57(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var405(x1), var217(x1), var494(x1), var213(x1), Not(var351(x1)), var47(x1), Not(var81(x1)), var255(x1), var269(x1), Not(var32(x1))), Not(var474(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var457(x1), var409(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var188(x1)), Or(var187(x), var204(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var432(x1), Not(var34(x1))), Or(Not(var408(x)), Not(var445(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var400(x1), Not(var336(x1))), Or(Not(var117(x)), Not(var297(x)), Not(var408(x)), Not(var139(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var376(x1), Not(var371(x1)), var255(x1), Not(var389(x1))), Or(Not(var312(x)), Not(var123(x)), Not(var220(x)), Not(var200(x)), Not(var219(x)), Not(var58(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var149(x1)), Not(var440(x1)), var427(x1), var417(x1), var343(x1), Not(var84(x1)), Not(var283(x1)), var95(x1)), Or(Not(var324(x)), Not(var489(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var124(x1)), var105(x1), var79(x1)), Or(var265(x), Not(var83(x)), var167(x), Not(var190(x)), Not(var18(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var295(x1), Not(var432(x1)), Not(var33(x1)), Not(var235(x1)), Not(var58(x1)), var232(x1), var343(x1), var468(x1)), Or(Not(var263(x)), var445(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var302(x1)), Or(var40(x), Not(var389(x)), Not(var258(x)), Not(var327(x)), Not(var404(x)), Not(var184(x)), var287(x), var347(x), Not(var362(x)), var312(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var162(x1), var420(x1), Not(var222(x1)), var149(x1), var294(x1), var490(x1), var18(x1), Not(var411(x1))), Or(var156(x), Not(var205(x)), var375(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var420(x1)), var153(x1), var10(x1), Not(var336(x1)), var155(x1), Not(var404(x1)), Not(var435(x1)), var292(x1), Not(var300(x1))), Or(Not(var464(x)), var448(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var126(x1), var361(x1)), Or(Not(var117(x)), Not(var42(x)), Not(var397(x)), var150(x), Not(var470(x)), var426(x), var44(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())