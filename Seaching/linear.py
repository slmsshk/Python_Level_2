print("This is Linear Search")
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['i','a','m','a','t','r','e','e']
x=input("Enter the element to search: ")
print("element found at index "+str(linearsearch(arr,x)))