import pandas as pd
import numpy as np
import sys
import os

def topsis(file_path, weights, impacts, output_file):
    try:
        data = pd.read_excel(file_path)
        
        if len(data.columns) < 3:
            raise ValueError("Input data must have at least 3 columns.")
        
        fund_names = data.iloc[:, 0]
        parameters = data.iloc[:, 1:]
        
        non_numeric_columns = parameters.select_dtypes(exclude=[np.number]).columns
        if len(non_numeric_columns) > 0:
            raise ValueError(
                f"The following columns contain non-numeric values: {', '.join(non_numeric_columns)}. "
                "All criteria columns must contain numeric values only."
            )
        
        valid_impacts = {'+', '-'}
        if not all(i in valid_impacts for i in impacts):
            raise ValueError(
                "Impacts must only contain '+' or '-' separated by commas."
            )
        
        if len(weights) != parameters.shape[1] or len(impacts) != parameters.shape[1]:
            raise ValueError("Number of weights and impacts must match the number of parameters.")
        
        # Corrected impact interpretation: '+' -> 1 (maximize), '-' -> -1 (minimize)
        impacts = [1 if i == '+' else -1 for i in impacts]
        
        normalized = parameters / np.sqrt((parameters**2).sum())
        
        weighted = normalized * weights
        
        ideal_best = [weighted.iloc[:, i].max() if impacts[i] == 1 else weighted.iloc[:, i].min() for i in range(len(impacts))]
        ideal_worst = [weighted.iloc[:, i].min() if impacts[i] == 1 else weighted.iloc[:, i].max() for i in range(len(impacts))]
        
        distance_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
        distance_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))
        
        topsis_score = distance_worst / (distance_best + distance_worst)
        
        data['Topsis Score'] = topsis_score
        data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)
        
        data.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}. Example rank: {data['Rank'].iloc[0]}")

    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        print("Example: python 102203770.py 102203770-data.xlsx \"1,1,1,1,1\" \"+, -, +, -, +\" 102203770-result.csv")
        sys.exit(1)
    
    try:
        file_path = sys.argv[1]
        weights = list(map(float, sys.argv[2].split(',')))
        impacts = sys.argv[3].split(',')
        output_file = sys.argv[4]
        
        if not os.path.isfile(file_path):
            raise Exception(f"File {file_path} does not exist")
            
        topsis(file_path, weights, impacts, output_file)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
