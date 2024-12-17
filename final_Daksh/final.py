from abc import ABC, abstractmethod
from typing import Dict

# Abstraction
class DeviceReport(ABC):
    def __init__(self, device):
        self._device = device
    
    @abstractmethod
    def generate_report(self) -> str:
        pass

# Refined Abstractions
class BasicReport(DeviceReport):
    def generate_report(self) -> str:
        return f"Basic Report:\nUsage: {self._device.get_usage()}\nTemperature: {self._device.get_temperature()}°C"

class DetailedReport(DeviceReport):
    def generate_report(self) -> str:
        return f"Detailed Report:\nUsage: {self._device.get_usage()}\n" \
               f"Temperature: {self._device.get_temperature()}°C\n" \
               f"Metrics: {self._device.get_performance_metrics()}"

# Implementation interface
class Device(ABC):
    @abstractmethod
    def get_usage(self) -> Dict:
        pass
    
    @abstractmethod
    def get_temperature(self) -> float:
        pass
    
    @abstractmethod
    def get_performance_metrics(self) -> Dict:
        pass

# Concrete Implementations
# sample data
class CPU(Device):
    def __init__(self):
        self._cores = 4
        self._frequency = 3.2
        
    def get_usage(self) -> Dict:
        return {"cpu_total": 45, "per_core": [40, 50, 45, 46]}
    
    def get_temperature(self) -> float:
        return 65.5
    
    def get_performance_metrics(self) -> Dict:
        return {"cores": self._cores, "frequency": f"{self._frequency}GHz"}

class GPU(Device):
    def __init__(self):
        self._memory = 8
        self._clock_speed = 1.5
        
    def get_usage(self) -> Dict:
        return {"gpu": 80, "memory": "6.4GB/8GB"}
    
    def get_temperature(self) -> float:
        return 72.3
    
    def get_performance_metrics(self) -> Dict:
        return {"memory": f"{self._memory}GB", "clock": f"{self._clock_speed}GHz"}

class HDD(Device):
    def __init__(self):
        self._capacity = 1000
        self._rpm = 7200
        
    def get_usage(self) -> Dict:
        return {"read": "120MB/s", "write": "90MB/s"}
    
    def get_temperature(self) -> float:
        return 42.0
    
    def get_performance_metrics(self) -> Dict:
        return {"capacity": f"{self._capacity}GB", "rpm": self._rpm}

class RAM(Device):
    def __init__(self):
        self._total = 16
        self._type = "DDR4"
        
    def get_usage(self) -> Dict:
        return {"used": "12GB", "available": "4GB"}
    
    def get_temperature(self) -> float:
        return 45.0
    
    def get_performance_metrics(self) -> Dict:
        return {"total": f"{self._total}GB", "type": self._type}

# Example usage
if __name__ == "__main__":
    # Create devices
    cpu = CPU()
    gpu = GPU()
    hdd = HDD()
    ram = RAM()
    
    # Create reports
    basic_cpu = BasicReport(cpu)
    detailed_gpu = DetailedReport(gpu)
    basic_hdd = BasicReport(hdd)
    detailed_ram = DetailedReport(ram)
    
    # Generate reports
    print(basic_cpu.generate_report())
    print("\n" + detailed_gpu.generate_report())
    print("\n" + basic_hdd.generate_report())
    print("\n" + detailed_ram.generate_report())