# Return True if a string is a valid IPv4 address, else False.

# Examples:

# "192.168.1.1" → True

# "256.1.2.3" → False

# "1.2.3" → False

class Solution:
    def valid_IP_V4(self, ip:str) -> bool:
        parts = ip.split(".")
        if len(parts) != 4: # IPv4 address needs to have 4 parts
            return False
        
        for part in parts: # part is one section of the ip, e.g. 192
            if not part.isdigit():
                return False
            if len(part) > 1 and part[0] == "0": # leading zero check: if the number has more than 1 digit and it starts with 0
                return False
            # In IPv4, "01" is not valid, only "0" is valid
            
            num = int(part) # turns string into integer 
            if not (0 <= num <= 255): # Ipv4 rule: each part must be between 0 and 255
                return False
            
        return True # this block means "after" loop - only if none fails -> return true
    
# Time: O(n) where n is the number of parts, and k is the length of each part (effectively O(1)); we usually put it as O(n)
# Space: O(1) we did not create extra data stucture with the growth of the input size
        




