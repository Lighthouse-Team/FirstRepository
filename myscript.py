import sys
def myfun(arg1):
    for i in len(arg1):
        print(arg1[i])

if __name__ == '__main__':
    print("脚本执行")
    myfun(sys.argv[1])