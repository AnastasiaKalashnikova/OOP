from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def print(self, markup, is_last):
        pass
    
    @abstractmethod
    def clone(self):
        pass


class IPAddress(Component):
    def __init__(self, address):
        self.address = address
    
    def print(self, markup, is_last):
        if is_last:
            separator = '\\-'
        else:
            separator = '+-'
        print(f"{markup}{separator}{self.address}")
    
    def clone(self):
        return IPAddress(self.address)


class CPU(Component):
    def __init__(self, cores, speed):
        self.cores = cores
        self.speed = speed
    
    def print(self, markup, is_last):
        if is_last:
            separator = '\\-'
        else:
            separator = '+-'
        print(f"{markup}{separator}CPU, {self.cores} cores @ {self.speed}MHz")
    
    def clone(self):
        return CPU(self.cores, self.speed)


class Memory(Component):
    def __init__(self, size):
        self.size = size
    
    def print(self, markup, is_last):
        if is_last:
            separator = '\\-'
        else:
            separator = '+-'
        print(f"{markup}{separator}Memory, {self.size} MiB")
    
    def clone(self):
        return Memory(self.size)


class HDD(Component):
    SSD = 0
    MAGNETIC = 1
    def __init__(self, storage_type, size):
        self.size = size
        self.storage_type = storage_type
        self.partitions = []
    
    def add_partition(self, number, size, designation):
        self.partitions.append({
            'number': number,
            'size': size,
            'designation': designation
        })
    
    def print(self, markup, is_last):
        if is_last:
            separator = '\\-'
        else:
            separator = '+-'
        print(f"{markup}{separator}HDD, {self.size} GiB")
        
        new_markup = markup + ('  ' if is_last else '| ')
        for i, part in enumerate(self.partitions):
            is_last_part = i == len(self.partitions) - 1
            if is_last_part:
                part_separator = '\\-'
            else:
                part_separator = '+-'
            print(f"{new_markup}{part_separator}[{part['number']}]: {part['size']} GiB, {part['designation']}")
    
    def clone(self):
        new_hdd = HDD(self.storage_type, self.size)
        for part in self.partitions:
            new_hdd.add_partition(part['number'], part['size'], part['designation'])
        return new_hdd


class Host(Component):
    def __init__(self, name):
        self.name = name
        self.ips = []
        self.components = []
    
    def add_ip(self, ip):
        self.ips.append(IPAddress(ip))
    
    def add_component(self, component):
        self.components.append(component)
    
    def print(self, markup, is_last):
        if is_last:
            separator = '\\-'
        else:
            separator = '+-'
        print(f"{markup}{separator}Host: {self.name}")
        
        new_markup = markup + ('  ' if is_last else '| ')
        
        for ip in self.ips:
            ip.print(new_markup, False)
        
        for i, comp in enumerate(self.components):
            comp.print(new_markup, i == len(self.components) - 1)
    
    def clone(self):
        new_host = Host(self.name)
        for ip in self.ips:
            new_host.add_ip(ip.address)
        for comp in self.components:
            new_host.add_component(comp.clone())
        return new_host


class Network:
    def __init__(self, name):
        self.name = name
        self.hosts = []
    
    def add_host(self, host):
        self.hosts.append(host)
    
    def print_network(self):
        print(f"Network: {self.name}")
        for i, host in enumerate(self.hosts):
            host.print("", i == len(self.hosts) - 1)
    
    def clone(self):
        new_net = Network(self.name)
        for host in self.hosts:
            new_net.add_host(host.clone())
        return new_net
    
    def find_host(self, name):
        for host in self.hosts:
            if host.name == name:
                return host
        return None