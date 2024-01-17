import re

# content = 'Xiaoshuaib has 100 bananas'
# res = re.match('^Xi.*(\d+)\s.*s$',content)
# # res = re.match('^Xi.*?(\d+)\s.*s$',content)
#
# print(res.group(1))
#
#
# content = 'Xiaoshuaib has 100 bananas'
# res = re.match('^Xi.*?(\d+)\s.*s$',content)
# print(res.group(1))

# content = """Xiaoshuaib has 100
# bananas"""

# content = 'Xiaoshuaib has 100 bananas'
#
# res = re.match('^Xi.*?(\d+)\s.*s$', content, re.S)
# print(res.group(1))

# import re
#
# content = """Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;"""
# res = re.findall('Xi.*?(\d+)\s.*?s;', content, re.Sr
# print(res)

# import re
#
# content = """Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas
# Xiaoshuaib has 100 bananas;
# Xiaoshuaib has 100 bananas;"""
# content = re.sub('\d+', '250', content)
# print(content)


import re

content = "Xiaoshuaib has 100 bananas"
pattern = re.compile('Xi.*?(\d+)\s.*s', re.S)
res = re.match(pattern, content)

print(res.group(1))
