from abc import abstractmethod

class GenerativeArtificialInteligence:
    
    @abstractmethod
    def generate_response(self, message: str) -> str:
        pass
       
