import random
import os
# Imgnum = 45
# path = "D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第九批\\09_第九批\\a"
# txtname = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第九批\\09_第九批\\a.txt'
# i = 0
# L = random.sample(range(0, Imgnum), Imgnum)
# filetype = ".jpg"  # 文件类型
# for filename in os.listdir(path):
#     portion = os.path.splitext(filename)  # 将文件名拆成名字和后缀
#     if portion[1] == filetype:  # 检查文件的后缀

#         newname = str(L[i]) + filetype
#         with open(txtname,'w') as f:
#             for j in L:
#                 f.writelines(str(j))
#                 f.write('\n')
#         print(newname)
#         filesname = os.path.join(path,filename)
#         new_path = os.path.join(path,newname) 
#         os.rename(filesname, new_path)  # 修改名称
#         i = i+1

json_path = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第九批\\09_第九批\\b'

txtname = 'D:\\gree_rice_rcognition\\Mask_RCNN-master\\train_data\\第九批\\09_第九批\\a.txt'
alllines = open(txtname)
line = alllines.readline()
while line:
    for json in os.listdir(json_path):
        portion = os.path.splitext(json)
        
        if portion[1] == '.json':
            new_names = line + portion[1]
            json_name = os.path.join(json_path,json)
            new_json_name = os.path.join(json_path,new_names)
            os.rename(json_name, new_json_name)

        
