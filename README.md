# CCWC - Count Characters, Words, and Lines


#output

$ python3 ccwc.py -c test.txt
  342190 test.txt

$ python3 ccwc.py -l test.txt
    7145 test.txt

$ python3 ccwc.py -w test.txt
   58164 test.txt

$ python3 ccwc.py -m test.txt
  332147 test.txt

$ python3 ccwc.py test.txt
    7145    58164   335045 test.txt

$ cat test.txt | python3 ccwc.py
    7145    58164   342190
