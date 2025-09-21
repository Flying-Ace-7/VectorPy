from vec_class import vec
import math as m
class vec_methods:
    def vec_add(v1:vec,v2:vec, mode="vector"):
        """ Adds the two column vectors and outputs a new column vector."""
        if v1.dim!=v2.dim:
            raise ValueError("Vectors must be of same dimension to add.")
        val=[v1.col[_]+v2.col[_] for _ in range(v1.dim)]
        return vec(*val) if mode=="vector" else tuple(val) if mode=="tuple" else None
    def vec_sub(v1:vec,v2:vec, mode="vector"):
        """ Subtracts the two column vectors and outputs a new column vector."""    
        if v1.dim!=v2.dim:
            raise ValueError("Vectors must be of same dimension to subtract.")
        val= [v1.col[_]-v2.col[_] for _ in range(v1.dim)]
        return vec(*val) if mode=="vector" else tuple(val) if mode=="tuple" else None
    def vec_mult_scalar(v:vec,scalar:float, mode="vector"):
        """ Multiplies the column vector with a scalar and outputs a new column vector."""
        return vec(*[v.col[_]*scalar for _ in range(v.dim)]) if  mode=="vector" else tuple((v.col[_]*scalar for _ in range(v.dim))) if mode=="tuple" else None
    def vec_mult_dot(v1:vec,v2:vec):
        """ Multiplies the two column vectors and outputs a scalar."""
        if v1.dim!=v2.dim:
            raise ValueError("Vectors must be of same dimension to multiply.")
        return sum((v1.col[_]*v2.col[_] for _ in range(v1.dim)))
    def vec_mult_cross(v1:vec,v2:vec, mode="vector"):
        """ Multiplies the two column vectors and outputs a new column vector. Only for 3D vectors."""
        if v1.dim!=3 or v2.dim!=3:
            raise ValueError("Vectors must be of dimension 2 3 to multiply.")
        val=[v1.col[1]*v2.col[2]-v1.col[2]*v2.col[1],v1.col[2]*v2.col[0]-v1.col[0]*v2.col[2],v1.col[0]*v2.col[1]-v1.col[1]*v2.col[0]]
        return vec(*val)if mode=="vector" else tuple(val) if mode=="tuple" else None    


    def vec_rawmult_cross(v1:vec,v2:vec,theta:float, mode="vector"):
        if v1.dim!=2 or v2.dim!=2:
            raise ValueError("Vectors must be of dimension 2 to multiply.")
        val=v1.mag*v2.mag*m.sin(theta)
        return vec(0,0,val) if mode=="vector" else (0,0,val) if mode=="tuple" else None


    def vec_angle(v1:vec,v2:vec, in_degrees=False):
        """ Returns the angle between the two column vectors in radians or degrees."""
        if v1.dim!=v2.dim:
            raise ValueError("Vectors must be of same dimension to find angle.")
        val=vec_methods.vec_mult_dot(v1,v2)/(v1.mag()*v2.mag())
        val=m.acos(val)
        return m.degrees(val) if in_degrees else val

    def vec_proj(v1:vec,dim, mode="vector"):
        """ Projects the column vector to the given dimension and outputs a new column vector."""
        if dim<0 or dim>=v1.dim:
            raise ValueError("Dimension must be between 0 and "+str(v1.dim-1)+".")
        val=[v1.col[_]  for _ in range(v1.dim) if _<dim ]
        return vec(*val) if mode=="vector" else tuple(val) if mode=="tuple" else None

vec_a=vec(1,2,3)
print(vec_a.unit())