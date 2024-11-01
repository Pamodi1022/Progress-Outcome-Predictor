# Progress-Outcome-Predictor
This Python project predicts students' academic progress outcomes in a university setting at the end of each academic year. Developed in compliance with university regulations, the program categorizes outcomes into four categories: Progress, Trailer, Retriever, and Exclude. Each outcome is recorded based on students' inputted course credits (Pass, Defer, Fail) and visualized in a histogram.

## Features
- User Type Selection: Allows the user to specify their role as either "student" or "staff."
- Credit Validation: Validates inputs for Pass, Defer, and Fail credits and ensures total credits equal 120.
- Outcome Calculation: Based on credit input, categorizes outcomes as Progress, Progress (module trailer), Do Not Progress (retriever), or Exclude.
- Text Output: For each outcome session, results are saved to a text file (output.txt) and displayed.
- Graphical Histogram: Uses Python's graphics library to display a histogram of outcomes with colored bars for each category.
- Looped Data Entry: Provides an option to enter multiple data sets for "staff" users.
