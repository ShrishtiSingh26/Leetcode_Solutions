# Last updated: 7/6/2026, 10:55:13 AM
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        list1=[]
4        for i in range(n):
5            list1.append(i+1)
6        for j in range(n):
7            if list1[j]%3==0 and list1[j]%5==0:
8                list1[j]="FizzBuzz"
9            elif list1[j]%3==0:
10                list1[j]="Fizz"
11            elif list1[j]%5==0:
12                list1[j]="Buzz"
13        
14        return list(map(str,list1))