#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

// A struct to store the left and right indices of a value in the array
struct Info {
  int left;
  int right;
};

// A function to get the info for each value in the array
unordered_map<int, Info> get_info(vector<int> &arr) {
  unordered_map<int, Info> info;
  unordered_map<int, int> is_exist;
  for (int i = 0; i < arr.size(); i++) {
    info[i] = {
        INT_MIN,
        INT_MAX}; // Initialize the left and right indices to -inf and +inf
    if (is_exist.count(arr[i])) { // If the value already exists in the array
      info[i].left =
          is_exist[arr[i]]; // Update the left index to the previous occurrence
      info[is_exist[arr[i]]].right =
          i; // Update the right index of the previous occurrence to the current
             // index
    }
    is_exist[arr[i]] = i; // Store the current index of the value
  }
  return info;
}

// A global variable to store the info map
unordered_map<int, Info> dic;

// A function to check if a point is unique in a range [start, end]
bool is_unique_point(int start, int end, int index) {
  if (dic[index].left < start &&
      dic[index].right >
          end) { // If both left and right indices are outside the range
    return true; // The point is unique
  } else {
    return false; // The point is not unique
  }
}

// A function to check if an array is non-boring in a range [start, end]
bool is_non_boring(int start, int end) {
  int r = start;
  int l = end;
  if (start >= end)
    return true;   // Base case: if the range has one or zero elements, it is
                   // non-boring
  while (r <= l) { // Loop from both ends of the range towards the middle
    if (is_unique_point(start, end,
                        r)) { // If r is a unique point in [start, end]
      return is_non_boring(start, r - 1) &&
             is_non_boring(r + 1, end); // Recursively check both subarrays on
                                        // its left and right sides
    }
    if (is_unique_point(start, end,
                        l)) { // If l is a unique point in [start,end]
      return is_non_boring(start, l - 1) &&
             is_non_boring(l + 1, end); // Recursively check both subarrays on
                                        // its left and right sides
    }
    r++; // Increment r
    l--; // Decrement l
  }
  return false; // If no unique point found in [start,end], it is boring
}

int main() {

  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
      cin >> arr[i];
    dic = get_info(arr);
    if (is_non_boring(0, n - 1))
      cout << "non-boring" << endl;
    else
      cout << "boring" << endl;
  }
  return 0;
}