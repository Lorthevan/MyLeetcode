class Solution:
    def longestPalindrome(self,s):
        ss = ''                     #装入加了#号的新字符串
        for i in s:
            ss = ss+'#'
            ss = ss+i
        ss = ss+'#'
        p = [0]*2001                #表示以i为中心的最长回文字符串半径
        start,end,maxlen,mx = 0,0,0,0  #mx是以id为中心的回文最右边，start end最长的开始和结束

        for i in range(len(ss)):
            if(i<mx):
                p[i] = min(p[2*id-i],mx-i)       #如果在id回文的边界之内，则可以借鉴对称位置的值
            else:
                p[i] = 1
            while((i - p[i])>=0 and i+p[i]<len(ss) and ss[i-p[i]] == ss[i+p[i]]):   #在已知基础上看还有没有其他值
                p[i] += 1
            if(mx<i+p[i]):                      #更新id和mx
                id = i
                mx = i+p[i]
            if(maxlen<(p[i]-1)):               #如果最大长度替换原来的
                maxlen = p[i]-1
                start = i+1-p[i]
                end = i+p[i]-1

        return ss[start:end+1].replace('#','')