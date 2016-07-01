import os # to excute linux command in python script
def send_data(data):
    f=open("data.txt",'w')
    f.write(data)
    f.close()
    os.system("scp data.txt pi@196.168.0.111:") # change pi to the remote user name
                                                #and the ip to your remote user nme
while True:
    data = raw_input("\nEnter what to send : ")
    send_data(data)
    if raw_input("Ener 0 to exit and any key to continue : ")=='0':break
