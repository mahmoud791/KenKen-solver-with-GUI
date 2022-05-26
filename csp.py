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