import ipaddress

class IPCalculator:
    def __init__(self, ip, cidr):
        self.ip = ip
        self.cidr = cidr
        self.network_address = self.calculate_network_address()
        self.broadcast_address = self.calculate_broadcast_address()
        self.subnet_mask = self.calculate_subnet_mask()
        self.wildcard_mask = self.calculate_wildcard_mask()
        self.host_range = self.calculate_host_range()

    def calculate_network_address(self):
        ip_parts = list(map(int, self.ip.split('.')))
        mask = (0xffffffff << (32 - self.cidr)) & 0xffffffff
        network = [ip_parts[i] & (mask >> (8 * (3 - i)) & 0xff) for i in range(4)]
        return '.'.join(map(str, network))

    def calculate_broadcast_address(self):
        ip_parts = list(map(int, self.ip.split('.')))
        mask = (0xffffffff << (32 - self.cidr)) & 0xffffffff
        broadcast = [ip_parts[i] | (~mask >> (8 * (3 - i)) & 0xff) for i in range(4)]
        return '.'.join(map(str, broadcast))

    def calculate_subnet_mask(self):
        mask = (0xffffffff << (32 - self.cidr)) & 0xffffffff
        subnet_mask = [(mask >> (8 * (3 - i)) & 0xff) for i in range(4)]
        return '.'.join(map(str, subnet_mask))

    def calculate_wildcard_mask(self):
        subnet_mask = self.calculate_subnet_mask().split('.')
        wildcard_mask = [255 - int(octet) for octet in subnet_mask]
        return '.'.join(map(str, wildcard_mask))

    def calculate_host_range(self):
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
        ip_obj = ipaddress.ip_address(self.ip)
        if ip_obj.is_private:
            return "Private"
        elif ip_obj.is_reserved:
            return "Reserved"
        else:
            return "Public"