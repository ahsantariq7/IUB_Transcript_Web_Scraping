from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re

html_content = """
        <div class="col-xs-12">
                    <div style="text-align: center" id="transcript">    <div>
            <div class="row">
                <div class="col-sm-8 "></div>
                <div class="col-sm-4">
                                        <a class="btn btn-primary" target="_blank" style="float: right" href="https://my.iub.edu.pk/cba/student/transcript">Download PDF</a>
<!--                    <a class="btn btn-primary" target="_blank" style="float: right" href="--><!--">Download Transcript</a>-->
                </div>
            </div>

        </div><div class="row">        <div class="col-md-6 col-xs-12">
            <div class="box">
                                <div class="box-header text-center"><b>1st Semester Fall 2020</b></div>
                <div class="box-body">
                    <div class="table-responsive">
                        <table class="table table-bordered table-striped">
                            <tbody><tr>
                                <th>Course Code</th>
                                <th>Course Title</th>
                                <th>Credit Hours</th>
                                <th>Quality Point</th>
                                <th>Grade</th>
                                <th>Remarks</th>
                                                            </tr>
                                                                <tr style="background: #dcfbda;">
                                        <td>COMP-01102L</td>
                                        <td>Computer Fundamentals Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>0</td>
                                        <td>F</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEN-01103</td>
                                        <td>Circuit Analysis</td>
                                        <td>3 (3-0)</td>
                                        <td>0</td>
                                        <td>F</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEN-01103L</td>
                                        <td>Circuit Analysis Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>0</td>
                                        <td>F</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEN-01105</td>
                                        <td>Workshop Practice</td>
                                        <td>1 (0-1)</td>
                                        <td>0</td>
                                        <td>F</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ISLA-00100</td>
                                        <td>Islamic Studies</td>
                                        <td>2 (2-0)</td>
                                        <td>0</td>
                                        <td>F</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ENGL-00104</td>
                                        <td>Functional English</td>
                                        <td>3 (3-0)</td>
                                        <td>12</td>
                                        <td>A</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01102</td>
                                        <td>Computer Fundamentals</td>
                                        <td>2 (2-0)</td>
                                        <td>0</td>
                                        <td>F</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>MATH-00101</td>
                                        <td>Calculus and Vector Algebra</td>
                                        <td>3 (3-0)</td>
                                        <td>8.1</td>
                                        <td>C</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                            <tr class="bg-olive">
                                <th></th>
                                <th></th>
                                <!--                                        <th>Total Credit Hours</th><td>--><!--</td>-->
                                <th>SGPA</th><td>1.26</td>
                                <th>CGPA</th><td>1.26</td>
                            </tr>
                        </tbody></table>
                    </div>
                </div>
            </div>
        </div>
                <div class="col-md-6 col-xs-12">
            <div class="box">
                                <div class="box-header text-center"><b>2nd Semester Spring 2021</b></div>
                <div class="box-body">
                    <div class="table-responsive">
                        <table class="table table-bordered table-striped">
                            <tbody><tr>
                                <th>Course Code</th>
                                <th>Course Title</th>
                                <th>Credit Hours</th>
                                <th>Quality Point</th>
                                <th>Grade</th>
                                <th>Remarks</th>
                                                            </tr>
                                                                <tr style="background: #dcfbda;">
                                        <td>COMP-01208L.</td>
                                        <td>Computer Programming Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>3.1</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEC-01210L</td>
                                        <td>Electronic Devices and Circuits Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>4</td>
                                        <td>A</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEC-01210</td>
                                        <td>Electronic Devices and Circuits</td>
                                        <td>3 (3-0)</td>
                                        <td>4.5</td>
                                        <td>D</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ENGL-00209</td>
                                        <td>Communication Skills</td>
                                        <td>3 (3-0)</td>
                                        <td>11.4</td>
                                        <td>B+</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01208</td>
                                        <td>Computer Programming</td>
                                        <td>3 (3-0)</td>
                                        <td>4.8</td>
                                        <td>D</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>PAKS-00207</td>
                                        <td>Pakistan Studies</td>
                                        <td>2 (2-0)</td>
                                        <td>7</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>MATH-00206</td>
                                        <td>Linear Algebra</td>
                                        <td>3 (3-0)</td>
                                        <td>8.1</td>
                                        <td>C</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                            <tr class="bg-olive">
                                <th></th>
                                <th></th>
                                <!--                                        <th>Total Credit Hours</th><td>--><!--</td>-->
                                <th>SGPA</th><td>2.68</td>
                                <th>CGPA</th><td>1.97</td>
                            </tr>
                        </tbody></table>
                    </div>
                </div>
            </div>
        </div>
        </div><div class="row">        <div class="col-md-6 col-xs-12">
            <div class="box">
                                <div class="box-header text-center"><b>3rd Semester Fall 2021</b></div>
                <div class="box-body">
                    <div class="table-responsive">
                        <table class="table table-bordered table-striped">
                            <tbody><tr>
                                <th>Course Code</th>
                                <th>Course Title</th>
                                <th>Credit Hours</th>
                                <th>Quality Point</th>
                                <th>Grade</th>
                                <th>Remarks</th>
                                                            </tr>
                                                                <tr style="background: #dcfbda;">
                                        <td>COMP-01315</td>
                                        <td>Computer Applications in Engineering</td>
                                        <td>1 (0-1)</td>
                                        <td>4</td>
                                        <td>A</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01313L</td>
                                        <td>Data Structures and Algorithms Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>3</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>MATH-00311</td>
                                        <td>Complex Variables and Transforms</td>
                                        <td>3 (3-0)</td>
                                        <td>12</td>
                                        <td>A</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEN-01312</td>
                                        <td>Digital Logic Design</td>
                                        <td>3 (3-0)</td>
                                        <td>12</td>
                                        <td>A</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEN-01312L</td>
                                        <td>Digital Logic Design Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>4</td>
                                        <td>A+</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01313</td>
                                        <td>Data Structures and Algorithms</td>
                                        <td>3 (3-0)</td>
                                        <td>6.3</td>
                                        <td>C</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>MATH-00314</td>
                                        <td>Discrete Structures</td>
                                        <td>3 (3-0)</td>
                                        <td>10.5</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                            <tr class="bg-olive">
                                <th></th>
                                <th></th>
                                <!--                                        <th>Total Credit Hours</th><td>--><!--</td>-->
                                <th>SGPA</th><td>3.45</td>
                                <th>CGPA</th><td>2.44</td>
                            </tr>
                        </tbody></table>
                    </div>
                </div>
            </div>
        </div>
                <div class="col-md-6 col-xs-12">
            <div class="box">
                                <div class="box-header text-center"><b>4th Semester Spring 2022</b></div>
                <div class="box-body">
                    <div class="table-responsive">
                        <table class="table table-bordered table-striped">
                            <tbody><tr>
                                <th>Course Code</th>
                                <th>Course Title</th>
                                <th>Credit Hours</th>
                                <th>Quality Point</th>
                                <th>Grade</th>
                                <th>Remarks</th>
                                                            </tr>
                                                                <tr style="background: #dcfbda;">
                                        <td>ELEN-01418L..</td>
                                        <td>Signals &amp; Systems Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>4</td>
                                        <td>A+</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ENGL-00419</td>
                                        <td>Technical Writing</td>
                                        <td>2 (2-0)</td>
                                        <td>7.6</td>
                                        <td>B+</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01420</td>
                                        <td>Computer Architecture and Organization</td>
                                        <td>2 (2-0)</td>
                                        <td>5.6</td>
                                        <td>C</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01420L</td>
                                        <td>Computer Architecture and Organization Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>3.7</td>
                                        <td>B+</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEN-01418</td>
                                        <td>Signals &amp; Systems</td>
                                        <td>3 (3-0)</td>
                                        <td>9.3</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01417L</td>
                                        <td>Object Oriented Programming Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>3.3</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01417</td>
                                        <td>Object Oriented Programming</td>
                                        <td>3 (3-0)</td>
                                        <td>3.6</td>
                                        <td>D</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>MATH-00416</td>
                                        <td>Differential Equations</td>
                                        <td>3 (3-0)</td>
                                        <td>10.5</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                            <tr class="bg-olive">
                                <th></th>
                                <th></th>
                                <!--                                        <th>Total Credit Hours</th><td>--><!--</td>-->
                                <th>SGPA</th><td>2.98</td>
                                <th>CGPA</th><td>2.58</td>
                            </tr>
                        </tbody></table>
                    </div>
                </div>
            </div>
        </div>
        </div><div class="row">        <div class="col-md-6 col-xs-12">
            <div class="box">
                                <div class="box-header text-center"><b>5th Semester Fall 2022</b></div>
                <div class="box-body">
                    <div class="table-responsive">
                        <table class="table table-bordered table-striped">
                            <tbody><tr>
                                <th>Course Code</th>
                                <th>Course Title</th>
                                <th>Credit Hours</th>
                                <th>Quality Point</th>
                                <th>Grade</th>
                                <th>Remarks</th>
                                                            </tr>
                                                                <tr style="background: #dcfbda;">
                                        <td>MATH-00525L</td>
                                        <td>Numerical Methods Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>3.5</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>MATH-00525</td>
                                        <td>Numerical Methods</td>
                                        <td>2 (2-0)</td>
                                        <td>6.6</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>ELEN-01521</td>
                                        <td>Probability Methods in Engg</td>
                                        <td>3 (3-0)</td>
                                        <td>9.6</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                            <tr class="bg-olive">
                                <th></th>
                                <th></th>
                                <!--                                        <th>Total Credit Hours</th><td>--><!--</td>-->
                                <th>SGPA</th><td>3.28</td>
                                <th>CGPA</th><td>2.64</td>
                            </tr>
                        </tbody></table>
                    </div>
                </div>
            </div>
        </div>
                <div class="col-md-6 col-xs-12">
            <div class="box">
                                <div class="box-header text-center"><b>6th Semester Spring 2023</b></div>
                <div class="box-body">
                    <div class="table-responsive">
                        <table class="table table-bordered table-striped">
                            <tbody><tr>
                                <th>Course Code</th>
                                <th>Course Title</th>
                                <th>Credit Hours</th>
                                <th>Quality Point</th>
                                <th>Grade</th>
                                <th>Remarks</th>
                                                            </tr>
                                                                <tr style="background: #dcfbda;">
                                        <td>COMP-01627</td>
                                        <td>Software Engineering</td>
                                        <td>3 (3-0)</td>
                                        <td>9</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-03663</td>
                                        <td>Artificial Intelligence</td>
                                        <td>3 (3-0)</td>
                                        <td>12</td>
                                        <td>A</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-03663L</td>
                                        <td>Artificial Intelligence LAB</td>
                                        <td>1 (0-1)</td>
                                        <td>4</td>
                                        <td>A</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-03673</td>
                                        <td>Data Mining</td>
                                        <td>3 (3-0)</td>
                                        <td>6.6</td>
                                        <td>C</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-03673L</td>
                                        <td>Data Mining LAB</td>
                                        <td>1 (0-1)</td>
                                        <td>3</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01628L</td>
                                        <td>Operating Systems Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>3.4</td>
                                        <td>B</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                                    <tr style="background: #dcfbda;">
                                        <td>COMP-01627L</td>
                                        <td>Software Engineering Lab</td>
                                        <td>1 (0-1)</td>
                                        <td>3.7</td>
                                        <td>B+</td>
                                        <td></td>
<!--                                        <td>--><!--</td>-->
                                    </tr>
                                                            <tr class="bg-olive">
                                <th></th>
                                <th></th>
                                <!--                                        <th>Total Credit Hours</th><td>--><!--</td>-->
                                <th>SGPA</th><td>3.21</td>
                                <th>CGPA</th><td>2.73</td>
                            </tr>
                        </tbody></table>
                    </div>
                </div>
            </div>
        </div>
            </div>
</div>
                </div>
"""
'''
# Parse the HTML content


# Extract general information
transcript_div = soup.find('div', {'id': 'transcript'})

# Extract course details
semesters = soup.find_all('div', class_='box')
for semester in semesters:
    semester_title = semester.find('div', class_='box-header').text.strip()
    print(f"\nSemester: {semester_title}")

    # Extract semester SGPA and CGPA
    sgpa_td, cgpa_td = semester.find_all('th', string=['SGPA', 'CGPA'])
    semester_sgpa = sgpa_td.find_next('td').text.strip() if sgpa_td else None
    semester_cgpa = cgpa_td.find_next('td').text.strip() if cgpa_td else None

    print(f"Semester SGPA: {semester_sgpa}")
    print(f"Semester CGPA: {semester_cgpa}")

    table = semester.find('table')
    rows = table.find_all('tr')[1:]  # Skip the header row

    for row in rows:
        columns = row.find_all('td')

        if len(columns) >= len(semesters):  # Ensure there are enough columns
            course_code = columns[0].text.strip()
            course_title = columns[1].text.strip()
            credit_hours = columns[2].text.strip()
            quality_point = columns[3].text.strip()
            grade = columns[4].text.strip()
            remarks = columns[5].text.strip()

            print(f"Course Code: {course_code}")
            print(f"Course Title: {course_title}")
            print(f"Credit Hours: {credit_hours}")
            print(f"Quality Point: {quality_point}")
            print(f"Grade: {grade}")
            print(f"Remarks: {remarks}")
            print("-" * 30)
        else:
            print("Completed")
'''

