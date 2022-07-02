import argparse
from datetime import datetime

import pandas as pd

TIMESTAMP_COL = 'time'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('column', type=str)
    parser.add_argument('condition', type=str)
    parser.add_argument('--debug')
    args = parser.parse_args()

    if args.debug:
        print(args.filename)
        print(args.column)
        print(args.condition)
        print()

    df = pd.read_csv(f'in/{args.filename}')
    col = df[args.column]
    mask = eval(args.condition)
    filtered = df[mask]
    dates = filtered[TIMESTAMP_COL]
    dates = dates.apply(datetime.utcfromtimestamp)

    for dt in dates:
        print(dt)
