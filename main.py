with open("unique_ip.txt", "r") as ins:
    unique_ip = []
    for line in ins:
        unique_ip.append(line)
 
print("Unique IP address from unique_ip.txt file\n")    
print("".join(unique_ip))