class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=0,0
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        for i,ele in enumerate(num1):
            n1 +=( (10**i)  * (ord(ele)- ord('0')))
        for i,ele in enumerate(num2):
            n2 +=( (10**i)  * (ord(ele)- ord('0')))
        
        return str(n1*n2)
            
  

        