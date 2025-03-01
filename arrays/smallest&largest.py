print("Arrays")
#working with static array
sampleData = [-4, -5, -3, -9]
requiredData = []

def SolutionA(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for i in range(len(numbers)):
        if(numbers[i] < smallest):
            smallest = numbers[i]
        if(numbers[i] > largest):
            largest = numbers[i]
    #inserting smallest number to index 0 of requiredData array
    requiredData.insert(0,smallest)
    #inserting largest number to index 1 of the requiredData array
    requiredData.insert(1,largest)
    return requiredData

#Trying out different test cases
print("Case 1 - [1,2,3,4]")
smallestAndLargest =  SolutionA([1,2,3,4])
print(f"Smallest= {smallestAndLargest[0]}\nLargest = {smallestAndLargest[1]}\n\n")
print("Case 2 - [-4, -5, -3, -9]")
smallestAndLargest =  SolutionA(sampleData)
print(f"Smallest= {smallestAndLargest[0]}\nLargest = {smallestAndLargest[1]}\n\n")
print("Case 3 - [400, 300, 600]")
smallestAndLargest =  SolutionA([400, 300, 600])
print(f"Smallest= {smallestAndLargest[0]}\nLargest = {smallestAndLargest[1]}\n\n")