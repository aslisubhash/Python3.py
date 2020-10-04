def binary_search(l,item):
     first=0
     last=len(l)-1

     while first<=last:
         mid = (first+last)//2
         if l[mid]== item:
             return mid
         else:
             if l[mid]>item:
                 last = mid-1
             else:
                 first=mid+1
     return "nai mila"
l=[1,2,4,5,6,7]
print(binary_search(l,4))
