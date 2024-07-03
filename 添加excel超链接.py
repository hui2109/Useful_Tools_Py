import os
import pandas

df = pandas.read_excel(r'E:\桌面\数据.xlsx', sheet_name='Sheet2',
                       dtype={'登记号': 'str', '检查号': 'str', '超声图像': 'str', \
                              '超声报告': 'str', '病理报告': 'str'})
register1 = []
for i in range(26):
    register1.append(df['登记号'][i])
for m in range(26):
    for n in register1:
        if df['登记号'][m] == n:
            df.iloc[m, 6] = '=HYPERLINK(".' + '\\' + n + '\\' + '超声图像' + '",' + '"' + '超声图像' + '")'
            df.iloc[m, 7] = '=HYPERLINK(".' + '\\' + n + '\\' + '超声报告' + '",' + '"' + '超声报告' + '")'
            df.iloc[m, 8] = '=HYPERLINK(".' + '\\' + n + '\\' + '病理报告.pdf' + '",' + '"' + '病理报告' + '")'
with pandas.ExcelWriter(r'E:\桌面\数据1.xlsx', datetime_format='YYYY-MM-DD') as writer:
    df.to_excel(writer, sheet_name='qwe', index=False)
