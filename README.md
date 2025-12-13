# CISC121 Final Project – Binary Search Visualization

This project is an interactive visualization of the Binary Search algorithm built using Python and the Gradio library. The user can enter a list of numbers and a target value, and the app shows each step of the binary search process in a clear and educational way.

---

## HuggingFace App
Link to the deployed application:  
**(https://huggingface.co/spaces/Kubair1/cisc121binarysearch)**

---

## Problem Breakdown & Computational Thinking

### Decomposition
Binary search can be broken into a sequence of smaller steps. The algorithm begins with a sorted list and sets two pointers called low and high. Low starts at 0 and high is set to the length of the list minus 1. During each iteration, the algorithm calculates the midpoint using the expression (low + high) // 2. It then compares the target value with the value stored at that midpoint. If the target is equal to list[mid], the search ends because the value has been found. If the target is less than list[mid], the search range is reduced by updating high to mid minus 1 so that the algorithm continues searching the left portion of the list. If the target is greater than list[mid], low is updated to mid plus 1 so that the search continues in the right portion. These steps repeat until the target is found or until low becomes greater than high, which means the target is not present in the list.

### Pattern Recognition
Binary search relies on several repeated patterns. Each step involves computing the midpoint using (low + high) // 2 and making the same three comparisons to determine whether the target is equal to, less than, or greater than the middle value. Another noticeable pattern is the consistent halving of the search space. Regardless of the values in the list, the algorithm repeatedly eliminates half of the remaining elements by adjusting either low or high. This repeated structure is what makes binary search significantly more efficient than a linear search.

### Abstraction
The program hides many of the internal details of binary search to make it easier for the user. The user does not need to understand how mid is calculated, how the search range shrinks, or why low and high change the way they do. Instead, the user simply provides a list of numbers and a target value. The program performs all midpoint calculations, comparisons, and updates internally while presenting only the essential reasoning steps in a clear and simplified explanation.

### Algorithmic Thinking
Binary search follows a clear structure based on input, processing, and output. The input is a list of integers and a target value that the user wants to locate. The processing stage applies the binary search algorithm by repeatedly calculating the midpoint using (low + high) // 2, comparing the midpoint value with the target, and updating either low or high depending on the comparison. This continues until the target is found or there are no remaining elements to search. The output is either the index where the target was found or a message explaining that the value does not appear in the list along with the reasoning used to reach that conclusion.

## Algorithm Implementation

The binary search algorithm was implemented in Python using an iterative approach.
The function maintains two pointers, low and high, and repeatedly calculates the
midpoint using (low + high) // 2. At each step, the midpoint value is compared
with the target value, and the search range is updated accordingly.

The implementation correctly terminates when the target is found or when the
search range becomes invalid (low > high). Key steps are commented in the code
to improve readability and understanding.

---

## Use of Python Libraries for UI

The user interface was built using the Gradio library. Gradio was chosen because
it provides a simple and beginner-friendly way to create interactive Python
applications. The interface includes input fields for the list of numbers and
the target value, along with an output area that displays each step of the
binary search process.

This interactive design allows users to clearly see how the algorithm updates
the low, high, and midpoint values at each iteration.


---

## How to Run the App

### Option 1 —> Use the HuggingFace App  
Simply visit the link above and run the program in your browser.

### Option 2 —> Run Locally  
1. Install dependencies:  
pip install -r requirements.txt
2. Run the app:  
python app.py

---
## Testing & Verification

To verify the correctness of the program, we tested the binary search visualization using the example shown in the previous screenshots. Using the input list 1, 4, 7, 10, 12 and target value 7, the program
- Correctly calculated the midpoint on each iteration

- Adjusted the low and high pointers properly

- Found the target value 7 at index 2

- Displayed every reasoning step in a clear and accurate sequence

The output matched the expected behavior of a properly implemented binary search, confirming that the algorithm works correctly and the interface behaves as intended.

## Screenshots

### App Interface (Before Running) 
![Interface](https://raw.githubusercontent.com/Kubairz/CISC121-project/main/screenshot1.png)

### Example Run (After Running) 
![Result](https://raw.githubusercontent.com/Kubairz/CISC121-project/main/screenshot2.png)
### App Interface (Before Running) 
![Example 2 Before](https://raw.githubusercontent.com/Kubairz/CISC121-project/main/Example%202%20Before.png)
### Example Run (After Running) 
![Example 2 After](https://raw.githubusercontent.com/Kubairz/CISC121-project/main/Example%202%20After.png)


## Conclusion
This project demonstrates how binary search can be visualized in an interactive and accessible way using Python and the Gradio library. By breaking the algorithm into clear steps and showing the reasoning behind each iteration, the application helps users understand both how binary search works and why it is efficient. The project also strengthened my skills in algorithm design, computational thinking, and building simple user interfaces in Python.

## Author
Kubair Mehta  
CISC 121 – Fall 2025  
Queen’s University


