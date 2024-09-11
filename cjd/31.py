# https://mp.weixin.qq.com/s/TRshz9w_wWRzYeAwD_kQHg

j = 0
for i in range(1, 501):
    j += 1
    while '9' in str(j) or j % 10 == 0:
        j += 1
print(j)
