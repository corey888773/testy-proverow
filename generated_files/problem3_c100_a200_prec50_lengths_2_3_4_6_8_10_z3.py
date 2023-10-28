from z3 import *

Object = DeclareSort('Object')

var181 = Function('var181', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var142 = Function('var142', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(Not(var181(x)), Not(var46(x))))),
	ForAll([x], Not(Or(var42(x), Not(var14(x))))),
	ForAll([x], Not(Or(var156(x), Not(var26(x))))),
	ForAll([x], Not(Or(Not(var154(x)), Not(var1(x))))),
	ForAll([x], Not(Or(var3(x), Not(var136(x))))),
	ForAll([x], Not(Or(var159(x), Not(var132(x))))),
	ForAll([x], Not(Or(var79(x), var63(x)))),
	ForAll([x], Not(Or(Not(var19(x)), Not(var152(x))))),
	ForAll([x], Not(Or(Not(var122(x)), var94(x)))),
	ForAll([x], Not(Or(var18(x), Not(var158(x))))),
	ForAll([x], Not(Or(Not(var29(x)), var38(x)))),
	ForAll([x], Not(Or(var169(x), Not(var131(x))))),
	ForAll([x], Not(Or(var186(x), Not(var163(x))))),
	ForAll([x], Not(Or(Not(var199(x)), Not(var30(x))))),
	ForAll([x], Not(Or(Not(var200(x)), var72(x)))),
	ForAll([x], Not(Or(Not(var55(x)), var8(x)))),
	ForAll([x], Not(Or(var52(x), var180(x)))),
	ForAll([x], Not(Or(Not(var141(x)), var112(x)))),
	ForAll([x], Not(Or(var37(x), var36(x)))),
	ForAll([x], Not(Or(Not(var175(x)), var34(x)))),
	ForAll([x], Not(Or(Not(var164(x)), var93(x)))),
	ForAll([x], Not(Or(var57(x), var33(x)))),
	ForAll([x], Not(Or(var27(x), var128(x)))),
	ForAll([x], Not(Or(var177(x), var191(x)))),
	ForAll([x], Not(Or(Not(var35(x)), Not(var67(x))))),
	ForAll([x], Not(Or(var95(x), var83(x)))),
	ForAll([x], Not(Or(Not(var31(x)), Not(var109(x))))),
	ForAll([x], Not(Or(Not(var107(x)), Not(var161(x))))),
	ForAll([x], Not(Or(Not(var59(x)), Not(var56(x))))),
	ForAll([x], Not(Or(Not(var178(x)), var150(x)))),
	ForAll([x], Not(Or(var126(x), var108(x)))),
	ForAll([x], Not(Or(var184(x), Not(var48(x))))),
	ForAll([x], Not(Or(var117(x), Not(var12(x))))),
	ForAll([x], Not(Or(var162(x), var32(x)))),
	ForAll([x], Not(Or(Not(var5(x)), Not(var111(x))))),
	ForAll([x], Not(Or(var76(x), Not(var110(x))))),
	ForAll([x], Not(Or(var62(x), Not(var197(x))))),
	ForAll([x], Not(Or(var6(x), Not(var39(x))))),
	ForAll([x], Not(Or(var121(x), var85(x)))),
	ForAll([x], Not(Or(var81(x), Not(var168(x))))),
	ForAll([x], Not(Or(Not(var119(x)), Not(var189(x))))),
	ForAll([x], Not(Or(var23(x), var125(x)))),
	ForAll([x], Not(Or(Not(var65(x)), Not(var194(x))))),
	ForAll([x], Not(Or(Not(var87(x)), Not(var78(x))))),
	ForAll([x], Not(Or(Not(var155(x)), var183(x)))),
	ForAll([x], Not(Or(Not(var61(x)), var118(x)))),
	ForAll([x], Not(Or(var74(x), Not(var129(x))))),
	ForAll([x], Not(Or(Not(var90(x)), var185(x)))),
	ForAll([x], Not(Or(var103(x), var70(x)))),
	ForAll([x], Not(Or(Not(var68(x)), Not(var43(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var137(x1)), var113(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var171(x1), var104(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var160(x1)), var69(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var102(x1), Not(var101(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var124(x1), var115(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var97(x1), var80(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var82(x1)), Not(var196(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var153(x1), var96(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var133(x1)), var105(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var71(x1), Not(var40(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var167(x1), Not(var148(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var123(x1)), var134(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var176(x1)), var127(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var60(x1), Not(var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var130(x1), Not(var135(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var165(x1), Not(var58(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var22(x1)), var188(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), var28(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var173(x1)), var146(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var13(x1), Not(var139(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var192(x1)), Not(var138(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var4(x1), var88(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var89(x1), Not(var100(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var174(x1), Not(var99(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var25(x1), var10(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var75(x1)), Not(var151(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var193(x1), var143(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var114(x1), var53(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var147(x1)), var24(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var187(x1), var120(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var54(x1), Not(var106(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var142(x1)), Not(var91(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var64(x1)), var15(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var149(x1), Not(var166(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var7(x1), var41(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var172(x1)), Not(var116(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var157(x1), var190(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var84(x1), Not(var98(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var170(x1), var198(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var86(x1)), Not(var50(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var2(x1)), Not(var77(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var182(x1)), var51(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), Not(var16(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var145(x1), Not(var21(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var73(x1), var92(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var144(x1), Not(var45(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var140(x1), Not(var47(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var66(x1), var195(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var49(x1), Not(var179(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var20(x1)), var17(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
