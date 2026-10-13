# affine_breaker.py
 Code tested on python==Python 3.8.6
# Instructions to run program 
 just open the terminal and run by command "python affine_breaker.py" or 
 "python3 affine_breaker.py"
# Libraries Used
    tabulate
The code uses probability table according to the frequency probabilities given by Douglas R. Stinson & Maura B. Paterson in the textbook Cryptography: Theory and Practice (4th Edition, 2019.
It uses the cryptanalysis technique where the most frequent alphabet 'e'
would be kept fixed to highest unigram frequency charachter from cipher text and candidate pairs would be test for group 2 which are(2. T, A,O, I, N, S, H, R, each having probability between 0.06 and 0.09)
