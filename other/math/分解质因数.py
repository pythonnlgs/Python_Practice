def zhishu(num):
    for i in range(2,num):
        if num % i == 0:
            return True  #合数
    else:
        return False  #质数

def zhiyinshufenjie(num):
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
    str1 = ''
    for i in range(len(tmp)):
        if i == 0:
            str1 = str1 + str(tmp[i])
        else:
            str1 = str1 + '*' + str(tmp[i])
    returnstr = '%d = %s' % (nump,str1)
    return returnstr

print(zhiyinshufenjie(411))