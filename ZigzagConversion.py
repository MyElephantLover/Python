class Solution:
    def convert(self, s: str, numRows: str) -> str:

        # we iterate each section of the matrix and fill it with the characters from the input string

        # we iterate down in the column -> increment currRow by 1 and keep CurrCol the same
        # we iterate diagonally up -> increment currCol by 1 and decrease currRow by 1

        if numRows == 1:
            return s
        
        n = len(s)
        sections = ceil( n / (2 * numRows - 2.0)) # ceil(...) rounds it up to make sure we have enough sections to 
        # hold all characters
        # this is using the zigzag formula for the length of one zigzag cycle

        num_cols = sections * numRows - 1

        matrix = [[" "] * num_cols for _ in range(numRows)]

        curr_row, curr_col = 0, 0
        curr_string_index = 0

        # iterate in zig-zag pattern on matrix and fill it with string characters

        while curr_string_index < n:
            # move down
            while curr_row < numRows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            curr_row -= 2 # the zig-zag pattern is moving down two rows and moving up and right one column
            curr_col += 1

            # move up (with moving right also)

            while curr_row > 0 and curr_col < num_cols and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1
        answer = ""

        for row in matrix:
            answer = "".join(row)

        return answer.replace(" ", "") # returning a concatenated version of the input string
    
# Time Complexity: O(numRows * n)
# Space Complexity: O(numRows * n)




