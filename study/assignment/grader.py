#!/usr/bin/env python3

import sys
import traceback

import autograder.assignment
import autograder.question
import autograder.cmd.gradeassignment

import cafe.explainer
import cafe.settings

class BFS(autograder.assignment.Assignment):
    def __init__(self,  **kwargs):
        input_dir = kwargs.get('input_dir', '.')
        super().__init__(
            questions = [
                TC1(1, 'cycle', timeout=None),
            ],
            additional_data = {"input_dir": input_dir},
            **kwargs)

class TC1(autograder.question.Question):
    def score_question(self, submission, input_dir):
        student_bfs = submission.__all__.BFS
        Node = submission.__all__.Node

        root = Node("root")
        child_1 = Node("child_1")
        child_2 = Node("child_2")
        grand_child = Node("grand_child")
        goal = Node("goal")

        root.neighbors.append(child_1)
        child_1.neighbors.append(root)

        root.neighbors.append(child_2)
        child_2.neighbors.append(root)

        child_1.neighbors.append(grand_child)
        grand_child.neighbors.append(child_1)

        child_2.neighbors.append(grand_child)
        grand_child.neighbors.append(child_2)

        grand_child.neighbors.append(goal)
        goal.neighbors.append(grand_child)

        try:
            submission.__all__.Queue.nodes_explored = 0
            student_path = student_bfs(root, goal)
        except NotImplementedError:
            self.fail('NotImplementedError')

        expected_explored_count = 4
        actual_explored_count = submission.__all__.Queue.nodes_explored

        if (actual_explored_count == expected_explored_count  and student_path == ["root", "child_1", "grand_child", "goal"]):
            self.full_credit()
        else:
            feedback = f"Wrong number of nodes expanded.\nExpected: {expected_explored_count}, Actual: {actual_explored_count}\n"

            if (cafe.settings.is_generate_feedback_enabled()):
                feedback += cafe.explainer.generate_feedback(input_dir, BFS, self, "solution_profile.json")

            self.fail(feedback)

def main():
    parser = autograder.cmd.gradeassignment._get_parser()

    group = parser.add_argument_group('CAFE Options')

    group.add_argument('--enable-cafe-feedback', dest = 'enable_cafe_feedback',
        action = 'store_true', help = 'Enables CAFE to generate feedback.'
    )

    args, _ = parser.parse_known_args()

    cafe.settings.set_generate_feedback_enabled(args.enable_cafe_feedback)

    return autograder.cmd.gradeassignment.run(args)

if (__name__ == '__main__'):
    sys.exit(main())
