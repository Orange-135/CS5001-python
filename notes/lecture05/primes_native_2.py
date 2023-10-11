import sys
import math

def main(max_val):
    #point out prime numbers from 2 to max_val
    START_VAL = 2
    START_DIVISOR = 3

    print(START_VAL)

    candidate = START_VAL + 1

    for candidate in range(START_VAL + 1, max_val+1, 2):#偶数一定不是质数，所以缩进2步
        is_prime = True
        
        sqare_root = math.sqrt(candidate)
        div = START_DIVISOR
        while (div <= sqare_root and is_prime):
          #非质数的两个除数都是在平方根前后
          #当不是prime时，可以不执行while步骤
            if (not(candidate % div)):#candidate % div == 0
                is_prime = False
            div += 1

        if (is_prime):
            print(candidate)
        
        candidate += 1

main(int(sys.argv[1]))
