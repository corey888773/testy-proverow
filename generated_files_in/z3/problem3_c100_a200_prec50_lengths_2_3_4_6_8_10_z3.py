from z3 import *

Object = DeclareSort('Object')

var137 = Function('var137', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms0 = [
	ForAll([x], Not(Or(Not(var137(x)), var64(x)))),
	ForAll([x], Not(Or(Not(var68(x)), Not(var79(x))))),
	ForAll([x], Not(Or(Not(var101(x)), var81(x)))),
	ForAll([x], Not(Or(var25(x), var159(x)))),
	ForAll([x], Not(Or(Not(var54(x)), Not(var28(x))))),
	ForAll([x], Not(Or(var52(x), Not(var149(x))))),
	ForAll([x], Not(Or(Not(var7(x)), var173(x)))),
	ForAll([x], Not(Or(var26(x), var19(x)))),
	ForAll([x], Not(Or(Not(var12(x)), var43(x)))),
	ForAll([x], Not(Or(Not(var23(x)), var47(x)))),
	ForAll([x], Not(Or(Not(var44(x)), var112(x)))),
	ForAll([x], Not(Or(var158(x), Not(var72(x))))),
	ForAll([x], Not(Or(Not(var114(x)), var128(x)))),
	ForAll([x], Not(Or(var123(x), Not(var100(x))))),
	ForAll([x], Not(Or(var89(x), Not(var133(x))))),
	ForAll([x], Not(Or(var116(x), var20(x)))),
	ForAll([x], Not(Or(Not(var46(x)), Not(var37(x))))),
	ForAll([x], Not(Or(Not(var80(x)), var97(x)))),
	ForAll([x], Not(Or(var106(x), Not(var174(x))))),
	ForAll([x], Not(Or(Not(var30(x)), Not(var146(x))))),
	ForAll([x], Not(Or(Not(var99(x)), var125(x)))),
	ForAll([x], Not(Or(var102(x), Not(var155(x))))),
	ForAll([x], Not(Or(var104(x), Not(var127(x))))),
	ForAll([x], Not(Or(var13(x), var38(x)))),
	ForAll([x], Not(Or(Not(var136(x)), var5(x)))),
	ForAll([x], Not(Or(Not(var92(x)), var76(x)))),
	ForAll([x], Not(Or(var197(x), Not(var63(x))))),
	ForAll([x], Not(Or(Not(var181(x)), Not(var200(x))))),
	ForAll([x], Not(Or(var53(x), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var29(x)), var120(x)))),
	ForAll([x], Not(Or(Not(var55(x)), var42(x)))),
	ForAll([x], Not(Or(Not(var51(x)), Not(var10(x))))),
	ForAll([x], Not(Or(var194(x), Not(var27(x))))),
	ForAll([x], Not(Or(Not(var108(x)), var69(x)))),
	ForAll([x], Not(Or(var196(x), var94(x)))),
	ForAll([x], Not(Or(var61(x), var49(x)))),
	ForAll([x], Not(Or(var131(x), Not(var163(x))))),
	ForAll([x], Not(Or(var45(x), Not(var31(x))))),
	ForAll([x], Not(Or(Not(var40(x)), var118(x)))),
	ForAll([x], Not(Or(Not(var113(x)), Not(var117(x))))),
	ForAll([x], Not(Or(Not(var8(x)), var150(x)))),
	ForAll([x], Not(Or(Not(var105(x)), var70(x)))),
	ForAll([x], Not(Or(Not(var109(x)), var148(x)))),
	ForAll([x], Not(Or(var110(x), var141(x)))),
	ForAll([x], Not(Or(Not(var121(x)), var166(x)))),
	ForAll([x], Not(Or(Not(var107(x)), var67(x)))),
	ForAll([x], Not(Or(Not(var156(x)), var60(x)))),
	ForAll([x], Not(Or(Not(var192(x)), var172(x)))),
	ForAll([x], Not(Or(var165(x), var160(x)))),
	ForAll([x], Not(Or(Not(var138(x)), Not(var17(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var15(x1)), Not(var140(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var82(x1)), Not(var144(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var193(x1), Not(var75(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var145(x1), var147(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var142(x1), var143(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var36(x1)), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var178(x1)), var33(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var65(x1)), var48(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var11(x1), Not(var135(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var98(x1)), Not(var180(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var41(x1)), Not(var77(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var87(x1)), var186(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var16(x1)), Not(var86(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var188(x1)), Not(var195(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var34(x1), Not(var189(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var59(x1), var154(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var130(x1), Not(var32(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var187(x1)), var162(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var21(x1)), var167(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var175(x1), var115(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var182(x1)), Not(var22(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var57(x1), Not(var185(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var78(x1), Not(var111(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var169(x1)), var198(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var129(x1), var35(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var179(x1), var58(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var14(x1), var4(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var18(x1), Not(var66(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var95(x1)), Not(var151(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var50(x1)), var199(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var164(x1), var56(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), Not(var171(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var184(x1)), var161(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var176(x1), Not(var62(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var126(x1), var6(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var152(x1), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var124(x1)), Not(var122(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var93(x1), Not(var103(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var132(x1), Not(var2(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var96(x1), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var83(x1), Not(var84(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var85(x1)), Not(var119(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var139(x1), Not(var157(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var191(x1)), var91(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), var134(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var1(x1)), Not(var73(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var183(x1), Not(var71(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var153(x1)), var190(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var177(x1)), Not(var168(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var170(x1)), Not(var39(x))))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms0)
print(s.check())
print(s.statistics())
