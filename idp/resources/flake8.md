---
title: Flake8
---

# Flake8
This is a command line <a href="https://en.wikipedia.org/wiki/Lint_(software)" target="_blank">lint</a> tool that verifies that your style meets standards.
Many people detest the pedantic verification of spaces and line lengths.
However, the tool will help assure that your code looks correct. Once you get
comfortable writing code to the standards, it'll go quickly and naturally. And, your code will be nicely readable!  


## Installation
You can install the `flake8` extension by going to the `Extensions` tab (it looks like three squares with one floating off) on the left sidebar in VS Code. Search up flake8 and click install.

By default, flake8 will show "errors" when you are in a .py file. **These are not actual errors, your code will compile without them being fixed.**

## Running in Terminal
One of the options for running flake8 - which you may consider useful - is running it through the command line in your terminal. **Note that as of now, it only appears to work in GitHub Codespaces, and NOT when you clone the repository and load it on VS Code locally.**

You must add a file called `.flake8` to your root repository. It must have the following content:
```
[flake8]
max-line-length = 110
ignore = W291,W292,W391,W504,E121,E402
```

Then, what you can do is run flake8 in your command line. You can run flake8 on a directory, or an individual .py file. For example:
```
flake8 hw3.py
```
Assuming hw3.py is in your root directory and not a sub-directory.

## Modifications
We do have some modifications, as by default, flake8 is overly harsh on your code quality. The following is **turned off in `.vscode/settings.json`**:
- Note that you should **NOT** modify this file yourself. When your code is examined, any rules you add to ignore WILL be considered.

|Codes|Descriptions|
|-----|------------|
|W291|Trailing whitespace: a line has a space at the end. Although this does assure that a coding file is super clean and professional, it is way more annoying than useful. This error is ignored|
|W292| This warning code indicates that there are no newline (blank) lines at the end of the file. This can appear to be contradictory to W391, which is also turned off.|
|W391| This warning code indicates a blank line at the end of a file. If your file has 10s of blank lines at the end, you'll get dinged. One blank line? Let's ignore it.|
|W504| This warning code indicates a line break after a binary operator. It reminds you that there should not be a line break between a binary operator (e.g., +, -, *, /) and its second operand. I figure, if it compiles and looks fine, go for it!|
|E121| This error code indicates an indentation error. It is raised when there are inconsistencies in the indentation of code blocks, such as mismatched or inconsistent indentation levels.|
|E402| This error code indicates a module-level import not at the top of the file. It reminds you that all imports should be placed at the beginning of the file before any other statements or code.|



## E501 line too long
The spirit of the rule is fabulous: your code needs to be readable and lines that are too long detract from readability.

**However**, the default 80-character line length (although not completely arbitrary) is too short for modern development
and it doesn't allow for other good conventions such as:  
* descriptive identifier names that are longer  
* concise, inline development style   
* perserving vertical real estate   

We will be customizing the maximum line length to be 110 and this length will be strictly enforced. This is done by adding the
the following configuration to `.vscode/settings.json`:  
```python
max-line-length = 110
```

### Why 80?
For those who are curious, feel free to read the following!

There are two good reasons why 80 was the chosen default length.  
1) When you print code out onto paper, the typical horizontal length of a sheet of paper would allow for 80 characters to be printed. Back in the old days, computer programmers would print code out onto paper for review.  
2) Monitors were lower resolution and typically would not allow more than 80 characters to be displayed horizontally across the screen.  

#### Old Days of Printing

Back in the old days, many printers were called <a href="https://en.wikipedia.org/wiki/Dot_matrix" target="_blank">dot matrix</a> printers where each character was comprised of an 6x7 matrix of visible dots.
The paper was <a href="https://en.wikipedia.org/wiki/Continuous_stationery" target="_blank">continuous stationary</a> : each page was linked to the prior page via perforation and had holes on the sides to allow the printer to feed the paper through.
