import sys


primeNumber = int(sys.argv[-1])

def IsPrimeNumber(number):
  
    if number < 2:
        return False
        
    for i in range(int(number/2) + 1):
        if i > 1:
            if number % i == 0:
                return False
    return True
    

def IsEvenNumber(number):
    if number%2 == 0:
        return True
    return False
 
def GetOddNumbers(number):
    for i in range(int(number)):
        if IsPrimeNumber(i):
            for j in range(int(number)):
                if IsPrimeNumber(j):
                    if i+j == number:
                        return i , j
                        
                        
    raise Exception("NOT FOUND ODD NUMBERS !!!!!")

if __name__ == "__main__":
    print("-----------------------")
    print("* Goldbach Calculator *")
    print("-----------------------")
    number = int(sys.argv[-1])
    
    if IsEvenNumber(number):
        print("The Number :", number)
        odd1, odd2 = GetOddNumbers(number)
        print("First Odd :", odd1)
        print("Second Odd :", odd2)
        print(odd1, "+", odd2, "=", odd1+odd2)
        
       
    else:
        print("The number is not even")
        exit()
    
    
    