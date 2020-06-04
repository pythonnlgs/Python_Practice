def zhishu(num):
    for i in range(2,num):
        if num % i == 0:
            return True  #合数
    else:
        return False  #质数

olg = 0
def zhiyinshufenjie(num):
    global olg
    nump = num
    tmp = []
    if not zhishu(num):
        print(num, '是个质数，请输入一个合数')
    else:
        while num:
            if not zhishu(num) and num != 1:
                print(num)
                tmp.append(num)
                num = 0
            else:
                for i in range(2, int(num**(1/2))+1):
                    if num % i == 0 & (not zhishu(i)):
                        print(i)
                        tmp.append(i)
                        num = int(num/i) 
                        break
    tmp = sorted(tmp)
    zhiyinshuzhonglei = {}
    zhiyinshu = []
    for x in tmp:
        if not(x in zhiyinshu):
            zhiyinshu.append(x)
    for x in zhiyinshu:
        a = tmp.count(x)
        zhiyinshuzhonglei[x] = a
    str1 = ''
    for i in range(len(zhiyinshu) - 1):
        olg = 0
        y = zhiyinshu[olg]
        str1 = str1 + str(y) + '^' + str(zhiyinshuzhonglei[y]) + '*'
        olg += 1
    y = zhiyinshu[olg]
    str1 = str1 + str(y) + '^' + str(zhiyinshuzhonglei[y])
    sl = len(zhiyinshu)
    returnstr = '%d = %s %d共有%d种质因数' % (nump, str1, nump, sl)
    return returnstr

print(zhiyinshufenjie(8889))