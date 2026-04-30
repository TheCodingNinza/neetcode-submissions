class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [(0, -1)] * 26

        for task in tasks:
            index = ord(task) - ord("A")
            (freq, last_index) = arr[index]
            arr[index] = (freq + 1, last_index)
        arr = [(a, b) for (a, b) in arr if a != 0]
        arr = [(-a, b) for (a, b) in arr]
        heapq.heapify(arr)
        cycle_count = 0

        while arr:
            (freq, last_index) = heapq.heappop(arr)
            if last_index == -1 or (last_index + n) < cycle_count:
                freq += 1
                last_index = cycle_count
                if freq != 0:
                    heapq.heappush(arr, (freq, last_index))
            else:
                heapq.heappush(arr, (freq, last_index))
                temp = []
                while arr:
                    (freq, last_index) = heapq.heappop(arr)
                    # print(f"freq: {freq} and last_index: {last_index}")
                    # print(f"arr size: {len(arr)}")
                    if last_index == -1 or (last_index + n) < cycle_count:
                        freq += 1
                        last_index = cycle_count
                        if freq != 0:
                            heapq.heappush(arr, (freq, last_index))
                        break
                    else:
                        temp.append((freq, last_index))
                for tmp in temp:
                    heapq.heappush(arr, tmp)
            cycle_count += 1

        return cycle_count
