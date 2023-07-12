
"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #1 - Paul's Palindrome Password (palindrome.py)


Author: Chris Lai

Difficulty Level: 1/10

Prompt: Paul has a brand new autonomous driving RACECAR that requires a password input 
before unlocking and allowing the user to drive. Since Paul can never remember his exact 
password, he set the following rule for a valid password: “If the password given to the 
RACECAR is more than 6 letters long and is a palindrome, unlock the car”. Write a Python
script that it returns “True” if the given password unlocks the car (is more than 6 
characters long and is a palindrome) and returns “False” if the given password is invalid.

Extra Challenge: Solve this problem in 1 line of code! (Excluding function definitions) 

Test Cases:
Input: “racecar”    Output: True
Input: “314156”     Output: False
Input: “dad”        Output: False
"""

class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
            #type s: string
            #return type: boolean
            
            #TODO: Write code below to return a boolean value with the solution to the prompt.
            pass

def main():
    tc1 = Solution()
    inpyt = input()
    def isPalindrome(x):
      y=x.casefold().replace(' ','')
      ylen=len(y)
      palindrome=True
      if len(y)<=6:
        palindrome=False
      if len(y)%2!=0:
        z=y[0:int((len(y)-1)/2)]
        z+=y[int((len(y)-1)/2)+1:ylen]
        y=z
      while len(y)!=0:
        if y[0]!=y[len(y)-1]:
          palindrome=False
        y=y[1:len(y)-1]
      return(palindrome)
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()
palindrome.py
