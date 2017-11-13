import csv
import os
import time
f = open("unique_ip.txt","r")
ip = f.readline()
unique_ip=ip.split(",")
print(unique_ip)
'''
with open("unique_ip.txt", "r") as ins:
    unique_ip = []
    for line in ins:
        unique_ip.append(line) 
print("Unique IP address from unique_ip.txt file\n") 
print("unique ip array length= ",len(unique_ip))   
print("".join(unique_ip))
'''
 
time = []
source = []
destination= []
packet_length=[]
 

def readMyFile(filename):
    
 
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            time.append(row[1])
            source.append(row[2])
            destination.append(row[3])
            packet_length.append(row[5])
 
    return time,source,destination,packet_length

path = 'C:\\Users\\Prima\\Documents\\LiClipse Workspace\\EdgeConnex\\Pcap'
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
print(csv_files)






i=0
while i<len(unique_ip):
    j=0
    while j< len(csv_files):
        readMyFile(csv_files[j])
        k=0
        while k< len(csv_files[j]):
            if(unique_ip[i]==source[k]):
                #writer = csv.writer(f)
                with open("SourceToDestination.csv", "w") as uplink_file:
                    wr = csv.writer(uplink_file)
                    wr.writerow({'Time': time[k], 'Source': source[k],'Destination': destination[k], 'Length': packet_length[k]})


            k=k+1
        j=j+1
    
    i=i+1

#uplink_file.closed()












'''
i=0
while i<len(csv_files):
    dir=str(path+csv_files[i])
    #print(dir)
    time,source,destination,packet_length=readMyFile(dir)
    print(unique_ip)
    j=0
    while j< len(unique_ip):
        k=0
        while k< len(source):
            if(unique_ip[j]==source[k]):
                writer.writerow({'Time': time[k], 'Source': source[k],'Destination': destination[k], 'Length': packet_length[k]})
            k=k+1
        j=j+1
    
    i=i+1            
readMyFile('capture1.csv')
print("arrays from csv file") 
print(time)
print(source)
print(destination)
print(packet_length)
'''

