def calculate_highest_Kannada(student_list):
    highest_score_in_Kannada = 0
    highest_score_in_Kannada_Name = ''
    for student in student_list:
        if (student.get("Kannada") > highest_score_in_Kannada):
            highest_score_in_Kannada = student.get("Kannada")
            highest_score_in_Kannada_Name = student.get("Name")

    print(f"The highest marks in Kannada {highest_score_in_Kannada} is scored by {highest_score_in_Kannada_Name}.")


def calculate_lowest_Maths(student_list):
    lowest_score_in_Maths = 35
    lowest_score_in_Maths_Name = ''
    for student in student_list:
        if (student.get("Maths") <= lowest_score_in_Maths):
            lowest_score_in_Maths = student.get("Maths")
            lowest_score_in_Maths_Name = student.get("Name")

    print(f"The lowest marks in Maths {lowest_score_in_Maths} is scored by {lowest_score_in_Maths_Name}.")

def student_region(student_list):
    highest_score_in_science = 0
    region_name = ''
    student_name = ''
    for regions in student_list:
        if regions.get("Science") > highest_score_in_science:
            highest_score_in_science = regions.get("Science")
            region_name = regions.get("region")
            student_name = regions.get("Name")



    print(f"The highest marks in Science {highest_score_in_science} is scored by {student_name} in {region_name} region.  ")

student_1 = {
    "Name": "Dheeraj",
    "Maths": 87,
    "Kannada": 80,
    "Science": 50,
    "region":"Hubli"
}
student_2 = {
    "Name": "Tanmay",
    "Maths": 50,
    "Kannada": 75,
    "Science": 95,
    "region":"Bangalore"
}
student_3 = {
    "Name": "Sooraj",
    "Maths": 21,
    "Kannada": 50,
    "Science": 60,
    "region":"Mangalore"
}
student_list = [student_1, student_2, student_3]

calculate_highest_Kannada(student_list)
calculate_lowest_Maths(student_list)
student_region(student_list)