class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            
        # On stocke [timestamp, value] -> timestamp est à l'indice 0, value à l'indice 1
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        value = self.store.get(key, [])

        l, r = 0, len(value) - 1

        while l <= r:
            mid = (l + r) // 2  

            if value[mid][0] <= timestamp:
                res = value[mid][1]  
                l = mid + 1          
            else:
                r = mid - 1          

        return res