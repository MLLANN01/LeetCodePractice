class Solution:
    def __init__(self):
        # Initialize any required variables or state here
        pass

    # O(n^2)
    def solveProblemBruteForce(self, nums, target):
        
        if len(nums) == 0:
            print("empty array")
            return ""

        for i, num in enumerate(nums):
            print(f"Index I: {i}, Value: {nums[i]}")

            if nums[i] > target:
                print("all numbers are bigger")
                return

            for j in range(i + 1, len(nums)):
                print(f"Index J: {j}, Value: {nums[j]}")

                if nums[i] + nums[j] == target:
                    result = [i, j]
                    return result
                
    # O(n)
    def solveProblem(self, nums, target):
        
        if not nums:  # More Pythonic way to check if list is empty
            print("empty array")
            return ""

        # Use a dictionary to map numbers to their indices
        num_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                # Found the pair that adds up to target, return their indices
                return [num_map[diff], i]
            num_map[num] = i  # Add the current number to the dictionary

        # If we reach here, no pair was found
        print("No pair found")
        return None


    @staticmethod
    def helperFunction(data):
        # Example static method that can be used as a utility function
        # Static methods don't rely on the state of the class instance
        # Implement any processing needed and return the result
        processed_data = data * 2  # Example operation
        return processed_data

# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Example input for a problem
    nums = [2, 7, 10, 11]
    target = 9

    # Solve the problem with the provided input
    result = solution.solveProblem(nums, target)

    # Print the result to the console
    print(f"Result: {result}")
