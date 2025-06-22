
class SumSolution:
    
    def compute(self, x : int, y : int) -> int:
        if not (0 <= x <= 100 and 0 <= y <= 100):
            raise ValueError("Inputs must be between 0 and 100 inclusive.")
        
        return x + y
            
