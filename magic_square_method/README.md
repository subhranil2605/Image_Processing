# Magic Square 

A magic square is a square array of numbers consisting of the distinct positive integers $1, 2, ..., n^2$ arranged such that the sum of the $n$ numbers in any horizontal, vertical, or main diagonal line is always the same number, known as the magic constant.


## Python 
* #### The magic-square table for n = 3 is 👇 
  
| | | |
| ------ | ------ | ------ |
| 6 | 1 | 8 |
| 7 | 5 | 3 |
| 2 | 9 | 4 |

#####  Magic constant (common sum) is: 15


* #### The magic-square table for n = 5 is 👇
||||||
|----|----|----|----|----|
| 15 |  8 |  1 | 24 | 17 |
| 16 | 14 |  7 |  5 | 23 |
| 22 | 20 | 13 |  6 |  4 |
|  3 | 21 | 19 | 12 | 10 |
|  9 |  2 | 25 | 18 | 11 |
#####  Magic constant (common sum) is: 65

* #### The magic-square table for n = 7 is 👇
||||||||
|----|----|----|----|----|----|----|
| 28 | 19 | 10 |  1 | 48 | 39 | 30 |
| 29 | 27 | 18 |  9 |  7 | 47 | 38 |
| 37 | 35 | 26 | 17 |  8 |  6 | 46 |
| 45 | 36 | 34 | 25 | 16 | 14 |  5 |
|  4 | 44 | 42 | 33 | 24 | 15 | 13 |
| 12 |  3 | 43 | 41 | 32 | 23 | 21 |
| 20 | 11 |  2 | 49 | 40 | 31 | 22 |
#####  Magic constant (common sum) is: 175

* #### The magic-square table for n = 11 is 👇
||||||||||||
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|  66 |  53 |  40 |  27 |  14 |   1 | 120 | 107 |  94 |  81 |  68 |
|  67 |  65 |  52 |  39 |  26 |  13 |  11 | 119 | 106 |  93 |  80 |
|  79 |  77 |  64 |  51 |  38 |  25 |  12 |  10 | 118 | 105 |  92 |
|  91 |  78 |  76 |  63 |  50 |  37 |  24 |  22 |   9 | 117 | 104 |
| 103 |  90 |  88 |  75 |  62 |  49 |  36 |  23 |  21 |   8 | 116 |
| 115 | 102 |  89 |  87 |  74 |  61 |  48 |  35 |  33 |  20 |   7 |
|   6 | 114 | 101 |  99 |  86 |  73 |  60 |  47 |  34 |  32 |  19 |
|  18 |   5 | 113 | 100 |  98 |  85 |  72 |  59 |  46 |  44 |  31 |
|  30 |  17 |   4 | 112 | 110 |  97 |  84 |  71 |  58 |  45 |  43 |
|  42 |  29 |  16 |   3 | 111 | 109 |  96 |  83 |  70 |  57 |  55 |
|  54 |  41 |  28 |  15 |   2 | 121 | 108 |  95 |  82 |  69 |  56 |
#####  Magic constant (common sum) is: 671

## C
Enter the value of n: 5 \
The magic-square for n = 5 is: \
15	8	1	24	17 \ 	
16	14	7	5	23 \	
22	20	13	6	4 \	
3	21	19	12	10 \	
9	2	25	18	11 \

Enter the value of n: 7 \
The magic-square for n = 7 is: \
28	19	10	1	48	39	30 \
29	27	18	9	7	47	38 \	
37	35	26	17	8	6	46 \	
45	36	34	25	16	14	5  \	
4	44	42	33	24	15	13 \
12	3	43	41	32	23	21 \	
20	11	2	49	40	31	22 \