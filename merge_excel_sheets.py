

import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("in_file")
parser.add_argument("out_file")
args = parser.parse_args()

print(args.in_file,  help = 'Input file' )
print(args.out_file,  help = 'Output file')

df = pd.read_excel(args.in_file, sheet_name = None ,  header=None)

writer2 = pd.ExcelWriter(args.out_file)


df2 = pd.concat(df , sort=False)
df2.to_excel(writer2, sheet_name = 'merge', index = False)

writer2.save()
