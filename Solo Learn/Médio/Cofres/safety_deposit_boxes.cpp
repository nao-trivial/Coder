#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

string find_item_time(const string& boxes, const string& target_item) {
    vector<string> boxes_list;
    stringstream ss(boxes);
    string item;
    
    // Split the string by commas
    while (getline(ss, item, ',')) {
        boxes_list.push_back(item);
    }
    
    int time_taken = 0;
    for (size_t i = 0; i < boxes_list.size(); i++) {
        time_taken += 5;
        if (boxes_list[i] == target_item) {
            return to_string(time_taken);
        }
    }
    
    return "Item not found in the boxes.";
}

int main() {
    string boxes;
    string target_item;
    
    getline(cin, boxes);
    getline(cin, target_item);
    
    cout << find_item_time(boxes, target_item) << endl;
    
    return 0;
}