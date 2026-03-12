def editDist(s1,s2,m,n):
    
    if m==0:
        return n
    if n==0:
        return m
    
    if s1[m-1]==s2[n-1]:
        return editDist(s1,s2,m-1,n-1)
    
    return 1 + min(
        editDist(s1,s2,m,n-1),
        editDist(s1,s2,m-1,n),
        editDist(s1,s2,m-1,n-1)
    )


str2="Saturday"

print("Edit Distance is:",editDist(str1,str2,len(str1),len(str2)))

print("performed by 44_Atharav Sawant")