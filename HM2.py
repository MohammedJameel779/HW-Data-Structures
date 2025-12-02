student_info = {
    "Name" : "Mohammed",
    "Student_Number":"779199708",
    "Major":"Information technology",
    "Level": " Tow"
}
student_info["GPA"] = 95.2
import json
print (json.dumps(student_info, ensure_ascii=False))