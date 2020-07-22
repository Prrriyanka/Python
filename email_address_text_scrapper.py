import re
text='ran45356565dom string.whatever@sjd.com hello i am fin45e@df78789gmail.com'

#pattern=re.compile('r')
#pattern=re.compile('[random]+')
#pattern=re.compile('[a-zA-Z]+')
#pattern=re.compile('[a-zA-Z0-9]+')
pattern=re.compile('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-z0-9]+')
#forescaping . [/.] is used


#result =pattern.search(text)
result=pattern.findall(text)
print(result)
