class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        stack_map = []

        for bracket in s:
            print(bracket)
            # if bracket = opening bracket
            if bracket in bracket_map:
                stack_map.append(bracket)
                # print(stack_map)
            else:
                # if stack_map is empty and we get closing bracket
                # or if last bracket not paired
                #  -> return false
                if (not stack_map) or (bracket_map[stack_map[-1]] != bracket):
                    return False
                else:
                    stack_map.pop()

        # if there are unopened brackets -> return true
        if stack_map:
            return False
        else:
            return True
