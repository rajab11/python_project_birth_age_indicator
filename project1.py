import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
    df = pd.read_excel(
        r'C:\Users\rajab\OneDrive\Documents\python_projects\project_#1\003_3.xls', sheet_name='esas')

    x_axis = df['years']
    y_axis = df['total']

    plt.plot(x_axis, y_axis)
    plt.xlabel('years')
    plt.ylabel('total')
    plt.show()

except Exception as e:
    print(e)
