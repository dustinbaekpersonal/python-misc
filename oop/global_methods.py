class OptimisationAttempt:
    
    def __init__(self,):
        pass
    
    def _optimisation_attempt_1(self,):
        return 1
   
    def _optimisation_attempt_2(self,):
        return 2
    

def optimisation_attempt_3():
    return 3

if __name__ == "__main__":
    oa = OptimisationAttempt()
    
    for i in range(1, 3):
        print(globals())