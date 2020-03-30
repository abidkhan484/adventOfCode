import 'dart:io';
import 'dart:core';

int requirement(List<String> numbers) {
  int total_val = 0;
  numbers.forEach((number_as_string) {
    int number = int.parse(number_as_string);
    total_val += ((number ~/ 3) - 2);
  });

  return total_val;
}


void main() {
  var input_file = new File('aoc_d1_input.txt');
  input_file.readAsLines()
  .then(requirement)
  // Callback function requirement return the total_vals (Future<int>)
  .then((total_vals) {
    print(total_vals);
  });

}
