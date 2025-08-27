print("\nChallenge 1: Letter Index Dictionary")
MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''


rows = MATRIX_STR.split('\n')
rows = [row for row in rows if row]

matrix = [list(row) for row in rows]

num_rows = len(matrix)
num_cols = len(matrix[0])

decoded_chars = []

for col in range(num_cols):
    for row in range(num_rows):
        decoded_chars.append(matrix[row][col])

raw_message = ''.join(decoded_chars)

result_chars = []
prev_was_alpha = False

i = 0
while i < len(raw_message):
    char = raw_message[i]
    if char.isalpha():
    
        result_chars.append(char)
        prev_was_alpha = True
        i += 1
    else:

        if prev_was_alpha:

            j = i
            while j < len(raw_message) and not raw_message[j].isalpha():
                j += 1
            if j < len(raw_message) and raw_message[j].isalpha():
                result_chars.append(' ')
            i = j
        else:
            i += 1
        prev_was_alpha = False

decoded_message = ''.join(result_chars)

print("Decoded Message:")
print(decoded_message)
