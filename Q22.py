def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i = i - 1
        else:
            nums1[k] = nums2[j]
            j = j - 1
        k = k - 1
    return nums1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    print(merge(nums1, 3, [2, 5, 6], 3))

    nums1 = [0]
    print(merge(nums1, 0, [1], 1))

    nums1 = [1]
    print(merge(nums1, 1, [], 0))

    nums1 = [4, 5, 6, 0, 0, 0]
    print(merge(nums1, 3, [1, 2, 3], 3))

    nums1 = [1, 3, 5, 0, 0]
    print(merge(nums1, 3, [2, 4], 2))


main()