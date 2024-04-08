class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        for _ in range(len(sandwiches)):
            turn = 0
            for _ in range(len(students)):
                if sandwiches[0] == students[0]:
                    sandwiches.popleft()
                    students.popleft()
                    break
                else:
                    students.append(students.popleft())
                    turn += 1
                    if turn >= len(students):
                        return turn

        return 0
