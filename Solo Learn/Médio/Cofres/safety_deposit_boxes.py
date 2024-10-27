def find_item_time(boxes, target_item):
    boxes_list = boxes.split(',')
    time_taken = 0
    for index, item in enumerate(boxes_list):
        time_taken += 5
        if item == target_item:
            return time_taken
    return "Item not found in the boxes."

# Test the function with sample input
boxes = input().strip()
target_item = input().strip()
print(find_item_time(boxes, target_item))
