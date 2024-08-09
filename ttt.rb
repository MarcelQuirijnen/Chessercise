
arr = [ [1,2], [2,3], [3,4], [-1,2], [2,-1], [8,0], [0,8] ]

p arr

arr.delete_if { |a| a[0] > 7 or a[0] < 0 or a[1] > 7 or a[1] < 0 }

for coord in arr do
    p coord
end