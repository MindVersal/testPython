import numpy as np
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('../data/mlbootcamp5_train.csv', sep=';', index_col='id')
    pd.set_option('display.width', 100)
    print('DataFrame head: \n{}'.format(df.head()))
    print('DataFrame shape: {}'.format(df.shape))
