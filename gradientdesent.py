import numpy as np
import matplotlib.pyplot as plt

function = lambda x: (x ** 3)-(3 *(x ** 2))+7

#Get 1000 evenly spaced numbers between -1 and 3 (arbitratil chosen to ensure steep curve)
x = np.linspace(-1,3,500)

#Plot the curve
plt.plot(x, function(x))
plt.show()


def deriv(x):
    
    '''
    Description: This function takes in a value of x and returns its derivative based on the 
    initial function we specified.
    
    Arguments:    
    x - a numerical value of x 
    
    Returns:    
    x_deriv - a numerical value of the derivative of x    
    '''
    
    x_deriv = 3* (x**2) - (6 * (x))
    return x_deriv


def step(x_new, x_prev, precision, l_r):
    
    '''
    Description: This function takes in an initial or previous value for x, updates it based on 
    steps taken via the learning rate and outputs the most minimum value of x that reaches the precision satisfaction.
    
    Arguments:    
    x_new - a starting value of x that will get updated based on the learning rate    
    x_prev - the previous value of x that is getting updated to the new one    
    precision - a precision that determines the stop of the stepwise descent     
    l_r - the learning rate (size of each descent step)
    
    Output:    
    1. Prints out the latest new value of x which equates to the minimum we are looking for
    2. Prints out the the number of x values which equates to the number of gradient descent steps
    3. Plots a first graph of the function with the gradient descent path
    4. Plots a second graph of the function with a zoomed in gradient descent path in the important area
    
    '''
    # create empty lists where the updated values of x and y wil be appended during each iteration    
    x_list, y_list = [x_new], [function(x_new)]
    # keep looping until your desired precision
    while abs(x_new - x_prev) > precision:        
        # change the value of x
        x_prev = x_new        
        # get the derivation of the old value of x
        d_x = - deriv(x_prev)        
        # get your new value of x by adding the previous, the multiplication of the derivative and the learning rate
        x_new = x_prev + (l_r * d_x)        
        print (" step", x_new, x_prev)
        # append the new value of x to a list of all x-s for later visualization of path
        x_list.append(x_new)        
        # append the new value of y to a list of all y-s for later visualization of path
        y_list.append(function(x_new))

    print ("Local minimum occurs at: "+ str(x_new))
    print ("Number of steps: " + str(len(x_list)))
        
    plt.subplot(1,2,2)
    plt.scatter(x_list,y_list,c="b", LineWidth = 2)
    plt.plot(x_list,y_list,c="g", LineWidth = 3)
    plt.plot(x,function(x), c="r")
    plt.title("Gradient descent")
    plt.show()

    plt.subplot(1,2,1)
    plt.scatter(x_list,y_list,c="g")
    plt.plot(x_list,y_list,c="g")
    plt.plot(x,function(x), c="r")
    plt.xlim([1.0,2.1])
    plt.title("Zoomed in Gradient descent to Key Area")
    plt.show()

step(0.5, 0, 0.0001, 0.1)