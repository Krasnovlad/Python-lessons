grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_sum = [sum(grades[0]), sum(grades[1]), sum(grades[2]),sum(grades[3]), sum(grades[4])]
grades_count = [len(grades[0]), len(grades[1]), len(grades[2]),len(grades[3]), len(grades[4])]
average_score = [grades_sum[0]/grades_count[0], grades_sum[1]/grades_count[1], grades_sum[2]/grades_count[2], grades_sum[3]/grades_count[3], grades_sum[4]/grades_count[4]]
sorted_student = sorted(students)
average_score_dict = dict(zip(sorted_student, average_score))
print(average_score_dict)