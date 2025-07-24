from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = sandwiches
        que = deque(students)
        count = 0
        while que and count < len(que):

            if stack[0] == que[0]:
                stack.pop(0)
                que.popleft()
                count = 0
            else:
                temp = que.popleft()
                que.append(temp)
                count =count +1
        return (len(que))


        