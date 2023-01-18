def func1(arg1, arg2):
    var49 = func2(arg1, arg2)
    var50 = (-945267117 & -1587876785 + (var49 - arg1 ^ arg1 | arg2 ^ (((arg2 | arg1 | -1779954150 - var49 & (arg2 & (-1765907273 + (2044273649 - var49) & arg1) ^ arg1 - arg2 | (-799 & -562))) & var49) - 622))) | var49
    var51 = var50 + arg1 - (2079182231 ^ var50 - -520 + arg2) | var49
    result = arg2 | var49
    return result
def func2(arg3, arg4):
    var9 = func3(arg4, arg3)
    var13 = func4(var9, arg3)
    var18 = func6(arg3, arg4)
    var36 = var21(var18, var13)
    var37 = (var9 - 373 ^ arg3) | var13
    var38 = var13 ^ (var37 & arg4) & arg4
    var39 = var38 + var9
    var40 = var38 - var38
    if var40 < var37:
        var41 = (var13 + (var40 ^ -526)) + var38
    else:
        var41 = ((var38 & 455) + arg3) ^ var13
    var42 = (var18 + 85) | var37
    var43 = var37 ^ var36
    var44 = var9 - (var9 + (var38 ^ var9))
    var45 = arg4 + var13
    var46 = 1937948042 - (var39 - var18 ^ arg3)
    if var38 < var39:
        var47 = arg3 - arg3 & var39 | var42
    else:
        var47 = var37 & var44
    var48 = 1954770526 - (-706067931 - arg4) & var18
    result = var37 & (var38 & var13 - var39 + var46) & var13 - arg3 + var18 & var43 + var44
    return result
def func9(arg22, arg23):
    var24 = ((arg22 ^ arg23) & arg22) + arg23
    var25 = 12 & -957569383
    if arg22 < var24:
        var26 = arg23 - arg22 | var25
    else:
        var26 = (1162880182 + arg22) ^ (arg22 + 466)
    var27 = var24 | var24
    var28 = -1088235555 - var27 & arg23 & var24
    var29 = -303338081 - arg22 + arg23
    var30 = arg23 & 1561400073 ^ (arg22 | arg22)
    var31 = (arg22 + var24) | arg22
    if var24 < arg23:
        var32 = 1324866171 | arg23
    else:
        var32 = (var28 | -420 & -196631505) ^ var25
    var33 = (var25 - 1664068293 - -1941237360) - var28
    var34 = var33 | var28 + var24
    var35 = var25 | var28 | var27 & var25
    result = var28 | ((var33 - var27 ^ var25) + var31)
    return result
def func8():
    closure = [6]
    def func7(arg19, arg20):
        closure[0] += func9(arg19, arg20)
        return closure[0]
    func = func7
    return func
var21 = func8()
def func6(arg14, arg15):
    var16 = 0
    for var17 in xrange(47):
        var16 += arg15 | -6
    return var16
def func3(arg5, arg6):
    var7 = 0
    for var8 in range(48):
        var7 += (1 & arg6) + var8
    return var7
def func4(arg10, arg11):
    closure = [0]
    def func5(acc, rest):
        var12 = (rest + 9) | (closure[0] & 9)
        closure[0] += var12
        if acc == 0:
            return var12
        else:
            result = func5(acc - 1, var12)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 52'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
