class Solution:
    def reverseDegree(self, s: str) -> int:
        """
        Calculate the reverse degree of a string.
      
        For each character in the string, compute its "reverse position" in the alphabet
        (where 'a' has reverse position 26, 'b' has 25, ..., 'z' has 1)
        and multiply by its 1-indexed position in the string.
      
        Args:
            s: Input string containing lowercase letters
          
        Returns:
            The sum of (position * reverse_alphabet_position) for all characters
        """
        total_sum = 0
      
        # Iterate through the string with 1-indexed positions
        for position, char in enumerate(s, 1):
            # Calculate reverse alphabetical position
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reverse_alphabet_position = 26 - (ord(char) - ord('a'))
          
            # Add the product of position and reverse alphabet position to total
            total_sum += position * reverse_alphabet_position
          
        return total_sum
