from z3 import *

Object = DeclareSort('Object')

var120 = Function('var120', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var656 = Function('var656', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var549 = Function('var549', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var480 = Function('var480', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var432 = Function('var432', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var913 = Function('var913', Object, BoolSort())
var476 = Function('var476', Object, BoolSort())
var242 = Function('var242', Object, BoolSort())
var235 = Function('var235', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var245 = Function('var245', Object, BoolSort())
var361 = Function('var361', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var563 = Function('var563', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var701 = Function('var701', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var908 = Function('var908', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var901 = Function('var901', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var221 = Function('var221', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var923 = Function('var923', Object, BoolSort())
var564 = Function('var564', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var806 = Function('var806', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var733 = Function('var733', Object, BoolSort())
var213 = Function('var213', Object, BoolSort())
var219 = Function('var219', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var254 = Function('var254', Object, BoolSort())
var991 = Function('var991', Object, BoolSort())
var218 = Function('var218', Object, BoolSort())
var479 = Function('var479', Object, BoolSort())
var236 = Function('var236', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var622 = Function('var622', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var252 = Function('var252', Object, BoolSort())
var257 = Function('var257', Object, BoolSort())
var881 = Function('var881', Object, BoolSort())
var604 = Function('var604', Object, BoolSort())
var305 = Function('var305', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var905 = Function('var905', Object, BoolSort())
var546 = Function('var546', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var664 = Function('var664', Object, BoolSort())
var705 = Function('var705', Object, BoolSort())
var404 = Function('var404', Object, BoolSort())
var621 = Function('var621', Object, BoolSort())
var900 = Function('var900', Object, BoolSort())
var814 = Function('var814', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var680 = Function('var680', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var234 = Function('var234', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var248 = Function('var248', Object, BoolSort())
var266 = Function('var266', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var880 = Function('var880', Object, BoolSort())
var508 = Function('var508', Object, BoolSort())
var311 = Function('var311', Object, BoolSort())
var672 = Function('var672', Object, BoolSort())
var968 = Function('var968', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var246 = Function('var246', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var793 = Function('var793', Object, BoolSort())
var541 = Function('var541', Object, BoolSort())
var773 = Function('var773', Object, BoolSort())
var243 = Function('var243', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var783 = Function('var783', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var858 = Function('var858', Object, BoolSort())
var911 = Function('var911', Object, BoolSort())
var649 = Function('var649', Object, BoolSort())
var853 = Function('var853', Object, BoolSort())
var952 = Function('var952', Object, BoolSort())
var203 = Function('var203', Object, BoolSort())
var630 = Function('var630', Object, BoolSort())
var389 = Function('var389', Object, BoolSort())
var550 = Function('var550', Object, BoolSort())
var210 = Function('var210', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var415 = Function('var415', Object, BoolSort())
var659 = Function('var659', Object, BoolSort())
var922 = Function('var922', Object, BoolSort())
var225 = Function('var225', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var694 = Function('var694', Object, BoolSort())
var708 = Function('var708', Object, BoolSort())
var719 = Function('var719', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var530 = Function('var530', Object, BoolSort())
var466 = Function('var466', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var485 = Function('var485', Object, BoolSort())
var876 = Function('var876', Object, BoolSort())
var974 = Function('var974', Object, BoolSort())
var255 = Function('var255', Object, BoolSort())
var579 = Function('var579', Object, BoolSort())
var921 = Function('var921', Object, BoolSort())
var260 = Function('var260', Object, BoolSort())
var223 = Function('var223', Object, BoolSort())
var456 = Function('var456', Object, BoolSort())
var851 = Function('var851', Object, BoolSort())
var681 = Function('var681', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var684 = Function('var684', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var465 = Function('var465', Object, BoolSort())
var867 = Function('var867', Object, BoolSort())
var942 = Function('var942', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var282 = Function('var282', Object, BoolSort())
var224 = Function('var224', Object, BoolSort())
var675 = Function('var675', Object, BoolSort())
var893 = Function('var893', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var376 = Function('var376', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var832 = Function('var832', Object, BoolSort())
var249 = Function('var249', Object, BoolSort())
var658 = Function('var658', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var884 = Function('var884', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var571 = Function('var571', Object, BoolSort())
var303 = Function('var303', Object, BoolSort())
var754 = Function('var754', Object, BoolSort())
var961 = Function('var961', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var214 = Function('var214', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var317 = Function('var317', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var287 = Function('var287', Object, BoolSort())
var208 = Function('var208', Object, BoolSort())
var319 = Function('var319', Object, BoolSort())
var963 = Function('var963', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var464 = Function('var464', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var232 = Function('var232', Object, BoolSort())
var782 = Function('var782', Object, BoolSort())
var585 = Function('var585', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var632 = Function('var632', Object, BoolSort())
var915 = Function('var915', Object, BoolSort())
var823 = Function('var823', Object, BoolSort())
var871 = Function('var871', Object, BoolSort())
var270 = Function('var270', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var538 = Function('var538', Object, BoolSort())
var714 = Function('var714', Object, BoolSort())
var332 = Function('var332', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var977 = Function('var977', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var886 = Function('var886', Object, BoolSort())
var721 = Function('var721', Object, BoolSort())
var201 = Function('var201', Object, BoolSort())
var643 = Function('var643', Object, BoolSort())
var588 = Function('var588', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var310 = Function('var310', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var825 = Function('var825', Object, BoolSort())
var595 = Function('var595', Object, BoolSort())
var996 = Function('var996', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var932 = Function('var932', Object, BoolSort())
var250 = Function('var250', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var352 = Function('var352', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var444 = Function('var444', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var241 = Function('var241', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var917 = Function('var917', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var231 = Function('var231', Object, BoolSort())
var532 = Function('var532', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var372 = Function('var372', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var477 = Function('var477', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var882 = Function('var882', Object, BoolSort())
var999 = Function('var999', Object, BoolSort())
var640 = Function('var640', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var987 = Function('var987', Object, BoolSort())
var392 = Function('var392', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var202 = Function('var202', Object, BoolSort())
var251 = Function('var251', Object, BoolSort())
var505 = Function('var505', Object, BoolSort())
var457 = Function('var457', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var780 = Function('var780', Object, BoolSort())
var461 = Function('var461', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var796 = Function('var796', Object, BoolSort())
var359 = Function('var359', Object, BoolSort())
var822 = Function('var822', Object, BoolSort())
var551 = Function('var551', Object, BoolSort())
var258 = Function('var258', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var426 = Function('var426', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var414 = Function('var414', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var294 = Function('var294', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var647 = Function('var647', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var542 = Function('var542', Object, BoolSort())
var768 = Function('var768', Object, BoolSort())
var875 = Function('var875', Object, BoolSort())
var342 = Function('var342', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var606 = Function('var606', Object, BoolSort())
var738 = Function('var738', Object, BoolSort())
var726 = Function('var726', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var261 = Function('var261', Object, BoolSort())
var953 = Function('var953', Object, BoolSort())
var336 = Function('var336', Object, BoolSort())
var895 = Function('var895', Object, BoolSort())
var960 = Function('var960', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var374 = Function('var374', Object, BoolSort())
var244 = Function('var244', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var584 = Function('var584', Object, BoolSort())
var978 = Function('var978', Object, BoolSort())
var715 = Function('var715', Object, BoolSort())
var824 = Function('var824', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var756 = Function('var756', Object, BoolSort())
var420 = Function('var420', Object, BoolSort())
var590 = Function('var590', Object, BoolSort())
var938 = Function('var938', Object, BoolSort())
var367 = Function('var367', Object, BoolSort())
var833 = Function('var833', Object, BoolSort())
var207 = Function('var207', Object, BoolSort())
var808 = Function('var808', Object, BoolSort())
var897 = Function('var897', Object, BoolSort())
var425 = Function('var425', Object, BoolSort())
var438 = Function('var438', Object, BoolSort())
var322 = Function('var322', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var534 = Function('var534', Object, BoolSort())
var345 = Function('var345', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var624 = Function('var624', Object, BoolSort())
var341 = Function('var341', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var346 = Function('var346', Object, BoolSort())
var760 = Function('var760', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var993 = Function('var993', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var770 = Function('var770', Object, BoolSort())
var603 = Function('var603', Object, BoolSort())
var902 = Function('var902', Object, BoolSort())
var496 = Function('var496', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var264 = Function('var264', Object, BoolSort())
var481 = Function('var481', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var513 = Function('var513', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var673 = Function('var673', Object, BoolSort())
var811 = Function('var811', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var265 = Function('var265', Object, BoolSort())
var215 = Function('var215', Object, BoolSort())
var220 = Function('var220', Object, BoolSort())
var272 = Function('var272', Object, BoolSort())
var599 = Function('var599', Object, BoolSort())
var967 = Function('var967', Object, BoolSort())
var522 = Function('var522', Object, BoolSort())
var935 = Function('var935', Object, BoolSort())
var387 = Function('var387', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var545 = Function('var545', Object, BoolSort())
var237 = Function('var237', Object, BoolSort())
var842 = Function('var842', Object, BoolSort())
var226 = Function('var226', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var605 = Function('var605', Object, BoolSort())
var560 = Function('var560', Object, BoolSort())
var217 = Function('var217', Object, BoolSort())
var259 = Function('var259', Object, BoolSort())
var712 = Function('var712', Object, BoolSort())
var435 = Function('var435', Object, BoolSort())
var447 = Function('var447', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var641 = Function('var641', Object, BoolSort())
var602 = Function('var602', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var653 = Function('var653', Object, BoolSort())
var362 = Function('var362', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var879 = Function('var879', Object, BoolSort())
var598 = Function('var598', Object, BoolSort())
var746 = Function('var746', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var482 = Function('var482', Object, BoolSort())
var300 = Function('var300', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var777 = Function('var777', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var580 = Function('var580', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var859 = Function('var859', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var826 = Function('var826', Object, BoolSort())
var834 = Function('var834', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var736 = Function('var736', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var872 = Function('var872', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var972 = Function('var972', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var473 = Function('var473', Object, BoolSort())
var846 = Function('var846', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var256 = Function('var256', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var577 = Function('var577', Object, BoolSort())
var283 = Function('var283', Object, BoolSort())
var600 = Function('var600', Object, BoolSort())
var290 = Function('var290', Object, BoolSort())
var601 = Function('var601', Object, BoolSort())
var927 = Function('var927', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var997 = Function('var997', Object, BoolSort())
var734 = Function('var734', Object, BoolSort())
var889 = Function('var889', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var781 = Function('var781', Object, BoolSort())
var610 = Function('var610', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var818 = Function('var818', Object, BoolSort())
var697 = Function('var697', Object, BoolSort())
var360 = Function('var360', Object, BoolSort())
var443 = Function('var443', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var495 = Function('var495', Object, BoolSort())
var791 = Function('var791', Object, BoolSort())
var812 = Function('var812', Object, BoolSort())
var445 = Function('var445', Object, BoolSort())
var209 = Function('var209', Object, BoolSort())
var799 = Function('var799', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var906 = Function('var906', Object, BoolSort())
var924 = Function('var924', Object, BoolSort())
var327 = Function('var327', Object, BoolSort())
var514 = Function('var514', Object, BoolSort())
var520 = Function('var520', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var918 = Function('var918', Object, BoolSort())
var227 = Function('var227', Object, BoolSort())
var629 = Function('var629', Object, BoolSort())
var357 = Function('var357', Object, BoolSort())
var211 = Function('var211', Object, BoolSort())
var766 = Function('var766', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var212 = Function('var212', Object, BoolSort())
var238 = Function('var238', Object, BoolSort())
var440 = Function('var440', Object, BoolSort())
var959 = Function('var959', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var790 = Function('var790', Object, BoolSort())
var313 = Function('var313', Object, BoolSort())
var847 = Function('var847', Object, BoolSort())
var328 = Function('var328', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var693 = Function('var693', Object, BoolSort())
var281 = Function('var281', Object, BoolSort())
var489 = Function('var489', Object, BoolSort())
var969 = Function('var969', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var582 = Function('var582', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var205 = Function('var205', Object, BoolSort())
var326 = Function('var326', Object, BoolSort())
var933 = Function('var933', Object, BoolSort())
var690 = Function('var690', Object, BoolSort())
var280 = Function('var280', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var230 = Function('var230', Object, BoolSort())
var247 = Function('var247', Object, BoolSort())
var716 = Function('var716', Object, BoolSort())
var253 = Function('var253', Object, BoolSort())
var363 = Function('var363', Object, BoolSort())
var868 = Function('var868', Object, BoolSort())
var263 = Function('var263', Object, BoolSort())
var691 = Function('var691', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var325 = Function('var325', Object, BoolSort())
var947 = Function('var947', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var383 = Function('var383', Object, BoolSort())
var636 = Function('var636', Object, BoolSort())
var679 = Function('var679', Object, BoolSort())
var381 = Function('var381', Object, BoolSort())
var944 = Function('var944', Object, BoolSort())
var373 = Function('var373', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var866 = Function('var866', Object, BoolSort())
var955 = Function('var955', Object, BoolSort())
var279 = Function('var279', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var233 = Function('var233', Object, BoolSort())
var442 = Function('var442', Object, BoolSort())
var787 = Function('var787', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var657 = Function('var657', Object, BoolSort())
var779 = Function('var779', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var970 = Function('var970', Object, BoolSort())
var391 = Function('var391', Object, BoolSort())
var702 = Function('var702', Object, BoolSort())
var539 = Function('var539', Object, BoolSort())
var526 = Function('var526', Object, BoolSort())
var333 = Function('var333', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var365 = Function('var365', Object, BoolSort())
var862 = Function('var862', Object, BoolSort())
var662 = Function('var662', Object, BoolSort())
var874 = Function('var874', Object, BoolSort())
var696 = Function('var696', Object, BoolSort())
var758 = Function('var758', Object, BoolSort())
var692 = Function('var692', Object, BoolSort())
var786 = Function('var786', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var240 = Function('var240', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var989 = Function('var989', Object, BoolSort())
var535 = Function('var535', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var607 = Function('var607', Object, BoolSort())
var239 = Function('var239', Object, BoolSort())
var228 = Function('var228', Object, BoolSort())
var945 = Function('var945', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var597 = Function('var597', Object, BoolSort())
var274 = Function('var274', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var330 = Function('var330', Object, BoolSort())
var587 = Function('var587', Object, BoolSort())
var206 = Function('var206', Object, BoolSort())
var229 = Function('var229', Object, BoolSort())
var306 = Function('var306', Object, BoolSort())
var297 = Function('var297', Object, BoolSort())
var409 = Function('var409', Object, BoolSort())
var499 = Function('var499', Object, BoolSort())
var501 = Function('var501', Object, BoolSort())
var885 = Function('var885', Object, BoolSort())
var329 = Function('var329', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var460 = Function('var460', Object, BoolSort())
var262 = Function('var262', Object, BoolSort())
var402 = Function('var402', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var929 = Function('var929', Object, BoolSort())
var509 = Function('var509', Object, BoolSort())
var707 = Function('var707', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var706 = Function('var706', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var807 = Function('var807', Object, BoolSort())
var315 = Function('var315', Object, BoolSort())
var753 = Function('var753', Object, BoolSort())
var985 = Function('var985', Object, BoolSort())
var222 = Function('var222', Object, BoolSort())
var677 = Function('var677', Object, BoolSort())
var463 = Function('var463', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var912 = Function('var912', Object, BoolSort())
var323 = Function('var323', Object, BoolSort())
var894 = Function('var894', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var271 = Function('var271', Object, BoolSort())
var547 = Function('var547', Object, BoolSort())
var450 = Function('var450', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var581 = Function('var581', Object, BoolSort())
var678 = Function('var678', Object, BoolSort())
var488 = Function('var488', Object, BoolSort())
var536 = Function('var536', Object, BoolSort())
var633 = Function('var633', Object, BoolSort())
var843 = Function('var843', Object, BoolSort())
var648 = Function('var648', Object, BoolSort())
var216 = Function('var216', Object, BoolSort())
var948 = Function('var948', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var204 = Function('var204', Object, BoolSort())
var567 = Function('var567', Object, BoolSort())
var355 = Function('var355', Object, BoolSort())
var510 = Function('var510', Object, BoolSort())
var507 = Function('var507', Object, BoolSort())
var848 = Function('var848', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var683 = Function('var683', Object, BoolSort())
var452 = Function('var452', Object, BoolSort())
var765 = Function('var765', Object, BoolSort())
var397 = Function('var397', Object, BoolSort())
var956 = Function('var956', Object, BoolSort())
var735 = Function('var735', Object, BoolSort())
var400 = Function('var400', Object, BoolSort())
var634 = Function('var634', Object, BoolSort())
var764 = Function('var764', Object, BoolSort())
var870 = Function('var870', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var120(x), Not(var36(x))))),
	ForAll([x], Not(Or(var113(x), var656(x)))),
	ForAll([x], Not(Or(var94(x), var549(x)))),
	ForAll([x], Not(Or(var145(x), var480(x)))),
	ForAll([x], Not(Or(var158(x), var7(x)))),
	ForAll([x], Not(Or(Not(var432(x)), var31(x)))),
	ForAll([x], Not(Or(var913(x), Not(var476(x))))),
	ForAll([x], Not(Or(Not(var242(x)), var235(x)))),
	ForAll([x], Not(Or(var172(x), Not(var16(x))))),
	ForAll([x], Not(Or(Not(var142(x)), var77(x)))),
	ForAll([x], Not(Or(var245(x), Not(var361(x))))),
	ForAll([x], Not(Or(Not(var135(x)), Not(var563(x))))),
	ForAll([x], Not(Or(Not(var147(x)), Not(var701(x))))),
	ForAll([x], Not(Or(Not(var68(x)), var908(x)))),
	ForAll([x], Not(Or(Not(var4(x)), var30(x)))),
	ForAll([x], Not(Or(var901(x), var80(x)))),
	ForAll([x], Not(Or(Not(var59(x)), Not(var185(x))))),
	ForAll([x], Not(Or(var221(x), Not(var52(x))))),
	ForAll([x], Not(Or(Not(var155(x)), var923(x)))),
	ForAll([x], Not(Or(var564(x), var45(x)))),
	ForAll([x], Not(Or(Not(var19(x)), Not(var806(x))))),
	ForAll([x], Not(Or(var168(x), Not(var107(x))))),
	ForAll([x], Not(Or(Not(var156(x)), var130(x)))),
	ForAll([x], Not(Or(var733(x), Not(var213(x))))),
	ForAll([x], Not(Or(var219(x), var53(x)))),
	ForAll([x], Not(Or(Not(var164(x)), var181(x)))),
	ForAll([x], Not(Or(Not(var61(x)), var195(x)))),
	ForAll([x], Not(Or(Not(var254(x)), var991(x)))),
	ForAll([x], Not(Or(var218(x), Not(var479(x))))),
	ForAll([x], Not(Or(Not(var236(x)), Not(var125(x))))),
	ForAll([x], Not(Or(Not(var132(x)), Not(var622(x))))),
	ForAll([x], Not(Or(Not(var15(x)), var252(x)))),
	ForAll([x], Not(Or(var257(x), var881(x)))),
	ForAll([x], Not(Or(var604(x), Not(var305(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var200(x1)), Not(var117(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var905(x1)), var546(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var46(x1), var144(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var664(x1), Not(var705(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var404(x1)), var621(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var900(x1)), var814(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var47(x1)), var680(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var60(x1)), Not(var128(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var234(x1)), var79(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var248(x1)), Not(var266(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var14(x1)), Not(var880(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var508(x1)), var311(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var672(x1), Not(var968(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var101(x1), var83(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var57(x1)), Not(var246(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var188(x1)), var793(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var541(x1), var773(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var243(x1), var191(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var783(x1), var166(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var167(x1), var858(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var911(x1), Not(var649(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var853(x1), Not(var952(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var203(x1)), var630(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var389(x1)), Not(var550(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var210(x1), var122(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var415(x1), var659(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var922(x1), Not(var225(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var69(x1), var70(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var694(x1), var708(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var719(x1)), Not(var38(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var106(x1), var530(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var466(x1), Not(var67(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var485(x1), var876(x))))),
	ForAll([x], Not(Or(Not(var974(x)), var255(x), var579(x)))),
	ForAll([x], Not(Or(Not(var921(x)), var260(x), Not(var223(x))))),
	ForAll([x], Not(Or(var456(x), Not(var851(x)), var681(x)))),
	ForAll([x], Not(Or(var174(x), Not(var6(x)), Not(var37(x))))),
	ForAll([x], Not(Or(Not(var90(x)), Not(var684(x)), Not(var153(x))))),
	ForAll([x], Not(Or(var114(x), var115(x), var465(x)))),
	ForAll([x], Not(Or(var867(x), Not(var942(x)), Not(var84(x))))),
	ForAll([x], Not(Or(var282(x), Not(var224(x)), var675(x)))),
	ForAll([x], Not(Or(var893(x), Not(var22(x)), var193(x)))),
	ForAll([x], Not(Or(Not(var376(x)), Not(var175(x)), Not(var832(x))))),
	ForAll([x], Not(Or(var249(x), var658(x), Not(var199(x))))),
	ForAll([x], Not(Or(var884(x), var48(x), Not(var571(x))))),
	ForAll([x], Not(Or(Not(var303(x)), var754(x), Not(var961(x))))),
	ForAll([x], Not(Or(Not(var127(x)), var54(x), Not(var18(x))))),
	ForAll([x], Not(Or(var50(x), Not(var187(x)), var81(x)))),
	ForAll([x], Not(Or(Not(var214(x)), var108(x), Not(var317(x))))),
	ForAll([x], Not(Or(var8(x), var287(x), Not(var208(x))))),
	ForAll([x], Not(Or(var319(x), Not(var963(x)), Not(var131(x))))),
	ForAll([x], Not(Or(var464(x), Not(var165(x)), var232(x)))),
	ForAll([x], Not(Or(Not(var782(x)), Not(var585(x)), var27(x)))),
	ForAll([x], Not(Or(Not(var632(x)), Not(var915(x)), var823(x)))),
	ForAll([x], Not(Or(Not(var871(x)), var270(x), Not(var133(x))))),
	ForAll([x], Not(Or(Not(var538(x)), var714(x), Not(var332(x))))),
	ForAll([x], Not(Or(var51(x), Not(var977(x)), Not(var9(x))))),
	ForAll([x], Not(Or(Not(var886(x)), var721(x), var201(x)))),
	ForAll([x], Not(Or(Not(var643(x)), Not(var588(x)), Not(var39(x))))),
	ForAll([x], Not(Or(var310(x), Not(var146(x)), var82(x)))),
	ForAll([x], Not(Or(var825(x), var595(x), var996(x)))),
	ForAll([x], Not(Or(Not(var25(x)), Not(var932(x)), Not(var250(x))))),
	ForAll([x], Not(Or(Not(var33(x)), var179(x), Not(var352(x))))),
	ForAll([x], Not(Or(var149(x), var444(x), var126(x)))),
	ForAll([x], Not(Or(Not(var241(x)), var65(x), var917(x)))),
	ForAll([x], Not(Or(var58(x), Not(var231(x)), Not(var532(x))))),
	ForAll([x], Not(Or(var21(x), Not(var372(x)), var152(x)))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var49(x1), Or(Not(var477(x)), var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var104(x1)), Not(var882(x1))), Not(var999(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var640(x1), Not(var88(x1))), var987(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var392(x1)), Not(var75(x1))), var71(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var202(x1)), Or(Not(var251(x)), Not(var505(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var457(x1)), Not(var161(x1))), var780(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var461(x1)), Or(Not(var32(x)), Not(var796(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var359(x1), Or(Not(var822(x)), var551(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var258(x1), Or(var112(x), Not(var41(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var123(x1)), Or(Not(var426(x)), var162(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var414(x1), var1(x1)), var143(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var294(x1), Or(var159(x), Not(var196(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var647(x1)), Or(Not(var139(x)), var542(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var768(x1)), Not(var875(x1))), Not(var342(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var109(x1), Or(var606(x), Not(var738(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var726(x1), Or(Not(var116(x)), Not(var56(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var10(x1)), Not(var194(x1))), var261(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var953(x1), Not(var336(x1))), var895(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var960(x1), var197(x1)), var64(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var374(x1), Or(var244(x), Not(var184(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var584(x1)), Or(Not(var978(x)), var715(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var824(x1), Or(var26(x), var756(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var420(x1), Or(var590(x), Not(var938(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var367(x1), var833(x1)), Not(var207(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var808(x1)), Or(Not(var897(x)), Not(var425(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var438(x1)), Or(var322(x), var163(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var534(x1), var345(x1)), var99(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var63(x1), Not(var624(x1))), var341(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var183(x1), var346(x1)), Not(var760(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var119(x1), Not(var134(x1))), var993(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var137(x1), Or(Not(var770(x)), Not(var603(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var902(x1)), Not(var496(x1))), var100(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var136(x1)), Or(Not(var192(x)), var28(x)))))),
	ForAll([x], Not(Or(var264(x), Not(var481(x)), Not(var178(x)), Not(var513(x))))),
	ForAll([x], Not(Or(var160(x), var673(x), var811(x), Not(var105(x))))),
	ForAll([x], Not(Or(Not(var265(x)), var215(x), Not(var220(x)), var272(x)))),
	ForAll([x], Not(Or(var599(x), Not(var967(x)), var522(x), Not(var935(x))))),
	ForAll([x], Not(Or(var387(x), Not(var55(x)), Not(var545(x)), Not(var237(x))))),
	ForAll([x], Not(Or(var842(x), var226(x), Not(var170(x)), Not(var96(x))))),
	ForAll([x], Not(Or(var605(x), var560(x), var217(x), var259(x)))),
	ForAll([x], Not(Or(Not(var712(x)), var435(x), var447(x), var151(x)))),
	ForAll([x], Not(Or(Not(var641(x)), Not(var602(x)), var2(x), Not(var653(x))))),
	ForAll([x], Not(Or(Not(var362(x)), var93(x), var182(x), Not(var879(x))))),
	ForAll([x], Not(Or(Not(var598(x)), var746(x), var89(x), Not(var482(x))))),
	ForAll([x], Not(Or(Not(var300(x)), Not(var189(x)), Not(var777(x)), var177(x)))),
	ForAll([x], Not(Or(Not(var129(x)), Not(var580(x)), var62(x), Not(var859(x))))),
	ForAll([x], Not(Or(var97(x), var826(x), var834(x), Not(var11(x))))),
	ForAll([x], Not(Or(Not(var736(x)), var24(x), Not(var872(x)), Not(var87(x))))),
	ForAll([x], Not(Or(var972(x), var34(x), Not(var66(x)), var473(x)))),
	ForAll([x], Not(Or(var846(x), Not(var95(x)), Not(var256(x)), var5(x)))),
	ForAll([x], Not(Or(var186(x), Not(var577(x)), Not(var283(x)), var600(x)))),
	ForAll([x], Not(Or(var290(x), var601(x), var927(x), var44(x)))),
	ForAll([x], Not(Or(var997(x), var734(x), var889(x), Not(var124(x))))),
	ForAll([x], Not(Or(Not(var169(x)), var86(x), var781(x), Not(var610(x))))),
	ForAll([x], Not(Or(Not(var98(x)), Not(var180(x)), var818(x), var697(x)))),
	ForAll([x], Not(Or(var360(x), Not(var443(x)), Not(var173(x)), Not(var495(x))))),
	ForAll([x], Not(Or(Not(var791(x)), Not(var812(x)), var445(x), var209(x)))),
	ForAll([x], Not(Or(var799(x), Not(var29(x)), Not(var906(x)), var924(x)))),
	ForAll([x], Not(Or(var327(x), Not(var514(x)), Not(var520(x)), var140(x)))),
	ForAll([x], Not(Or(Not(var918(x)), var227(x), var629(x), Not(var357(x))))),
	ForAll([x], Not(Or(Not(var211(x)), var766(x), Not(var20(x)), var212(x)))),
	ForAll([x], Not(Or(var238(x), Not(var440(x)), Not(var959(x)), Not(var154(x))))),
	ForAll([x], Not(Or(var790(x), var313(x), var847(x), Not(var328(x))))),
	ForAll([x], Not(Or(var103(x), var693(x), Not(var281(x)), Not(var489(x))))),
	ForAll([x], Not(Or(Not(var969(x)), Not(var157(x)), var582(x), var17(x)))),
	ForAll([x], Not(Or(Not(var141(x)), Not(var150(x)), var205(x), var326(x)))),
	ForAll([x], Not(Or(var933(x), var690(x), var280(x), Not(var42(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var12(x1), Not(var176(x1))), Or(var230(x), Not(var247(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var716(x1)), Not(var253(x1))), Or(var363(x), var868(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var263(x1)), Not(var691(x1)), Not(var74(x1))), Not(var325(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var947(x1), Not(var171(x1)), Not(var383(x1))), Not(var636(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var679(x1)), var381(x1)), Or(Not(var944(x)), Not(var373(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var148(x1)), var866(x1)), Or(Not(var955(x)), Not(var279(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var72(x1), Or(var233(x), var442(x), var787(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var102(x1), Not(var76(x1))), Or(Not(var657(x)), var779(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var138(x1), Or(Not(var970(x)), Not(var391(x)), var702(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var539(x1), Not(var526(x1)), Not(var333(x1))), var78(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var365(x1), Not(var862(x1))), Or(Not(var662(x)), var874(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var696(x1), Or(var758(x), Not(var692(x)), Not(var786(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var40(x1), var240(x1), Not(var92(x1))), var989(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var535(x1), Not(var110(x1)), var607(x1)), Not(var239(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var228(x1), var945(x1)), Or(Not(var121(x)), Not(var597(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var274(x1), var3(x1)), Or(var330(x), var587(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var206(x1)), Not(var229(x1))), Or(var306(x), var297(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var409(x1), Or(var499(x), var501(x), var885(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var329(x1)), Or(Not(var85(x)), var460(x), Not(var262(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var402(x1), Or(Not(var43(x)), var929(x), var509(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var707(x1), Not(var198(x1))), Or(Not(var706(x)), Not(var73(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var807(x1), Or(Not(var315(x)), Not(var753(x)), var985(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(var222(x1), var677(x1)), Or(var463(x), var190(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var13(x1)), Not(var912(x1))), Or(Not(var323(x)), var894(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var91(x1)), Or(var271(x), Not(var547(x)), var450(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var118(x1)), Not(var581(x1)), var678(x1)), Not(var488(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var536(x1)), Or(var633(x), Not(var843(x)), var648(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var216(x1)), Not(var948(x1)), var23(x1)), Not(var204(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var567(x1), Or(var355(x), var510(x), Not(var507(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var848(x1), Or(var35(x), Not(var683(x)), Not(var452(x))))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Or(Not(var765(x1)), var397(x1), var956(x1)), var735(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var400(x1)), Or(Not(var634(x)), Not(var764(x)), var870(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
