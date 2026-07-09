/*  
STORY  
In a magical garden, flowers bloom in patterns based on the letters they are named after. Each flower has a name that can be manipulated to produce special effects when a gardener casts a spell. The gardener needs to check if two flower names are anagrams of each other, and also needs to clean up names by removing spaces and converting them to lowercase for comparison.

YOUR TASK  
1. `is_anagram(const std::string& name1, const std::string& name2)`  
   - Input: Two strings representing flower names.  
   - Output: A boolean indicating whether the two names are anagrams.  
   - Rules:  
     - An anagram means both strings contain the same letters with the same frequency, ignoring case and spaces.  
     - Return false if either string is empty.  

2. `normalize_name(const std::string& name)`  
   - Input: A flower name string that may contain spaces and mixed case letters.  
   - Output: A cleaned version of the name with all spaces removed and all letters converted to lowercase.  
   - Rules:  
     - Return an empty string if input is empty.  

ASSERTS  
```  
assert(is_anagram("Rose", "Eros") == true);  
assert(is_anagram("Garden", "Dnareg") == true);  
assert(is_anagram("Flower", "Bloom") == false);  
assert(is_anagram("", "Rose") == false);  
assert(normalize_name("Sun Flower") == "sunflower");  
assert(normalize_name("Tulip") == "tulip");  
assert(normalize_name("") == "");  
```  

BACKGROUND  
- A string is a sequence of characters, often used to represent text. In C++, `std::string` is a class from the standard library that handles strings safely and efficiently.  
- An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. For example, "listen" and "silent" are anagrams.  
- Case sensitivity refers to how uppercase and lowercase letters are treated: "A" and "a" are different characters. To compare strings without case differences, we often convert them to the same case (e.g., all lowercase).  
- A space is a character in a string that separates words. In this challenge, spaces should be ignored when determining anagrams.  
- The `std::tolower()` function from `<cctype>` converts a character to lowercase.  
- The `std::sort()` function from `<algorithm>` arranges elements in ascending order. This can help compare if two strings contain the same letters.  

HINTS  
1. For anagram detection, consider sorting characters in both strings and comparing them.  
2. The `normalize_name` function should remove spaces and convert to lowercase.  
3. Think about what happens with empty strings — make sure they are handled properly.  
4. Use standard library functions like `std::sort`, `std::tolower`, and `std::remove_if`.  

*/