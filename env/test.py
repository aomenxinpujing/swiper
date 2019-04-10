# def quick_sort(L):
#     return q_sort(L, 0, len(L) - 1)
#
#
# def q_sort(L, left, right):
#     if left < right:
#         pivot = Partition(L, left, right)
#
#         q_sort(L, left, pivot - 1)
#         q_sort(L, pivot + 1, right)
#     return L
#
#
# def Partition(L, left, right):
#     pivotkey = L[left]
#
#     while left < right:
#         while left < right and L[right] >= pivotkey:
#             right -= 1
#         L[left] = L[right]
#         while left < right and L[left] <= pivotkey:
#             left += 1
#         L[right] = L[left]
#
#     L[left] = pivotkey
#     return left
#
#
# L = [5, 9, 1, 11, 6, 7, 2, 4]
#
# print(quick_sort(L))


# import time
# import datetime
#
#
# a =  time.localtime()
# b = time.strptime('01', "%d")
# print(type(a), type(b))
# print(a)
# breakpoint()
# e = a - b
# print(e)
# c = time.strftime("%Y-%m-%d %H:%M:%S", a)
#
# print(c)
import re
from functools import reduce
from itertools import permutations


# a = {
#     '1': 1,
#     '2': 2,
#     '3': 3,
# }
#
# k = zip(a.values(), a.keys())
# for i in k:
#     print(i)
#
# print(dict(k))
#
# print(a)
#
# f = {key: var for var, key in a.items()}
#
# print(f)

# lst = [1, 2, 3, 4, 5, 6, 8]
# k = sum(map(lambda x: x + 3, lst[::2]))
# k1 = sum([i + 3 for i in lst[::2]])
# print(k1)


# # 合并有序列表 -》》》 未完成
# lst1 = [1, 2, 3, 4]
# lst2 = [2, 4, 5, 6]
#
#
# def sort(ls1: list, ls2: list):
#     result = []
#     index1, index2 = 0, 0
#     len1, len2 = len(ls1), len(ls2)
#     while True:
#         if len1 >= index1 and len2 >= index2:
#             return result
#         flag = ls1[index1] < ls2[index2]
#         x = ls1[index1] if flag else ls2[index2]
#         if flag:
#             index1 += 1
#         else:
#             index2 += 1


# 排序
# lst = [3, 5, -4, -1, 0, -2, -6]
# p = sorted(lst)
# p.reverse()
# print(p)

# import os
# c = os.walk('.')  # dir,folder,file
# # dir为file的目录、folder为dir下的目录


# from itertools import combinations, product
# # groupby:用于分组
# # permutations：按照给定位数对可迭代对象内元素进行组合
# # combinations: 单个序列求n个成员的组合不重复情况
# # product:  对多个序列进行组合，且无重复
# lst = [1, 2, 3, 4]
#
# for i in range(len(lst)+1):
#     ite =  combinations(lst, i)
#     print(ite)
#     for j in ite:
#         print(list(j))


# # 数组模拟加法运算
# class NewList(list):
#     def __add__(self, other):
#         len = self.__len__()
#         if not isinstance(other, int):
#             raise TypeError('add_number type error')
#         for var in self[::-1]:
#             len -= 1
#             print(len)
#             sum = var + other
#             other = sum // 10
#             if other:
#                 self[len] = sum % 10 if len > 0 else sum
#             else:
#                 self[len] = sum
#                 break
#         return self
#
#
# c = NewList([1, 2, 8, 4])
# c = c + 80116
# print(c)


