# IUB_Transcript_Web_Scraping

# Analysis of Academic Performance

## Overview

This Python script is designed to analyze academic performance data extracted from an HTML document containing semester-wise course details. The script categorizes subjects based on their grades and calculates percentages for each grade category. Additionally, it calculates the weighted averages of credit hours and quality points to determine the overall performance.

## Instructions

### Requirements

- Python 3
- BeautifulSoup (for HTML parsing)
- Matplotlib (for data visualization)

Install the required libraries using the following command:

```bash
pip install beautifulsoup4 matplotlib
```

### Usage

1. Replace `html_content` with the actual HTML content or modify the script to read the HTML from a file.

```python
html_content = '''
<!-- Your HTML content here -->
'''
```

2. Run the script.

```bash
python script_name.py
```

3. View the generated output, including details about each course, semester SGPA and CGPA, and the distribution of subjects based on grades.

## Output

### Course Details

For each course, the script prints the following information:

- Course Code
- Course Title
- Credit Hours
- Quality Point
- Grade
- Remarks

### Semester Information

For each semester, the script provides:

- Semester Title
- Semester SGPA
- Semester CGPA

### Categorization

The script categorizes subjects into the following grades:

- Excellent (A, A+)
- Good (B, B+, C, C+)
- Average (D, D+, E, E+)
- Fail (F)

### Overall Statistics

The script calculates and prints:

- Total Credit Hours
- Weighted Quality Points
- Percentages of Excellent, Good, Average, and Fail subjects

## Visualization

The script generates a bar graph illustrating the distribution of subject grades across different categories.

## Example Output



## License

This script is provided under the [MIT License](LICENSE).

Feel free to modify and adapt it according to your needs. If you find any issues or have suggestions for improvement, please open an [issue](https://github.com/your_username/your_repository/issues) on GitHub.

Happy analyzing!
