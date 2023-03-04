def reverse_String(s):
    str=''
    for i in s:
        str=i+str
    return str
s='india'
print(reverse_String(s))

""" Another method 
print(s[::-1])
"""