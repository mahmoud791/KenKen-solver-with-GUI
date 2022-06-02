from time import time
from kenken import *
from csv import writer
import sys

def timing(kenken, algorithm):
       
        kenken.checks = kenken.nassigns = 0

        dt = time()

        assignment = algorithm(kenken)

        dt = time() - dt

        return assignment, (kenken.checks, kenken.nassigns, dt)



def generate_report(iterations, out):
   
    bt         = lambda ken: backtracking_search(ken)
    
    fc         = lambda ken: backtracking_search(ken, inference=forward_checking)
    
    ac        = lambda ken: backtracking_search(ken, inference=mac)
    

    algorithms = {
        "BT": bt,
        
        "BT & FC": fc,
        
        "BT & AC": ac,
        
    }

    with open(out, "w+") as file:

        out = writer(file)

        out.writerow(["Algorithm", "Size",  "Constraint checks", "Assignments", "Completion time"])

        for name, algorithm in algorithms.items():
            for size in range(3, 8):
                checks, assignments, dt = (0, 0, 0)
                for iteration in range(1, iterations + 1):
                    size, cliques = generate(size)

                    assignment, data = timing(Kenken(size, cliques), algorithm)
                    

                    print("algorithm =",  name, "size =", size, "iteration =", iteration, "result =", "Success" if assignment else "Failure", file=sys.stderr)

                    checks      += data[0] / iterations
                    assignments += data[1] / iterations
                    dt          += data[2] / iterations
                    
                out.writerow([name, size, checks, assignments, dt])



generate_report(7,'C:\\Users\Mahmoud\Desktop\kenken-python-master\src\out.csv')