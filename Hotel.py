items = {
    'pizza':40,
    'coffee':20,
    'salad':90,
    'icecreams':50
}
print('welcome to our retaurent')
for it in items:
    print(it,items[it])
ans='y'
customerOrder=0
while(ans=='y'):
    print('enter yout order =>')
    order= input()
    if order in items:
        customerOrder+=items[order]
    ans=input('do you need anything more y/n')

print('your total bill :',customerOrder)
