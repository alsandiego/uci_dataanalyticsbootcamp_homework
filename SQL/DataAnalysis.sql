--List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees e LEFT JOIN salaries s on e.emp_no = s.emp_no

--List employees who were hired in 1986.
SELECT *
FROM employees
WHERE hire_date > '01-01-1986'

--List the manager of each department with the following information:
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT dm.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name, dm.from_date, dm.to_date
FROM dept_manager dm
	LEFT JOIN departments d on dm.dept_no = d.dept_no
	LEFT JOIN employees e on dm.emp_no = e.emp_no

--List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e 
	LEFT JOIN dept_emp de on e.emp_no = de.emp_no
	LEFT JOIN departments d on de.dept_no = d.dept_no

--List all employees whose first name is "Hercules" and last names begin with "B."
SELECT *
FROM employees
WHERE first_name like 'Hercules' and last_name like 'B%'

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
	LEFT JOIN dept_emp de on e.emp_no = de.emp_no
	LEFT JOIN departments d on de.dept_no = d.dept_no
WHERE d.dept_name like 'Sales'

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees e
	LEFT JOIN dept_emp de on e.emp_no = de.emp_no
	LEFT JOIN departments d on de.dept_no = d.dept_no
WHERE d.dept_name in ('Sales', 'Development')

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(last_name) as frequency
FROM employees
GROUP BY last_name
ORDER BY frequency DESC;