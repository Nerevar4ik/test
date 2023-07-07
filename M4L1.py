# def str_counter(s): #N*2
#     for sym in s:
#         counter=0
#         for sub_sym in s:
#             if sym==sub_sym:
#                 counter+=1
#         print(sym,counter)

# def str_counter(s): #N*M
#      for sym in set(s):
#         counter=0
#         for sub_sym in s:
#             if sym==sub_sym:
#                 counter+=1
#         print(sym,counter)

def str_counter(s): #N
    syms_counter={}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0)+1
    print(syms_counter)


str_counter('aabbssddfs')

# str1='all33423dsf'
# print(set(str1))