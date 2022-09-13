import copy

class Row:
    
    def __init__(self,num_cells):
        self.cells=num_cells
        self.cooked=copy.deepcopy(self.cells)
        self.isEvaled=True