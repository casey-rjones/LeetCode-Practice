 #
 # toLowerCase.py
 #
 # Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
 #
 # Example 1:
 #
 # Input: "Hello"
 # Output: "hello"
 #
 # Example 2:
 #
 # Input: "PiTAs"
 # Output: "pitas"
 # Example 3:
 #
 # Input: "love"
 # Output: "love"
 #

class Solution(object):
    def toLowerCase(self, str):
        outputStr=''
        for s in str:
            if 'A' <= s and s <= 'Z':
                outputStr += s.lower()
            else:
                outputStr += s   
        return outputStr

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            str = stringToString(line)
            
            ret = Solution().toLowerCase(str)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
