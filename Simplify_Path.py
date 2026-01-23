# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

# Constraints:

# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

class Solution:
    def simplifiedPath(self, path: str) -> str:
        stack = []

        # for ch in path:
        #     check = stack.top()
        for part in path.split('/'):
            if part == '' or part == '.': # '.' means the current directory, we do nothing
                continue
            elif part == '..': # parent 
                if stack: # an non-empty list is True - does the stack have at least one directory in it?
                    # the same as if len(stack) > 0
                    stack.pop()
                    # '..' requires going to the parent directory -> remove the last directory
                    # so we check if there's something to remove in stack
            else:
                # this means this token is not:
                # 1) empty ""
                # 2) current directory '.'
                # 3) parent directory '..'
                stack.append(part)
                    # the stack means the root directory to where I am now
                    # so when we move forward to a folder, we add it to the path
        return '/' + '/'.join(stack)
    
# example path: /usr/local/bin
# stack = ['user', 'local', 'bin']
# the question stated that any sequence of periods not match '.' or '..' are valid directory
# so we store them. e.g. '/a..b/', '/.../'
    
## Time Complexity: O(n) path scan once
## Space Complexity: O(n)


            