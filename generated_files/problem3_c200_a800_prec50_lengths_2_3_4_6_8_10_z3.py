from z3 import *

Object = DeclareSort('Object')

var309 = Function('var309', Object, BoolSort())
var660 = Function('var660', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var365 = Function('var365', Object, BoolSort())
var781 = Function('var781', Object, BoolSort())
var789 = Function('var789', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var585 = Function('var585', Object, BoolSort())
var623 = Function('var623', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var364 = Function('var364', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var503 = Function('var503', Object, BoolSort())
var405 = Function('var405', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var538 = Function('var538', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var549 = Function('var549', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var523 = Function('var523', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var658 = Function('var658', Object, BoolSort())
var337 = Function('var337', Object, BoolSort())
var730 = Function('var730', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var750 = Function('var750', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var407 = Function('var407', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var788 = Function('var788', Object, BoolSort())
var676 = Function('var676', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var709 = Function('var709', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var724 = Function('var724', Object, BoolSort())
var484 = Function('var484', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var385 = Function('var385', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var340 = Function('var340', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var408 = Function('var408', Object, BoolSort())
var411 = Function('var411', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var455 = Function('var455', Object, BoolSort())
var582 = Function('var582', Object, BoolSort())
var372 = Function('var372', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var486 = Function('var486', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var499 = Function('var499', Object, BoolSort())
var624 = Function('var624', Object, BoolSort())
var338 = Function('var338', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var269 = Function('var269', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var392 = Function('var392', Object, BoolSort())
var597 = Function('var597', Object, BoolSort())
var691 = Function('var691', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var609 = Function('var609', Object, BoolSort())
var703 = Function('var703', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var502 = Function('var502', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var336 = Function('var336', Object, BoolSort())
var476 = Function('var476', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var729 = Function('var729', Object, BoolSort())
var278 = Function('var278', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var313 = Function('var313', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var293 = Function('var293', Object, BoolSort())
var755 = Function('var755', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var518 = Function('var518', Object, BoolSort())
var656 = Function('var656', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var356 = Function('var356', Object, BoolSort())
var649 = Function('var649', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var711 = Function('var711', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var532 = Function('var532', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var727 = Function('var727', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var286 = Function('var286', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var615 = Function('var615', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var398 = Function('var398', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var622 = Function('var622', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var396 = Function('var396', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
var618 = Function('var618', Object, BoolSort())
var665 = Function('var665', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var640 = Function('var640', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var517 = Function('var517', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var757 = Function('var757', Object, BoolSort())
var581 = Function('var581', Object, BoolSort())
var799 = Function('var799', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var475 = Function('var475', Object, BoolSort())
var350 = Function('var350', Object, BoolSort())
var367 = Function('var367', Object, BoolSort())
var756 = Function('var756', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var410 = Function('var410', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var782 = Function('var782', Object, BoolSort())
var652 = Function('var652', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var450 = Function('var450', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var557 = Function('var557', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var316 = Function('var316', Object, BoolSort())
var528 = Function('var528', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var636 = Function('var636', Object, BoolSort())
var349 = Function('var349', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var362 = Function('var362', Object, BoolSort())
var536 = Function('var536', Object, BoolSort())
var377 = Function('var377', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var348 = Function('var348', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var670 = Function('var670', Object, BoolSort())
var302 = Function('var302', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var713 = Function('var713', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var426 = Function('var426', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var778 = Function('var778', Object, BoolSort())
var491 = Function('var491', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var379 = Function('var379', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var678 = Function('var678', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var446 = Function('var446', Object, BoolSort())
var522 = Function('var522', Object, BoolSort())
var417 = Function('var417', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var389 = Function('var389', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var419 = Function('var419', Object, BoolSort())
var351 = Function('var351', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var430 = Function('var430', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var318 = Function('var318', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var489 = Function('var489', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var547 = Function('var547', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var800 = Function('var800', Object, BoolSort())
var406 = Function('var406', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var468 = Function('var468', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var382 = Function('var382', Object, BoolSort())
var404 = Function('var404', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var285 = Function('var285', Object, BoolSort())
var586 = Function('var586', Object, BoolSort())
var638 = Function('var638', Object, BoolSort())
var371 = Function('var371', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var792 = Function('var792', Object, BoolSort())
var497 = Function('var497', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var552 = Function('var552', Object, BoolSort())
var429 = Function('var429', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var690 = Function('var690', Object, BoolSort())
var378 = Function('var378', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var542 = Function('var542', Object, BoolSort())
var510 = Function('var510', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var493 = Function('var493', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var580 = Function('var580', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var721 = Function('var721', Object, BoolSort())
var794 = Function('var794', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var369 = Function('var369', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var594 = Function('var594', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var529 = Function('var529', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var401 = Function('var401', Object, BoolSort())
var370 = Function('var370', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var774 = Function('var774', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var728 = Function('var728', Object, BoolSort())
var627 = Function('var627', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var402 = Function('var402', Object, BoolSort())
var551 = Function('var551', Object, BoolSort())
var524 = Function('var524', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var482 = Function('var482', Object, BoolSort())
var741 = Function('var741', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var707 = Function('var707', Object, BoolSort())
var768 = Function('var768', Object, BoolSort())
var599 = Function('var599', Object, BoolSort())
var515 = Function('var515', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var494 = Function('var494', Object, BoolSort())
var685 = Function('var685', Object, BoolSort())
var344 = Function('var344', Object, BoolSort())
var766 = Function('var766', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var343 = Function('var343', Object, BoolSort())
var541 = Function('var541', Object, BoolSort())
var292 = Function('var292', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var588 = Function('var588', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var589 = Function('var589', Object, BoolSort())
var333 = Function('var333', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var644 = Function('var644', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var777 = Function('var777', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var373 = Function('var373', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var496 = Function('var496', Object, BoolSort())
var425 = Function('var425', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var613 = Function('var613', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var680 = Function('var680', Object, BoolSort())
var697 = Function('var697', Object, BoolSort())
var650 = Function('var650', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var439 = Function('var439', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var600 = Function('var600', Object, BoolSort())
var675 = Function('var675', Object, BoolSort())
var516 = Function('var516', Object, BoolSort())
var284 = Function('var284', Object, BoolSort())
var646 = Function('var646', Object, BoolSort())
var308 = Function('var308', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var307 = Function('var307', Object, BoolSort())
var694 = Function('var694', Object, BoolSort())
var451 = Function('var451', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var745 = Function('var745', Object, BoolSort())
var592 = Function('var592', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var403 = Function('var403', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var780 = Function('var780', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var576 = Function('var576', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var354 = Function('var354', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var606 = Function('var606', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var458 = Function('var458', Object, BoolSort())
var462 = Function('var462', Object, BoolSort())
var625 = Function('var625', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var566 = Function('var566', Object, BoolSort())
var715 = Function('var715', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var485 = Function('var485', Object, BoolSort())
var505 = Function('var505', Object, BoolSort())
var511 = Function('var511', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var603 = Function('var603', Object, BoolSort())
var754 = Function('var754', Object, BoolSort())
var708 = Function('var708', Object, BoolSort())
var573 = Function('var573', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var507 = Function('var507', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var667 = Function('var667', Object, BoolSort())
var428 = Function('var428', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var544 = Function('var544', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var722 = Function('var722', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var671 = Function('var671', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var512 = Function('var512', Object, BoolSort())
var761 = Function('var761', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var736 = Function('var736', Object, BoolSort())
var386 = Function('var386', Object, BoolSort())
var276 = Function('var276', Object, BoolSort())
var470 = Function('var470', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var456 = Function('var456', Object, BoolSort())
var444 = Function('var444', Object, BoolSort())
var433 = Function('var433', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var617 = Function('var617', Object, BoolSort())
var686 = Function('var686', Object, BoolSort())
var366 = Function('var366', Object, BoolSort())
var748 = Function('var748', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var514 = Function('var514', Object, BoolSort())
var376 = Function('var376', Object, BoolSort())
var687 = Function('var687', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var590 = Function('var590', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var306 = Function('var306', Object, BoolSort())
var714 = Function('var714', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var742 = Function('var742', Object, BoolSort())
var747 = Function('var747', Object, BoolSort())
var637 = Function('var637', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var447 = Function('var447', Object, BoolSort())
var390 = Function('var390', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var785 = Function('var785', Object, BoolSort())
var666 = Function('var666', Object, BoolSort())
var296 = Function('var296', Object, BoolSort())
var776 = Function('var776', Object, BoolSort())
var760 = Function('var760', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var560 = Function('var560', Object, BoolSort())
var716 = Function('var716', Object, BoolSort())
var712 = Function('var712', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var710 = Function('var710', Object, BoolSort())
var317 = Function('var317', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var696 = Function('var696', Object, BoolSort())
var539 = Function('var539', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var610 = Function('var610', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var732 = Function('var732', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var718 = Function('var718', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var321 = Function('var321', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var786 = Function('var786', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var324 = Function('var324', Object, BoolSort())
var521 = Function('var521', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var545 = Function('var545', Object, BoolSort())
var395 = Function('var395', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var796 = Function('var796', Object, BoolSort())
var461 = Function('var461', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var540 = Function('var540', Object, BoolSort())
var323 = Function('var323', Object, BoolSort())
var705 = Function('var705', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var765 = Function('var765', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var504 = Function('var504', Object, BoolSort())
var673 = Function('var673', Object, BoolSort())
var391 = Function('var391', Object, BoolSort())
var699 = Function('var699', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var459 = Function('var459', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var602 = Function('var602', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var498 = Function('var498', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var601 = Function('var601', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var423 = Function('var423', Object, BoolSort())
var335 = Function('var335', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var309(x), Not(var660(x))))),
	ForAll([x], Not(Or(var160(x), Not(var339(x))))),
	ForAll([x], Not(Or(Not(var365(x)), Not(var781(x))))),
	ForAll([x], Not(Or(var789(x), Not(var186(x))))),
	ForAll([x], Not(Or(Not(var374(x)), Not(var141(x))))),
	ForAll([x], Not(Or(Not(var230(x)), var585(x)))),
	ForAll([x], Not(Or(var623(x), Not(var221(x))))),
	ForAll([x], Not(Or(Not(var32(x)), var388(x)))),
	ForAll([x], Not(Or(var155(x), Not(var273(x))))),
	ForAll([x], Not(Or(var242(x), Not(var364(x))))),
	ForAll([x], Not(Or(Not(var464(x)), var101(x)))),
	ForAll([x], Not(Or(var148(x), var126(x)))),
	ForAll([x], Not(Or(Not(var503(x)), var405(x)))),
	ForAll([x], Not(Or(Not(var184(x)), Not(var79(x))))),
	ForAll([x], Not(Or(var252(x), Not(var90(x))))),
	ForAll([x], Not(Or(var77(x), Not(var246(x))))),
	ForAll([x], Not(Or(var162(x), Not(var538(x))))),
	ForAll([x], Not(Or(var198(x), Not(var268(x))))),
	ForAll([x], Not(Or(var248(x), Not(var549(x))))),
	ForAll([x], Not(Or(Not(var108(x)), var12(x)))),
	ForAll([x], Not(Or(Not(var523(x)), var147(x)))),
	ForAll([x], Not(Or(var282(x), var69(x)))),
	ForAll([x], Not(Or(var264(x), var197(x)))),
	ForAll([x], Not(Or(var51(x), Not(var346(x))))),
	ForAll([x], Not(Or(Not(var315(x)), var104(x)))),
	ForAll([x], Not(Or(var658(x), Not(var337(x))))),
	ForAll([x], Not(Or(Not(var730(x)), var22(x)))),
	ForAll([x], Not(Or(var750(x), Not(var13(x))))),
	ForAll([x], Not(Or(Not(var407(x)), Not(var106(x))))),
	ForAll([x], Not(Or(var275(x), Not(var70(x))))),
	ForAll([x], Not(Or(var4(x), Not(var788(x))))),
	ForAll([x], Not(Or(var676(x), var14(x)))),
	ForAll([x], Not(Or(var270(x), Not(var709(x))))),
	ForAll([x], Not(Or(Not(var387(x)), var724(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var484(x1), var80(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var206(x1)), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var234(x1)), Not(var332(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var71(x1), var355(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var385(x1)), var85(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var58(x1), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var340(x1), var105(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var200(x1)), Not(var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var408(x1), var411(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var149(x1), Not(var291(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var257(x1), var97(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var84(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var357(x1), Not(var455(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var582(x1), var372(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var157(x1), Not(var486(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var217(x1), Not(var499(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var624(x1)), var338(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var55(x1)), var269(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var212(x1)), Not(var180(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var392(x1), Not(var597(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var691(x1), var258(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var72(x1), var118(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var609(x1)), var703(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var228(x1), var183(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var59(x1)), Not(var502(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var191(x1), var44(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var336(x1), var476(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var116(x1)), var19(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var729(x1), Not(var278(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var95(x1)), var313(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var17(x1)), Not(var293(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var755(x1), var304(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var518(x1), Not(var656(x)))))),
	ForAll([x], Not(Or(var213(x), Not(var271(x)), var256(x)))),
	ForAll([x], Not(Or(Not(var356(x)), Not(var649(x)), Not(var129(x))))),
	ForAll([x], Not(Or(var240(x), Not(var120(x)), Not(var99(x))))),
	ForAll([x], Not(Or(var711(x), var67(x), var532(x)))),
	ForAll([x], Not(Or(var347(x), Not(var42(x)), var144(x)))),
	ForAll([x], Not(Or(var361(x), Not(var277(x)), var727(x)))),
	ForAll([x], Not(Or(Not(var37(x)), Not(var286(x)), Not(var156(x))))),
	ForAll([x], Not(Or(var53(x), Not(var310(x)), var196(x)))),
	ForAll([x], Not(Or(Not(var615(x)), Not(var28(x)), var166(x)))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var398(x)), Not(var78(x))))),
	ForAll([x], Not(Or(Not(var38(x)), var622(x), Not(var35(x))))),
	ForAll([x], Not(Or(Not(var290(x)), Not(var74(x)), Not(var396(x))))),
	ForAll([x], Not(Or(Not(var394(x)), var618(x), Not(var665(x))))),
	ForAll([x], Not(Or(Not(var241(x)), Not(var330(x)), Not(var640(x))))),
	ForAll([x], Not(Or(var250(x), var312(x), var328(x)))),
	ForAll([x], Not(Or(Not(var287(x)), Not(var11(x)), Not(var322(x))))),
	ForAll([x], Not(Or(var517(x), Not(var215(x)), Not(var300(x))))),
	ForAll([x], Not(Or(var151(x), var245(x), var757(x)))),
	ForAll([x], Not(Or(Not(var581(x)), Not(var799(x)), Not(var274(x))))),
	ForAll([x], Not(Or(var1(x), var208(x), Not(var272(x))))),
	ForAll([x], Not(Or(Not(var169(x)), var475(x), Not(var350(x))))),
	ForAll([x], Not(Or(Not(var367(x)), var756(x), Not(var211(x))))),
	ForAll([x], Not(Or(var410(x), var243(x), Not(var117(x))))),
	ForAll([x], Not(Or(Not(var782(x)), var652(x), Not(var381(x))))),
	ForAll([x], Not(Or(Not(var450(x)), var23(x), var557(x)))),
	ForAll([x], Not(Or(var341(x), var316(x), Not(var528(x))))),
	ForAll([x], Not(Or(Not(var113(x)), Not(var199(x)), var9(x)))),
	ForAll([x], Not(Or(Not(var110(x)), Not(var52(x)), Not(var636(x))))),
	ForAll([x], Not(Or(var349(x), Not(var7(x)), Not(var134(x))))),
	ForAll([x], Not(Or(var362(x), var536(x), var377(x)))),
	ForAll([x], Not(Or(var399(x), var348(x), var81(x)))),
	ForAll([x], Not(Or(var103(x), var670(x), Not(var302(x))))),
	ForAll([x], Not(Or(Not(var233(x)), var244(x), var342(x)))),
	ForAll([x], Not(Or(var146(x), Not(var201(x)), var331(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var713(x1), var25(x1)), var426(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var128(x1), var260(x1)), Not(var153(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var778(x1), Or(Not(var491(x)), Not(var236(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var60(x1), var379(x1)), Not(var253(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var177(x1), var678(x1)), Not(var194(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var446(x1), Or(Not(var522(x)), Not(var417(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var111(x1), Or(Not(var86(x)), Not(var389(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var235(x1)), Not(var40(x1))), Not(var226(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var419(x1)), Or(var351(x), var91(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var131(x1), var430(x1)), Not(var301(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var188(x1)), Not(var318(x1))), var109(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var325(x1)), var489(x1)), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var547(x1), var46(x1)), Not(var393(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var800(x1)), var406(x1)), var263(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var182(x1)), Or(var18(x), var222(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var468(x1), Or(Not(var353(x)), Not(var382(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var404(x1), Or(var247(x), Not(var6(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var397(x1), Or(Not(var320(x)), var285(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var586(x1), Not(var638(x1))), Not(var371(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var45(x1)), Or(var36(x), Not(var102(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var792(x1), Not(var497(x1))), var27(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var552(x1)), var429(x1)), Not(var259(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var690(x1), var378(x1)), Not(var92(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var73(x1), var542(x1)), Not(var510(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var8(x1)), Or(Not(var251(x)), var493(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var175(x1), Not(var580(x1))), Not(var29(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var721(x1)), Or(Not(var794(x)), var165(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var369(x1), Or(Not(var161(x)), Not(var137(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var594(x1), Not(var136(x1))), Not(var219(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var98(x1), Or(Not(var529(x)), Not(var358(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var401(x1)), Not(var370(x1))), var178(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var56(x1)), Not(var774(x1))), var326(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var174(x1)), var61(x1)), Not(var57(x)))))),
	ForAll([x], Not(Or(var62(x), var93(x), var728(x), var627(x)))),
	ForAll([x], Not(Or(Not(var41(x)), var127(x), var189(x), Not(var150(x))))),
	ForAll([x], Not(Or(var402(x), Not(var551(x)), Not(var524(x)), Not(var210(x))))),
	ForAll([x], Not(Or(var281(x), var288(x), var482(x), Not(var741(x))))),
	ForAll([x], Not(Or(var124(x), var283(x), var707(x), var768(x)))),
	ForAll([x], Not(Or(Not(var599(x)), Not(var515(x)), Not(var163(x)), var494(x)))),
	ForAll([x], Not(Or(var685(x), Not(var344(x)), var766(x), Not(var262(x))))),
	ForAll([x], Not(Or(var375(x), Not(var343(x)), var541(x), var292(x)))),
	ForAll([x], Not(Or(var220(x), var588(x), var327(x), Not(var589(x))))),
	ForAll([x], Not(Or(var333(x), var107(x), var223(x), Not(var363(x))))),
	ForAll([x], Not(Or(var644(x), Not(var20(x)), Not(var255(x)), var777(x)))),
	ForAll([x], Not(Or(Not(var239(x)), Not(var195(x)), Not(var138(x)), var204(x)))),
	ForAll([x], Not(Or(Not(var135(x)), var63(x), Not(var125(x)), var383(x)))),
	ForAll([x], Not(Or(var373(x), var154(x), Not(var496(x)), var425(x)))),
	ForAll([x], Not(Or(Not(var297(x)), Not(var613(x)), var167(x), Not(var190(x))))),
	ForAll([x], Not(Or(var680(x), Not(var697(x)), var650(x), var289(x)))),
	ForAll([x], Not(Or(var159(x), var295(x), var439(x), var227(x)))),
	ForAll([x], Not(Or(Not(var168(x)), Not(var600(x)), var675(x), var516(x)))),
	ForAll([x], Not(Or(Not(var284(x)), var646(x), var308(x), var142(x)))),
	ForAll([x], Not(Or(Not(var33(x)), Not(var307(x)), Not(var694(x)), var451(x)))),
	ForAll([x], Not(Or(Not(var5(x)), var16(x), Not(var10(x)), var745(x)))),
	ForAll([x], Not(Or(Not(var592(x)), Not(var133(x)), Not(var15(x)), Not(var171(x))))),
	ForAll([x], Not(Or(Not(var205(x)), var209(x), var94(x), Not(var112(x))))),
	ForAll([x], Not(Or(var329(x), var403(x), var24(x), var68(x)))),
	ForAll([x], Not(Or(Not(var780(x)), Not(var345(x)), var380(x), Not(var114(x))))),
	ForAll([x], Not(Or(var576(x), Not(var75(x)), Not(var88(x)), var298(x)))),
	ForAll([x], Not(Or(var354(x), var50(x), var606(x), var303(x)))),
	ForAll([x], Not(Or(var458(x), var462(x), var625(x), var334(x)))),
	ForAll([x], Not(Or(var359(x), Not(var566(x)), Not(var715(x)), Not(var49(x))))),
	ForAll([x], Not(Or(var65(x), var181(x), var485(x), var505(x)))),
	ForAll([x], Not(Or(Not(var511(x)), var203(x), var603(x), var754(x)))),
	ForAll([x], Not(Or(var708(x), Not(var573(x)), var214(x), Not(var139(x))))),
	ForAll([x], Not(Or(var130(x), var415(x), Not(var507(x)), var232(x)))),
	ForAll([x], Not(Or(var43(x), var145(x), Not(var319(x)), var229(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var311(x1)), Not(var667(x1)), Not(var428(x1))), var384(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var152(x1)), var544(x1), Not(var119(x1))), var722(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var261(x1), var671(x1), Not(var185(x1))), Not(var31(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var64(x1), Not(var143(x1))), Or(Not(var39(x)), var512(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var761(x1)), Or(Not(var87(x)), var83(x), var218(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var736(x1), var386(x1), Not(var276(x1))), Not(var470(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var368(x1), Not(var456(x1)), var444(x1)), Not(var433(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var54(x1)), var400(x1)), Or(var617(x), var686(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var366(x1)), Not(var748(x1)), var305(x1)), var26(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var193(x1), var514(x1)), Or(Not(var376(x)), Not(var687(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var352(x1), Or(Not(var123(x)), var96(x), Not(var115(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var590(x1)), Or(Not(var216(x)), Not(var306(x)), var714(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var254(x1), var742(x1)), Or(var747(x), Not(var637(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var480(x1), var447(x1)), Or(Not(var390(x)), Not(var266(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var785(x1)), var666(x1), var296(x1)), var776(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var760(x1)), Or(Not(var170(x)), var179(x), var238(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var560(x1), Not(var716(x1))), Or(Not(var712(x)), var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var192(x1), Not(var710(x1))), Or(Not(var317(x)), Not(var280(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var696(x1)), var539(x1)), Or(var265(x), var132(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var610(x1)), Or(var176(x), var66(x), var732(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var237(x1)), Or(var76(x), Not(var121(x)), var718(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var267(x1), Or(Not(var321(x)), Not(var224(x)), Not(var786(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var207(x1)), Or(Not(var231(x)), Not(var360(x)), var140(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var202(x1), Not(var324(x1)), Not(var521(x1))), Not(var164(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var545(x1), Or(Not(var395(x)), var172(x), Not(var796(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var461(x1)), Not(var122(x1)), var540(x1)), Not(var323(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var705(x1)), Not(var249(x1))), Or(Not(var3(x)), Not(var299(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var765(x1)), Or(Not(var279(x)), Not(var504(x)), var673(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var391(x1), Or(var699(x), Not(var173(x)), Not(var314(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var459(x1), var47(x1), var602(x1)), var294(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var498(x1)), Or(Not(var89(x)), Not(var601(x)), Not(var100(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var225(x1)), Not(var187(x1)), Not(var423(x1))), Not(var335(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
