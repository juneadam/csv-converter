# CSV to JSON converter

## Purpose

This program is designed to convert a CSV file into a JSON object. In this first iteration, it is designed for use with the bird-app (URL TO BIRDDEX REPOSITORY) to parse a CSV full of data that our React app uses to populate the entries for each bird. 

This version of the program reads the top row as keys for each object, and uses the following rows to fill in values.

The underlying logic is handled using functional logic with Python and Flask.

## Intent for Future Functionality

Future versions will play with reading CSV files with more diverse data setups - i.e., reading columns as key:value pairs, reading column 1 as keys and row 1 as data sets (i.e., naming each item with in the JSON object by date per the top row, and using the first column as keys for each item).