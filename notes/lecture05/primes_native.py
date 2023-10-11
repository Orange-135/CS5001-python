# 找出零到终端输入数字中的质数
# 对于比较大的数字来说时间太长了，如何修改程序使缩短时间
import sys

def main(max_val):
    #point out prime numbers from 2 to max_val
    START_VAL = 2
    START_DIVISOR = 2

    print(START_VAL)

    candidate = START_VAL + 1

    while (candidate <= max_val):
        is_prime = True
        
        div = START_DIVISOR
        while (div < candidate):
            if (not(candidate % div)):#candidate % div == 0
                is_prime = False
            div += 1

        if (is_prime):
            print(candidate)
        
        candidate += 1

main(int(sys.argv[1]))
