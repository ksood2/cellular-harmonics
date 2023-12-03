from scipy.ndimage import gaussian_filter1d

def sg_derivative(evals): # use Savitzky-Golay filter to compute smoothed eigenvalue derivative
    evals = [evals[2], evals[1]] + evals + [evals[-2], evals[-3]]
    d_list = []
    for i in range(2, len(evals)-2):
        derivative = 1/12 * (evals[i-2]-8*evals[i-1]+8*evals[i+1]-evals[i+2]) # Savitzky-Golay filter derivative
        d_list.append(derivative)
    d_list = d_list[2:(len(d_list)-2)]
    for i in range(2, len(evals)-2):
        d_list = gaussian_filter1d(d_list, 5) # convolve with Gaussian filter
    return d_list

