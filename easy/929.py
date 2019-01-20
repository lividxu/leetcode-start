"""
题目列表:
https://leetcode-cn.com/problems/unique-email-addresses/
思路:
给定一个规则,便利一把所有的列表,用set进行一次计数即可;
python中的map最快即为{};
java中即可使用HashSet

"""


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        distinct_list = {}

        for email in emails:
            add = self.parse_email(email)
            distinct_list[add] = 0
        
        return len(distinct_list)

    """
        return an simply email add
    """
    def parse_email(self, email):
        # [0]:名称 [1]:uri
        email_list = email.split('@')

        # 处理'.' and '+'
        name = email_list[0].replace('.','')
        name = name.split('+')[0]

        return name +  email_list[1]

solution = Solution()
list = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
num = solution.numUniqueEmails(list)
print(num)



        