# Assuming you have already parsed the HTML content and obtained the 'soup' object
soup = BeautifulSoup(html_content, 'html.parser')
# Initialize lists for different categories
excellent_subjects = []
good_subjects = []
average_subjects = []
fail_subjects = []

# Variables to calculate weighted averages
total_credit_hours = 0
weighted_quality_points = 0
categories = ['Excellent', 'Good', 'Average', 'Fail']


# Extract course details
semesters = soup.find_all('div', class_='box')
for semester in semesters:
    semester_title = semester.find('div', class_='box-header').text.strip()
    print(f"\nSemester: {semester_title}")

    # Extract semester SGPA and CGPA
    sgpa_td, cgpa_td = semester.find_all('th', string=['SGPA', 'CGPA'])
    semester_sgpa = sgpa_td.find_next('td').text.strip() if sgpa_td else None
    semester_cgpa = cgpa_td.find_next('td').text.strip() if cgpa_td else None

    print(f"Semester SGPA: {semester_sgpa}")
    print(f"Semester CGPA: {semester_cgpa}")

    table = semester.find('table')
    rows = table.find_all('tr')[1:]  # Skip the header row

    for row in rows:
        columns = row.find_all('td')

        if len(columns) >= len(semesters):  # Ensure there are enough columns
            course_code = columns[0].text.strip()
            course_title = columns[1].text.strip()
            credit_hours_text = columns[2].text.strip()
            credit_hours_match = re.search(r'\d+', credit_hours_text)
            credit_hours = int(credit_hours_match.group()) if credit_hours_match else 0
            total_credit_hours += credit_hours
            quality_point = float(columns[3].text.strip())
            weighted_quality_points += credit_hours * quality_point
            grade = columns[4].text.strip()
            remarks = columns[5].text.strip()
            

            print(f"Course Code: {course_code}")
            print(f"Course Title: {course_title}")
            print(f"Credit Hours: {credit_hours}")
            print(f"Quality Point: {quality_point}")
            print(f"Grade: {grade}")
            print(f"Remarks: {remarks}")

            # Categorize subjects and append to respective lists
            if grade == 'A' or grade=='A+':
                excellent_subjects.append((course_code, course_title))
            elif grade == 'B' or grade=='B+' or grade == 'C' or grade=='C+':
                good_subjects.append((course_code, course_title))
            elif grade == 'D' or grade=='D+' or grade == 'E' or grade=='E+':
                average_subjects.append((course_code, course_title))
            else:
                fail_subjects.append((course_code, course_title))

            print("-" * 30)
        else:
            print("Completed")

