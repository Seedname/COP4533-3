# COP 4533 Assignment 3

**Names:**  
Julian Dominguez (Seedname) - 80849534  
Alex Milanes (Alex42006) - 51506411  

## Usage

Running this program requires Python 3.14.

To run the program, use the command
```sh
python src/run.py
```  

Change the input file by updating the `file_name` variable on line `20`. Do not include the path to the file, nor the `.in` extension.  


To run the analyzer, use the command
```sh
python src/graph.py
```

This requires `matplotlib` and `tqdm`, which can be installed to your python environment with
```
pip install -r requirements.txt
```


### Input/Output

Define an input file in the `inputs/` directory. Input files must be in the format `[name].in`.  

Example input file `inputs/file1.in`:
```
3
a 2
b 4
c 5
aacb
caab
```

The first line contains the number of letters to be used in the alphabet, K.  
The next K lines contain each letter with its corresponding value, separated by a space.  
The last two lines contain the strings A and B, which are the inputs to the algorithm and must contain letters defined in the previous K lines.  

Output files contain the value of the highest value longest common subsequence on the first line, and the subsequence on the second line. For example, `outputs/file2.out`:

```
9
cb
```


## Written Component

### Question 1: Empirical Comparison

In `src/graph.py`, 20 string lengths ranging from 25 to 1925 characters, evenly spaced by 100 characters, with a constant alphabet size of 26 were analyzed for completion time with 10 samples each. The resulting plot is shown below

![Graph](data/graph.png)

This figure suggests a quadratic trend, and fitting it to a quadratic polynomial with regression yields the following curve, with an R<sup>2</sup> coefficient of approximately 1. This shows that the data is fit by a quadratic curve, which suggests that the average-case time complexity of the algorithm scales by n<sup>2</sup>.

![Desmos Graph](data/desmos-graph.png)


### Question 2: Recurrence Equation


### Question 3: Big-Oh

