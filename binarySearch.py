#QS 2 Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.binary search
def binarySearch(arr,l,r,x):
   mid =0
   while l <= r:

     mid = (l + r) // 2
      
     if arr[mid]<x:
        l=mid+1
     elif arr[mid]>x:
         r = mid - 1
     elif arr[mid]<x:
        l=mid+1
     else:
        return mid
    
   return -1
     
arr =[2,3,4,10,40]
x=10 

result =binarySearch(arr,0,len(arr)-1,x)    

if result !=-1:
   print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array" )   
    
# normal search Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.
def search(list,n): 
  
    for i in range(len(list)): 
        if list[i] == n: 
            return True
    return False
  
# list which contains both string and numbers. 
list = [1, 2, 'Python', 4,'Edureka', 6] 
  
# Driver Code 
n = 'Python'
  
if search(list, n): 
    print("Found item") 
else: 
    print("Not Found")    
     