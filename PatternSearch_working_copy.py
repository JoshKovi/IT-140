import re

# This is the string we will be working with

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''


# This is a usage of ranges to find all (using re.findall()) non AlphaNumeric characters in the 
# string, saves them to results and then prints the length/ amount of those characters the
# special characters "[" and "]" indicate a set and "^" makes the program match all chars not in the set 
pattern = "[^a-zA-Z0-9]"
results = re.findall(pattern, lorem_ipsum)
print(len(results))

# This is used to find all instances of 'sit-amet' or 'sit:amet' saves them to the 
# variable occurrences_sit_amet and then print the length/number of 
# instances(again using re.findall()) and literal characters
patternSitAmet = "sit"+"[-:]" + "amet"
occurrences_sit_amet = re.findall(patternSitAmet, lorem_ipsum)
print(len(occurrences_sit_amet))

# This uses two patterns to replace ever instance of "sit-amet" and "sit:amet" with "sit amet"
# using the re.sub() function.There is no ouutput for this, the result is simply saved to replace_results
patternReplace = "sit"+"[-:]" + "amet"
replaceWith = "sit amet" 
replace_results = re.sub(patternReplace, replaceWith, lorem_ipsum)

# This once again uses re.findall() to find all instances of "sit amet", saves that list to 
# occurrences_sit_amet and then outputs the length/amount of those instances
patternSitAmet = "sit amet"
occurrences_sit_amet = re.findall(patternSitAmet, replace_results)
print(len(occurrences_sit_amet))
