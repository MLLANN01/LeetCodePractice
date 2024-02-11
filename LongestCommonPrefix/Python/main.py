class Solution:
    def __init__(self):
        # Initialize any required variables or state here
        pass

    def solveProblem(self, input):

        if len(input) == 0:
            print("empty array")
            return ""
        
        currentPrefix = input[0]

        for word in input[1:]:

            prefix = []
            charaterRange = len(currentPrefix)

            #print(f"Current Prefix: {currentPrefix}")
            #print(f"Char Range: {charaterRange}")
            #print(f"Word: {word}")
            #print(f"Length of Word: {len(word)}")

            if charaterRange > len(word):
                charaterRange = len(word)

            for j in range(charaterRange):
                
                #print(f"{currentPrefix[j]} - {word[j]}" )
                
                if currentPrefix[j] == word[j]:
                    prefix.append(word[j])

            currentPrefix = prefix

        return ''.join(currentPrefix)



# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    strs1 = ["flower","flow","flight"]
    strs2 = ["aaabcdea","aaabfredsasdfg","aaabc"]
    strs3 = ["car","can","cat"]
    strs4 = ["dog","racecar","car"]
    strs5 = ["bats","batter","barn"]

    # Solve the problem with the provided input
    result = solution.solveProblem(strs1)
    print(f"IN1: {result}")

    result = solution.solveProblem(strs2)
    print(f"IN2: {result}")

    result = solution.solveProblem(strs3)
    print(f"IN3: {result}")

    result = solution.solveProblem(strs4)
    print(f"IN4: {result}")

    result = solution.solveProblem(strs5)
    print(f"IN5: {result}")