# This function performs binary search on a sorted list
# And also records each step so the user can understand the process.
def binary_search_steps(arr, target):
    steps = []
    low = 0
    high = len(arr) - 1

    # Continue searching while the range is valid
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        steps.append("Middle index is " + str(mid) + " with value " + str(arr[mid]) + ".")

        # Check if the middle element is the target
        if arr[mid] == target:
            steps.append("The target " + str(target) + " was found at index " + str(mid) + ".")
            return "\n".join(steps)

        # If the target is smaller, search the left half
        if target < arr[mid]:
            steps.append("The target is smaller than " + str(arr[mid]) + " so the search continues on the left side.")
            high = mid - 1

        # If the target is larger, search the right half
        else:
            steps.append("The target is larger than " + str(arr[mid]) + " so the search continues on the right side.")
            low = mid + 1

    # If the loop ends, the target was not found
    steps.append("The target " + str(target) + " was not found in the list.")
    return "\n".join(steps)


# This function takes the raw user input, and converts it into:
# Usable integers, sorts the list, and then runs binary search.
def process_user_input(list_text, target_text):
    try:
        # Convert the user's list into integers
        arr = [int(x.strip()) for x in list_text.split(",")]

        # Sort the list to make sure binary search works correctly
        arr.sort()

        # Convert the target to an integer
        target = int(target_text)

        # Run the binary search function
        return binary_search_steps(arr, target)

    except:
        # If anything goes wrong, show an error message
        return "There was an error with the input. Make sure the list contains only numbers separated by commas and that the target is a number."


# ----------------------------------------------------------
# Below is the Gradio interface code that creates the UI
# ----------------------------------------------------------

import gradio as gr

# Create the layout of the interface
with gr.Blocks() as demo:
    list_input = gr.Textbox(
        label="Enter a list of numbers separated by commas",
        placeholder="Example: 1, 4, 7, 10, 12"
    )

    target_input = gr.Textbox(
        label="Enter the target number",
        placeholder="Example: 7"
    )

    output_box = gr.Textbox(
        label="Binary Search Steps",
        lines=10
    )

    run_button = gr.Button("Run Binary Search")

    # Connect the button to the processing function
    run_button.click(
        fn=process_user_input,
        inputs=[list_input, target_input],
        outputs=output_box
    )

# Start the app
demo.launch()

