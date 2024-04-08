class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        for _ in range(n):
            turn = 0
            for _ in range(len(students)):

                if sandwiches[0] == students[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                    break
                else:
                    students.append(students.pop(0))
                    print(students)
                    turn += 1
                    if turn >= len(students):
                        return turn
        
        return 0