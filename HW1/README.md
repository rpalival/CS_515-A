>**Raj Palival** rpalival@stevens.edu

* What is the difference between print and return in Python? Answer in just a sentence or two. You can use an example if you like.  
    A) Print statement returns a final output to the console and it's job is done, but return returns an output from an excecution which can be further used in the code.
* Are there any known bugs or issues with your program? Even if the answer is no, please include this question and just say 'no'.  
    A) No bugs or issues.
* Describe an issue that you encountered and resolved when writing and testing your code. It doesn't have to be complex, but it should be something that didn't work the first time. Tell us a about it---what were you trying to do, what went wrong, and how did you fix it?  
    A) When computing salary in pay.py program, I wanted to round the floating point number to the nearest digit for unfair company system. Using the round() function of python on 3.5 and above such as 3.67 was rounding the float to 4 but according the problem description it should round off to the lowest nearest integer which in this case was 3. Hence to fix this issue, I imported math library and used math.floor which rounds of my float to the int value of one's place.
