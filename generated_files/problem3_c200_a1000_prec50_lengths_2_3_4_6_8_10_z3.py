from z3 import *

Object = DeclareSort('Object')

var269 = Function('var269', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var371 = Function('var371', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var963 = Function('var963', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var446 = Function('var446', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var564 = Function('var564', Object, BoolSort())
var743 = Function('var743', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var331 = Function('var331', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var364 = Function('var364', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var755 = Function('var755', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var316 = Function('var316', Object, BoolSort())
var711 = Function('var711', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var455 = Function('var455', Object, BoolSort())
var573 = Function('var573', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var659 = Function('var659', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var654 = Function('var654', Object, BoolSort())
var825 = Function('var825', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var733 = Function('var733', Object, BoolSort())
var712 = Function('var712', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var671 = Function('var671', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var779 = Function('var779', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var478 = Function('var478', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var893 = Function('var893', Object, BoolSort())
var870 = Function('var870', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var791 = Function('var791', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var761 = Function('var761', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var880 = Function('var880', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var594 = Function('var594', Object, BoolSort())
var369 = Function('var369', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var991 = Function('var991', Object, BoolSort())
var534 = Function('var534', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var301 = Function('var301', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var560 = Function('var560', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var803 = Function('var803', Object, BoolSort())
var388 = Function('var388', Object, BoolSort())
var902 = Function('var902', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var835 = Function('var835', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var602 = Function('var602', Object, BoolSort())
var463 = Function('var463', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var732 = Function('var732', Object, BoolSort())
var919 = Function('var919', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var570 = Function('var570', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var961 = Function('var961', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var368 = Function('var368', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var426 = Function('var426', Object, BoolSort())
var985 = Function('var985', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var966 = Function('var966', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var993 = Function('var993', Object, BoolSort())
var862 = Function('var862', Object, BoolSort())
var486 = Function('var486', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var468 = Function('var468', Object, BoolSort())
var887 = Function('var887', Object, BoolSort())
var428 = Function('var428', Object, BoolSort())
var543 = Function('var543', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var806 = Function('var806', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var298 = Function('var298', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var536 = Function('var536', Object, BoolSort())
var437 = Function('var437', Object, BoolSort())
var340 = Function('var340', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var723 = Function('var723', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var899 = Function('var899', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var347 = Function('var347', Object, BoolSort())
var931 = Function('var931', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var648 = Function('var648', Object, BoolSort())
var998 = Function('var998', Object, BoolSort())
var608 = Function('var608', Object, BoolSort())
var427 = Function('var427', Object, BoolSort())
var823 = Function('var823', Object, BoolSort())
var955 = Function('var955', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var485 = Function('var485', Object, BoolSort())
var726 = Function('var726', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var621 = Function('var621', Object, BoolSort())
var618 = Function('var618', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var753 = Function('var753', Object, BoolSort())
var742 = Function('var742', Object, BoolSort())
var829 = Function('var829', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var481 = Function('var481', Object, BoolSort())
var626 = Function('var626', Object, BoolSort())
var699 = Function('var699', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var767 = Function('var767', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var820 = Function('var820', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var320 = Function('var320', Object, BoolSort())
var754 = Function('var754', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var815 = Function('var815', Object, BoolSort())
var884 = Function('var884', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var484 = Function('var484', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var907 = Function('var907', Object, BoolSort())
var633 = Function('var633', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var744 = Function('var744', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var497 = Function('var497', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var375 = Function('var375', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var706 = Function('var706', Object, BoolSort())
var846 = Function('var846', Object, BoolSort())
var1000 = Function('var1000', Object, BoolSort())
var268 = Function('var268', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var507 = Function('var507', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var384 = Function('var384', Object, BoolSort())
var960 = Function('var960', Object, BoolSort())
var333 = Function('var333', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var868 = Function('var868', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var376 = Function('var376', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var759 = Function('var759', Object, BoolSort())
var730 = Function('var730', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var600 = Function('var600', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var575 = Function('var575', Object, BoolSort())
var632 = Function('var632', Object, BoolSort())
var558 = Function('var558', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var923 = Function('var923', Object, BoolSort())
var445 = Function('var445', Object, BoolSort())
var559 = Function('var559', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var749 = Function('var749', Object, BoolSort())
var953 = Function('var953', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var746 = Function('var746', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var469 = Function('var469', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var492 = Function('var492', Object, BoolSort())
var734 = Function('var734', Object, BoolSort())
var713 = Function('var713', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var304 = Function('var304', Object, BoolSort())
var728 = Function('var728', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var500 = Function('var500', Object, BoolSort())
var864 = Function('var864', Object, BoolSort())
var462 = Function('var462', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var844 = Function('var844', Object, BoolSort())
var927 = Function('var927', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var587 = Function('var587', Object, BoolSort())
var818 = Function('var818', Object, BoolSort())
var725 = Function('var725', Object, BoolSort())
var609 = Function('var609', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var296 = Function('var296', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var688 = Function('var688', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var997 = Function('var997', Object, BoolSort())
var339 = Function('var339', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var948 = Function('var948', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var752 = Function('var752', Object, BoolSort())
var947 = Function('var947', Object, BoolSort())
var686 = Function('var686', Object, BoolSort())
var288 = Function('var288', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var623 = Function('var623', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var695 = Function('var695', Object, BoolSort())
var710 = Function('var710', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var885 = Function('var885', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var399 = Function('var399', Object, BoolSort())
var267 = Function('var267', Object, BoolSort())
var414 = Function('var414', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var549 = Function('var549', Object, BoolSort())
var918 = Function('var918', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var539 = Function('var539', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var275 = Function('var275', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var512 = Function('var512', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var511 = Function('var511', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var585 = Function('var585', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var978 = Function('var978', Object, BoolSort())
var696 = Function('var696', Object, BoolSort())
var794 = Function('var794', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var698 = Function('var698', Object, BoolSort())
var691 = Function('var691', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var407 = Function('var407', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var614 = Function('var614', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var750 = Function('var750', Object, BoolSort())
var900 = Function('var900', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var531 = Function('var531', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var470 = Function('var470', Object, BoolSort())
var976 = Function('var976', Object, BoolSort())
var546 = Function('var546', Object, BoolSort())
var502 = Function('var502', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var569 = Function('var569', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var611 = Function('var611', Object, BoolSort())
var474 = Function('var474', Object, BoolSort())
var457 = Function('var457', Object, BoolSort())
var775 = Function('var775', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var524 = Function('var524', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var421 = Function('var421', Object, BoolSort())
var682 = Function('var682', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var718 = Function('var718', Object, BoolSort())
var786 = Function('var786', Object, BoolSort())
var637 = Function('var637', Object, BoolSort())
var981 = Function('var981', Object, BoolSort())
var810 = Function('var810', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var910 = Function('var910', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var422 = Function('var422', Object, BoolSort())
var593 = Function('var593', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var809 = Function('var809', Object, BoolSort())
var782 = Function('var782', Object, BoolSort())
var309 = Function('var309', Object, BoolSort())
var783 = Function('var783', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var568 = Function('var568', Object, BoolSort())
var527 = Function('var527', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var353 = Function('var353', Object, BoolSort())
var273 = Function('var273', Object, BoolSort())
var519 = Function('var519', Object, BoolSort())
var765 = Function('var765', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var429 = Function('var429', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var684 = Function('var684', Object, BoolSort())
var858 = Function('var858', Object, BoolSort())
var477 = Function('var477', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var358 = Function('var358', Object, BoolSort())
var837 = Function('var837', Object, BoolSort())
var299 = Function('var299', Object, BoolSort())
var312 = Function('var312', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var454 = Function('var454', Object, BoolSort())
var417 = Function('var417', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var914 = Function('var914', Object, BoolSort())
var627 = Function('var627', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var289 = Function('var289', Object, BoolSort())
var354 = Function('var354', Object, BoolSort())
var756 = Function('var756', Object, BoolSort())
var540 = Function('var540', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var897 = Function('var897', Object, BoolSort())
var412 = Function('var412', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var495 = Function('var495', Object, BoolSort())
var394 = Function('var394', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var678 = Function('var678', Object, BoolSort())
var773 = Function('var773', Object, BoolSort())
var856 = Function('var856', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var925 = Function('var925', Object, BoolSort())
var449 = Function('var449', Object, BoolSort())
var972 = Function('var972', Object, BoolSort())
var396 = Function('var396', Object, BoolSort())
var574 = Function('var574', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var646 = Function('var646', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var811 = Function('var811', Object, BoolSort())
var604 = Function('var604', Object, BoolSort())
var920 = Function('var920', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var561 = Function('var561', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var628 = Function('var628', Object, BoolSort())
var766 = Function('var766', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var860 = Function('var860', Object, BoolSort())
var673 = Function('var673', Object, BoolSort())
var547 = Function('var547', Object, BoolSort())
var404 = Function('var404', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var973 = Function('var973', Object, BoolSort())
var522 = Function('var522', Object, BoolSort())
var410 = Function('var410', Object, BoolSort())
var348 = Function('var348', Object, BoolSort())
var954 = Function('var954', Object, BoolSort())
var510 = Function('var510', Object, BoolSort())
var610 = Function('var610', Object, BoolSort())
var946 = Function('var946', Object, BoolSort())
var980 = Function('var980', Object, BoolSort())
var314 = Function('var314', Object, BoolSort())
var959 = Function('var959', Object, BoolSort())
var277 = Function('var277', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var544 = Function('var544', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var393 = Function('var393', Object, BoolSort())
var624 = Function('var624', Object, BoolSort())
var553 = Function('var553', Object, BoolSort())
var974 = Function('var974', Object, BoolSort())
var491 = Function('var491', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var635 = Function('var635', Object, BoolSort())
var933 = Function('var933', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var778 = Function('var778', Object, BoolSort())
var915 = Function('var915', Object, BoolSort())
var577 = Function('var577', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var518 = Function('var518', Object, BoolSort())
var802 = Function('var802', Object, BoolSort())
var589 = Function('var589', Object, BoolSort())
var861 = Function('var861', Object, BoolSort())
var499 = Function('var499', Object, BoolSort())
var653 = Function('var653', Object, BoolSort())
var999 = Function('var999', Object, BoolSort())
var473 = Function('var473', Object, BoolSort())
var801 = Function('var801', Object, BoolSort())
var891 = Function('var891', Object, BoolSort())
var851 = Function('var851', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var838 = Function('var838', Object, BoolSort())
var852 = Function('var852', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var995 = Function('var995', Object, BoolSort())
var790 = Function('var790', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var334 = Function('var334', Object, BoolSort())
var909 = Function('var909', Object, BoolSort())
var781 = Function('var781', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var380 = Function('var380', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var785 = Function('var785', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var827 = Function('var827', Object, BoolSort())
var514 = Function('var514', Object, BoolSort())
var441 = Function('var441', Object, BoolSort())
var676 = Function('var676', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var656 = Function('var656', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var936 = Function('var936', Object, BoolSort())
var582 = Function('var582', Object, BoolSort())
var596 = Function('var596', Object, BoolSort())
var990 = Function('var990', Object, BoolSort())
var881 = Function('var881', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var504 = Function('var504', Object, BoolSort())
var619 = Function('var619', Object, BoolSort())
var792 = Function('var792', Object, BoolSort())
var487 = Function('var487', Object, BoolSort())
var295 = Function('var295', Object, BoolSort())
var476 = Function('var476', Object, BoolSort())
var652 = Function('var652', Object, BoolSort())
var957 = Function('var957', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var882 = Function('var882', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var748 = Function('var748', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var629 = Function('var629', Object, BoolSort())
var854 = Function('var854', Object, BoolSort())
var529 = Function('var529', Object, BoolSort())
var848 = Function('var848', Object, BoolSort())
var391 = Function('var391', Object, BoolSort())
var800 = Function('var800', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var913 = Function('var913', Object, BoolSort())
var968 = Function('var968', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var672 = Function('var672', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var952 = Function('var952', Object, BoolSort())
var740 = Function('var740', Object, BoolSort())
var911 = Function('var911', Object, BoolSort())
var459 = Function('var459', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var620 = Function('var620', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var436 = Function('var436', Object, BoolSort())
var291 = Function('var291', Object, BoolSort())
var634 = Function('var634', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var917 = Function('var917', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var269(x)), var5(x)))),
	ForAll([x], Not(Or(var154(x), Not(var371(x))))),
	ForAll([x], Not(Or(Not(var173(x)), Not(var85(x))))),
	ForAll([x], Not(Or(var7(x), var963(x)))),
	ForAll([x], Not(Or(Not(var245(x)), var194(x)))),
	ForAll([x], Not(Or(var15(x), Not(var446(x))))),
	ForAll([x], Not(Or(var45(x), Not(var564(x))))),
	ForAll([x], Not(Or(Not(var743(x)), Not(var104(x))))),
	ForAll([x], Not(Or(Not(var251(x)), var311(x)))),
	ForAll([x], Not(Or(Not(var187(x)), var214(x)))),
	ForAll([x], Not(Or(var331(x), var281(x)))),
	ForAll([x], Not(Or(var71(x), Not(var215(x))))),
	ForAll([x], Not(Or(var145(x), var364(x)))),
	ForAll([x], Not(Or(Not(var157(x)), var755(x)))),
	ForAll([x], Not(Or(Not(var134(x)), var229(x)))),
	ForAll([x], Not(Or(var88(x), Not(var25(x))))),
	ForAll([x], Not(Or(var316(x), Not(var711(x))))),
	ForAll([x], Not(Or(Not(var97(x)), Not(var253(x))))),
	ForAll([x], Not(Or(Not(var455(x)), var573(x)))),
	ForAll([x], Not(Or(var110(x), Not(var151(x))))),
	ForAll([x], Not(Or(var659(x), var227(x)))),
	ForAll([x], Not(Or(var13(x), Not(var654(x))))),
	ForAll([x], Not(Or(var825(x), var86(x)))),
	ForAll([x], Not(Or(var10(x), var4(x)))),
	ForAll([x], Not(Or(Not(var133(x)), Not(var84(x))))),
	ForAll([x], Not(Or(Not(var733(x)), Not(var712(x))))),
	ForAll([x], Not(Or(Not(var166(x)), Not(var102(x))))),
	ForAll([x], Not(Or(var671(x), var117(x)))),
	ForAll([x], Not(Or(var779(x), var79(x)))),
	ForAll([x], Not(Or(Not(var148(x)), var478(x)))),
	ForAll([x], Not(Or(var37(x), Not(var893(x))))),
	ForAll([x], Not(Or(Not(var870(x)), Not(var52(x))))),
	ForAll([x], Not(Or(var360(x), Not(var791(x))))),
	ForAll([x], Not(Or(var111(x), var761(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var172(x1)), Not(var880(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var67(x1), Not(var53(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var231(x1), var3(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var266(x1), var6(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var594(x1), Not(var369(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var36(x1), Not(var213(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var991(x1)), var534(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var94(x1)), var210(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var42(x1)), Not(var109(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var198(x1)), var28(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var301(x1), Not(var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var189(x1), Not(var265(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var560(x1)), Not(var254(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var246(x1)), var152(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var803(x1), var388(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var902(x1)), Not(var158(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var216(x1)), Not(var124(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var835(x1)), var121(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var159(x1), Not(var602(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var463(x1), var112(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var732(x1), var919(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var146(x1), Not(var570(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var138(x1), var961(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var242(x1)), Not(var106(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var68(x1)), var21(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var24(x1)), var49(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var368(x1)), Not(var93(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var426(x1), Not(var985(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var70(x1), Not(var60(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var174(x1), Not(var30(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var966(x1)), Not(var271(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var993(x1), Not(var862(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var486(x1), Not(var184(x)))))),
	ForAll([x], Not(Or(var165(x), var468(x), Not(var887(x))))),
	ForAll([x], Not(Or(var428(x), Not(var543(x)), Not(var233(x))))),
	ForAll([x], Not(Or(Not(var191(x)), var806(x), Not(var247(x))))),
	ForAll([x], Not(Or(var298(x), Not(var222(x)), Not(var536(x))))),
	ForAll([x], Not(Or(var437(x), Not(var340(x)), var35(x)))),
	ForAll([x], Not(Or(Not(var264(x)), var723(x), Not(var132(x))))),
	ForAll([x], Not(Or(Not(var14(x)), Not(var899(x)), var200(x)))),
	ForAll([x], Not(Or(Not(var29(x)), var64(x), Not(var34(x))))),
	ForAll([x], Not(Or(var232(x), var303(x), var347(x)))),
	ForAll([x], Not(Or(Not(var931(x)), Not(var119(x)), Not(var221(x))))),
	ForAll([x], Not(Or(Not(var648(x)), var998(x), var608(x)))),
	ForAll([x], Not(Or(var427(x), Not(var823(x)), var955(x)))),
	ForAll([x], Not(Or(var260(x), Not(var118(x)), var72(x)))),
	ForAll([x], Not(Or(Not(var83(x)), var485(x), Not(var726(x))))),
	ForAll([x], Not(Or(Not(var16(x)), Not(var11(x)), Not(var103(x))))),
	ForAll([x], Not(Or(var621(x), Not(var618(x)), var61(x)))),
	ForAll([x], Not(Or(Not(var129(x)), Not(var38(x)), var753(x)))),
	ForAll([x], Not(Or(Not(var742(x)), var829(x), var243(x)))),
	ForAll([x], Not(Or(Not(var481(x)), Not(var626(x)), Not(var699(x))))),
	ForAll([x], Not(Or(Not(var249(x)), var31(x), Not(var95(x))))),
	ForAll([x], Not(Or(Not(var767(x)), var20(x), Not(var12(x))))),
	ForAll([x], Not(Or(Not(var820(x)), Not(var66(x)), Not(var320(x))))),
	ForAll([x], Not(Or(var754(x), Not(var116(x)), Not(var55(x))))),
	ForAll([x], Not(Or(var91(x), Not(var209(x)), Not(var815(x))))),
	ForAll([x], Not(Or(var884(x), var161(x), Not(var207(x))))),
	ForAll([x], Not(Or(var484(x), var397(x), Not(var907(x))))),
	ForAll([x], Not(Or(Not(var633(x)), var135(x), Not(var256(x))))),
	ForAll([x], Not(Or(var142(x), Not(var136(x)), var744(x)))),
	ForAll([x], Not(Or(var153(x), var54(x), var497(x)))),
	ForAll([x], Not(Or(Not(var239(x)), var244(x), Not(var375(x))))),
	ForAll([x], Not(Or(var185(x), Not(var706(x)), Not(var846(x))))),
	ForAll([x], Not(Or(var1000(x), var268(x), var193(x)))),
	ForAll([x], Not(Or(var87(x), Not(var507(x)), Not(var211(x))))),
	ForAll([x], Not(Or(var384(x), var960(x), var333(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var155(x1), Or(var868(x), Not(var169(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var130(x1)), Not(var188(x1))), var376(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var44(x1), Not(var47(x1))), Not(var19(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var160(x1), Or(Not(var206(x)), var113(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var58(x1)), Or(Not(var101(x)), Not(var228(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var759(x1)), var730(x1)), Not(var178(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var600(x1), var65(x1)), Not(var575(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var632(x1), var558(x1)), Not(var73(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var923(x1)), Or(var445(x), var559(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var208(x1)), Or(Not(var749(x)), var953(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var234(x1), var141(x1)), var746(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var115(x1)), Not(var469(x1))), var105(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var190(x1)), var492(x1)), Not(var734(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var713(x1), Not(var57(x1))), Not(var304(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var728(x1)), Or(var204(x), var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var500(x1), Not(var864(x1))), Not(var462(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var263(x1)), var75(x1)), var844(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var927(x1), var248(x1)), Not(var587(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var818(x1), Not(var725(x1))), Not(var609(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var140(x1)), Or(var144(x), Not(var296(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var223(x1)), Not(var257(x1))), Not(var688(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var197(x1)), Not(var76(x1))), var997(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var339(x1)), Or(Not(var48(x)), Not(var212(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var948(x1)), Not(var156(x1))), var752(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var947(x1), var686(x1)), Not(var288(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var217(x1), Or(var623(x), var180(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var695(x1), Not(var710(x1))), Not(var177(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var885(x1), Not(var162(x1))), Not(var74(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var399(x1)), Or(Not(var267(x)), Not(var414(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var131(x1), Or(Not(var549(x)), var918(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var352(x1), var149(x1)), Not(var539(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var480(x1)), var9(x1)), Not(var275(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var98(x1), Or(var258(x), var512(x)))))),
	ForAll([x], Not(Or(Not(var270(x)), var374(x), Not(var511(x)), Not(var262(x))))),
	ForAll([x], Not(Or(Not(var585(x)), var77(x), var240(x), var978(x)))),
	ForAll([x], Not(Or(var696(x), Not(var794(x)), var120(x), var33(x)))),
	ForAll([x], Not(Or(Not(var2(x)), Not(var92(x)), Not(var698(x)), Not(var691(x))))),
	ForAll([x], Not(Or(var78(x), var41(x), Not(var46(x)), var179(x)))),
	ForAll([x], Not(Or(var241(x), Not(var226(x)), var407(x), var56(x)))),
	ForAll([x], Not(Or(Not(var50(x)), var614(x), Not(var176(x)), Not(var750(x))))),
	ForAll([x], Not(Or(var900(x), var400(x), Not(var531(x)), Not(var464(x))))),
	ForAll([x], Not(Or(Not(var470(x)), Not(var976(x)), var546(x), var502(x)))),
	ForAll([x], Not(Or(Not(var107(x)), Not(var569(x)), var237(x), Not(var279(x))))),
	ForAll([x], Not(Or(var51(x), var611(x), var474(x), var457(x)))),
	ForAll([x], Not(Or(var775(x), var203(x), Not(var69(x)), var524(x)))),
	ForAll([x], Not(Or(var139(x), Not(var99(x)), var23(x), var421(x)))),
	ForAll([x], Not(Or(Not(var682(x)), var328(x), Not(var718(x)), var786(x)))),
	ForAll([x], Not(Or(Not(var637(x)), Not(var981(x)), Not(var810(x)), var252(x)))),
	ForAll([x], Not(Or(var238(x), Not(var910(x)), var96(x), var230(x)))),
	ForAll([x], Not(Or(var422(x), var593(x), Not(var122(x)), var809(x)))),
	ForAll([x], Not(Or(var782(x), var309(x), var783(x), var126(x)))),
	ForAll([x], Not(Or(Not(var181(x)), Not(var568(x)), Not(var527(x)), var108(x)))),
	ForAll([x], Not(Or(var353(x), var273(x), var519(x), var765(x)))),
	ForAll([x], Not(Or(Not(var255(x)), var429(x), var163(x), var684(x)))),
	ForAll([x], Not(Or(Not(var858(x)), Not(var477(x)), Not(var196(x)), Not(var358(x))))),
	ForAll([x], Not(Or(Not(var837(x)), Not(var299(x)), var312(x), Not(var164(x))))),
	ForAll([x], Not(Or(var454(x), Not(var417(x)), var123(x), Not(var205(x))))),
	ForAll([x], Not(Or(Not(var167(x)), Not(var315(x)), var914(x), var627(x)))),
	ForAll([x], Not(Or(Not(var62(x)), var289(x), var354(x), Not(var756(x))))),
	ForAll([x], Not(Or(var540(x), var32(x), var897(x), var412(x)))),
	ForAll([x], Not(Or(var219(x), var495(x), Not(var394(x)), var90(x)))),
	ForAll([x], Not(Or(Not(var678(x)), Not(var773(x)), Not(var856(x)), Not(var81(x))))),
	ForAll([x], Not(Or(Not(var170(x)), var143(x), Not(var925(x)), Not(var449(x))))),
	ForAll([x], Not(Or(Not(var972(x)), var396(x), var574(x), var182(x)))),
	ForAll([x], Not(Or(Not(var646(x)), Not(var199(x)), var236(x), var225(x)))),
	ForAll([x], Not(Or(var218(x), Not(var125(x)), Not(var359(x)), Not(var811(x))))),
	ForAll([x], Not(Or(var604(x), var920(x), Not(var127(x)), Not(var561(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var274(x1), Or(Not(var628(x)), var766(x), var235(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var39(x1)), Not(var860(x1)), var673(x1)), Not(var547(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var404(x1)), Not(var89(x1))), Or(var973(x), Not(var522(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var410(x1)), Or(var348(x), Not(var954(x)), var510(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var610(x1)), Or(var946(x), var980(x), Not(var314(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var959(x1)), var277(x1), var82(x1)), Not(var100(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var544(x1), Not(var137(x1))), Or(Not(var393(x)), var624(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var553(x1), Or(var974(x), var491(x), var18(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var128(x1)), var635(x1)), Or(var933(x), var202(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var283(x1)), Or(Not(var8(x)), Not(var261(x)), var26(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var778(x1)), Not(var915(x1))), Or(var577(x), var147(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var250(x1), Or(Not(var518(x)), var802(x), Not(var589(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var861(x1)), Or(var499(x), var653(x), var999(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var473(x1), var801(x1), var891(x1)), var851(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var114(x1)), Not(var80(x1)), var838(x1)), var852(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var183(x1), Not(var995(x1))), Or(var790(x), var224(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var334(x1), var909(x1), var781(x1)), Not(var150(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var220(x1)), Not(var380(x1)), var63(x1)), Not(var192(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var785(x1), Not(var305(x1))), Or(Not(var175(x)), var827(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var514(x1)), Or(Not(var441(x)), var676(x), var195(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var383(x1)), Or(var656(x), var59(x), Not(var936(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var582(x1)), var596(x1), var990(x1)), Not(var881(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var171(x1), var504(x1)), Or(var619(x), var792(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var487(x1)), Not(var295(x1))), Or(var476(x), var652(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var957(x1), Or(var17(x), Not(var259(x)), var882(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var40(x1)), Not(var748(x1))), Or(Not(var319(x)), var629(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var854(x1), var529(x1)), Or(var848(x), Not(var391(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var800(x1)), Not(var415(x1))), Or(Not(var913(x)), var968(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var43(x1)), var168(x1)), Or(Not(var672(x)), var186(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var952(x1)), Not(var740(x1))), Or(Not(var911(x)), Not(var459(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var342(x1)), Not(var620(x1))), Or(var27(x), Not(var436(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var291(x1)), Or(var634(x), Not(var201(x)), var917(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
