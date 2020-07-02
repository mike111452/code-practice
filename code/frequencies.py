import sys
r=False
for n in sys.stdin:
    word_ascii=[]
    ll=[]
    ans=[]
    
    #n=str(input("輸入一串"))
    if r:
        print()
    for i in n[:-1]:
        ascii_transform=ord(i)
        word_ascii.append(ascii_transform)
        word_ascii.sort(reverse=True)
   
    ll=list(set(word_ascii))
    
    ll.sort(reverse=True)
    
    for i in ll:
        ans.append([i,word_ascii.count(i)])
    ans=sorted(ans,key=(lambda x:x[1]))

    for j in  range(len(ans)):
        print(ans[j][0], ans[j][1])    
        #print((" ").join('%s' % id for id in ans[j]).strip())
    r=True 