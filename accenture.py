import sys
from typing import List

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

    for i, v in enumerate(lines):
        if(i == 0): n:int = v
        elif(i==1): arr:List[int] = v.split(" ")
    
    len_cnt = [0 for i in range(51)]

    for num in arr:
        len_cnt[int(num)] += 1

        if(len_cnt[int(num)]>=4):
            print('YES')
            return
    
    print('No')
    return



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)