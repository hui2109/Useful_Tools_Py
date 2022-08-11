'''
把一个浮点数分解成整数部分和小数部分字符串
num是需要被分解的浮点数
返回分解出来的整数部分和小数部分
第一个数组元素是整数部分，第二个数组元素是小数部分
'''
def divide(num):
    #将一个浮点数强制类型转换为int类型，即得到它的整数部分
    integer=int(num)
    #浮点数减去整数部分，得到小数部分，小数部分乘以100后再取整，得到两位小数
    fraction=round((num-integer)*100)
    #下面把整数和小数转换为字符串
    return (str(integer),str(fraction))

han_list=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
unit_list=['十','百','千']

'''
把一个4位的数字字符串变成汉字字符串
num_str是需要被转换的4位数字字符串
返回4位数字字符串被转换成汉字字符串
'''
def four_to_hanstr(num_str):
    result=''
    num_len=len(num_str)
    #依次遍历数字字符串的每一位数字
    for i in range(num_len):
        #把字符串转换成数值
        num=int(num_str[i])
        #如果不是最后一位数字，而且数字不是0，则需要添加单位（千、百、十）
        if i != num_len-1 and num != 0 :
            result += han_list[num] + unit_list[num_len-2-i]
        #否则不要添加单位
        else:
            result += han_list[num]
    return result

'''
把数字字符串变成汉字字符串
num_str是需要被转换的数字字符串
返回数字字符串被转换成汉字字符串
'''
def integer_to_str(num_str):
    str_len=len(num_str)
    if str_len>12:
        print('数字太大，翻译不了')
        return
    #如果大于8位，包含单位“亿”
    elif str_len>8:
        return four_to_hanstr(num_str[:-8])+'亿'+\
            four_to_hanstr(num_str[-8:-4])+'万'+\
            four_to_hanstr(num_str[-4:])+'元'
    #如果大于4位，包含单位“万”
    elif str_len>4:
        return four_to_hanstr(num_str[:-4])+'万'+\
            four_to_hanstr(num_str[-4:])+'元'
    else:
        return four_to_hanstr(num_str)+'元'
'''
把小数字符串变成汉字字符串
num_str是需要被转换的小数字符串
返回小数字符串被转换成汉字字符串
'''
def fraction_to_str(num_str):
    num_len=len(num_str)
    if int(num_str)==0:
        return '没有零钱'
    elif num_len==1:
        return han_list[int(num_str)]+'分'
    elif num_len==2 and num_str[-1]!= '0':
        return han_list[int(num_str[0])]+'角'+\
            han_list[int(num_str[1])]+'分'
    else:
        return han_list[int(num_str[0])]+'角'
'''
纠正多余的零
先查找汉字字符串中‘零零’的位置，再将其转换为list类型
删除list中‘零零’的位置，只删除一个
重复以上操作（最多重复8次），即可获得只包含一个‘零’的情况
'''
def correct_zero(num_str):
    for i in range(8):
        #将汉字字符串转换为list类型，便于后续删除
        list_num=list(num_str)
        zero_ordinal=num_str.find('零零')
        if zero_ordinal==-1:
            pass
        else:
            del list_num[zero_ordinal]
            num_str=''.join(list_num)
    return num_str

'''
最后，将靠近‘元’、‘万’、‘亿’的‘零’以及‘亿万’删除即可
'''
def correct_zero_new(hanzi_str):
    #将汉字字符串转换为list类型，便于后续删除
    list_hanzi=list(hanzi_str)
    #删除‘零元’
    yuan_ordinal=hanzi_str.find('零元')
    if yuan_ordinal==-1:
        pass
    else:
        del list_hanzi[yuan_ordinal]
    #删除‘万零’
    wanzero_ordinal=hanzi_str.find('万零')
    if wanzero_ordinal==-1:
        pass
    else:
        del list_hanzi[wanzero_ordinal+1]
    #删除‘零万’
    zerowan_ordinal=hanzi_str.find('零万')
    if zerowan_ordinal==-1:
        pass
    else:
        del list_hanzi[zerowan_ordinal]
    #删除‘亿零’
    yizero_ordinal=hanzi_str.find('亿零')
    if yizero_ordinal==-1:
        pass
    else:
        del list_hanzi[yizero_ordinal+1]
    #删除‘零亿’
    zeroyi_ordinal=hanzi_str.find('零亿')
    if zeroyi_ordinal==-1:
        pass
    else:
        del list_hanzi[zeroyi_ordinal]
    yiwan_str=''.join(list_hanzi)
    #最后还要删除特殊的‘亿万’
    yiwan_ordinal=yiwan_str.find('亿万')
    if yiwan_ordinal==-1:
        return yiwan_str
    else:
        list_yiwan=list(yiwan_str)
        del list_yiwan[yiwan_ordinal+1]
        return ''.join(list_yiwan)

#测试把一个浮点数分解成整数部分和小数部分
num=float(input('请输入一个浮点数：'))
integer,fraction=divide(num)
#测试把数字字符串变成汉字字符串,并去除多余的零
hanzi=integer_to_str(integer)+'，'+fraction_to_str(fraction)
#print(hanzi)
correct_hanzi=correct_zero(hanzi)
#print(correct_hanzi)
correct_hanzi_new=correct_zero_new(correct_hanzi)
print(correct_hanzi_new)