
def check_sorted(lst):
    if lst == sorted(lst):
        return "Ascending Order"
    elif lst == sorted(lst, reverse=True):
        return "Descending Order"
    else:
        return "Unsorted"
print(check_sorted([1,2,3,4]))  
print(check_sorted([9,8,7,6]))
print("**********")
def missing(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum
print(missing([1, 2, 3, 5, 6, 7, 9, 8],9))
print("*********")
def find_missing_number(lst, n):
    for num in range(1, n+1):
        if num not in lst:
            return num
print(find_missing_number([1, 2, 3, 4, 6, 7, 9, 8],10))
print("***************")
def find_missing_number_xor(lst, n):
    xor_all = 0
    xor_list = 0
    for i in range(1, n+1):
        xor_all ^= i
    for num in lst:
        xor_list ^= num
    return xor_all ^ xor_list
lst = [1, 2, 3, 5, 6, 7, 9, 8]
n = 9
print(find_missing_number_xor(lst, n))  
print("***********")
def find_missing_number_sorting(lst):
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i + 1] != lst[i] + 1:
            return lst[i] + 1
lst = [1, 2, 3, 5, 6, 7, 9, 8]
print(find_missing_number_sorting(lst)) 
print("********************")
def sub_set(list1,list2):
    for i in list2:
        if i not in list1:
            return False
        return True
print(sub_set([1,2,3,4],[2,3,4]))  

print("**************")

def pairwithsum(arr,target):
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        current = arr[left] + arr[right]
        if current == target:
            return f"element is pair with sum {arr[left]},{arr[right]}"
        elif current < target:
            left += 1
        else:
            right -= 1
    return "not a pair"
print(pairwithsum([1,2,3,4,5,6,7,8],10))    