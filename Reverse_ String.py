num= "Piyush"
print(num[::-1])

# Output: hsuyiP
# Explanation: The slicing method [::-1] is used to reverse the string. It starts from the end towards the first taking each character.
# Another method to reverse a string is by using the reversed() function along with the join() method.

reversed_string = ''.join(reversed(num))
print(reversed_string)

# Output: hsuyiP
# This code demonstrates two methods to reverse a string in Python.
# Method 1: Using slicing
# Method 2: Using the reversed() function and join() method 
# Both methods will give the same output.


            
