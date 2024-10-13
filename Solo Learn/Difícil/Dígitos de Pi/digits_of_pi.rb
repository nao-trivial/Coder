# Import the value of Pi from the Math module
require 'bigdecimal/math'
include BigMath

# Function to find the Nth decimal digit of Pi
def pi_digit(n)
  # Calculate Pi to a high precision (e.g., 1000 decimal places)
  pi = BigMath.PI(1000)

  # Extract the Nth decimal digit
  pi_str = pi.to_s
  decimal_digit = pi_str[n + 2].to_i  # Skip the decimal point

  decimal_digit
end

# Get input from the user
input = gets.chomp.to_i

# Validate the input
if input > 0 && input < 1000
  result = pi_digit(input)
  puts "#{result}"
else
  puts 'Invalid input. Please enter an integer between 0 and 1000.'
end
