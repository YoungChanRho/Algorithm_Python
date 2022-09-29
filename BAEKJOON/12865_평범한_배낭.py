# knapsack 알고리즘

N, K = map(int,input().split())    # N: 물품의 수, K: 버틸 수 있는 무게
item = [list(map(int,input().split())) for _ in range(N)]   # 물건들의 정보가 담겨있는 리스트

lst_1 = [[] for _ in range(1<<len(item))]
lst_2 = [[] for _ in range(1<<len(item))]

for i in range(1<<len(item)):
    for j in range(len(item)):
        if i & (1<<j):
            lst_1[i].append(item[j][0])
            lst_2[i].append(item[j][1])
print(lst_1)
print(lst_2)

ans_lst = []
for i in range(len(lst_1)):
    if sum(lst_1[i]) <= K:
        ans_lst.append(sum(lst_2[i]))

print(max(ans_lst))


# N, K = map(int,input().split())    # N: 물품의 수, K: 버틸 수 있는 무게
# item = [list(map(int,input().split())) for _ in range(N)]   # 물건들의 정보가 담겨있는 리스트

# lst_1 = [[] for _ in range(1<<len(item))]
# lst_2 = [[] for _ in range(1<<len(item))]
# # lst_1 = []
# # lst_2 = []
# # print()
# for i in range(1<<len(item)):
#     # sub_weight_list = []
#     # sub_value_list = []
#     for j in range(len(item)):
#         if i & (1<<j):
#             lst_1[i].append(item[j][0])
#             lst_2[i].append(item[j][1])
#             # sub_weight_list.append(item[j][0])
#             # sub_value_list.append(item[j][1])
#     # lst_1.append(sub_weight_list)
#     # lst_2.append(sub_value_list)
# # print(lst_1)
# # print(lst_2)


# ans_lst = []
# for i in range(len(lst_1)):
#     if sum(lst_1[i]) <= K:
#         ans_lst.append(sum(lst_2[i]))

# print(max(ans_lst))