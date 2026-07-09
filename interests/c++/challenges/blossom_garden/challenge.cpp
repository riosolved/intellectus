/*  
STORY  
In a small garden, a gardener is planting flowers in rows. Each row contains a different number of flowers, and the gardener wants to calculate how many flowers are in each row and the total number planted. The gardener has recorded the number of flowers per row in a vector, but sometimes makes mistakes when counting. If any row has zero or negative flowers, it's an error and must be rejected.

YOUR TASK  
1. `count_flowers_in_row` - Takes a vector of integers representing flower counts per row, and returns the sum of all valid rows (positive numbers only). Invalid rows (zero or negative) are skipped.  
2. `get_total_flowers` - Takes a vector of integers representing flower counts per row, and returns the total number of flowers across all rows, but throws an exception if there are more than 10 rows.

ASSERTS  
```cpp
#include <cassert>
#include <vector>
#include <stdexcept>

std::vector<int> test_data_1 = {5, 3, -1, 7, 2};
assert(count_flowers_in_row(test_data_1) == 17);

std::vector<int> test_data_2 = {0, -3, 4, 6};
assert(count_flowers_in_row(test_data_2) == 10);

std::vector<int> test_data_3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
try {
    get_total_flowers(test_data_3);
    assert(false); // Should not reach here
} catch (const std::exception&) {
    // Expected to throw
}

std::vector<int> test_data_4 = {10, 20, 30};
assert(get_total_flowers(test_data_4) == 60);

std::vector<int> test_data_5 = {};
assert(count_flowers_in_row(test_data_5) == 0);
```

BACKGROUND  
A vector in C++ is a dynamic array that can grow or shrink during runtime. It's part of the standard library and allows you to store elements of any type. You access elements using an index starting from 0, like `vec[0]`. Iteration means going through each element one by one.

To iterate over a vector in C++, you can use a for loop or a range-based for loop (`for (const auto& item : vec)`). In this challenge, you'll be using the latter because it's cleaner and safer.

The task requires checking whether the number of rows is valid. A row with zero or fewer flowers is invalid, so you must skip those when calculating the total. The `get_total_flowers` function also has a hard limit: there can’t be more than 10 rows. If that’s exceeded, it should throw an exception.

C++ exceptions are used to signal errors in code. You can use `throw std::runtime_error("message")` to raise an error with a descriptive message. This helps your program respond gracefully when something goes wrong instead of crashing.

HINTS  
1. Use a range-based for loop to iterate over the vector elements.  
2. Keep track of valid rows (positive values) in `count_flowers_in_row`.  
3. In `get_total_flowers`, check if the size exceeds 10 before calculating the sum.  
4. When throwing an exception, make sure you're using `std::runtime_error` from `<stdexcept>`.  
*/