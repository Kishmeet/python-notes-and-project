def longestSubstring(s):
    charSet=set()
    l=0
    res=0
    long=""
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l +=1
        charSet.add(s[r])
        if(r-l+1>res):
            long=s[l:r+1]
        res=max(res,r-l+1)
    return long,res
print(longestSubstring(input("enter:")))