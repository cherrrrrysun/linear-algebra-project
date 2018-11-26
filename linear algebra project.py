#A is the input matrx, and k is the number of singular values you want to return
#need a helper function that takes in ATA directly, which can be either iterative or recursive
#need to experiment a little to figure the reasonable power we want to raise ATA to
#need to experiment a little to choose the reasonable vector we want to multiply ATA^t with
def power_method (A, k):
    #compute ATA

    #raise ATA to a reasonably high power without compromising the runtime of the program
    #use a reasonable vector to multiply ATA^t with s.t. the resulting vector allows for
    #approximation of the singular vector
    #once the singular vector is acquired, compute ATA-\sigma\vec{u}\vec{v}^T
    #repeat the procedures after the first one with the new matrix until all k vectors are computed
    #return the list of singular stuff
    
    return False