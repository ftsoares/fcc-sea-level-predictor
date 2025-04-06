import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',delimiter=',',float_precision='legacy')

    # Create scatter plot
    csiro_mask = df['CSIRO Adjusted Sea Level'] != None
    csiro_y = df.loc[csiro_mask,['CSIRO Adjusted Sea Level']].to_numpy().T[0]
    csiro_x = df.loc[csiro_mask,['Year']].to_numpy().T[0]

    fig, ax = plt.subplots(1,1)
    ax.scatter(
        x=csiro_x,
        y=csiro_y,
        marker='.',
        label='original data'
    )

    # Create first line of best fit
    result_1 = linregress(csiro_x,csiro_y)

    # Coefficient of determination (R-squared):
    # print(f"Fit1 R-squared: {result_1.rvalue**2:.6f}")

    # Plot the data along with the fitted line:
    fit1_x = np.concatenate([csiro_x[0:-1],range(csiro_x[-1],2051)])

    ax.plot(fit1_x, result_1.intercept + result_1.slope * fit1_x, 'r', label='fit 1')
    ax.legend()
    fig

    # Create second line of best fit
    fit2_index = (csiro_x == 2000).nonzero()[0][0]

    result_2 = linregress(csiro_x[fit2_index:],csiro_y[fit2_index:])

    # Coefficient of determination (R-squared):
    # print(f"Fit1 R-squared: {result_2.rvalue**2:.6f}")

    # Plot the data along with the fitted line:
    fit2_x = fit1_x[fit2_index:]

    ax.plot(fit2_x, result_2.intercept + result_2.slope * fit2_x, 'r', label='fit 2')
    ax.legend()
    fig

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    fig
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()