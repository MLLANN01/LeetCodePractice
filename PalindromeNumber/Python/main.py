class Solution:
    def __init__(self):
        # Initialize any required variables or state here
        pass

    def solveProblem(self, input):

        if(input < 0):
            return False
        
        print(input)

        input = str(input)

        left = 0
        right = len(input) - 1

        while(left < right):

            if(input[left] != input[right]):
                return False
            
            left += 1
            right -= 1

        return True
    
    def solveProblemWithoutConvertingFromIntToString(self, input):

        if(input < 0):
            return False
        
        print(input)

        reversed_num = 0
        original_num = input

        while input != 0:
            digit = input % 10
            reversed_num = reversed_num * 10 + digit
            #Floor Division
            input //= 10

        if(reversed_num != original_num):
            return False

        return True

# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Example input for a problem
    first = 121
    second = -121
    third = 10

    # Solve the problem with the provided input
    result = solution.solveProblem(first)
    print(f"IN1: {result}")

    result = solution.solveProblem(second)
    print(f"IN2: {result}")

    result = solution.solveProblem(third)
    print(f"IN3: {result}")