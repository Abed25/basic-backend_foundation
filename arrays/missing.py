test1 = [3,4,6,5,1]
test2 = [12,10,13]
test3 = [1,4,6,8]
        
def findMissingNumber(numbers):
    print(f"\nGiven array:\t{numbers}")
    numbers.sort()
    print(f"Sorted array\t{numbers}")
    #Accessing each element of a sorted array with a for loop
    for i in range(len(numbers)):
        # we know x is a constant increament which should be always 1
        #x = current - previous
        x = numbers[i] - numbers[i-1]
        #for the case that x exceeds 1 means next element from theprevious is skipped
        if(x > 1):
            print(f"Skipped number = {numbers[i-1] + 1}")

print("Test cases")
findMissingNumber(test1)
findMissingNumber(test2)
findMissingNumber(test3)