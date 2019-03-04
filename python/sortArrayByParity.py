



class Solution(object):
    def sortArrayByParity(self, A):
        evenList=[]
        oddList=[]
        for i in A:
            modNum= i%2
            if modNum == 0:
                evenList.append(i)
            else:
                oddList.append(i)
        return(evenList+oddList)

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            A = stringToIntegerList(line)
            
            ret = Solution().sortArrayByParity(A)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
