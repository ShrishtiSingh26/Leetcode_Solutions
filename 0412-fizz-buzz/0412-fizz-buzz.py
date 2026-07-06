class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list1=[]
        for i in range(n):
            list1.append(i+1)
        for j in range(n):
            if list1[j]%3==0 and list1[j]%5==0:
                list1[j]="FizzBuzz"
            elif list1[j]%3==0:
                list1[j]="Fizz"
            elif list1[j]%5==0:
                list1[j]="Buzz"
        
        return list(map(str,list1))