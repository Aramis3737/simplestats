def mean(vals):
    """Computes the mean from a list of values."""
    try:
        total = float(sum(vals))
        length = len(vals)
    except TypeError:
        raise TypeError("The list was not numbers.")
    except:
        print "Something unknown happened with the list."

def median(vals):
    vals.sort()
    z = len(vals)
<<<<<<< HEAD
    name = z / 2
=======
    list = z / 2
>>>>>>> 550973783198e287da94f03b6b03070998838485
    if z % 2 == 0:
       return mean([vals[index], vals[index - 1]])
    else:
       return vals[index]

def mode(vals):
    """Computes the mode from a list of values."""
    pass

def std(vals):
    """Computes the standard deviation from a list of values."""
    n = len(vals)
    if n == 0:
        return 0.0
    mu = sum(vals) / n
    if mu == 1e500:
        return NotImplemented
    var = 0.0
    for val in vals:
        var = var + (val - mu)**2
    return (var / n)**0.5

def var(vals):
    """Computes the variance from a list of values."""
    pass
 

