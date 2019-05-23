from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges two sorted arrays in place, doesn't returns anything. After
    the function is done, the first array will be sorted and will
    contain all elements from the second array

    :param nums1: List[int] - First array
    :param m: Integer - length of first array
    :param nums2: List[int] - Second array
    :param n: Integer - length of second array
    :return: None
    """
    i = len(nums1) - 1
    last1 = m - 1
    last2 = n - 1

    while i >= 0:
        if last1 < 0 or last2 < 0:
            break

        if nums1[last1] > nums2[last2]:
            nums1[i] = nums1[last1]
            last1 -= 1
        else:
            nums1[i] = nums2[last2]
            last2 -= 1
        i -= 1

    if last2 >= 0:
        while last2 >= 0:
            nums1[i] = nums2[last2]
            last2 -= 1
            i -= 1
