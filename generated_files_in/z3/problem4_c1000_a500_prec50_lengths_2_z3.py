from z3 import *

Object = DeclareSort('Object')

var195 = Function('var195', Object, BoolSort())
var492 = Function('var492', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var313 = Function('var313', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var481 = Function('var481', Object, BoolSort())
var425 = Function('var425', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var476 = Function('var476', Object, BoolSort())
var458 = Function('var458', Object, BoolSort())
var471 = Function('var471', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var477 = Function('var477', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var497 = Function('var497', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var308 = Function('var308', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var390 = Function('var390', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var500 = Function('var500', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var386 = Function('var386', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var483 = Function('var483', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var424 = Function('var424', Object, BoolSort())
var378 = Function('var378', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var403 = Function('var403', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var429 = Function('var429', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var475 = Function('var475', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var484 = Function('var484', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var348 = Function('var348', Object, BoolSort())
var408 = Function('var408', Object, BoolSort())
var411 = Function('var411', Object, BoolSort())
var422 = Function('var422', Object, BoolSort())
var371 = Function('var371', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var490 = Function('var490', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var486 = Function('var486', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var474 = Function('var474', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var414 = Function('var414', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var356 = Function('var356', Object, BoolSort())
var416 = Function('var416', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var482 = Function('var482', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var404 = Function('var404', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var467 = Function('var467', Object, BoolSort())
var453 = Function('var453', Object, BoolSort())
var367 = Function('var367', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var391 = Function('var391', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var369 = Function('var369', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var432 = Function('var432', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var493 = Function('var493', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var466 = Function('var466', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var276 = Function('var276', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var401 = Function('var401', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var307 = Function('var307', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var349 = Function('var349', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var463 = Function('var463', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var451 = Function('var451', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var469 = Function('var469', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var373 = Function('var373', Object, BoolSort())
var389 = Function('var389', Object, BoolSort())
var340 = Function('var340', Object, BoolSort())
var452 = Function('var452', Object, BoolSort())
var412 = Function('var412', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var437 = Function('var437', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var465 = Function('var465', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var438 = Function('var438', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var362 = Function('var362', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var431 = Function('var431', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var318 = Function('var318', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var413 = Function('var413', Object, BoolSort())
var354 = Function('var354', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var324 = Function('var324', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var421 = Function('var421', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var317 = Function('var317', Object, BoolSort())
var457 = Function('var457', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var441 = Function('var441', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var459 = Function('var459', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var350 = Function('var350', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var440 = Function('var440', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var487 = Function('var487', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var473 = Function('var473', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var405 = Function('var405', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var377 = Function('var377', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var379 = Function('var379', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var407 = Function('var407', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var460 = Function('var460', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var489 = Function('var489', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var445 = Function('var445', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var449 = Function('var449', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var494 = Function('var494', Object, BoolSort())
var269 = Function('var269', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var455 = Function('var455', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var472 = Function('var472', Object, BoolSort())
var372 = Function('var372', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var365 = Function('var365', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var406 = Function('var406', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var495 = Function('var495', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var479 = Function('var479', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var446 = Function('var446', Object, BoolSort())
var420 = Function('var420', Object, BoolSort())
var316 = Function('var316', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var410 = Function('var410', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var468 = Function('var468', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var454 = Function('var454', Object, BoolSort())
var430 = Function('var430', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var417 = Function('var417', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var485 = Function('var485', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var461 = Function('var461', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var434 = Function('var434', Object, BoolSort())
var309 = Function('var309', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var436 = Function('var436', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var335 = Function('var335', Object, BoolSort())
var402 = Function('var402', Object, BoolSort())
var439 = Function('var439', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var296 = Function('var296', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var418 = Function('var418', Object, BoolSort())
var442 = Function('var442', Object, BoolSort())
var498 = Function('var498', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var376 = Function('var376', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var385 = Function('var385', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var499 = Function('var499', Object, BoolSort())
var333 = Function('var333', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var395 = Function('var395', Object, BoolSort())
var396 = Function('var396', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var478 = Function('var478', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var323 = Function('var323', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var491 = Function('var491', Object, BoolSort())
var433 = Function('var433', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var364 = Function('var364', Object, BoolSort())
var423 = Function('var423', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var409 = Function('var409', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var426 = Function('var426', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var450 = Function('var450', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var419 = Function('var419', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var447 = Function('var447', Object, BoolSort())
var336 = Function('var336', Object, BoolSort())
var444 = Function('var444', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var306 = Function('var306', Object, BoolSort())
var456 = Function('var456', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var302 = Function('var302', Object, BoolSort())
var351 = Function('var351', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var488 = Function('var488', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var427 = Function('var427', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var435 = Function('var435', Object, BoolSort())
var448 = Function('var448', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var470 = Function('var470', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var428 = Function('var428', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var462 = Function('var462', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var398 = Function('var398', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var392 = Function('var392', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var443 = Function('var443', Object, BoolSort())
var496 = Function('var496', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms0 = [
	ForAll([x], Not(Or(Not(var195(x)), var492(x)))),
	ForAll([x], Not(Or(var366(x), Not(var313(x))))),
	ForAll([x], Not(Or(var78(x), var245(x)))),
	ForAll([x], Not(Or(var94(x), Not(var481(x))))),
	ForAll([x], Not(Or(var425(x), var112(x)))),
	ForAll([x], Not(Or(Not(var139(x)), Not(var249(x))))),
	ForAll([x], Not(Or(Not(var223(x)), var102(x)))),
	ForAll([x], Not(Or(Not(var76(x)), Not(var476(x))))),
	ForAll([x], Not(Or(Not(var458(x)), Not(var471(x))))),
	ForAll([x], Not(Or(var294(x), var65(x)))),
	ForAll([x], Not(Or(var132(x), Not(var42(x))))),
	ForAll([x], Not(Or(Not(var175(x)), Not(var256(x))))),
	ForAll([x], Not(Or(Not(var251(x)), Not(var4(x))))),
	ForAll([x], Not(Or(var8(x), var280(x)))),
	ForAll([x], Not(Or(Not(var195(x)), Not(var49(x))))),
	ForAll([x], Not(Or(var280(x), var360(x)))),
	ForAll([x], Not(Or(Not(var99(x)), Not(var477(x))))),
	ForAll([x], Not(Or(var258(x), var189(x)))),
	ForAll([x], Not(Or(var497(x), var381(x)))),
	ForAll([x], Not(Or(Not(var308(x)), Not(var347(x))))),
	ForAll([x], Not(Or(var366(x), Not(var47(x))))),
	ForAll([x], Not(Or(var87(x), Not(var16(x))))),
	ForAll([x], Not(Or(Not(var178(x)), var130(x)))),
	ForAll([x], Not(Or(var165(x), Not(var331(x))))),
	ForAll([x], Not(Or(var237(x), var390(x)))),
	ForAll([x], Not(Or(var66(x), Not(var216(x))))),
	ForAll([x], Not(Or(Not(var271(x)), var500(x)))),
	ForAll([x], Not(Or(var197(x), Not(var235(x))))),
	ForAll([x], Not(Or(var480(x), Not(var386(x))))),
	ForAll([x], Not(Or(Not(var116(x)), Not(var483(x))))),
	ForAll([x], Not(Or(var289(x), Not(var160(x))))),
	ForAll([x], Not(Or(Not(var90(x)), Not(var424(x))))),
	ForAll([x], Not(Or(Not(var331(x)), Not(var378(x))))),
	ForAll([x], Not(Or(var147(x), Not(var403(x))))),
	ForAll([x], Not(Or(Not(var368(x)), var429(x)))),
	ForAll([x], Not(Or(var341(x), var220(x)))),
	ForAll([x], Not(Or(Not(var63(x)), Not(var475(x))))),
	ForAll([x], Not(Or(var380(x), Not(var59(x))))),
	ForAll([x], Not(Or(Not(var484(x)), Not(var128(x))))),
	ForAll([x], Not(Or(Not(var500(x)), Not(var244(x))))),
	ForAll([x], Not(Or(var13(x), Not(var348(x))))),
	ForAll([x], Not(Or(Not(var271(x)), var408(x)))),
	ForAll([x], Not(Or(var13(x), var411(x)))),
	ForAll([x], Not(Or(var422(x), var371(x)))),
	ForAll([x], Not(Or(Not(var149(x)), var490(x)))),
	ForAll([x], Not(Or(var248(x), var486(x)))),
	ForAll([x], Not(Or(var140(x), var48(x)))),
	ForAll([x], Not(Or(Not(var474(x)), var153(x)))),
	ForAll([x], Not(Or(var263(x), var414(x)))),
	ForAll([x], Not(Or(Not(var58(x)), var339(x)))),
	ForAll([x], Not(Or(var252(x), var332(x)))),
	ForAll([x], Not(Or(Not(var266(x)), Not(var352(x))))),
	ForAll([x], Not(Or(Not(var89(x)), Not(var356(x))))),
	ForAll([x], Not(Or(Not(var175(x)), var416(x)))),
	ForAll([x], Not(Or(Not(var227(x)), Not(var273(x))))),
	ForAll([x], Not(Or(var8(x), var113(x)))),
	ForAll([x], Not(Or(Not(var193(x)), var24(x)))),
	ForAll([x], Not(Or(var416(x), Not(var482(x))))),
	ForAll([x], Not(Or(Not(var157(x)), Not(var244(x))))),
	ForAll([x], Not(Or(Not(var404(x)), var327(x)))),
	ForAll([x], Not(Or(Not(var152(x)), var128(x)))),
	ForAll([x], Not(Or(var467(x), Not(var453(x))))),
	ForAll([x], Not(Or(var367(x), Not(var329(x))))),
	ForAll([x], Not(Or(var391(x), var117(x)))),
	ForAll([x], Not(Or(var142(x), var497(x)))),
	ForAll([x], Not(Or(var287(x), var369(x)))),
	ForAll([x], Not(Or(Not(var45(x)), Not(var44(x))))),
	ForAll([x], Not(Or(Not(var219(x)), var322(x)))),
	ForAll([x], Not(Or(var321(x), Not(var374(x))))),
	ForAll([x], Not(Or(var8(x), Not(var357(x))))),
	ForAll([x], Not(Or(var60(x), Not(var432(x))))),
	ForAll([x], Not(Or(Not(var250(x)), var490(x)))),
	ForAll([x], Not(Or(Not(var493(x)), var186(x)))),
	ForAll([x], Not(Or(var348(x), var193(x)))),
	ForAll([x], Not(Or(Not(var250(x)), Not(var466(x))))),
	ForAll([x], Not(Or(Not(var129(x)), var194(x)))),
	ForAll([x], Not(Or(Not(var33(x)), Not(var301(x))))),
	ForAll([x], Not(Or(Not(var79(x)), Not(var276(x))))),
	ForAll([x], Not(Or(var34(x), Not(var203(x))))),
	ForAll([x], Not(Or(Not(var108(x)), var314(x)))),
	ForAll([x], Not(Or(Not(var401(x)), var159(x)))),
	ForAll([x], Not(Or(Not(var200(x)), Not(var184(x))))),
	ForAll([x], Not(Or(var66(x), Not(var346(x))))),
	ForAll([x], Not(Or(Not(var72(x)), var249(x)))),
	ForAll([x], Not(Or(var254(x), Not(var307(x))))),
	ForAll([x], Not(Or(var160(x), var384(x)))),
	ForAll([x], Not(Or(Not(var3(x)), var166(x)))),
	ForAll([x], Not(Or(Not(var349(x)), Not(var192(x))))),
	ForAll([x], Not(Or(var378(x), Not(var480(x))))),
	ForAll([x], Not(Or(Not(var165(x)), var91(x)))),
	ForAll([x], Not(Or(Not(var337(x)), var121(x)))),
	ForAll([x], Not(Or(var252(x), var73(x)))),
	ForAll([x], Not(Or(Not(var331(x)), var463(x)))),
	ForAll([x], Not(Or(Not(var98(x)), var451(x)))),
	ForAll([x], Not(Or(Not(var106(x)), Not(var161(x))))),
	ForAll([x], Not(Or(Not(var278(x)), var180(x)))),
	ForAll([x], Not(Or(Not(var469(x)), var295(x)))),
	ForAll([x], Not(Or(Not(var288(x)), var107(x)))),
	ForAll([x], Not(Or(Not(var283(x)), var288(x)))),
	ForAll([x], Not(Or(Not(var373(x)), var389(x)))),
	ForAll([x], Not(Or(var340(x), Not(var452(x))))),
	ForAll([x], Not(Or(Not(var412(x)), Not(var156(x))))),
	ForAll([x], Not(Or(Not(var380(x)), var187(x)))),
	ForAll([x], Not(Or(var437(x), var88(x)))),
	ForAll([x], Not(Or(Not(var103(x)), var255(x)))),
	ForAll([x], Not(Or(var480(x), var458(x)))),
	ForAll([x], Not(Or(var207(x), Not(var300(x))))),
	ForAll([x], Not(Or(Not(var248(x)), var165(x)))),
	ForAll([x], Not(Or(Not(var39(x)), Not(var411(x))))),
	ForAll([x], Not(Or(var465(x), var186(x)))),
	ForAll([x], Not(Or(Not(var315(x)), Not(var438(x))))),
	ForAll([x], Not(Or(var101(x), Not(var72(x))))),
	ForAll([x], Not(Or(var414(x), Not(var362(x))))),
	ForAll([x], Not(Or(var44(x), Not(var452(x))))),
	ForAll([x], Not(Or(var344(x), Not(var239(x))))),
	ForAll([x], Not(Or(Not(var182(x)), var237(x)))),
	ForAll([x], Not(Or(Not(var431(x)), Not(var194(x))))),
	ForAll([x], Not(Or(var307(x), var75(x)))),
	ForAll([x], Not(Or(Not(var28(x)), Not(var26(x))))),
	ForAll([x], Not(Or(Not(var318(x)), var229(x)))),
	ForAll([x], Not(Or(var126(x), Not(var413(x))))),
	ForAll([x], Not(Or(Not(var331(x)), Not(var354(x))))),
	ForAll([x], Not(Or(Not(var130(x)), Not(var110(x))))),
	ForAll([x], Not(Or(Not(var208(x)), var307(x)))),
	ForAll([x], Not(Or(var324(x), Not(var108(x))))),
	ForAll([x], Not(Or(var483(x), var363(x)))),
	ForAll([x], Not(Or(Not(var273(x)), var75(x)))),
	ForAll([x], Not(Or(var338(x), var78(x)))),
	ForAll([x], Not(Or(var149(x), var59(x)))),
	ForAll([x], Not(Or(var388(x), var202(x)))),
	ForAll([x], Not(Or(var251(x), Not(var74(x))))),
	ForAll([x], Not(Or(var458(x), var217(x)))),
	ForAll([x], Not(Or(Not(var151(x)), Not(var315(x))))),
	ForAll([x], Not(Or(var421(x), var210(x)))),
	ForAll([x], Not(Or(var95(x), var348(x)))),
	ForAll([x], Not(Or(Not(var150(x)), Not(var317(x))))),
	ForAll([x], Not(Or(Not(var457(x)), var17(x)))),
	ForAll([x], Not(Or(Not(var268(x)), var441(x)))),
	ForAll([x], Not(Or(Not(var84(x)), Not(var47(x))))),
	ForAll([x], Not(Or(Not(var68(x)), var6(x)))),
	ForAll([x], Not(Or(Not(var359(x)), Not(var198(x))))),
	ForAll([x], Not(Or(var222(x), var459(x)))),
	ForAll([x], Not(Or(Not(var278(x)), Not(var329(x))))),
	ForAll([x], Not(Or(var169(x), Not(var237(x))))),
	ForAll([x], Not(Or(Not(var463(x)), Not(var157(x))))),
	ForAll([x], Not(Or(var54(x), var305(x)))),
	ForAll([x], Not(Or(Not(var469(x)), var471(x)))),
	ForAll([x], Not(Or(Not(var350(x)), var373(x)))),
	ForAll([x], Not(Or(var40(x), Not(var11(x))))),
	ForAll([x], Not(Or(var399(x), var244(x)))),
	ForAll([x], Not(Or(Not(var286(x)), var440(x)))),
	ForAll([x], Not(Or(Not(var4(x)), Not(var366(x))))),
	ForAll([x], Not(Or(Not(var327(x)), Not(var282(x))))),
	ForAll([x], Not(Or(Not(var305(x)), var357(x)))),
	ForAll([x], Not(Or(Not(var34(x)), var358(x)))),
	ForAll([x], Not(Or(Not(var319(x)), var195(x)))),
	ForAll([x], Not(Or(var457(x), Not(var304(x))))),
	ForAll([x], Not(Or(var28(x), var487(x)))),
	ForAll([x], Not(Or(Not(var100(x)), Not(var230(x))))),
	ForAll([x], Not(Or(Not(var187(x)), var123(x)))),
	ForAll([x], Not(Or(var96(x), Not(var473(x))))),
	ForAll([x], Not(Or(var175(x), Not(var483(x))))),
	ForAll([x], Not(Or(var166(x), Not(var234(x))))),
	ForAll([x], Not(Or(Not(var405(x)), Not(var374(x))))),
	ForAll([x], Not(Or(var188(x), var377(x)))),
	ForAll([x], Not(Or(Not(var95(x)), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var224(x)), var379(x)))),
	ForAll([x], Not(Or(Not(var46(x)), Not(var82(x))))),
	ForAll([x], Not(Or(var484(x), var189(x)))),
	ForAll([x], Not(Or(var393(x), Not(var465(x))))),
	ForAll([x], Not(Or(var214(x), var400(x)))),
	ForAll([x], Not(Or(Not(var276(x)), Not(var286(x))))),
	ForAll([x], Not(Or(Not(var137(x)), var245(x)))),
	ForAll([x], Not(Or(var298(x), var83(x)))),
	ForAll([x], Not(Or(Not(var85(x)), var407(x)))),
	ForAll([x], Not(Or(Not(var152(x)), var266(x)))),
	ForAll([x], Not(Or(Not(var5(x)), Not(var329(x))))),
	ForAll([x], Not(Or(Not(var460(x)), Not(var289(x))))),
	ForAll([x], Not(Or(var482(x), var185(x)))),
	ForAll([x], Not(Or(Not(var94(x)), var203(x)))),
	ForAll([x], Not(Or(var489(x), var25(x)))),
	ForAll([x], Not(Or(Not(var421(x)), Not(var32(x))))),
	ForAll([x], Not(Or(var105(x), Not(var445(x))))),
	ForAll([x], Not(Or(var178(x), var168(x)))),
	ForAll([x], Not(Or(var449(x), Not(var156(x))))),
	ForAll([x], Not(Or(Not(var475(x)), var164(x)))),
	ForAll([x], Not(Or(var476(x), var308(x)))),
	ForAll([x], Not(Or(var18(x), var327(x)))),
	ForAll([x], Not(Or(Not(var104(x)), Not(var215(x))))),
	ForAll([x], Not(Or(Not(var494(x)), var389(x)))),
	ForAll([x], Not(Or(var373(x), var337(x)))),
	ForAll([x], Not(Or(Not(var269(x)), var242(x)))),
	ForAll([x], Not(Or(Not(var455(x)), Not(var144(x))))),
	ForAll([x], Not(Or(var338(x), Not(var472(x))))),
	ForAll([x], Not(Or(Not(var372(x)), var325(x)))),
	ForAll([x], Not(Or(var270(x), var232(x)))),
	ForAll([x], Not(Or(Not(var365(x)), Not(var274(x))))),
	ForAll([x], Not(Or(var192(x), Not(var268(x))))),
	ForAll([x], Not(Or(var59(x), Not(var406(x))))),
	ForAll([x], Not(Or(Not(var64(x)), Not(var48(x))))),
	ForAll([x], Not(Or(Not(var387(x)), var495(x)))),
	ForAll([x], Not(Or(Not(var9(x)), var479(x)))),
	ForAll([x], Not(Or(var341(x), Not(var370(x))))),
	ForAll([x], Not(Or(Not(var144(x)), Not(var275(x))))),
	ForAll([x], Not(Or(var98(x), Not(var260(x))))),
	ForAll([x], Not(Or(var87(x), var70(x)))),
	ForAll([x], Not(Or(var141(x), Not(var277(x))))),
	ForAll([x], Not(Or(Not(var344(x)), var112(x)))),
	ForAll([x], Not(Or(Not(var248(x)), Not(var483(x))))),
	ForAll([x], Not(Or(var196(x), Not(var140(x))))),
	ForAll([x], Not(Or(var198(x), var321(x)))),
	ForAll([x], Not(Or(var13(x), var152(x)))),
	ForAll([x], Not(Or(Not(var429(x)), Not(var183(x))))),
	ForAll([x], Not(Or(Not(var446(x)), Not(var374(x))))),
	ForAll([x], Not(Or(Not(var420(x)), var440(x)))),
	ForAll([x], Not(Or(var316(x), var358(x)))),
	ForAll([x], Not(Or(Not(var23(x)), var82(x)))),
	ForAll([x], Not(Or(var322(x), var131(x)))),
	ForAll([x], Not(Or(var295(x), Not(var110(x))))),
	ForAll([x], Not(Or(Not(var113(x)), Not(var14(x))))),
	ForAll([x], Not(Or(Not(var483(x)), Not(var270(x))))),
	ForAll([x], Not(Or(Not(var460(x)), Not(var410(x))))),
	ForAll([x], Not(Or(Not(var7(x)), var188(x)))),
	ForAll([x], Not(Or(var384(x), var16(x)))),
	ForAll([x], Not(Or(var403(x), Not(var468(x))))),
	ForAll([x], Not(Or(Not(var431(x)), var172(x)))),
	ForAll([x], Not(Or(Not(var454(x)), Not(var430(x))))),
	ForAll([x], Not(Or(var170(x), Not(var228(x))))),
	ForAll([x], Not(Or(Not(var108(x)), Not(var308(x))))),
	ForAll([x], Not(Or(var263(x), Not(var347(x))))),
	ForAll([x], Not(Or(var314(x), Not(var59(x))))),
	ForAll([x], Not(Or(var239(x), Not(var135(x))))),
	ForAll([x], Not(Or(var91(x), var137(x)))),
	ForAll([x], Not(Or(var263(x), var194(x)))),
	ForAll([x], Not(Or(Not(var118(x)), var417(x)))),
	ForAll([x], Not(Or(Not(var239(x)), var342(x)))),
	ForAll([x], Not(Or(var486(x), Not(var366(x))))),
	ForAll([x], Not(Or(var42(x), Not(var494(x))))),
	ForAll([x], Not(Or(Not(var330(x)), Not(var59(x))))),
	ForAll([x], Not(Or(var48(x), Not(var241(x))))),
	ForAll([x], Not(Or(var321(x), var320(x)))),
	ForAll([x], Not(Or(Not(var213(x)), var320(x)))),
	ForAll([x], Not(Or(Not(var205(x)), var295(x)))),
	ForAll([x], Not(Or(Not(var80(x)), var349(x)))),
	ForAll([x], Not(Or(var386(x), Not(var290(x))))),
	ForAll([x], Not(Or(var175(x), Not(var193(x))))),
	ForAll([x], Not(Or(Not(var266(x)), var338(x)))),
	ForAll([x], Not(Or(var464(x), Not(var270(x))))),
	ForAll([x], Not(Or(Not(var161(x)), var246(x)))),
	ForAll([x], Not(Or(var51(x), var209(x)))),
	ForAll([x], Not(Or(var110(x), var37(x)))),
	ForAll([x], Not(Or(Not(var51(x)), Not(var303(x))))),
	ForAll([x], Not(Or(Not(var485(x)), Not(var274(x))))),
	ForAll([x], Not(Or(var300(x), var82(x)))),
	ForAll([x], Not(Or(Not(var174(x)), Not(var455(x))))),
	ForAll([x], Not(Or(var271(x), var156(x)))),
	ForAll([x], Not(Or(Not(var371(x)), var397(x)))),
	ForAll([x], Not(Or(Not(var412(x)), var181(x)))),
	ForAll([x], Not(Or(Not(var449(x)), Not(var461(x))))),
	ForAll([x], Not(Or(var476(x), Not(var387(x))))),
	ForAll([x], Not(Or(Not(var36(x)), Not(var286(x))))),
	ForAll([x], Not(Or(var248(x), Not(var421(x))))),
	ForAll([x], Not(Or(var29(x), var7(x)))),
	ForAll([x], Not(Or(Not(var54(x)), Not(var269(x))))),
	ForAll([x], Not(Or(Not(var93(x)), Not(var156(x))))),
	ForAll([x], Not(Or(Not(var294(x)), Not(var92(x))))),
	ForAll([x], Not(Or(var472(x), var483(x)))),
	ForAll([x], Not(Or(var106(x), var196(x)))),
	ForAll([x], Not(Or(Not(var177(x)), var434(x)))),
	ForAll([x], Not(Or(var420(x), var309(x)))),
	ForAll([x], Not(Or(var490(x), var70(x)))),
	ForAll([x], Not(Or(Not(var86(x)), var339(x)))),
	ForAll([x], Not(Or(Not(var78(x)), var252(x)))),
	ForAll([x], Not(Or(Not(var436(x)), Not(var262(x))))),
	ForAll([x], Not(Or(Not(var91(x)), var335(x)))),
	ForAll([x], Not(Or(var402(x), var363(x)))),
	ForAll([x], Not(Or(Not(var484(x)), Not(var346(x))))),
	ForAll([x], Not(Or(Not(var439(x)), Not(var210(x))))),
	ForAll([x], Not(Or(var145(x), var486(x)))),
	ForAll([x], Not(Or(Not(var259(x)), Not(var391(x))))),
	ForAll([x], Not(Or(Not(var299(x)), var149(x)))),
	ForAll([x], Not(Or(var281(x), Not(var18(x))))),
	ForAll([x], Not(Or(var191(x), Not(var400(x))))),
	ForAll([x], Not(Or(Not(var296(x)), Not(var318(x))))),
	ForAll([x], Not(Or(var424(x), Not(var379(x))))),
	ForAll([x], Not(Or(var63(x), Not(var61(x))))),
	ForAll([x], Not(Or(var167(x), Not(var34(x))))),
	ForAll([x], Not(Or(var19(x), var332(x)))),
	ForAll([x], Not(Or(var404(x), Not(var497(x))))),
	ForAll([x], Not(Or(Not(var248(x)), var390(x)))),
	ForAll([x], Not(Or(var251(x), var200(x)))),
	ForAll([x], Not(Or(Not(var173(x)), var375(x)))),
	ForAll([x], Not(Or(var151(x), var359(x)))),
	ForAll([x], Not(Or(Not(var266(x)), var251(x)))),
	ForAll([x], Not(Or(Not(var57(x)), Not(var96(x))))),
	ForAll([x], Not(Or(Not(var270(x)), var373(x)))),
	ForAll([x], Not(Or(Not(var375(x)), var59(x)))),
	ForAll([x], Not(Or(var418(x), Not(var208(x))))),
	ForAll([x], Not(Or(Not(var442(x)), var117(x)))),
	ForAll([x], Not(Or(var222(x), var145(x)))),
	ForAll([x], Not(Or(var498(x), var195(x)))),
	ForAll([x], Not(Or(Not(var286(x)), Not(var313(x))))),
	ForAll([x], Not(Or(var459(x), var483(x)))),
	ForAll([x], Not(Or(Not(var115(x)), var227(x)))),
	ForAll([x], Not(Or(var61(x), var341(x)))),
	ForAll([x], Not(Or(var185(x), Not(var329(x))))),
	ForAll([x], Not(Or(Not(var59(x)), Not(var224(x))))),
	ForAll([x], Not(Or(var4(x), var422(x)))),
	ForAll([x], Not(Or(Not(var400(x)), Not(var205(x))))),
	ForAll([x], Not(Or(Not(var405(x)), var374(x)))),
	ForAll([x], Not(Or(Not(var467(x)), Not(var311(x))))),
	ForAll([x], Not(Or(var376(x), var207(x)))),
	ForAll([x], Not(Or(Not(var434(x)), var204(x)))),
	ForAll([x], Not(Or(Not(var405(x)), Not(var459(x))))),
	ForAll([x], Not(Or(var445(x), var11(x)))),
	ForAll([x], Not(Or(Not(var224(x)), var14(x)))),
	ForAll([x], Not(Or(Not(var474(x)), var460(x)))),
	ForAll([x], Not(Or(var250(x), var146(x)))),
	ForAll([x], Not(Or(Not(var375(x)), Not(var283(x))))),
	ForAll([x], Not(Or(Not(var130(x)), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var334(x)), Not(var84(x))))),
	ForAll([x], Not(Or(var213(x), var197(x)))),
	ForAll([x], Not(Or(Not(var439(x)), var385(x)))),
	ForAll([x], Not(Or(Not(var22(x)), var123(x)))),
	ForAll([x], Not(Or(var352(x), Not(var274(x))))),
	ForAll([x], Not(Or(Not(var285(x)), var251(x)))),
	ForAll([x], Not(Or(var475(x), var166(x)))),
	ForAll([x], Not(Or(Not(var421(x)), var382(x)))),
	ForAll([x], Not(Or(var380(x), var38(x)))),
	ForAll([x], Not(Or(var499(x), var333(x)))),
	ForAll([x], Not(Or(var292(x), var151(x)))),
	ForAll([x], Not(Or(var164(x), var283(x)))),
	ForAll([x], Not(Or(var256(x), var420(x)))),
	ForAll([x], Not(Or(var460(x), Not(var340(x))))),
	ForAll([x], Not(Or(Not(var375(x)), var148(x)))),
	ForAll([x], Not(Or(Not(var305(x)), var134(x)))),
	ForAll([x], Not(Or(Not(var58(x)), Not(var243(x))))),
	ForAll([x], Not(Or(Not(var219(x)), Not(var186(x))))),
	ForAll([x], Not(Or(Not(var29(x)), Not(var395(x))))),
	ForAll([x], Not(Or(Not(var147(x)), var198(x)))),
	ForAll([x], Not(Or(var75(x), Not(var350(x))))),
	ForAll([x], Not(Or(var482(x), var411(x)))),
	ForAll([x], Not(Or(Not(var403(x)), Not(var396(x))))),
	ForAll([x], Not(Or(Not(var465(x)), var289(x)))),
	ForAll([x], Not(Or(var483(x), var223(x)))),
	ForAll([x], Not(Or(Not(var286(x)), var483(x)))),
	ForAll([x], Not(Or(var109(x), var445(x)))),
	ForAll([x], Not(Or(var176(x), Not(var418(x))))),
	ForAll([x], Not(Or(Not(var12(x)), Not(var98(x))))),
	ForAll([x], Not(Or(var1(x), var478(x)))),
	ForAll([x], Not(Or(Not(var92(x)), var65(x)))),
	ForAll([x], Not(Or(var245(x), Not(var252(x))))),
	ForAll([x], Not(Or(var156(x), var415(x)))),
	ForAll([x], Not(Or(Not(var282(x)), var266(x)))),
	ForAll([x], Not(Or(var434(x), var422(x)))),
	ForAll([x], Not(Or(var214(x), Not(var357(x))))),
	ForAll([x], Not(Or(Not(var183(x)), var213(x)))),
	ForAll([x], Not(Or(var277(x), Not(var112(x))))),
	ForAll([x], Not(Or(Not(var132(x)), var380(x)))),
	ForAll([x], Not(Or(var126(x), Not(var235(x))))),
	ForAll([x], Not(Or(Not(var254(x)), Not(var116(x))))),
	ForAll([x], Not(Or(var186(x), var248(x)))),
	ForAll([x], Not(Or(var119(x), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var368(x)), Not(var332(x))))),
	ForAll([x], Not(Or(var323(x), Not(var260(x))))),
	ForAll([x], Not(Or(var354(x), var138(x)))),
	ForAll([x], Not(Or(var356(x), var2(x)))),
	ForAll([x], Not(Or(var385(x), Not(var62(x))))),
	ForAll([x], Not(Or(Not(var220(x)), Not(var143(x))))),
	ForAll([x], Not(Or(var138(x), Not(var131(x))))),
	ForAll([x], Not(Or(Not(var293(x)), var277(x)))),
	ForAll([x], Not(Or(Not(var109(x)), var1(x)))),
	ForAll([x], Not(Or(var63(x), var315(x)))),
	ForAll([x], Not(Or(var491(x), var223(x)))),
	ForAll([x], Not(Or(Not(var315(x)), var300(x)))),
	ForAll([x], Not(Or(Not(var342(x)), var433(x)))),
	ForAll([x], Not(Or(var297(x), Not(var282(x))))),
	ForAll([x], Not(Or(var77(x), var66(x)))),
	ForAll([x], Not(Or(Not(var432(x)), Not(var262(x))))),
	ForAll([x], Not(Or(var104(x), Not(var12(x))))),
	ForAll([x], Not(Or(var475(x), Not(var364(x))))),
	ForAll([x], Not(Or(var423(x), Not(var86(x))))),
	ForAll([x], Not(Or(var37(x), Not(var183(x))))),
	ForAll([x], Not(Or(Not(var224(x)), var116(x)))),
	ForAll([x], Not(Or(Not(var120(x)), Not(var295(x))))),
	ForAll([x], Not(Or(var65(x), Not(var211(x))))),
	ForAll([x], Not(Or(Not(var195(x)), var141(x)))),
	ForAll([x], Not(Or(Not(var116(x)), Not(var305(x))))),
	ForAll([x], Not(Or(Not(var92(x)), var281(x)))),
	ForAll([x], Not(Or(Not(var338(x)), var146(x)))),
	ForAll([x], Not(Or(Not(var233(x)), Not(var197(x))))),
	ForAll([x], Not(Or(Not(var465(x)), var263(x)))),
	ForAll([x], Not(Or(var267(x), var411(x)))),
	ForAll([x], Not(Or(var126(x), Not(var274(x))))),
	ForAll([x], Not(Or(var409(x), var134(x)))),
	ForAll([x], Not(Or(Not(var23(x)), var360(x)))),
	ForAll([x], Not(Or(Not(var106(x)), Not(var237(x))))),
	ForAll([x], Not(Or(var329(x), Not(var491(x))))),
	ForAll([x], Not(Or(var66(x), Not(var80(x))))),
	ForAll([x], Not(Or(Not(var340(x)), Not(var270(x))))),
	ForAll([x], Not(Or(var335(x), Not(var355(x))))),
	ForAll([x], Not(Or(var43(x), var25(x)))),
	ForAll([x], Not(Or(var499(x), Not(var140(x))))),
	ForAll([x], Not(Or(var112(x), var330(x)))),
	ForAll([x], Not(Or(Not(var83(x)), Not(var463(x))))),
	ForAll([x], Not(Or(Not(var242(x)), var405(x)))),
	ForAll([x], Not(Or(var198(x), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var361(x)), var83(x)))),
	ForAll([x], Not(Or(Not(var362(x)), var442(x)))),
	ForAll([x], Not(Or(var360(x), Not(var331(x))))),
	ForAll([x], Not(Or(var426(x), var399(x)))),
	ForAll([x], Not(Or(Not(var15(x)), var226(x)))),
	ForAll([x], Not(Or(var299(x), var441(x)))),
	ForAll([x], Not(Or(var450(x), var61(x)))),
	ForAll([x], Not(Or(Not(var484(x)), var127(x)))),
	ForAll([x], Not(Or(Not(var14(x)), Not(var150(x))))),
	ForAll([x], Not(Or(var400(x), var193(x)))),
	ForAll([x], Not(Or(var28(x), Not(var344(x))))),
	ForAll([x], Not(Or(Not(var79(x)), Not(var13(x))))),
	ForAll([x], Not(Or(var79(x), Not(var295(x))))),
	ForAll([x], Not(Or(var415(x), Not(var388(x))))),
	ForAll([x], Not(Or(var339(x), Not(var419(x))))),
	ForAll([x], Not(Or(var431(x), var53(x)))),
	ForAll([x], Not(Or(Not(var97(x)), var75(x)))),
	ForAll([x], Not(Or(Not(var146(x)), Not(var6(x))))),
	ForAll([x], Not(Or(Not(var379(x)), Not(var174(x))))),
	ForAll([x], Not(Or(Not(var78(x)), var36(x)))),
	ForAll([x], Not(Or(var253(x), var176(x)))),
	ForAll([x], Not(Or(Not(var261(x)), var304(x)))),
	ForAll([x], Not(Or(Not(var460(x)), Not(var447(x))))),
	ForAll([x], Not(Or(var468(x), var458(x)))),
	ForAll([x], Not(Or(Not(var174(x)), Not(var321(x))))),
	ForAll([x], Not(Or(Not(var263(x)), var74(x)))),
	ForAll([x], Not(Or(Not(var288(x)), Not(var300(x))))),
	ForAll([x], Not(Or(var489(x), var249(x)))),
	ForAll([x], Not(Or(Not(var280(x)), var139(x)))),
	ForAll([x], Not(Or(var408(x), var79(x)))),
	ForAll([x], Not(Or(var361(x), Not(var354(x))))),
	ForAll([x], Not(Or(Not(var159(x)), var337(x)))),
	ForAll([x], Not(Or(Not(var4(x)), var355(x)))),
	ForAll([x], Not(Or(Not(var486(x)), var36(x)))),
	ForAll([x], Not(Or(Not(var346(x)), var460(x)))),
	ForAll([x], Not(Or(var487(x), var142(x)))),
	ForAll([x], Not(Or(Not(var365(x)), var109(x)))),
	ForAll([x], Not(Or(Not(var336(x)), Not(var280(x))))),
	ForAll([x], Not(Or(Not(var174(x)), Not(var94(x))))),
	ForAll([x], Not(Or(Not(var467(x)), Not(var471(x))))),
	ForAll([x], Not(Or(Not(var19(x)), Not(var131(x))))),
	ForAll([x], Not(Or(var444(x), var242(x)))),
	ForAll([x], Not(Or(var144(x), var459(x)))),
	ForAll([x], Not(Or(var356(x), var145(x)))),
	ForAll([x], Not(Or(Not(var261(x)), Not(var299(x))))),
	ForAll([x], Not(Or(Not(var237(x)), Not(var348(x))))),
	ForAll([x], Not(Or(var388(x), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var109(x)), Not(var432(x))))),
	ForAll([x], Not(Or(Not(var235(x)), var180(x)))),
	ForAll([x], Not(Or(var101(x), Not(var146(x))))),
	ForAll([x], Not(Or(Not(var458(x)), var49(x)))),
	ForAll([x], Not(Or(Not(var86(x)), var386(x)))),
	ForAll([x], Not(Or(Not(var497(x)), Not(var349(x))))),
	ForAll([x], Not(Or(var259(x), Not(var426(x))))),
	ForAll([x], Not(Or(var240(x), Not(var401(x))))),
	ForAll([x], Not(Or(var285(x), var334(x)))),
	ForAll([x], Not(Or(Not(var455(x)), Not(var117(x))))),
	ForAll([x], Not(Or(var223(x), Not(var167(x))))),
	ForAll([x], Not(Or(var350(x), var325(x)))),
	ForAll([x], Not(Or(var334(x), var145(x)))),
	ForAll([x], Not(Or(Not(var295(x)), Not(var237(x))))),
	ForAll([x], Not(Or(var91(x), Not(var446(x))))),
	ForAll([x], Not(Or(var116(x), Not(var320(x))))),
	ForAll([x], Not(Or(Not(var116(x)), Not(var99(x))))),
	ForAll([x], Not(Or(Not(var142(x)), Not(var3(x))))),
	ForAll([x], Not(Or(var239(x), var419(x)))),
	ForAll([x], Not(Or(Not(var35(x)), Not(var422(x))))),
	ForAll([x], Not(Or(Not(var315(x)), Not(var393(x))))),
	ForAll([x], Not(Or(var221(x), Not(var106(x))))),
	ForAll([x], Not(Or(Not(var58(x)), Not(var500(x))))),
	ForAll([x], Not(Or(var433(x), var315(x)))),
	ForAll([x], Not(Or(Not(var413(x)), Not(var127(x))))),
	ForAll([x], Not(Or(var17(x), var372(x)))),
	ForAll([x], Not(Or(Not(var365(x)), Not(var38(x))))),
	ForAll([x], Not(Or(Not(var259(x)), var134(x)))),
	ForAll([x], Not(Or(var399(x), Not(var323(x))))),
	ForAll([x], Not(Or(Not(var226(x)), var192(x)))),
	ForAll([x], Not(Or(var490(x), Not(var156(x))))),
	ForAll([x], Not(Or(Not(var164(x)), var105(x)))),
	ForAll([x], Not(Or(Not(var119(x)), var207(x)))),
	ForAll([x], Not(Or(var166(x), var212(x)))),
	ForAll([x], Not(Or(Not(var183(x)), Not(var107(x))))),
	ForAll([x], Not(Or(Not(var344(x)), Not(var245(x))))),
	ForAll([x], Not(Or(var41(x), Not(var306(x))))),
	ForAll([x], Not(Or(var347(x), Not(var212(x))))),
	ForAll([x], Not(Or(var147(x), var221(x)))),
	ForAll([x], Not(Or(var170(x), var456(x)))),
	ForAll([x], Not(Or(Not(var253(x)), Not(var373(x))))),
	ForAll([x], Not(Or(var35(x), var225(x)))),
	ForAll([x], Not(Or(var182(x), Not(var325(x))))),
	ForAll([x], Not(Or(var229(x), var102(x)))),
	ForAll([x], Not(Or(Not(var291(x)), Not(var302(x))))),
	ForAll([x], Not(Or(var64(x), var137(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var80(x1), Not(var397(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var391(x1)), Not(var351(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var152(x1), Not(var465(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var284(x1), Not(var147(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), var235(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var478(x1)), var270(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var177(x1), var282(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var337(x1), Not(var416(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var294(x1), var473(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var417(x1), var485(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var390(x1)), Not(var447(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var137(x1), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var447(x1), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var295(x1), Not(var492(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var118(x1), Not(var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var189(x1)), Not(var144(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var113(x1), Not(var500(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var71(x1)), Not(var191(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var171(x1), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var34(x1), var201(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var101(x1)), Not(var254(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var161(x1), var441(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var301(x1)), var47(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var497(x1), Not(var225(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var76(x1), var321(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var283(x1)), var155(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var102(x1)), Not(var239(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var411(x1), var16(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var115(x1)), var313(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var437(x1), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var279(x1)), Not(var112(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var239(x1)), var297(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var77(x1)), Not(var365(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var132(x1)), Not(var334(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var444(x1), var122(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var376(x1), var300(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var423(x1)), Not(var452(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var487(x1), var471(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var463(x1)), var426(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var487(x1)), Not(var407(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var86(x1)), var445(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var302(x1), Not(var352(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var188(x1)), var133(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var236(x1), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var409(x1), var92(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var426(x1)), Not(var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var81(x1)), Not(var214(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var144(x1), Not(var245(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var83(x1), var409(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var301(x1)), var67(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var345(x1), var454(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var277(x1)), Not(var51(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var382(x1), var419(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var413(x1), Not(var461(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var247(x1), Not(var173(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var121(x1), Not(var203(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var79(x1)), var488(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var50(x1), Not(var157(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var367(x1), var410(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var396(x1), Not(var154(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var131(x1)), Not(var231(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var162(x1), Not(var475(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var53(x1), var278(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var334(x1)), Not(var37(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var427(x1)), Not(var59(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var327(x1), Not(var95(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var154(x1)), Not(var292(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var186(x1)), var389(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var472(x1), var343(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), var317(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var386(x1)), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var409(x1)), var493(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var375(x1)), var411(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var339(x1), Not(var294(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var442(x1)), var330(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var40(x1)), Not(var266(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var130(x1)), var476(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var28(x1)), var424(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var366(x1), Not(var72(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var415(x1), Not(var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var351(x1)), Not(var435(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var468(x1)), Not(var293(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var3(x1)), Not(var128(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var292(x1)), var120(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var277(x1)), var102(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var262(x1)), Not(var220(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var448(x1)), var493(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var180(x1), var488(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var442(x1), Not(var230(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var70(x1), Not(var322(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var239(x1)), Not(var310(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var204(x1), var337(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var330(x1), Not(var102(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var80(x1), Not(var150(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var57(x1), Not(var8(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var174(x1), var234(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var245(x1)), Not(var470(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var84(x1)), var452(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var77(x1), Not(var475(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var92(x1), Not(var413(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var466(x1), var105(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var137(x1)), Not(var115(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var435(x1), Not(var248(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var422(x1)), Not(var121(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var94(x1), Not(var471(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var63(x1), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var460(x1), var260(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var314(x1)), var414(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var219(x1), var117(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var390(x1)), var271(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var141(x1)), Not(var186(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var428(x1)), Not(var160(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var460(x1), Not(var368(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var476(x1), var478(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var53(x1), Not(var168(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var277(x1)), Not(var254(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var294(x1), var83(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var366(x1)), var88(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var266(x1)), var199(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var19(x1), var441(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var288(x1), var400(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var215(x1), Not(var95(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var452(x1)), var68(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var371(x1)), var42(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var421(x1)), Not(var424(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var462(x1), var196(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var473(x1), Not(var337(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var448(x1)), Not(var348(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var274(x1)), var475(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var190(x1), var232(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var320(x1)), var481(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var156(x1)), var328(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var367(x1)), Not(var96(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var277(x1), var356(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var27(x1), Not(var345(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var485(x1), var15(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var66(x1)), Not(var106(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var154(x1)), var151(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var325(x1)), Not(var427(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var292(x1)), var219(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var176(x1)), var424(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var48(x1), var428(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var171(x1), var477(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var153(x1)), var250(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var42(x1)), Not(var291(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var223(x1), Not(var78(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var133(x1), Not(var13(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var237(x1)), var70(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var497(x1), var95(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var323(x1)), Not(var369(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var226(x1), Not(var182(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var318(x1)), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var253(x1)), Not(var439(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var153(x1), Not(var121(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var229(x1)), var182(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var226(x1)), Not(var223(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var386(x1)), Not(var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var57(x1), var201(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var142(x1)), Not(var398(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var290(x1)), var117(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var236(x1)), var221(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var69(x1)), Not(var156(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var439(x1), Not(var227(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var322(x1)), Not(var163(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var143(x1), Not(var280(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var476(x1)), var348(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var185(x1), Not(var116(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var109(x1)), Not(var345(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var190(x1), Not(var327(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var445(x1)), Not(var265(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var467(x1)), Not(var100(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var420(x1)), var68(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var264(x1), Not(var160(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var110(x1), var297(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var384(x1)), Not(var353(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var228(x1)), Not(var187(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var417(x1), var195(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var10(x1), var390(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var456(x1), var271(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var201(x1)), var212(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var83(x1), var368(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var326(x1), Not(var195(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var159(x1), Not(var44(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var155(x1), Not(var64(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var94(x1)), var335(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var440(x1), var336(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var143(x1), var287(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var75(x1), Not(var199(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var172(x1)), Not(var69(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var349(x1), Not(var141(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var445(x1), var265(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var73(x1)), var96(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var107(x1)), Not(var12(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var191(x1), var339(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var317(x1)), var77(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var80(x1), var314(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var192(x1)), Not(var303(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var57(x1), Not(var384(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var274(x1), var365(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var445(x1), var268(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var132(x1)), var219(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var62(x1)), Not(var126(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var47(x1)), var29(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var292(x1)), var482(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var5(x1)), var37(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var309(x1), Not(var312(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var202(x1), Not(var454(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var365(x1)), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var363(x1), Not(var42(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var329(x1)), Not(var151(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var188(x1), Not(var408(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var470(x1), var400(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var180(x1), var236(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var7(x1)), Not(var453(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var94(x1)), var215(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var355(x1)), var265(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var197(x1)), Not(var408(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var369(x1)), var466(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var152(x1), var440(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var141(x1)), var149(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var179(x1)), Not(var254(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var135(x1)), Not(var121(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var353(x1)), Not(var406(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var169(x1), Not(var307(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var478(x1), var311(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), Not(var461(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var47(x1), var417(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var94(x1), Not(var283(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var281(x1), var489(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var344(x1)), var125(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var53(x1), var86(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var46(x1)), Not(var402(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var121(x1)), var151(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), var313(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var169(x1)), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var138(x1), Not(var223(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var420(x1), var220(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var28(x1)), var167(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var315(x1)), var207(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var367(x1), var207(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var116(x1)), var360(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var69(x1), Not(var421(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var157(x1), var257(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var186(x1)), Not(var420(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var224(x1)), Not(var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var459(x1), Not(var287(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var148(x1)), var51(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var43(x1)), var257(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), Not(var139(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var295(x1)), var104(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var351(x1), Not(var368(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var186(x1)), Not(var224(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var251(x1)), Not(var407(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var251(x1), Not(var320(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var403(x1), Not(var204(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var448(x1), var42(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var373(x1)), Not(var320(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var360(x1), Not(var357(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var190(x1), Not(var133(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var186(x1), Not(var133(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var257(x1)), Not(var152(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var304(x1)), var53(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var2(x1)), var127(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var304(x1)), Not(var482(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var125(x1), var292(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var201(x1), Not(var315(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var70(x1)), Not(var114(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var63(x1), Not(var134(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var303(x1), Not(var467(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var284(x1), Not(var382(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var336(x1)), var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var313(x1)), var106(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var354(x1)), var313(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var34(x1), Not(var290(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var80(x1)), var206(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var495(x1)), Not(var171(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), Not(var373(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var124(x1), var213(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var191(x1)), Not(var353(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var353(x1), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var95(x1), Not(var157(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var100(x1)), Not(var203(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var169(x1)), var401(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var31(x1)), var199(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var152(x1), var72(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var190(x1), var217(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var82(x1)), var91(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var470(x1), var431(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var404(x1), Not(var302(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var283(x1), var372(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var76(x1), var135(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var426(x1)), Not(var105(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var132(x1), Not(var301(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var89(x1), Not(var178(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var379(x1)), var282(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var450(x1), var278(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var161(x1), var252(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var184(x1)), var229(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var236(x1), var490(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var81(x1)), var261(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var451(x1), Not(var153(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var479(x1)), Not(var296(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var320(x1)), Not(var213(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var264(x1), Not(var418(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var262(x1)), Not(var46(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var34(x1)), var311(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var7(x1)), Not(var368(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var495(x1)), var28(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var398(x1)), var55(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var52(x1), Not(var239(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var406(x1), var346(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var350(x1), Not(var101(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var221(x1), var22(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var261(x1), Not(var269(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var279(x1), Not(var377(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var323(x1), var327(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var235(x1), Not(var112(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var340(x1), var477(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var497(x1)), var204(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var416(x1), Not(var413(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var447(x1), var251(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var432(x1), var345(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var105(x1), Not(var391(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var31(x1), var40(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var274(x1), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var357(x1)), Not(var218(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var392(x1)), Not(var412(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var164(x1)), var294(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var94(x1)), var389(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var77(x1)), var228(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var304(x1), var93(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var69(x1)), Not(var40(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var40(x1), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var220(x1), Not(var475(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var174(x1)), var33(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var259(x1), Not(var499(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var299(x1), var69(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var394(x1)), Not(var304(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var184(x1), var411(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var450(x1)), var376(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var238(x1)), Not(var175(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var130(x1), var32(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var378(x1), var34(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), Not(var292(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var225(x1), Not(var206(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var332(x1), var249(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var443(x1)), var76(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var496(x1), Not(var395(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var480(x1)), Not(var457(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var303(x1), var481(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var99(x1)), var478(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), Not(var429(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var455(x1)), var468(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var190(x1)), var61(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var442(x1)), var365(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var158(x1), Not(var286(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var429(x1), Not(var163(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var188(x1), var192(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var428(x1)), var193(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var371(x1), var128(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var250(x1), Not(var411(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var461(x1), var497(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var123(x1), var404(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var456(x1), Not(var214(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var411(x1)), var106(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var385(x1)), var188(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var456(x1)), var429(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var287(x1), var53(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var185(x1)), var382(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var293(x1), var73(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var101(x1)), var233(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var407(x1)), Not(var420(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var124(x1)), Not(var177(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var242(x1), Not(var462(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), var86(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var487(x1)), var458(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var415(x1)), var218(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var107(x1), Not(var364(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var180(x1)), var222(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var355(x1), Not(var383(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var345(x1)), Not(var254(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var15(x1), var289(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var114(x1), var259(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var291(x1)), Not(var292(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var143(x1), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var4(x1)), Not(var340(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var269(x1)), Not(var204(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var204(x1), Not(var380(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var480(x1)), var185(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var133(x1), var340(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var50(x1)), var163(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var153(x1), Not(var260(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var459(x1), var86(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var213(x1), var17(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var142(x1), Not(var488(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var463(x1), var415(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var16(x1)), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var211(x1)), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var421(x1), var251(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var126(x1)), Not(var384(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var277(x1), var464(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var7(x1), Not(var237(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var31(x1), Not(var256(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var144(x1)), var198(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var301(x1), Not(var236(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var268(x1), Not(var208(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var260(x1), var404(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var389(x1), var127(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var138(x1)), var75(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var428(x1), Not(var384(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var114(x1)), Not(var336(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var111(x1)), var121(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var239(x1), var229(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var102(x1), Not(var192(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var460(x1), Not(var112(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var490(x1), var417(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var344(x1)), var33(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var484(x1)), var429(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var351(x1)), var352(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var102(x1)), Not(var450(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var93(x1), var40(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var309(x1), var67(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var346(x1)), var148(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var202(x1), Not(var419(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var305(x1), Not(var266(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var236(x1)), Not(var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var213(x1), Not(var331(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var75(x1), var346(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), var235(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var380(x1), Not(var132(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var340(x1), var167(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var111(x1), Not(var191(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var214(x1), var195(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var193(x1), Not(var121(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var235(x1)), var152(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var173(x1)), Not(var462(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var62(x1), var116(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var286(x1)), var272(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var403(x1), Not(var484(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var297(x1), Not(var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var228(x1), var97(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var123(x1)), Not(var78(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var436(x1)), var447(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var148(x1)), Not(var156(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var273(x1), var329(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var400(x1)), Not(var68(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var329(x1)), var161(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var285(x1), Not(var220(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var453(x1)), Not(var395(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var277(x1), Not(var260(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var266(x1), Not(var268(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var247(x1)), var459(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var398(x1)), var51(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var148(x1)), var32(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var423(x1), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var436(x1), Not(var351(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var306(x1), var357(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var464(x1)), Not(var352(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var308(x1), var163(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var384(x1)), var90(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var56(x1)), Not(var200(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var94(x1), Not(var394(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var268(x1), var150(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var127(x1)), var99(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var386(x1)), Not(var317(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var137(x1), Not(var227(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var125(x1), Not(var334(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var338(x1)), var441(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var58(x1), var312(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var247(x1)), Not(var214(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var153(x1)), var256(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var458(x1), var87(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var185(x1), Not(var240(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var229(x1), var11(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var344(x1), var495(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var146(x1), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var293(x1)), var160(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var20(x1)), Not(var41(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var160(x1), var348(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var318(x1)), var384(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var433(x1)), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var133(x1)), var165(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var66(x1)), var394(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var365(x1)), var170(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var350(x1), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var131(x1)), var56(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var365(x1)), Not(var136(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var101(x1), Not(var55(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var149(x1)), Not(var400(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var300(x1)), Not(var500(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var434(x1), var61(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var127(x1)), var398(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var230(x1)), Not(var282(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var429(x1), var71(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var181(x1)), Not(var238(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var130(x1), Not(var435(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var257(x1), var95(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var499(x1), var88(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var444(x1), var14(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var255(x1)), Not(var121(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms0)
print(s.check())
print(s.statistics())
