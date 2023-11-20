class Student:
 pass
class marks:
 pass
student_instance=Student()
marks_instance=marks()
is_student_instance=isinstance(student_instance,Student)
is_marks_instance=isinstance(marks_instance,marks)
is_student_subclass_object=issubclass(Student,object)
is_marks_subclass_object=isinstance(marks,object)
print(f"is student_instance an instance of Student class?{is_student_instance}")
print(f"is marks_instance an instance of marks class?{is_marks_instance}")
print(f"is Student class a subclass of the built-in 'object' class?{is_student_subclass_object}")
print(f"is marks class a subclass of the built-in 'object' class?{is_marks_subclass_object}")
