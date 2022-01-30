'''
字母變大寫 字串.upper()
字母變小寫 字串.lower()


https://leetcode-cn.com/problems/rearrange-words-in-a-sentence/

「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :

句子的首字母大写
text 中的每个单词都用单个空格分隔。
请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-words-in-a-sentence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


text = "Leetcode is cool"
text = text.split()
text = text.lower()
text = "Leetcode is cool"
text = text.lower()
print(text)
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
text = "Keep calm and code on"
text = list(text.split())
ans = ""
for j in range(len(text)):
    for i in range(len(text)-1):
        if len(text[i])>len(text[i+1]):
            temp = text[i]
            text[i]= text[i+1]
            text[i+1]=temp
for i in range(len(text)):
    if i==0:
        text[i]=text[i][0].upper()+text[i][1:]
    else:
        text[i]=text[i].lower()
    ans+=text[i]
    ans+=" "
print(ans)
