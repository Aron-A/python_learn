def maximo(x, y, z):

    if (x > y) and (y > z) :
        return x

    elif (x < y) and (y < z):
        return z
    
    else:
        if (x > y) and (y > z):
            if x > z:
                return x 
            else:
                return z
        
        else:
            print("São iguais.")

maximo(5, 10, 20)