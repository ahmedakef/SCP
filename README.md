# SCP (Secure Copy)

scrip to send data(instruction) to raspberry pi (or any device) on the  network using Secure Copy

## usage

download or clone it ,unzip it then go to the folder from terminal like

    cd ~/Documents/SCP
    python send.py

copy the file '**receive.py**' to the home of your raspberry
run the receive script
    python receive.py

## content

**send.py** : you can edit this file as you wand and just send the data using the function **send_data(data)**

**receive.py** : it have the function **recived_data()** which return the data received that you can use to take decisions 

**data.txt** : the file which will be send to the rasspberry containning the data

you can put the two functions in the same file to send and recive from each device

this will ask for the password to login every time so you can ignor this by follow these instructions
https://www.howtoforge.com/tutorial/ssh-and-scp-with-public-key-authentication/

## resources
https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md
