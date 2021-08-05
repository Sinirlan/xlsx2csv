import sys
import os
import pandas as pd
import argparse


#set arguments from entered paramters
parser = argparse.ArgumentParser(description='Utility converting xlsx files to csv with optional custom delimiter')
parser.add_argument('-i', '--input', action="store", help='Input xlsx file')
parser.add_argument('-o', '--output', action="store",  help='Folder to which output file will be saved. If not specified will save in same location as input file (If contains spaces enclose in quotation marks)')
parser.add_argument('-d', '--delimiter', action="store", help='Define delimiter, if empty default delimiter (comma) will be used')
parser.add_argument('-a', '--ascii', action="store_true", help='Flag if delimiter is provided as ASCII code')

 # if no parameters entered show help (-h)
if len(sys.argv[1:])==0:
    parser.print_help()
    parser.exit()

#store arguments in variables
args = parser.parse_args()
input_file = args.input
output_folder = args.output
delimiter_str = args.delimiter
IsASCII_flg = args.ascii

#check if delimiter is defined and if its provided as ASCII code, if not use comma
if delimiter_str and IsASCII_flg:
    delimiter = chr(int(delimiter_str))
elif delimiter_str and not IsASCII_flg:
    delimiter = delimiter_str
else:
    delimiter = ','

# if output folder was not specified then use current folder as output
if output_folder is None:      
    output_folder = os.getcwd()

# if list with urls is not specified exit program with message
if input_file is None: 
    sys.exit("Input file was not specified")

#get filename for output
file_name = os.path.basename(input_file)

#create output path
output_file = output_folder + '\\' + file_name.replace('xlsx','csv')

#import excel file
df = pd.read_excel (input_file)

#save to csv
df.to_csv(output_file, sep=delimiter, index=False)