print(credit_hours)
# Print values for debugging
print(f"Total Credit Hours: {total_credit_hours}")
print(f"Weighted Quality Points: {weighted_quality_points}")
# Target CGPA

# Calculate percentages
total_subjects = len(excellent_subjects) + len(good_subjects) + len(average_subjects) + len(fail_subjects)
excellent_percentage = (len(excellent_subjects) / total_subjects) * 100 if total_subjects > 0 else 0
good_percentage = (len(good_subjects) / total_subjects) * 100 if total_subjects > 0 else 0
average_percentage = (len(average_subjects) / total_subjects) * 100 if total_subjects > 0 else 0
fail_percentage = (len(fail_subjects) / total_subjects) * 100 if total_subjects > 0 else 0




# Print or use the separated lists and percentages as needed
print("\nExcellent Subjects:", excellent_subjects)
print("Good Subjects:", good_subjects)
print("Average Subjects:", average_subjects)
print("Fail Subjects:", fail_subjects)

print("\nPercentage of Excellent Subjects:", excellent_percentage)
print("Percentage of Good Subjects:", good_percentage)
print("Percentage of Average Subjects:", average_percentage)
print("Percentage of Fail Subjects:", fail_percentage)

categories = ['Excellent', 'Good', 'Average', 'Fail']
percentages = [excellent_percentage, good_percentage, average_percentage, fail_percentage]

# Plotting the bar graph
plt.bar(categories, percentages, color=['green', 'blue', 'yellow', 'red'])
plt.xlabel('Categories')
plt.ylabel('Percentage')
plt.title('Distribution of Subject Grades')
plt.ylim(0, 100)  # Set the y-axis range to 0-100%
plt.show()

