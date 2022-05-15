import numpy as np 

x_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_values = np.array([1, 4, 1, 6, 4, 7, 4, 6, 10, 8])

def best_fit_line(x_values, y_values):
    m = (((x_values.mean() * y_values.mean()) - (x_values * y_values).mean()) / ((x_values.mean()) ** 2 - (x_values ** 2).mean()))

    b = y_values.mean() - m * x_values.mean()

    return m, b

m, b = best_fit_line(x_values, y_values)

print(f"regression line: y = {round(m, 2)}x + {round(b, 2)}")

x_prediction = 15
y_prediction = (m * x_prediction) + b

print(f"predicted coordinate: ({round(x_prediction, 2)}, {round(y_prediction, 2)})")

# y values of the regression line 
regression_line = [(m * x) + b for x in x_values]

# helper function to return the sum of the distances between the two y values squared
def squared_error(ys_orig, ys_line): 
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))

def r_squared_value(ys_orig, ys_line): 
    squared_error_regr = squared_error(ys_orig, ys_line) #  squarred error of regression line
    y_mean_line = [ys_orig.mean() for y in ys_orig] #  horizontal line (mean of y values)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line) #  squarred error of the y mean line
    return 1 - (squared_error_regr / squared_error_y_mean)

r_squared = r_squared_value(y_values, regression_line)
print(f"r^2 value: {round(r_squared, 2)}")


import matplotlib.pyplot as plt

plt.title("Linear Regression")
plt.scatter(x_values, y_values, color = '#5b9dff', label = 'data')
plt.scatter(x_prediction, y_prediction, color = '#fc003f', label = 'predicted')
plt.plot(x_values, regression_line, color = '000000', label = 'regression line')
plt.legend(loc = 4)
plt.savefig("graph.png")
