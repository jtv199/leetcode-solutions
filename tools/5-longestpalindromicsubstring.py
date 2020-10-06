'''
    tests
        empty
        0
        10
        0101
        10101
        12101
        00011

    option1
        a moving reader that is the size of the entire string at first n**2
        gradualy decreasing in size by 1

'''
def is_pallindrome(s:str)-> bool:
    '''
    >>> is_pallindrome('010')
    True

    >>> is_pallindrome('10')
    False

    :param s:
    :return:
    '''
    return s == s[::-1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        buffer_size = len(s)
        max_substring = ''

        while buffer_size > len(max_substring):
            front_index = 0
            while front_index+buffer_size is not len(s)+1:
                assert buffer_size-front_index > -1
                buffer = s[front_index:buffer_size+front_index]
                if is_pallindrome(buffer) and len(buffer) > len(max_substring):
                    max_substring = buffer

                front_index+=1
            buffer_size -=1

        return max_substring

'''
    tests
        empty
        0
        10
        0101
        10101
        12101
        00011
'''
test_cases = [
    '',
    '0',
    '10',
    '122',
    '1222',
    '11',
    '0101',
    '10101',
    '12101',
    '00011',
    '0010010010010001010010',
    '010010191910191910191019'
]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    s = Solution()
    for i in test_cases:
        print(f"{i}   {s.longestPalindrome(i)}")