'''
https://leetcode-cn.com/problems/rearrange-words-in-a-sentence/

「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :

句子的首字母大写
text 中的每个单词都用单个空格分隔。
请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-words-in-a-sentence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         text = text.lower()
#         text = text.split() 
#         for i in range(len(text)):
#             text[i] = [len(text[i]),i,text[i]]
#         text.sort()
#         ans = ""
#         print(text[0][1])
#         text[0][2] = text[0][2][0].upper() + text[0][2][1:]
#         for i in text[:-1]:
#             ans += i[2] + " "
#         ans += text[-1][2]
                
#         print(ans)
        
#         return ans
text = input()
text = text.lower()
text = text.split() 

for i in range(len(text) - 1):
    for j in range(len(text) - 1 - i):
        if len(text[j]) > len(text[j+1]):
            temp = text[j]
            text[j] = text[j+1]
            text[j+1] = temp
text[0] = text[0][0].upper() + text[0][1:]
return " ".join(text)
print(" ".join(text))




'''
a = [[1,2],[2,3,4]]

'''