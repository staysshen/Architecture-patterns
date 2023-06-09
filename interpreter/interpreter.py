class Expression:
    def interpret(self, context):
        pass


class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self, context):
        return self.data


class NonterminalExpression(Expression):
    def __init__(self, expression):
        self.expression = expression

    def interpret(self, context):
        return context.get_result(self.expression)


class Context:
    def __init__(self):
        self.symbol_table = {}

    def set_variable(self, variable, value):
        self.symbol_table[variable] = value

    def get_result(self, expression):
        return self.symbol_table.get(expression)


class Parser:
    def __init__(self, expression):
        self.expression = expression

    def parse(self, context):
        # Parse the expression and generate the tree structure
        # This is just a placeholder
        # You would typically implement more complex logic here
        return self.expression


def build_expression_tree():
    # Build the expression tree based on the grammar
    # This is just a placeholder
    # You would typically implement more complex logic here
    variable_a = TerminalExpression("A")
    variable_b = TerminalExpression("B")
    expression = NonterminalExpression("Add")
    expression.expression = [variable_a, variable_b]

    return expression
