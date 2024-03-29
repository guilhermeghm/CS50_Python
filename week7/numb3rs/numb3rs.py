import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
   if not re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
       return False

   bytes = ip.split(".")

   if (len(bytes)) > 4:
    return False
  
   for ip_byte in bytes:
       if int(ip_byte) < 0 or int(ip_byte) > 255:
           return False
   return True

if __name__ == "__main__":
    main()