import docx

import os
# os is used to change directories, get files in the directory

word_to_search = "hobbit"

path = "/Users/user/Documents/IE/docx"

all_files = os.listdir(path)

print(all_files)

doc_files = []
# we check for each file if it is a docx file or not


for file in all_files:
    if file.startswith("~$"):
        continue
    if file.endswith(".docx"):
        doc_files.append(file)

print (doc_files)

result_files = []

os.chdir(path) # we change the current directory to open files easier - always do that

for file_name in doc_files: #we open, go through each paragraph and search the keyword
    f = open(file_name, "rb") # open as a binary
    # this is how you convert an opened generic file to a docx document
    doc = docx.Document(f)
    # we iterate through each paragraph in the document
    for para in doc.paragraphs:
        # we check to see if the word to search in this paragraph
        if word_to_search.lower() in para.text.lower():
            result_files.append(file_name)
            break
    f.close()

print(result_files)
