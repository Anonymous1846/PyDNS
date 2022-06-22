from dns import resolver
import pyfiglet
import sys

RECORD_TYPES=['A','AAAA','CNAME','MX','TXT'] #list of all recognized record types
if __name__=="__main__":
    heading=pyfiglet.figlet_format('PyDNS')
    print('Version 1.0')
    print(heading)
    if len(sys.argv)==1:
        print('Usage: main.py <domain>\nExiting.....!')
        exit(1)
    else:
        DOMAIN = sys.argv[1]        #getting the domain name from the command line args 
        for record in RECORD_TYPES:
            try:
                print(f'\n{record} records !')
                print('-'*50)
                _resolved = resolver.resolve(DOMAIN,record)
                for server in _resolved:
                    print(server.to_text())
            except resolver.NoAnswer:
                print('DNS no response !')
            except KeyboardInterrupt:
                print('Exiting.......!')
                quit()
