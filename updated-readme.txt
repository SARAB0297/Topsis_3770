# TOPSIS Python Package

A Python package that implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. This package helps in solving Multi-Criteria Decision Making (MCDM) problems by ranking alternatives based on multiple criteria.

## Package Link
[PyPI Package Link](https://pypi.org/project/topsis-3770/1.0.0/)

## Installation

```bash
pip install topsis-yourname
```

## Usage

The package can be used both as a command-line tool and as a Python module.

### Command Line Usage

```bash
python -m topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

Example:
```bash
python -m topsis data.xlsx "1,1,1,1,1" "+,-,+,-,+" result.csv
```

### Input File Format

- Excel file with .xlsx extension
- First column: Fund/Alternative names
- 2+ columns: Numerical values for criteria
- Example:
  ```
  Fund Name | Return | Risk | Expense | ...
  Fund A    | 10     | 20   | 30     | ...
  Fund B    | 15     | 25   | 35     | ...
  ```

### Parameters

- Weights: Comma-separated values of weights (e.g., "1,1,1,1,1")
- Impacts: Comma-separated +/- signs for maximizing/minimizing criteria (e.g., "+,-,+,-,+")
- ResultFileName: Output CSV file name

### Output

The program will create a CSV file containing the input data along with:
- Topsis Score
- Rank

## Sample Python Usage

```python
from topsis import topsis

topsis("input.xlsx", [1,1,1,1,1], ['+','-','+','-','+'], "output.csv")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Sarabjeet Singh (ssingh20_be22@thapar.edu)
