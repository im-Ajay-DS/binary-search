arr=[1,2,3,4,4,6]
x=4
l=0
h=len(arr)-1
while (l<=h):
  mid=l+(h-l)//2
  if arr[mid]==x:
    print(mid)
    break
  elif arr[mid]>x:
    h=mid-1
  else:
    l=mid+1
else:
  print(-1)
