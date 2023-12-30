import urllib.request as url

bulbapioff='https://api.thingspeak.com/update?api_key=LBXMM8KLIB9KLUO6&field1=0'
bulbapion='https://api.thingspeak.com/update?api_key=LBXMM8KLIB9KLUO6&field1=10'
fanapioff='https://api.thingspeak.com/update?api_key=KNG1OKEVQ5R0HSO1&field1=0'
fanapion='https://api.thingspeak.com/update?api_key=KNG1OKEVQ5R0HSO1&field1=10'

while True:
    f=open('log.txt','r')
    try:
        data=int(f.read())
        #print(data)
        if(data==1):
            print(data)
            while True:
                k=url.urlopen(bulbapion).read()
                print(k)
                k=k.decode('utf-8')
                if(k!=0):
                    print('query1 sent')
                    break
        elif(data==2):
            print(data)
            while True:
                k=url.urlopen(bulbapioff).read()
                print(k)
                k=k.decode('utf-8')
                if(k!=0):
                    print('query2 sent')
                    break
        elif(data==5):
            print(data)
            while True:
                k=url.urlopen(fanapioff).read()
                print(k)
                k=k.decode('utf-8')
                if(k!=0):
                    print('query5 sent')
                    break
        elif(data==6):
            print(data)
            while True:
                k=url.urlopen(fanapion).read()
                print(k)
                k=k.decode('utf-8')
                if(k!=0):
                    print('query6 sent')
                    break
    except Exception as e:
        print('Exception Raised',e)
    
    f.close()
    f=open('log.txt','w')
    f.write('0')
    f.close()