# function to return the median of 3 integers

def median_of_3(n1, n2, n3):
    if n1 < n2:
        if n2 < n3:
            return n2
        if n1 > n3:
            return n1
        else:
            return n3
    else:
        if n1 < n3:
            return n1
        if n2 > n3:
            return n2
        else:
            return n3
