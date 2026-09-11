from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = set(deadends)
        visited.add(0000)
        queue = collections.deque([("0000", 0)])

        def get_children(lock_number):
            children = []
            for i in range(4):
                digit = int(lock_number[i])
                turn_up = (digit+1)%10
                children.append(lock_number[:i] + str(turn_up) + lock_number[i+1:])
                turn_down = (digit-1)%10
                children.append(lock_number[:i] + str(turn_down) + lock_number[i+1:])
            return children
        
        while queue:
            current_lock, turns = queue.popleft()
            if current_lock == target:
                return turns

            for child in get_children(current_lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns+1))
        return -1

        