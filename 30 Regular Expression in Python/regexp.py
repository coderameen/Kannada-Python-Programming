import re
text = "The Python is know for its simplicity and Python is amazingly good"
#search for a pattern
match =re.search("Python",text)
print(match)
if match:
    print("match found!")
    print("start index: ",match.start())
    print("end index: ",match.end())
    
else:
    print("match not found!")

text = "I have 12 apples and 3 bananas"
result = re.search(r"\d+", text)
print(result.group()) 


    
    
print("-----------Find all-------")
matches = re.findall("Python", text, re.IGNORECASE)#Case-insensitive search
print(matches)


result = re.findall(r"\d+", text)
print(result)  # Output: ['12', '3']

#----------------
new_text = re.sub("Python","Java",text)
print(new_text)

#C------
import re

text = "Call me at 98772342132 or 1234567890."
pattern = r"\d{10,}"

numbers = re.findall(pattern, text)
print(numbers)  # ['98772342132', '1234567890']

#-------------------
text = "Hello all this @#$@#%$^ is python regular expression "
text = re.sub(r'[^a-zA-Z0-9\s]','',text)
print(text)
text = "Hello! This is a string with @special# characters."
cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print(cleaned_text)

#Remove URLs from text
text2 = "This is my link http://demo.com "
text = re.sub(r'http\S+','',text2)
print(text)

#Remove HTML 
text3 = "This is my <html> code <br> for creating front end"
text = re.sub(r'<.*?>','',text3)
print(text)
