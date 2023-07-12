class Solution:
    # Write code below to complete prompt
     def isPalindrome(self,x):
      y=self.x.casefold().replace(' ','')
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

def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()
