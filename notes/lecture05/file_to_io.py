import sys

def main(files):
    """
     Summarizes poems
     """
    try:
       out = open("result.txt", "w")
    except OSError as e:
       print("Can't opem results.txt for writing")
       print(e)
       return
     
    for filename in files:
        try:
          file_handle = open(filename, "r", encoding="utf-8")
        except FileNotFoundError as e:
         print(f"{filename} not found")
         return
      #用python3 file_to_io.py poems\*调出第一行作为title，files之间的title会有空格,strip可以去掉空格
        title = file_handle.readline().strip()
        print(f"Title: >>{title}<<")
      #调出author
        author = file_handle.readline().strip()
        author = ' '.join(author.split()[1:])#去掉by
        print(f"Author: {author}")

      #将以上信息放在results里面，并且显示去除掉title和author外，正文有多少行
        line_count = 0
        for _line in file_handle:
         line_count += 1

        out.write("Processed poem:\n")
        out.write(f"Title: {title}\n") 
        out.write(f"Author: {author}\n") 
        out.write(f"Lines: {line_count}\n")
        out.write("\n")  

main(sys.argv[1:])
     #显示文件名
#      for file in files:
#           print(file)
##mkdir
##touch
##ls
##ls *
##out：输出数据
##chmod用来设置修改权限：chmod+用户标识+设置类型（+添加 =设置 —删除）+文件名
    