from tabulate import tabulate
cipher_text='''KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBK
RXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEQPKAZBKRHAIBKAPCCIBURCCDKDC
CJCIDFUIXPAFFERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVK SCPICBRKIJPKABI'''
print("Cipher Text:",cipher_text)
cleaned_cipher_txt="".join(cipher_text.split())
print("Number of alphabets in cipher text after cleaning:",len(cleaned_cipher_txt))
print("Unigram frequency count:")
freq={}
for i in cleaned_cipher_txt:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] =1
for key,value in freq.items():
    freq[key]=value/len(cleaned_cipher_txt)
sorted_freq=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
print(tabulate(
    sorted_freq.items(),
    headers=["Character", "Unigram Frequency"],
    tablefmt="grid"
))
english_prob = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127,
    'F': 0.022, 'G': 0.020, 'H': 0.061, 'I': 0.070, 'J': 0.002,
    'K': 0.008, 'L': 0.040, 'M': 0.024, 'N': 0.067, 'O': 0.075,
    'P': 0.019, 'Q': 0.001, 'R': 0.060, 'S': 0.063, 'T': 0.091,
    'U': 0.028, 'V': 0.010, 'W': 0.023, 'X': 0.001, 'Y': 0.020,
    'Z': 0.001
}
english_prob = dict(sorted(
    english_prob.items(),
    key=lambda x: x[1],
    reverse=True
))
print("Most Frequent English Character Letter:",english_prob)

def letter_num(letter):
    return ord(letter) - ord('A')

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s

def inv_mod(x):
    g, s = extended_gcd(x % 26, 26)
    if g != 1:
        return None
    return s % 26
english_letters = list(english_prob.keys())
cipher_letters = list(sorted_freq.keys())

print("\nRunning for candidate pairs:")

for i in range(5):
    x_1 = letter_num(english_letters[0])
    x_2 = letter_num(english_letters[1])

    y_1 = letter_num(cipher_letters[0])
    y_2 = letter_num(cipher_letters[i + 1])

    u = (x_1 - x_2) % 26
    v = (y_1 - y_2) % 26

    u_inv = inv_mod(u)
    a = (u_inv * v) % 26

    g, s = extended_gcd(a, 26)
    if g != 1:
        print("\nAssumption:", english_letters[0], "->", cipher_letters[0], ",",
              english_letters[1], "->", cipher_letters[i + 1])
        print("Invalid a:", a, "gcd(a, 26) =", g)
        continue

    b = (y_1 - a * x_1) % 26

    a_inv = inv_mod(a)
    plaintext = ""

    for letter in cleaned_cipher_txt:
        y = letter_num(letter)
        x = (a_inv * (y - b)) % 26
        plaintext += chr(x + ord('A'))

    print("\nAssumption:", english_letters[0], "->", cipher_letters[0], ",",
          english_letters[1], "->", cipher_letters[i + 1])
    print("a =", a, "b =", b)
    print("Plaintext:", plaintext)