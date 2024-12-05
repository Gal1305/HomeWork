numbers = [1, 5, 8, 10, 13, 4, 111, 86, 95, 0, -15, 99]

def bubble_sort (nums):
    swap = True
    while swap:
        swap = False
        for q in range(len(nums)-1):
            if nums[q] > nums[q+1]:
                nums[q], nums[q+1] = nums[q+1], nums[q]
                swap = True

bubble_sort(numbers)
print(numbers)

def selections_sort (nums):
    for q in range(len(nums)):
        lowest = q
        for w in range(q + 1, len(nums)):
            if nums[w] < nums [lowest]:
                lowest = w
        nums [q], nums [lowest] = nums[lowest], nums[q]

selections_sort(numbers)
print(numbers)