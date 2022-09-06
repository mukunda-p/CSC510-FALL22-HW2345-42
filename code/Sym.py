class Sym:
    def __init__(self) -> None:
        self.n = 0
        self._has = dict()


    
    def add(self, v):
        if v != '?':
            self.n = self.n + 1
            self._has[v] = 1 + self._has.get(v, 0)
    


