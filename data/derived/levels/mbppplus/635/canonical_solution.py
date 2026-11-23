import heapq as hq
def heap_sort(iterable):
    hq.heapify(iterable)
    return [hq.heappop(iterable) for _ in range(len(iterable))]
