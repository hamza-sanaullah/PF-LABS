#Write a program that takes the range from the user and display all the prime numbers in that range and also print their sum
def prime_sum(start,end):
    sum = 0
    for i in range(start,end):
        prime = True      #assuming prime initially
        if i == 1:
            prime = False
        for j in range(2,i):
            if i % j ==0:
                prime = False     #eliminating numbers that are not prime
                break
        if prime:
            sum+=i


    print(f"The sum of prime numbers between the given range is {sum}")
start_range = int(input("Enter the starting range:\n "))
end_range = int(input("Enter the ending range:\n"))
prime_sum(start_range,end_range)






