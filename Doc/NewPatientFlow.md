#  New paitent flow
NewPatientForm creates PatientID.json in the data directory that contains the patients name, address, DoB, email and phone number and insurance details.
TestSetSelector loads the test sets from the config directory and allows the user to select the test set to use.
Start Test creates a new TestID.json in the data directory that contains the test set name, the patient ID and the date and time the test was started.
Record Results allows the user to record the results of the test, based on the test set selected.
Save saves the results to the TestID.json file, then returns to the home screen.
Print loads the TestID.json file and the PatientID.json file and creates a report in the reports directory.

``` mermaid
---
title: New Patient Flow
---

classDiagram
    Home --> NewPatientForm : navigates to
    NewPatientForm --> Home : returns to
    NewPatientForm --> TestSetSelector : navigates to
    TestSetSelector --> StartTest : navigates to
    StartTest --> Testing : navigates to
    Testing --> RecordResults : navigates to
    RecordResults --> Save : navigates to
    Save --> Home : returns to
    RecordResults --> Print : navigates to
    Print --> Home : returns to
    class Home {
    }
    class NewPatientForm {
        +String Name
        +String Address
        +String DoB
        +String Email
        +String Phone
        +String Insurance
        +createPatientID()
    }
    class TestSetSelector {
        +loadTestSets()
        +selectTestSet()
    }
    class StartTest {
        +createTestID()
    }
    class Testing {
    }
    class RecordResults {
        +recordResults()
    }
    class Save {
        +saveResults()
    }
    class Print {
        +loadFiles()
        +createReport()
    }
```

Encapsulation: Ensure that the data in your classes is hidden from other classes and can be accessed only through methods. This will help maintain the integrity of the data.
Single Responsibility Principle: Each class should have a single responsibility. For example, the NewPatientForm class is responsible for creating a new patient ID. It should not be responsible for anything else.
Use of Inheritance and Polymorphism: If there are common methods or attributes among classes, consider using inheritance. This will help reduce code duplication and increase code reusability.
Error Handling: Implement robust error handling. For example, what happens if the createPatientID() method in the NewPatientForm class fails? Your code should be able to handle such scenarios gracefully.
Code Comments: Include comments in your code to explain what each class and method does. This will make your code easier to understand and maintain.
Naming Conventions: Follow a consistent naming convention for your classes, methods, and variables. This will make your code easier to read and understand.
Unit Testing: Consider writing unit tests for your classes and methods. This will help ensure that your code is working as expected and makes it easier to identify and fix bugs.
Data Validation: Ensure that your classes validate the data they are given. For example, the NewPatientForm class should validate that the patient's name, address, DoB, email, and phone number are in the correct format before creating a new patient ID.
Remember, these are just suggestions and best practices. The actual implementation may vary based on the specific requirements of your project.