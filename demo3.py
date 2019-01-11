def main():
    # num = 0 #拥有宝石的数量

    # #print('输入宝石类型：')
    # J = set(input())
    # print(J)

    #print('输入拥有的石头：')
    #S = list(input())

    
    #集合
    set1 = {'a', 'b', 'c'}
    #列表
    list1 = ['abc', 123,set1] 
   
    print(list1[1:2])
    print(list1[2:])
    list1[2:] 
    #print(list1) 
    #字典
    dict1 = {'lxf':'刘栩丰', 'msw':'麦盛威', 'ct':'陈通', 'txs':'谭显森'}
    #元组
    tup1 = (list1, set1, dict1, 'a', 12)

    #print(tup1)
    #print(tup1[2]['msw'])

    # for x in S:
    #     if x in J:
    #         num += 1
    #     elif expression:
    #         pass
    #     else
    #     break
    #     continue

    # while 条件：

    #      break
    #     continue
    #for i in range(10):
    a = range(10)
    #print(a)
    # print('拥有的宝石数量：', num)

if __name__ == "__main__":
    main()