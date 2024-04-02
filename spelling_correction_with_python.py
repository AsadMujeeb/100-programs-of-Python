


from textblob import TextBlob

# misspelled words
blob = TextBlob("I havv a guud ideea")

# perform spelling correction
corrected_blob = blob.correct()

# print the corrected answer
print("Original Text : ", blob)
print("Corrected Text : ", corrected_blob)




































# a = 0
# b = 1
# print(a, "", b, end = " ")

# for i in range(1,7):
#     c = a + b
#     print(c, end = " ")
#     a = b 
#     b = c 



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
n_terms = 10
print("Fibonacci series:")
for i in range(n_terms):
    print(fibonacci(i))


