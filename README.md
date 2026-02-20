# AI Assignment 01 - Kids in the Yard
## Comparision Section README

### Which tool(s) did you use?
I used an LLM, Claude Code.

### If you used an LLM, what was your prompt to the LLM?
My first prompt to Claude was "Please implement the following project using the rules, style, and requirements attached below. Use simple syntax, it's a python project.". I then proceeeded to attach
a copy and paste of the implementation part of the spec. It then asked for the CSV files and I gave it that to work with.

### What differences are there between your implementation and the LLM?
Overall, I felt that Claude had some clean parts of code but was far more complicated than my implementation. I separated all of my classes into their respective files; however, the LLM put everything into one big file that was about 500 lines of code. Claude generated fancy comments that were outlined with dashes to mimic boxes. I used the pandas library to handle CSV parsing, while Claude used the built-in csv module along with nested dictionaries to parse. 
There was also a stark difference in the way I performed data retrieval. For example, I would use simple if statements to check if things were in lists or where I wanted them, while the LLM utilized the set() method. Claude also made the first two people, along with the start and end year constant variables, to deal with the special case. I had to build things around the first two people being hardcoded and uniquely generated on their own. Claude also implemented the graduate version of the project.

### What changes would you make to your implementation in general based on suggestions from the LLM?
Claude specifically used step calculations when calculating how to evenly distribute children amongst the elder_parent_year + 25 - elder_parent_year + 45. Meanwhile, I used a gap calculation that made the most sense in my head. It consisted of the (end_year - beg_year)/number of children, and I would use that as my increment on where each child was born. If I could change my implementation, I would want to explore with more concrete formulas like that so that even distribution would be more guarenteed. 

### What changes would you refuse to make?
I refuse to make the change to using the csv module instead of pandas. It was my first time trying out pandas, and I feel like the data parsing was so much more seamless. You could read everything into a dataframe with one line and convert what you needed into usable variables. For me, it made the project much more easy to complete.