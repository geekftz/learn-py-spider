import json

jsondata = '''
{
"MemberList":[
{
"UserName":"小帅b",
"sex":"男"
},
{
"UserName":"小帅b的1号女朋友",
"sex":"女"
},
{
"UserName":"小帅b的2号女朋友",
"sex":"女"
}
]
}
'''

myfriends = json.loads(jsondata)
memberList = myfriends.get('MemberList')

print(memberList)
