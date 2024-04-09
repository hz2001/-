# 第一题
'''
Example 1:
Input: source = "abc", target = "abcbc"Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of
source "abc".
Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string
due to the character "d" in target string.
Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
'''
def question1(source:str = "xyz", target:str = "xzyxz") -> int:
    # 使用2 pointers 扫描
    sourceIndex = 0
    targetIndex = 0
    substringCount = 1 # 最少一个
    while targetIndex != len(target): #如果不到最后则一直循环
        if target[targetIndex] not in source: # 如果target中有不存在于source的字符，则必定找不到，故return -1
            substringCount = -1
            break
        if sourceIndex == len(source):
            sourceIndex = 0 # 一遍扫描完成，增加count
            substringCount += 1 # 开启下一个substring search
        elif source[sourceIndex] == target[targetIndex]: # 如果找到顺序中的substring则找target中的下一位
            targetIndex += 1
        else:
            sourceIndex += 1 # 如果此循环什么都不做则自增

    print(source,target)
    print(substringCount)
    return substringCount

# 第二题
'''
每输入一个字符串,检查括号是否匹配。如果只有左括号没有右括号,我们就在它下面标一个x
,如果只有右括号,我们就在它下面标一个问号。每行为单独测试用例。
样例输入:
bge)))))))))
((IIII))))))
()()()()(uuu
))))UUUU((()
样例输出:

bge)))))))))
?????????
((IIII))))))
????
()()()()(uuu
x
))))UUUU((()
???? xx
'''

def question2(s:str) -> str:
    stack = [] # 使用stack作为数据结构进行处理    
    for i in s:
        if i == "(":
            stack.append('x') # 如果遇见左括号，则加入一个需要被消除的字符x
        elif i == ")":
            if stack != [] and stack[-1] == 'x': # 说明stack中有待匹配的左括号，我们需要消除它
                stack.pop()
            else:
                stack.append('?') # 说明没有左括号，所以直接append ？
    print(s)
    print("".join(stack))
    return "".join(stack)
    


if __name__ == "__main__":
    question1(source = "abc", target = "acdbc")
    question1(source = "abc", target = "abcbc")
    question1(source = "xyz", target = "xzyxz")
    
    
    question2("bge)))))))))")
    question2("((IIII))))))")
    question2("()()()()(uuu")
    question2("))))UUUU((()")


# 第三题 简述
# 请简述您希望加入我们团队的原因以及您期望从本次实习中获得什么。(限50字以内)
'''
最重要的两点如下：
1. 我的目标是做一个优秀的AI相关产品经理，为此我需要了解、理解并且上手先进的AI技术，我认为贵团队可以为我提供一个很好的成长性平台。
2. 我非常重视和行业尖端人士的交流，我们太容易被困在自己固定的信息流中，只有主动改变所处环境才能更为高效地提升自己。

'''