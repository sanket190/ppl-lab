%NAME - SANKET CHAUDHARI

% courses in department

dept_course(comp_dept,dsa).
dept_course(comp_dept,ppl).
dept_course(comp_dept,dsgt).
dept_course(comp_dept,dld).
dept_course(comp_dept,fcs).
dept_course(math_dept,ode).
dept_course(math_dept,uvc).

% faculty teaches these courses

course_faculty(v.khatavkar,ppl).
course_faculty(v.kamble,dsgt).
course_faculty(p.pawar,dld).
course_faculty(s.kalamakar,dsa).
course_faculty(g.datta,la).
course_faculty(j.mathija,ode).
course_faculty(j.mathija,uvc).


% departments having students

dept_student(comp_dept,sanket).
dept_student(math_dept,akash).
dept_student(comp_dept,vivek).
dept_student(math_dept,ritik).
dept_student(comp_dept,akansha).
dept_student(math_dept,geet).
dept_student(comp_dept,rohit).
dept_student(math_dept,vipul).




% faculties in department
dept_faculty(D,F):-dept_course(Z,C),course_faculty(D,S).


% courses taken by students

student_course(S,C):-dept_student(Z,S),dept_course(Z,C).

% faculty teaches these students

faculty_student(F,S):-dept_student(Z,S),dept_course(Z,C),course_faculty(F,C).