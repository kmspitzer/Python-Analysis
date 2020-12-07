#
# Kate Spitzer
# UCSD Data Science and Visualization Bootcamp
# 9 Nov 2020 Cohort
#
# Python Homework  PYPARAGRAPH
# 9 Dec 2020
#


import re



word_count = 0
char_count = 0


# set the input filename
filepath = "c:/python-challenge/PyParagraph/Resources/paragraph_input.txt"

# open input file
with open(filepath, 'r', encoding='utf-8') as text:


    # read contents into var
    paragraph = text.read()


# break paragraph into sentences
sentences = re.split("(?<=[.!?]) +", paragraph)

# loop through each sentence
for sentence in sentences:
    # break sentence into words
    words = sentence.split()

    # accumulate number of words in each sentence
    word_count += len(words)

    # loop through each word in the sentence
    for word in words:
        # accumulate numer of characters in each word
        char_count += len(word)



# calculate and print analysis to terminal
print(f"\nApproximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {len(sentences)}")
print(f"Average Letter Count: {round(char_count/word_count, 2)}")
print(f"Average Sentence Length: {round(word_count/len(sentences), 2)}\n")


# set output filename
output_file = "c:/python-challenge/PyParagraph/analysis/pyparagraph_analysis.txt"

# open the output file and write the
# analysis
with open(output_file, "w") as datafile:
    datafile.write(f"Approximate Word Count: {word_count}\n")
    datafile.write(f"Approximate Sentence Count: {len(sentences)}\n")
    datafile.write(f"Average Letter Count: {round(char_count/word_count, 2)}\n")
    datafile.write(f"Average Sentence Length: {round(word_count/len(sentences), 2)}\n")
