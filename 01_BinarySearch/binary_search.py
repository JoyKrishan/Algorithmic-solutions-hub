
class BinarySearch:

    def search_iterative(self, list, item):
        low = 0
        high = len(list) - 1

        while high >= low:
            mid = (high + low)//2
            guess = list[mid]

            if guess == item:
                return mid
            
            elif guess > item: 
                high = mid - 1
            
            else:
                low = mid + 1
      
        return None

    def search_recursive(self, list, high, low, item):

        if high < low: # base case
            return None
        
        else:
            mid = (high + low) // 2
            print(mid)
            guess = list[mid]

            if guess == item:
                return mid
            
            elif guess > item:
                return self.search_recursive(list, mid - 1, low, item)

            else:
                return self.search_recursive(list, high, mid + 1, item)

if __name__ == '__main__':

    import random 
    random.seed(42) # for reproducibility

    li = sorted([random.randint(0, 20) for _ in range(10)]) # [0, 2, 3, 3, 4, 7, 7, 8, 17, 20]
    bs = BinarySearch()
    print(bs.search_iterative(li, 17)) # => 8
    print(bs.search_recursive(li, 0, len(li) - 1, 21)) # => None
