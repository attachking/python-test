import re

res1 = re.compile(r'<h1>.+</h1>', re.IGNORECASE).findall('asda dasd<H1>qweq we</H1>')
res2 = re.compile(r'\s', re.IGNORECASE).findall('asda dasd<H1>qweq we</H1>')
res3 = re.compile(r'\.').split('www.qq.com')
res4 = re.compile(r'[a-z][^cf][a-z]').findall('abc, acc, adc, aec, afc, ahc')
print(res1)
print(res2)
print(res3)
print(res4)


def convert(value):
    return '@' + value.group()


res5 = re.compile('js', re.I).sub(convert, 'c++ c java JS js ')
print(res5)

res6 = re.compile(r'[a-z][^cf][a-z]', re.I | re.A).match('abc, acc, adc, aec, afc, ahc')
print(res6)
print(res6.group())

res7 = re.compile(r'asd(.*)asd(.*)').search('asd242930295 python asd python')
print(res7.group(1))
print(res7.groups())
