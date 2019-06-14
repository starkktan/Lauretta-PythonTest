from numpy import median
import sys
import ast

def value_predictor(x):
	if len(x) < 6:
		print("The List does not have the minimum requirement of 6 values")
	elif len(x)%2 == 1:
		print("The List does not contain an even number of values")
	else:
		print(median(x))
		
if __name__ == "__main__":
    inputList = ast.literal_eval(sys.argv[1])
    value_predictor(inputList)