from solver import first,count


class CSP():
   
    def __init__(self, variables, domains, neighbors, constraints):
        """Construct a CSP problem"""
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0
        
    def assign(self, var, val, assignment):
        
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
       
        def conflict(var2):
            return (var2 in assignment and
                    not self.constraints(var, val, var2, assignment[var2]))
        return count(conflict(v) for v in self.neighbors[var])