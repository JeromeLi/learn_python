str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
index_temp = str1.find('www.fishc.com')
print(str1[index_temp:(index_temp + len('www.fishc.com'))])
print(index_temp, (index_temp + len('www.fishc.com')))
print(index_temp - len(str1), (index_temp + len('www.fishc.com')) - len(str1))
str2 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str2[::3])
