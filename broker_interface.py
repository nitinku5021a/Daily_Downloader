from abc import ABC, abstractmethod

class get_instruments(ABC):

    @abstractmethod
    def get_login(self):
        pass
    
    @abstractmethod
    def get_all_instruments(self):
        pass
