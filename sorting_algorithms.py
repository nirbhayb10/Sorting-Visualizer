import time

def bubble_sort(data, drawrectangle, delay, stop_flag):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if stop_flag(): return
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])

def insertion_sort(data, drawrectangle, delay, stop_flag):
    for i in range(1, len(data)):
        if stop_flag(): return
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            if stop_flag(): return
            data[j+1] = data[j]
            j -= 1
            drawrectangle(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))])
            time.sleep(delay)
        data[j+1] = key
    drawrectangle(data, ['blue' for _ in range(len(data))])

def selection_sort(data, drawrectangle, delay, stop_flag):
    for i in range(len(data)):
        if stop_flag(): return
        min_idx = i
        for j in range(i+1, len(data)):
            if stop_flag(): return
            if data[j] < data[min_idx]:
                min_idx = j
            drawrectangle(data, ['blue' if x == j or x == min_idx else 'red' for x in range(len(data))])
            time.sleep(delay)
        data[i], data[min_idx] = data[min_idx], data[i]
    drawrectangle(data, ['blue' for _ in range(len(data))])

def merge_sort(data, drawrectangle, delay, stop_flag):
    def merge_sort_rec(arr, left, right):
        if stop_flag(): return
        if left < right:
            mid = (left + right) // 2
            merge_sort_rec(arr, left, mid)
            merge_sort_rec(arr, mid+1, right)
            merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        if stop_flag(): return
        left_part = arr[left:mid+1]
        right_part = arr[mid+1:right+1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if stop_flag(): return
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
            drawrectangle(data, ['blue' if x == k else 'red' for x in range(len(data))])
            time.sleep(delay)

        while i < len(left_part):
            if stop_flag(): return
            arr[k] = left_part[i]
            i += 1
            k += 1
            drawrectangle(data, ['blue' if x == k else 'red' for x in range(len(data))])
            time.sleep(delay)

        while j < len(right_part):
            if stop_flag(): return
            arr[k] = right_part[j]
            j += 1
            k += 1
            drawrectangle(data, ['blue' if x == k else 'red' for x in range(len(data))])
            time.sleep(delay)

    merge_sort_rec(data, 0, len(data)-1)
    drawrectangle(data, ['blue' for _ in range(len(data))])

def quick_sort(data, drawrectangle, delay, stop_flag):
    def quick_sort_rec(arr, low, high):
        if stop_flag(): return
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_rec(arr, low, pi-1)
            quick_sort_rec(arr, pi+1, high)

    def partition(arr, low, high):
        if stop_flag(): return high
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if stop_flag(): return high
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            drawrectangle(data, ['blue' if x == j or x == high else 'red' for x in range(len(data))])
            time.sleep(delay)
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    quick_sort_rec(data, 0, len(data)-1)
    drawrectangle(data, ['blue' for _ in range(len(data))])
