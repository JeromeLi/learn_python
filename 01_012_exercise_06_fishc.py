list1 = ['1.Just do it', '2.一切皆有可能', '3.让编程改变世界', '4.Impossible is nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.fishc', '1.耐克']
list3 = [brand + ':' + slogan[2:] for slogan in list1 for brand in list2 if slogan[0] == brand[0]]
for each in list3:
    print(each)
