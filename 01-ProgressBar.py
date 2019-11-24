'''
1.含有处理文件个数的情况
对于程序中有循环的地方，可以直接将range（365）替换成你的处理的文件个数
2.不含文件个数信息的情况
要满足是可迭代的便可以加入进度条，感觉天秀
'''
from tqdm import tqdm
import time
# for i in tqdm(range(365)):
#     time.sleep(0.2)
# 效果展示   12%|█▏        | 45/365 [00:09<01:04,  4.99it/s]
# for i in tqdm(['happy','new','year']):
#     time.sleep(1.5)
# # 对元祖类型可行
# for i in tqdm(('happy','new','year')):
#     time.sleep(1.5)
for i in tqdm({'year':2019,'month':1,'day':3}):
    time.sleep(1.5)
##效果展示 100%|██████████| 3/3 [00:04<00:00,  1.50s/it]
