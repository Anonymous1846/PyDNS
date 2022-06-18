import dns.resolver
import sys

if __name__=="__main__":
    print(dns.resolver.resolve(sys.argv[1], 'A')[0].to_text())
    if len(sys.argv)==1:
        print("Usage: main.py <domain>")
        sys.exit(1)