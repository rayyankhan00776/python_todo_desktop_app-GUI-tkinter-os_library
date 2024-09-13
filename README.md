This program is a simple Task Manager implemented in Python that allows users to manage their tasks through a text-based menu. Users can add, remove, update, and display tasks interactively. Below is a breakdown of the functionality:

Features:
Add Task:

Allows users to input a task they want to add to their to-do list.
The task is appended to the tasks list, and a confirmation message is printed.
Remove Task:

Prompts the user to enter the task they wish to remove.
The program checks if the task exists in the list, removes it, and confirms the removal.
If the task is not found, it notifies the user.
Update Task:

Enables the user to modify an existing task.
The program asks for the task to update and the new task name, replacing the old one if it exists in the list.
Display Tasks:

Prints all tasks in the list in a numbered format.
If no tasks are present, it informs the user that the list is empty.
Exit Program:

Allows the user to exit the program by selecting option 5.
Main Menu:
The user is presented with a main menu that displays the available options.
The menu runs in an infinite loop until the user chooses to exit by selecting option 5.
For each valid input, the corresponding task-related function is executed.
User Flow:
Users interact with the program by selecting options from the main menu.
Input validation ensures only valid choices are accepted (between 1 and 5), while invalid inputs prompt the user to try again.
Example Workflow:
The user adds a task like "Complete homework."
They can then display the list to see tasks.
If needed, they can update "Complete homework" to "Complete math homework."
They can remove any task when it's completed.
Finally, they exit the program.
This program is an ideal starting point for learning basic list manipulations and user interaction in Python. It could be extended with more advanced features, such as saving tasks to a file or sorting by priority.
