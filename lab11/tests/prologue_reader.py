test = {
  'name': 'Prologue - Reader',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Read-Eval-Print-Loop',
          'choices': [
            'Read-Eval-Print-Loop',
            'Really-Enormous-Purple-Llamas',
            'Read-Eval-Parse-Lex'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does REPL stand for?'
        },
        {
          'answer': 'Turns input into a useful data structure',
          'choices': [
            'Evaluates call expressions',
            'Turns input into tokens',
            'Ensures a function has been defined before it is called',
            'Turns input into a useful data structure'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the read component of the REPL loop do?'
        },
        {
          'answer': 'Input expression represented as a list of tokens',
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does the tokenize function in reader.py return?'
        },
        {
          'answer': "['add', '(', 3, ',', 4, ')']",
          'choices': [
            "['add', '(', 3, ',', 4, ')']",
            "['a', 'd', 'd', '(', '3', ',', '4', ')']",
            "['add', '(', '3', ',', '4', ')']",
            "['a', 'd', 'd', '(', 3, ',', 4, ')']"
          ],
          'hidden': False,
          'locked': False,
          'question': "What will tokenize('add(3, 4)') output?"
        },
        {
          'answer': "['(', 'lambda', ':', 4, ')', '(', ')']",
          'choices': [
            "['(', LambdaExpr, 4, ')', '(', ')']",
            "['lambda', 4, '(', ')']",
            "['(', 'lambda', ':', 4, ')', '(', ')']",
            "['(', LambdaExpr, ':', 4, ')', '(', ')']"
          ],
          'hidden': False,
          'locked': False,
          'question': "What will tokenize('(lambda: 4)()') output?"
        },
        {
          'answer': 'List of tokens and an instance of a subclass of Expr',
          'choices': [
            'List of tokens and number of parentheses',
            'Input expression and list of tokens',
            'List of tokens and an instance of a subclass of Expr',
            'Input expression and an instance of a subclass of Expr'
          ],
          'hidden': False,
          'locked': False,
          'question': r"""
          What does the read_expr function in reader.py accept as input and
          return?  (looking at the read function may help answer this question)
          """
        },
        {
          'answer': '80af8652919456caa138db792047e10b',
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What does the read function in reader.py return?'
        },
        {
          'answer': '5ebba5348fc6d0e85fd39023632defc4',
          'choices': [
            'Literal(1)',
            'Number(1)',
            "Name('1')",
            'Name(1)'
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('1') output?"
        },
        {
          'answer': 'e060f0d7986150912d102d3db300a17b',
          'choices': [
            'Literal(x)',
            'x',
            'Name(x)',
            "Name('x')"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('x') output?"
        },
        {
          'answer': '653e3db72739a557759ade3088b95b82',
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])"
          ],
          'hidden': False,
          'locked': True,
          'question': "What will read('add(3, 4)') output?"
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
