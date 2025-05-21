import ipaddress

class IpTools:
    def __init__(self, ip, cidr):
        self.ip = ip
        self.cidr = cidr
        self.network_address = self.calculate_network_address()
        self.broadcast_address = self.calculate_broadcast_address()
        self.subnet_mask = self.calculate_subnet_mask()
        self.wildcard_mask = self.calculate_wildcard_mask()
        self.host_range = self.calculate_host_range()

    def calculate_network_address(self):
        # calculate network address by applying subnet mask to IP
        ip_parts = list(map(int, self.ip.split('.')))
        mask = (0xffffffff << (32 - self.cidr)) & 0xffffffff
        network = [ip_parts[i] & (mask >> (8 * (3 - i)) & 0xff) for i in range(4)]
        return '.'.join(map(str, network))

    def calculate_broadcast_address(self):
        # calculate broadcast address by applying inverted subnet mask to IP
        ip_parts = list(map(int, self.ip.split('.')))
        mask = (0xffffffff << (32 - self.cidr)) & 0xffffffff
        broadcast = [ip_parts[i] | (~mask >> (8 * (3 - i)) & 0xff) for i in range(4)]
        return '.'.join(map(str, broadcast))

    def calculate_subnet_mask(self):
        # calculate subnet mask from CIDR notation
        mask = (0xffffffff << (32 - self.cidr)) & 0xffffffff
        subnet_mask = [(mask >> (8 * (3 - i)) & 0xff) for i in range(4)]
        return '.'.join(map(str, subnet_mask))

    def calculate_wildcard_mask(self):
        # calculate wildcard mask as the inverse of subnet mask
        subnet_mask = self.calculate_subnet_mask().split('.')
        wildcard_mask = [255 - int(octet) for octet in subnet_mask]
        return '.'.join(map(str, wildcard_mask))

    def calculate_host_range(self):
        # calculate the first and last usable host addresses in the subnet
        network_address = self.calculate_network_address().split('.')
        broadcast_address = self.calculate_broadcast_address().split('.')
        first_host = network_address[:]
        first_host[-1] = str(int(first_host[-1]) + 1)
        last_host = broadcast_address[:]
        last_host[-1] = str(int(last_host[-1]) - 1)
        return '.'.join(first_host), '.'.join(last_host)
    
    def classe(self):
        # calcolo della classe con i leading bit
        first_byte_ip = int(self.ip.split('.')[0])
        if first_byte_ip & 0b10000000 == 0:
            return "A"
        elif first_byte_ip & 0b11000000 == 0b10000000:
            return "B"
        elif first_byte_ip & 0b11100000 == 0b11000000:
            return "C"
        elif first_byte_ip & 0b11110000 == 0b11100000:
            return "D"
        elif first_byte_ip & 0b11111000 == 0b11110000:
            return "E"
        else:
            return "Unknown"

    def get_ip_type(self):
        # determine if the IP is private, reserved, or public
        ip_obj = ipaddress.ip_address(self.ip)
        if ip_obj.is_private:
            return "Private"
        elif ip_obj.is_reserved:
            return "Reserved"
        else:
            return "Public"
        
    def add(self, n):
        # save all 4 byte of the ip address on 4 different variables
        b1, b2, b3, b4 = map(int, self.ip.split("."))

        # just add the value to the fourth byte 
        b4 += n
        
        # check if every bytes is over than 255 in a loop
        while b4 > 255:
            b4 -= 256
            b3 += 1
        while b3 > 255:
            b3 -= 256
            b2 += 1
        while b2 > 255:
            b2 -= 256
            b1 += 1

        # obvisually if the number is too large so the first byte exceed than 255 return an error
        if b1 > 255:
            raise Exception(f"Resulting IP exceeds the maximum allowable value in the first byte: {b1}")
        return str(b1)+"."+str(b2)+"."+str(b3)+"."+str(b4)
    
    def sub(self, n):
        # save all 4 byte of the ip address on 4 different variables
        b1, b2, b3, b4 = map(int, self.ip.split("."))

        # just sub the value to the fourth byte 
        b4 -= n
        
        # check if every bytes is negative in a loop
        while b4 < 0:
            b4 += 256
            b3 -= 1
        while b3 < 0:
            b3 += 256
            b2 -= 1
        while b2 < 0:
            b2 += 256
            b1 -= 1

        # obvisually if the first byte is negative return an error
        if b1 < 0:
            raise Exception(f"Resulting IP exceeds the maximum allowable value in the first byte: {b1}")
        return str(b1)+"."+str(b2)+"."+str(b3)+"."+str(b4)