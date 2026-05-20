class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        
        for car in pos_speed:
            time_taken = (target - car[0])/car[1]
            stack.append(time_taken)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
  
        return len(stack)