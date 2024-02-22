# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   KC, 2/19/2024, Modified script, created classes and nested methods under each class, using pass as placeholder
#   KC, 2/21/2024, Modified script, created functions
# ------------------------------------------------------------------------------------------ #
import json
import io as _io  # Needed to try closing in the finally block

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

# Processing ----------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog:
    Kelly, 2/18/24, Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This method reads the data from the specified file name

        Change Log:
        Kelly, 2/18/24, Created method
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("JSON file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data #I forgot this statement, and kept getting errors!

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This method writes the data into the specified file name

        Change Log:
        Kelly, 2/18/24, Created method
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)
        finally:
            if file.closed == False:
                file.close()

#  ----------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog:
    Kelly, 2/18/24, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the custom error messages to the user

        ChangeLog:
        Kelly, 2/19/24, Created function
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:  # if there is an error, then print these
            print("--Technical Error Message__")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        Change Log:
        Kelly, 2/19/24, Created Function
        :return: None
        """

        print(menu)
        # return menu_choice

    @staticmethod
    def input_menu_choice():
        """This function gets a menu choice from the user
        :return: string w/ the user's choice
        """

        choice = "0"  # setting initial local var
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # acceptable values in string
                raise Exception("Please only choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def input_student_info(student_data):
        """ This function gets the first name, last name, and course they are registering for

        Change Log:
        Kelly, 2/19/24, created function
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("There was an error with the value type. Please try again", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return student_data

    @staticmethod
    def output_student_info(student_data: list):
        """This function displays student's first name, last name, and the course they registered for

        Change Log:
        Kelly, 2/19/24, Created function
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

#End of class definitions


# ----------Beginning of the main body of this script----------- #

# Present and Process the data
students = FileProcessor.read_data_from_file(file_name= FILE_NAME, student_data=students)

while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_info(student_data = students)
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        IO.output_student_info(student_data = students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
