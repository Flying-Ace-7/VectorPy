import math as m

class vec:
    def __init__(self,*args):
        self.col=list(args)
        self.dim=len(self.col)
    def __repr__(self):
        return "vec("+",".join(map(str,self.col))+")"
    def dimn(self,li:list):
        xo=tuple((self.col[_]for _ in li if _<self.dim and _>=0))
        return xo
    
    def mag(self):
        return m.sqrt(sum((map(lambda x: x**2,self.col))))
    def unit(self, mode="vector"):
        val=[self.col[_]/self.mag() for _ in range(self.dim)]
        return vec(*val) if mode=="vector" else tuple(val) if mode=="tuple" else None
    def selfplot_2d(self, start=(0,0), color='blue', head_width=0.2, head_length=0.3):
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.arrow(start[0], start[1], self.col[0], self.col[1], head_width=head_width, head_length=head_length, fc=color, ec=color)
        ax.set_xlim(min(start[0], start[0]+self.col[0])-1, max(start[0], start[0]+self.col[0])+1)
        ax.set_ylim(min(start[1], start[1]+self.col[1])-1, max(start[1], start[1]+self.col[1])+1)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Vector Plot')
        ax.grid(True)
        ax.set_aspect('equal', adjustable='box')
        plt.show()
    