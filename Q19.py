def reverse(nums, left, right):
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left = left + 1
        right = right - 1


def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    if k == 0:
        return nums
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(rotate(nums, 3))

    nums = [-1, -100, 3, 99]
    print(rotate(nums, 2))

    nums = [1, 2]
    print(rotate(nums, 5))

    nums = [1]
    print(rotate(nums, 10))

    nums = [1, 2, 3]
    print(rotate(nums, 0))


main()