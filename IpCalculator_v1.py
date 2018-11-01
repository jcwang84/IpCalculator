import ipaddress
#Validate ip adress 
def validate_ipaddress(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as errorCode:
         pass
    return False
 
#all string questions, easy to update or delete, keep main() clean
def text_fucntion(number):
    text_list = ["Please enter an ip address<ie:216.216.216.1>(q for quit):\n",
                 "Please enter an subnet address<ie:255.255.255.0>(q for quit):\n",
                 "This is an invalid address.\n" ,
                 "Quit(q) or Run Again(enter)\n"  
                ]  
    return text_list[number]


#create empty space in terminal
def empty_space():
    print()
    print()



#taking ip and subnet input call validate_ipaddress and text_fucntion
def input_ipnsubnet(text_number):
    
    addr=input(text_fucntion(text_number))
    if(addr.lower()=='q'):
        exit(0)
    else:    
        while(True):
            
            if(validate_ipaddress(addr)==False):
                print(text_fucntion(2))
            else:
                empty_space()
                break
            addr=input(text_fucntion(text_number))
        
    return addr

#all the result prints +split ip addresses and calculate indiviually for Wildcard and subnet binary
def print_fuction(subnet_mask_address,ip_networkv):


    ipbinary=subnet_mask_address.split(".")
    useable_ip=str(len(list(ip_networkv))-2)
    print()
    print()
    #print(ip_networkv)
    print('Network address:       ', ip_networkv.network_address)
    print('Broadcast address:     ', ip_networkv.broadcast_address)
    print('Subnet mask in binary: {0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ipbinary[0]),int(ipbinary[1]),int(ipbinary[2]),int(ipbinary[3])))
    print ('Wildcard mask:         {}.{}.{}.{}'.format(255-int(ipbinary[0]),255-int(ipbinary[1]),255-int(ipbinary[2]),255-int(ipbinary[3])))
    print('Number of useable host:'+useable_ip)
    empty_space()

    


#main
def main():
 
    
    while True:

        ipaddr=str(input_ipnsubnet(0))
        subnet_mask=input_ipnsubnet(1)
        
        full_net_addr=ipaddr+"/"+subnet_mask
        ip_networkv4=ipaddress.ip_network(full_net_addr,strict=False)
        print_fuction(subnet_mask,ip_networkv4)

        last_question=input(text_fucntion(3))
        if(last_question.lower()=='q'):
            break
    
    

if __name__ == "__main__":
    main()
