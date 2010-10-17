import _levmar


def leastsq(func, x0, meas, args=(), Dfun=None, max_iter = 1000, full_output=0):
    
    if Dfun != None:
        result, iterations, run_info =  _levmar.dder(func, Dfun, x0, meas, max_iter, data = args)
        
    else:
        result, iterations, run_info =  _levmar.ddif(func, x0, meas, max_iter, data = args)

    
    
    return result, iterations, run_info
