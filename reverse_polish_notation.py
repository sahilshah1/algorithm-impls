# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
import unittest


def eval_rpn(tokens):
    eval_stack = []

    for token in tokens:
        if token in ("+", "-", "*", "/"):
            second_operand = float(eval_stack.pop())
            first_operand = float(eval_stack.pop())

            result = 0
            if token == "+":
                result = first_operand + second_operand
            if token == "-":
                result = first_operand - second_operand
            if token == "*":
                result = first_operand * second_operand
            if token == "/":
                result = first_operand / second_operand
            eval_stack.append(int(result))
        else:
            eval_stack.append(int(token))

    return eval_stack[0]


class ReversePolishNotationTests(unittest.TestCase):

    def test_add_only(self):
        solution = eval_rpn(["2", "3", "+"])

        self.assertEquals(5, solution)

    def test_subtract_only(self):
        solution = eval_rpn(["5", "3", "-"])

        self.assertEquals(2, solution)

    def test_add_and_subtract(self):
        solution = eval_rpn(["5", "3", "2", "+", "-"])

        self.assertEquals(0, solution)

    def test_add_and_multiply(self):
        solution = eval_rpn(["2", "1", "+", "3", "*"])

        self.assertEquals(9, solution)

    def test_add_and_divide(self):
        solution = eval_rpn(["4", "13", "5", "/", "+"])

        self.assertEquals(6, solution)

    def test_failure(self):
        solution = eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        # ((10 * (6 / ((9 + 3) * -11))) + 17 + 5)

        self.assertEquals(22, solution)


if __name__ == '__main__':
    unittest.main()