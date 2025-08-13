def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print(sorted(s1))
        print(sorted(s2))
        print("the given string is anagram")
    else:
        print("the given string aren't anagram")
s1="listen"
s2="silent"
check(s1,s2)

#calander
import calendar
# yy = 2025
# mm = 3
# print(calendar.month(yy,mm))
print(calendar.month(2004,7))
