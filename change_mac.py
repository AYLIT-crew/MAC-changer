import subprocess, time, sys
from termcolor import colored
from pyfiglet import figlet_format

#function to change a string of length 12 to the format of a MAC address
def format_add(mac):
    new_mac = ''
    for i in range(12):
        if i%2 == 0 or i == 11:
            new_mac += mac[i]
        else:
            new_mac += mac[i]+':'
    return new_mac

def check_if_mac_avail(mac):
    data = subprocess.check_output(f'ifconfig hw ether {mac}'.split(' ')).decode().split('\n')


#function to give interfaces available
def check_interfaces():
    result = []
    data = subprocess.check_output(['ifconfig']).decode().split('\n')
    result.append(data[0][:data[0].index(':')])
    for i in range(len(data)):
        try:
            if data[i] == '':
                result.append(data[i+1][:data[i+1].index(':')])
        except:
            pass
    return result

#main function
def main(ma, i):
    subprocess.call('ifconfig', shell=True)
    print(colored('-'*20, 'red'))
    time.sleep(2)
    try:
        command = f'sudo ifconfig {i} down'
        subprocess.call(command, shell=True)
        print(colored('Command successful', 'green'))
    except:
        print(colored('Unexpected error!', 'red'))
    print(colored('-'*20, 'red'))
    time.sleep(2)
    try:
        command = f'sudo ifconfig {i} hw ether {ma}'
        subprocess.check_output(command.split())
        print(colored('Command successful', 'green'))
    except:
        print(colored('MAC not available', 'red'))
        subprocess.call(f'sudo ifconfig {i} up', shell=True)
        print('-'*10)
        print(colored('Interface up  again', 'green'))
        sys.exit()
    print(colored('-'*20, 'red'))
    time.sleep(2)
    try:
        command = f'sudo ifconfig {i} up'
        subprocess.call(command, shell=True)
        print(colored('Command successful', 'green'))
    except:
        print(colored('Unexpected error!', 'red'))
    print(colored('-'*20, 'red'))
    time.sleep(1)
    print(colored('Changed information:', 'red'))
    subprocess.call('ifconfig {i}', shell=True)


while True:
    #clears the screen
    subprocess.call('clear', shell=True)

    print(colored('-'*60, 'red'))
    print(colored(figlet_format('Change MAC')+'\n\t-A MAC address changer program\n\t-An AYLIT production', 'red'))
    print(colored('-'*60, 'red'))
    mac_address = input(colored('Enter a 12 character length string:', 'red')).strip()
    interface = input(colored("Enter the interface for which the MAC address should be changed to(type 'getinterfaces' to get a list of interfaces available):", 'red'))
    if interface == 'getinterfaces':
        print(colored('-'*20, 'red'))
        interfaces = check_interfaces()
        for i in range(len(interfaces)):
            print(colored(f'{str(i+1)}. {interfaces[i]}', 'green'))
        print(colored('-'*20, 'red'))
        interface = input(colored('Enter the interface:', 'red'))
        main(mac_address, interface)
    else:
        main(mac_address, interface)
    cont = input(colored('Press enter to quit', 'red'))
    if cont == '':
        break
