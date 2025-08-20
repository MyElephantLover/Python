class Solution:
    def validSudoku(self, board: List[List[str]]) -> bool:

        # the intuition is to create a hashset for rows, columns, and boxes

        # the formula to decide if which box the row and the column falls is
        # r / 3 * 3 + c / 3, the '/' signifies the floor devision
        # hence, we create an array of length 9 (the range is 0 to 8) with the values
        # 0 or 1 to dictate whether the value was seen or not ("seen" or "not previously seen")

        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number

                # check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + (c // 3) # the double slashes means floor division
                # meaning always rounds down to the nearest integer
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True


## Time Complexity: O(N^2) where N is the length of the board. Though N = 9 is fixed in this case
## we treat N as an arbitrary number in complexity analysis. We traverse each position
## and each of the four steps is a O(1) operation

## Space Complexity: O(N^2)

