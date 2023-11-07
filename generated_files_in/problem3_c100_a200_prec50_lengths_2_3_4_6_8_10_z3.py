from z3 import *

Object = DeclareSort('Object')

var142 = Function('var142', Object, BoolSort())
var193 = Function('var193', Object, BoolSort())
var113 = Function('var113', Object, BoolSort())
var19 = Function('var19', Object, BoolSort())
var165 = Function('var165', Object, BoolSort())
var187 = Function('var187', Object, BoolSort())
var120 = Function('var120', Object, BoolSort())
var101 = Function('var101', Object, BoolSort())
var109 = Function('var109', Object, BoolSort())
var200 = Function('var200', Object, BoolSort())
var40 = Function('var40', Object, BoolSort())
var155 = Function('var155', Object, BoolSort())
var5 = Function('var5', Object, BoolSort())
var168 = Function('var168', Object, BoolSort())
var199 = Function('var199', Object, BoolSort())
var63 = Function('var63', Object, BoolSort())
var29 = Function('var29', Object, BoolSort())
var177 = Function('var177', Object, BoolSort())
var164 = Function('var164', Object, BoolSort())
var151 = Function('var151', Object, BoolSort())
var198 = Function('var198', Object, BoolSort())
var88 = Function('var88', Object, BoolSort())
var191 = Function('var191', Object, BoolSort())
var161 = Function('var161', Object, BoolSort())
var160 = Function('var160', Object, BoolSort())
var52 = Function('var52', Object, BoolSort())
var8 = Function('var8', Object, BoolSort())
var17 = Function('var17', Object, BoolSort())
var50 = Function('var50', Object, BoolSort())
var150 = Function('var150', Object, BoolSort())
var123 = Function('var123', Object, BoolSort())
var124 = Function('var124', Object, BoolSort())
var163 = Function('var163', Object, BoolSort())
var84 = Function('var84', Object, BoolSort())
var26 = Function('var26', Object, BoolSort())
var154 = Function('var154', Object, BoolSort())
var102 = Function('var102', Object, BoolSort())
var107 = Function('var107', Object, BoolSort())
var184 = Function('var184', Object, BoolSort())
var128 = Function('var128', Object, BoolSort())
var55 = Function('var55', Object, BoolSort())
var96 = Function('var96', Object, BoolSort())
var81 = Function('var81', Object, BoolSort())
var66 = Function('var66', Object, BoolSort())
var68 = Function('var68', Object, BoolSort())
var73 = Function('var73', Object, BoolSort())
var104 = Function('var104', Object, BoolSort())
var41 = Function('var41', Object, BoolSort())
var118 = Function('var118', Object, BoolSort())
var182 = Function('var182', Object, BoolSort())
var139 = Function('var139', Object, BoolSort())
var87 = Function('var87', Object, BoolSort())
var75 = Function('var75', Object, BoolSort())
var83 = Function('var83', Object, BoolSort())
var153 = Function('var153', Object, BoolSort())
var108 = Function('var108', Object, BoolSort())
var53 = Function('var53', Object, BoolSort())
var22 = Function('var22', Object, BoolSort())
var33 = Function('var33', Object, BoolSort())
var132 = Function('var132', Object, BoolSort())
var25 = Function('var25', Object, BoolSort())
var58 = Function('var58', Object, BoolSort())
var146 = Function('var146', Object, BoolSort())
var20 = Function('var20', Object, BoolSort())
var16 = Function('var16', Object, BoolSort())
var27 = Function('var27', Object, BoolSort())
var170 = Function('var170', Object, BoolSort())
var43 = Function('var43', Object, BoolSort())
var32 = Function('var32', Object, BoolSort())
var97 = Function('var97', Object, BoolSort())
var103 = Function('var103', Object, BoolSort())
var12 = Function('var12', Object, BoolSort())
var116 = Function('var116', Object, BoolSort())
var15 = Function('var15', Object, BoolSort())
var140 = Function('var140', Object, BoolSort())
var181 = Function('var181', Object, BoolSort())
var64 = Function('var64', Object, BoolSort())
var111 = Function('var111', Object, BoolSort())
var136 = Function('var136', Object, BoolSort())
var117 = Function('var117', Object, BoolSort())
var158 = Function('var158', Object, BoolSort())
var99 = Function('var99', Object, BoolSort())
var60 = Function('var60', Object, BoolSort())
var166 = Function('var166', Object, BoolSort())
var62 = Function('var62', Object, BoolSort())
var65 = Function('var65', Object, BoolSort())
var183 = Function('var183', Object, BoolSort())
var98 = Function('var98', Object, BoolSort())
var122 = Function('var122', Object, BoolSort())
var23 = Function('var23', Object, BoolSort())
var178 = Function('var178', Object, BoolSort())
var54 = Function('var54', Object, BoolSort())
var31 = Function('var31', Object, BoolSort())
var137 = Function('var137', Object, BoolSort())
var4 = Function('var4', Object, BoolSort())
var89 = Function('var89', Object, BoolSort())
var85 = Function('var85', Object, BoolSort())
var57 = Function('var57', Object, BoolSort())
var162 = Function('var162', Object, BoolSort())
var70 = Function('var70', Object, BoolSort())
var195 = Function('var195', Object, BoolSort())
var167 = Function('var167', Object, BoolSort())
var77 = Function('var77', Object, BoolSort())
var147 = Function('var147', Object, BoolSort())
var78 = Function('var78', Object, BoolSort())
var95 = Function('var95', Object, BoolSort())
var186 = Function('var186', Object, BoolSort())
var176 = Function('var176', Object, BoolSort())
var130 = Function('var130', Object, BoolSort())
var24 = Function('var24', Object, BoolSort())
var196 = Function('var196', Object, BoolSort())
var82 = Function('var82', Object, BoolSort())
var59 = Function('var59', Object, BoolSort())
var129 = Function('var129', Object, BoolSort())
var112 = Function('var112', Object, BoolSort())
var28 = Function('var28', Object, BoolSort())
var189 = Function('var189', Object, BoolSort())
var169 = Function('var169', Object, BoolSort())
var173 = Function('var173', Object, BoolSort())
var180 = Function('var180', Object, BoolSort())
var80 = Function('var80', Object, BoolSort())
var3 = Function('var3', Object, BoolSort())
var148 = Function('var148', Object, BoolSort())
var56 = Function('var56', Object, BoolSort())
var71 = Function('var71', Object, BoolSort())
var48 = Function('var48', Object, BoolSort())
var86 = Function('var86', Object, BoolSort())
var125 = Function('var125', Object, BoolSort())
var18 = Function('var18', Object, BoolSort())
var106 = Function('var106', Object, BoolSort())
var61 = Function('var61', Object, BoolSort())
var175 = Function('var175', Object, BoolSort())
var127 = Function('var127', Object, BoolSort())
var45 = Function('var45', Object, BoolSort())
var190 = Function('var190', Object, BoolSort())
var67 = Function('var67', Object, BoolSort())
var38 = Function('var38', Object, BoolSort())
var192 = Function('var192', Object, BoolSort())
var105 = Function('var105', Object, BoolSort())
var100 = Function('var100', Object, BoolSort())
var37 = Function('var37', Object, BoolSort())
var145 = Function('var145', Object, BoolSort())
var149 = Function('var149', Object, BoolSort())
var94 = Function('var94', Object, BoolSort())
var185 = Function('var185', Object, BoolSort())
var11 = Function('var11', Object, BoolSort())
var188 = Function('var188', Object, BoolSort())
var110 = Function('var110', Object, BoolSort())
var2 = Function('var2', Object, BoolSort())
var197 = Function('var197', Object, BoolSort())
var79 = Function('var79', Object, BoolSort())
var194 = Function('var194', Object, BoolSort())
var121 = Function('var121', Object, BoolSort())
var133 = Function('var133', Object, BoolSort())
var135 = Function('var135', Object, BoolSort())
var34 = Function('var34', Object, BoolSort())
var9 = Function('var9', Object, BoolSort())
var10 = Function('var10', Object, BoolSort())
var93 = Function('var93', Object, BoolSort())
var114 = Function('var114', Object, BoolSort())
var30 = Function('var30', Object, BoolSort())
var172 = Function('var172', Object, BoolSort())
var51 = Function('var51', Object, BoolSort())
var76 = Function('var76', Object, BoolSort())
var13 = Function('var13', Object, BoolSort())
var36 = Function('var36', Object, BoolSort())
var144 = Function('var144', Object, BoolSort())
var35 = Function('var35', Object, BoolSort())
var90 = Function('var90', Object, BoolSort())
var6 = Function('var6', Object, BoolSort())
var143 = Function('var143', Object, BoolSort())
var92 = Function('var92', Object, BoolSort())
var115 = Function('var115', Object, BoolSort())
var126 = Function('var126', Object, BoolSort())
var159 = Function('var159', Object, BoolSort())
var69 = Function('var69', Object, BoolSort())
var119 = Function('var119', Object, BoolSort())
var14 = Function('var14', Object, BoolSort())
var46 = Function('var46', Object, BoolSort())
var179 = Function('var179', Object, BoolSort())
var47 = Function('var47', Object, BoolSort())
var91 = Function('var91', Object, BoolSort())
var49 = Function('var49', Object, BoolSort())
var174 = Function('var174', Object, BoolSort())
var156 = Function('var156', Object, BoolSort())
var42 = Function('var42', Object, BoolSort())
var171 = Function('var171', Object, BoolSort())
var39 = Function('var39', Object, BoolSort())
var72 = Function('var72', Object, BoolSort())
var74 = Function('var74', Object, BoolSort())
var7 = Function('var7', Object, BoolSort())
var157 = Function('var157', Object, BoolSort())
var21 = Function('var21', Object, BoolSort())
var152 = Function('var152', Object, BoolSort())
var138 = Function('var138', Object, BoolSort())
var134 = Function('var134', Object, BoolSort())
var131 = Function('var131', Object, BoolSort())
var1 = Function('var1', Object, BoolSort())
var44 = Function('var44', Object, BoolSort())
var141 = Function('var141', Object, BoolSort())
GTE = Function('GTE', Object, Object, BoolSort())

