def evaluate_expression(expression):
    context = Context()
    parser = Parser(expression)
    parsed_expression = parser.parse(context)
    result = parsed_expression.interpret(context)
    return result


def main():
    expression = build_expression_tree()
    result = evaluate_expression(expression)
    print("Result:", result)


if __name__ == '__main__':
    main()
