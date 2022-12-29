import os
for file in os.listdir():#今回は作業フォルダの中身を確認するためパス指定はない
    name, ext = os.path.splitext(file)
    if ext == '.py':
        f = open(file)
        lines = f.readlines()
        for c in lines:
            print(len(c))
            f.close()        