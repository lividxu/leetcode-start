


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new_str = ''
        for i in str:
            num = ord(i)
            if num > 96 and num < 123:
                new_char = chr(num + 32)
                print(new_char)
                new_str += new_char
            else:
                new_str += i

        return new_str

rs = Solution()
l = rs.toLowerCase("abAba")
print(l)