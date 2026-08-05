students_marks=[
    {"id": "S101", "name": "Amina", "marks": [75, 84, 69]},
    {"id": "S102", "name": "Bina", "marks": [55, 61, 58]},
    {"id": "S103", "name": "Chen", "marks": [91, 88, 95]},
    {"id": "S104", "name": "Dipa", "marks": [42, 49, 46]}
]
def prepare_results(students):
    results= {}
    for student in students:
        total=0
        #loop through marks
        for mark in student["marks"]:
            total +=mark
        average =total/len(student["marks"])
        #Assign grades
        if average >=80:
            grade = "A"
        elif average >=70:
            grade = "B"
        elif average >=60:
            grade= "C"
        elif average >=50:
            grade = "D"
        else:
            grade ="F"
        # Store result in dictionary
        results[student["id"]]= {
            "name": student["name"],
            "average": round(average, 2), 
            "grade": grade
        }
    return results
#call function 
final_results=prepare_results(students_marks)
#print("Studnet Results:")
for sid, info in final_results.items():
    print(f"{sid} - {info['name']}: Average = {info['average']}, Grade= {info['grade']}")
#grade frequency 
grade_frequency = {}
for info in final_results.values():
    grade = info["grade"]
    if grade in grade_frequency: 
        grade_frequency[grade] +=1
    else: 
        grade_frequency[grade] = 1
print("\nGrade frequency:")
print(grade_frequency)





