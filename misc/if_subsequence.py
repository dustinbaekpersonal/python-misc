def isSubsequence(s: str, t: str) -> bool:
    """Two pointer."""
    n, m = len(s), len(t)
    
    i = j = 0
    
    while i < n and j < m:
        if s[i] == t[j]:
            i+=1
            j+=1
        else:
            j+=1
    if i == n:
        return True
    return False
print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("aec", "abcde"))
print(isSubsequence("ab", "baab"))