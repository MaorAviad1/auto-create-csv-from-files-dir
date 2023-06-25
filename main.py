import os
import csv

# get the current directory
dir_path = os.getcwd()

# Check if the script has been run before
if os.path.exists(os.path.join(dir_path, 'script_has_run.txt')):
    print("The script has already been run.")
    exit(0)

# list all files in the directory
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# filter out only the png files and sort them to ensure order
png_files = sorted([file for file in files if file.endswith('.png')])

# specify the txt files for each column
title_file = 'title.txt'
description_file = 'description.txt'
tags_file = 'tags.txt'
price_file = 'price.txt'

# read data from the txt files
with open(title_file, 'r') as file:
    titles = [line.strip() for line in file]
with open(description_file, 'r') as file:
    descriptions = [line.strip() for line in file]
with open(tags_file, 'r') as file:
    tags = [line.strip() for line in file]
with open(price_file, 'r') as file:
    prices = [line.strip() for line in file]

# check that all lists have the same length
if not len(png_files) == len(titles) == len(descriptions) == len(tags) == len(prices):
    print("Error: Not all files have the same number of lines.")
    exit(1)

# specify the csv file you want to write to
csv_file_path = os.path.join(dir_path, 'file_list.csv')

# write the png file names and other information into the csv file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Description", "Tags", "Price", "Image Path"])
    for i, png_file in enumerate(png_files):
        writer.writerow([titles[i], descriptions[i], tags[i], prices[i], png_file])

# Write the flag file
with open(os.path.join(dir_path, 'script_has_run.txt'), 'w') as file:
    file.write('This script has been run.')

print("Script has run successfully and the file 'script_has_run.txt' has been created to prevent it from running again.")
