#A python script for trimming text files with long lines to 
# specific maximum linewidth

import textwrap
import codecs
'''codecs.open('your_filename_here', encoding='utf-8', mode='w+')'''

# Print an example of text wrapping on screen
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print ('\n'.join(textwrap.wrap(txt, 20, break_long_words=False)))

# Prompt the user for input filename 
filename = input("prompt")

# read input file
with codecs.open(filename, encoding='utf-8', mode='r') as f:
    lines = f.readlines()

# make wrapping function, lindewidth hardcoded here
def wrap(line):
    linewidth = 60
    if len(line) > linewidth:
        #break line into maximum allowable strings (in an array)
        broken = textwrap.wrap(line, 60, break_long_words=False)
        #join the strings from array as separated by \n = newline, and two of these after 
        # the "paragraph"=whole array
        return '\n'.join(broken) + '\n\n'
    else:
        #if line is short already use as is, expect that omit extra line change character
        line = line.replace("\r",' ')
        return line 

# call wrap function in loop for each line of input data
wrapped = [wrap(line) for line in lines]

#for line in wrapped:
#    print(line)

#write the processed outputfile
with open(filename + 'Wrap.txt', 'w') as f:
    for line in wrapped:
        f.write(line)  
    

