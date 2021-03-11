# matts-algorithm-for-interval-partitioning
A Python implementation of Matt's Algorithm for the Interval Partitioning Problem.

## Instructions
### How to run
- To run the program, simply run `assignment4_part2_cpsc482_isayharaposo.py`, either using the command `python` on the command line (while in the same directory as the source files), or the IDE of your choice
    - For reference, this program was written in Python 3.8.6, and requires the packages `tabulate` and `datetime`, which can be installed using Pip by running `pip install tabulate` and `pip install datetime`
    - The program will ask for the name of a desired input data file during execution unless a name is specified as an argument on the command line when running the program:
        - e.g., `python assignment4_part2_cpsc482_isayharaposo.py example1_data.txt` will run the program with the first given set of example data (see **Pseudocode and Examples**) specified
        - Note that the file extension must be specified when specifying input data file names
        - Also note that the input data files must be in the same directory as the program itself
### Pseudocode and Examples
- A document containing equivalent pseudocode can be found under the file name `assignment4_part1_cpsc482_isayharaposo.txt`
- Two sets of example data (inputs) are found under the file names:
    - `example1_data.txt`
    - `example2_data.txt`
- A document containing images of said inputs, images of the outputs corresponding to each input, and diagrammatic depictions of the outputs can be found under the file name: `assignment4_part3_cpsc482_isayharaposo.pdf`
### How to format input data
- For data input, this program accepts a single, particularly formatted text file
    - Said file must be formatted correctly, otherwise the program will either catch data formatting issue(s) and exit,
    output incorrect results, or simply crash
- The correct formatting of input data files is as follows:
    - Each lecture (time interval) must be on its own line of the input data file
    - Each time within each time interval must be 4 digits in length, where the first two digits refer to the hour *in military time (on a 24-hour clock)*, and the last two digits refer to the minutes
        - The start time and end time within each time interval should be separated by a hyphen (`-`)