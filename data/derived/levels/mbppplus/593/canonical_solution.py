import re
def removezero_ip(ip):
 return re.sub('\.[0]*', '.', ip)
