# xlsx2csv - Excel to csv converter

### Table of contents
* [General info](#general-info)
* [Usage](#usage)

### General info
Simple script converting xlsx file to csv format with option to define custom delimiter by providing character or ascii code
	

### Usage

* Convert to csv with comma as delimiter and save in same location as input file:
  * `python xlsx2csv.py -i 'C:\path\to\excel\file.xlsx'`

* Convert to csv with comma as delimiter and save in same location as input file:
  * `python xlsx2csv.py -i 'C:\path\to\excel\file.xlsx' -o 'C:\path\to\new\location\`  

* Convert to csv with custom delimiter defined as ASCII code:
  * `python xlsx2csv.py -i 'C:\path\to\excel\file.xlsx' -d 28 -a`

* Convert to csv with custom delimiter defined as plain text:
  * `python xlsx2csv.py -i 'C:\path\to\excel\file.xlsx' -d |`
