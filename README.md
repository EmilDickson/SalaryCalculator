# SalaryCalculator
I wanted to build a tool that would calculate my salary from working at the job I had alongside my studies at this point. I had recently taken a few courses programming in Python at KTH, so this was a natural starting point for me. I simply took a table of tax deductions from the Swedish tax authority and put it into a csv file, creating a lower and higher span of gross salary for each deduction amount in the table. Then I could simply create an algorithm for this and implement it using Python. The result was a script that I could run at the command line, input the hours I had worked and get an estimate of what I would get that month.

To run, download the files main1.py and skatt.csv and then simply run the following:

```
python3 main.py
```

At the command line from that directory. All instructions within the app are in Swedish.
