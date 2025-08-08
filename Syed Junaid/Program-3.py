#  With a single integer as the input, generate the following until a = x [series of numbers]
# Output: (examples)
    # 1) input a = 1, then output : 1
    # 2) input a = 2, then output : 1
    # 3) input a = 3, then output : 1, 3, 5
a=int(input('Enter the number:\n'))

def odd_series(a):
    if a%2 == 0:
        a-=1
    nums=[2*i+1 for i in range(a) ]
    print(','.join(map(str,nums)))

odd_series(a)