x = Const('x', Object)
x1 = Const('x1', Object)

axioms = [
	ForAll([x], Not(Or(var142(x), var193(x)))),
	ForAll([x], Not(Or(var113(x), Not(var19(x))))),
	ForAll([x], Not(Or(Not(var165(x)), Not(var187(x))))),
	ForAll([x], Not(Or(Not(var120(x)), var101(x)))),
	ForAll([x], Not(Or(Not(var109(x)), Not(var200(x))))),
	ForAll([x], Not(Or(var40(x), Not(var155(x))))),
	ForAll([x], Not(Or(Not(var5(x)), var168(x)))),
	ForAll([x], Not(Or(var199(x), var63(x)))),
	ForAll([x], Not(Or(var29(x), Not(var177(x))))),
	ForAll([x], Not(Or(var164(x), var151(x)))),
	ForAll([x], Not(Or(var198(x), Not(var88(x))))),
	ForAll([x], Not(Or(Not(var191(x)), var161(x)))),
	ForAll([x], Not(Or(var160(x), var52(x)))),
	ForAll([x], Not(Or(Not(var8(x)), var17(x)))),
	ForAll([x], Not(Or(var50(x), Not(var150(x))))),
	ForAll([x], Not(Or(var123(x), var124(x)))),
	ForAll([x], Not(Or(Not(var163(x)), Not(var84(x))))),
	ForAll([x], Not(Or(var26(x), Not(var154(x))))),
	ForAll([x], Not(Or(Not(var102(x)), var107(x)))),
	ForAll([x], Not(Or(Not(var184(x)), var128(x)))),
	ForAll([x], Not(Or(var55(x), var96(x)))),
	ForAll([x], Not(Or(var81(x), Not(var66(x))))),
	ForAll([x], Not(Or(var68(x), Not(var73(x))))),
	ForAll([x], Not(Or(Not(var104(x)), Not(var41(x))))),
	ForAll([x], Not(Or(var118(x), Not(var182(x))))),
	ForAll([x], Not(Or(var139(x), var87(x)))),
	ForAll([x], Not(Or(Not(var75(x)), Not(var83(x))))),
	ForAll([x], Not(Or(var153(x), var108(x)))),
	ForAll([x], Not(Or(var53(x), Not(var22(x))))),
	ForAll([x], Not(Or(Not(var33(x)), var132(x)))),
	ForAll([x], Not(Or(var25(x), var58(x)))),
	ForAll([x], Not(Or(Not(var146(x)), Not(var20(x))))),
	ForAll([x], Not(Or(var16(x), Not(var27(x))))),
	ForAll([x], Not(Or(Not(var170(x)), var43(x)))),
	ForAll([x], Not(Or(var32(x), Not(var97(x))))),
	ForAll([x], Not(Or(var103(x), Not(var12(x))))),
	ForAll([x], Not(Or(var116(x), Not(var15(x))))),
	ForAll([x], Not(Or(var140(x), var181(x)))),
	ForAll([x], Not(Or(var64(x), var111(x)))),
	ForAll([x], Not(Or(var136(x), var117(x)))),
	ForAll([x], Not(Or(Not(var158(x)), var99(x)))),
	ForAll([x], Not(Or(Not(var60(x)), var166(x)))),
	ForAll([x], Not(Or(var62(x), var65(x)))),
	ForAll([x], Not(Or(var183(x), var98(x)))),
	ForAll([x], Not(Or(var122(x), Not(var23(x))))),
	ForAll([x], Not(Or(Not(var178(x)), Not(var54(x))))),
	ForAll([x], Not(Or(var31(x), var137(x)))),
	ForAll([x], Not(Or(Not(var4(x)), var89(x)))),
	ForAll([x], Not(Or(var85(x), Not(var57(x))))),
	ForAll([x], Not(Or(var162(x), Not(var70(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var195(x1), Not(var167(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var77(x1)), Not(var147(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var78(x1)), Not(var95(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var186(x1)), var176(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var130(x1)), Not(var24(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var196(x1)), Not(var82(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var59(x1), var129(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var112(x1)), Not(var28(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var189(x1), Not(var169(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var173(x1)), Not(var180(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var80(x1), Not(var3(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var148(x1), Not(var56(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var71(x1), Not(var48(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var86(x1), var125(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var18(x1)), var106(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var61(x1), var175(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var127(x1)), var45(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var190(x1)), Not(var67(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var38(x1)), var192(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var105(x1), Not(var100(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var37(x1), var145(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var149(x1), Not(var94(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var185(x1)), Not(var11(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var188(x1)), var110(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var2(x1), var197(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var79(x1), Not(var194(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var121(x1), var133(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var135(x1), Not(var34(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var9(x1), Not(var10(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var93(x1), var114(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var30(x1)), var172(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var51(x1), Not(var76(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var13(x1), Not(var36(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var144(x1), var35(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var90(x1), Not(var6(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var143(x1), Not(var92(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var115(x1)), var126(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var159(x1), Not(var69(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var119(x1), var14(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var46(x1), Not(var179(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var47(x1), var91(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var49(x1)), Not(var174(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var156(x1)), var42(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var171(x1)), Not(var39(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var72(x1)), var74(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var7(x1), Not(var157(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var21(x1)), Not(var152(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var138(x1)), var134(x))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(var131(x1), Not(var1(x)))))),
	ForAll([x], Exists([x1], And(GTE(x, x1), Implies(Not(var44(x1)), var141(x)))))
]
s = Solver()
s.set("timeout", 300)
s.add(axioms)
print(s.check())
print(s.statistics())
