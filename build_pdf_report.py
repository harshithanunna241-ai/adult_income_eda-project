from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os


# ==========================================
# 1. SET PROJECT PATHS
# ==========================================

# Get the folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Go one level up from src to the main project folder
project_folder = os.path.abspath(
    os.path.join(current_folder, "..")
)

# Reports folder
reports_folder = os.path.join(
    project_folder,
    "reports"
)

# Charts folder
charts_folder = os.path.join(
    reports_folder,
    "charts"
)

# PDF output path
output_file = os.path.join(
    reports_folder,
    "EDA_Report.pdf"
)


# ==========================================
# 2. CREATE PDF DOCUMENT
# ==========================================

doc = SimpleDocTemplate(
    output_file,
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

story = []


# ==========================================
# 3. TITLE
# ==========================================

story.append(
    Paragraph(
        "Adult Income Data Cleaning and EDA Report",
        styles["Title"]
    )
)

story.append(Spacer(1, 20))


# ==========================================
# 4. PROJECT SUMMARY
# ==========================================

story.append(
    Paragraph(
        "1. Project Summary",
        styles["Heading1"]
    )
)

story.append(
    Paragraph(
        "This project analyzes the UCI Adult Income dataset to understand "
        "which demographic, education, and work-related characteristics "
        "are associated with annual income above USD 50K.",
        styles["BodyText"]
    )
)

story.append(Spacer(1, 15))


# ==========================================
# 5. DATASET OVERVIEW
# ==========================================

story.append(
    Paragraph(
        "2. Dataset Overview",
        styles["Heading1"]
    )
)

story.append(
    Paragraph(
        "The dataset contains 48,842 census records and 14 original "
        "features with income as the target variable.",
        styles["BodyText"]
    )
)

story.append(Spacer(1, 15))


# ==========================================
# 6. DATA CLEANING
# ==========================================

story.append(
    Paragraph(
        "3. Data Cleaning",
        styles["Heading1"]
    )
)

cleaning_steps = [
    "Combined adult.data and adult.test files.",
    "Added source_split to identify train and test records.",
    "Replaced '?' values with missing values.",
    "Replaced missing workclass, occupation, and native_country with Unknown.",
    "Cleaned income labels.",
    "Created high_income.",
    "Created age_group.",
    "Created hours_group.",
    "Created net_capital.",
    "Counted duplicate records without deleting them."
]

for step in cleaning_steps:

    story.append(
        Paragraph(
            "• " + step,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 5))

story.append(Spacer(1, 10))


# ==========================================
# 7. EXPLORATORY DATA ANALYSIS
# ==========================================

story.append(
    Paragraph(
        "4. Exploratory Data Analysis",
        styles["Heading1"]
    )
)

story.append(
    Paragraph(
        "The analysis examined income distribution and relationships "
        "between income and education, occupation, age, workclass, sex, "
        "working hours, and capital-related variables.",
        styles["BodyText"]
    )
)

story.append(Spacer(1, 15))


# ==========================================
# 8. EDA CHARTS
# ==========================================

story.append(
    Paragraph(
        "5. EDA Charts",
        styles["Heading1"]
    )
)

charts = [
    ("Income Distribution", "income_distribution.png"),
    ("Income by Education", "education_income.png"),
    ("Income by Occupation", "occupation_income.png"),
    ("Income by Age Group", "age_income.png"),
    ("Income by Workclass", "workclass_income.png"),
    ("Income by Sex", "sex_income.png"),
    ("Weekly Working Hours by Income", "hours_income_boxplot.png"),
    ("Income by Working-Hour Group", "hours_income.png"),
    ("Correlation Heatmap", "correlation_heatmap.png")
]


for chart_title, chart_file in charts:

    chart_path = os.path.join(
        charts_folder,
        chart_file
    )

    # Check if chart exists
    if os.path.exists(chart_path):

        story.append(
            Paragraph(
                chart_title,
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 5))

        story.append(
            Image(
                chart_path,
                width=6 * inch,
                height=4 * inch
            )
        )

        story.append(Spacer(1, 15))

    else:

        print(
            "Chart not found:",
            chart_path
        )


# ==========================================
# 9. LIMITATIONS
# ==========================================

story.append(
    Paragraph(
        "6. Limitations",
        styles["Heading1"]
    )
)

story.append(
    Paragraph(
        "This analysis describes associations and does not establish "
        "causal relationships. The dataset is historical and contains "
        "demographic attributes. The analysis is descriptive and "
        "unweighted.",
        styles["BodyText"]
    )
)

story.append(Spacer(1, 15))


# ==========================================
# 10. CONCLUSION
# ==========================================

story.append(
    Paragraph(
        "7. Conclusion",
        styles["Heading1"]
    )
)

story.append(
    Paragraph(
        "The analysis provides an overview of the relationship between "
        "income and demographic, education, occupation, work, and "
        "capital-related variables. The cleaned dataset can now be "
        "used for the machine-learning stage of the project.",
        styles["BodyText"]
    )
)


# ==========================================
# 11. BUILD PDF
# ==========================================

doc.build(story)


# ==========================================
# 12. SUCCESS MESSAGE
# ==========================================

print()
print("====================================")
print("PDF report created successfully!")
print("====================================")
print("Saved at:")
print(output_file)
