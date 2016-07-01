def recived_data():
    f=open("data.txt",'r')
    data= f.read()
    f.close()
    return data;

data=recived_data()
print data
