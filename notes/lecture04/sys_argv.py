#先在终端执行脚本， 并从外部传入参数（可以是多个），获得一个列表(list). sys.argv其实可以看作是一个列表，所以才能用[ ]提取其中的元素。其第一个元素是程序本身，随后才依次是外部传入的参数。
import sys


def main():
    print(sys.argv)

main()
