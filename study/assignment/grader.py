#!/usr/bin/env python3

import sys
import traceback

import autograder.assignment
import autograder.question
import autograder.cmd.gradeassignment

import cafe.explainer

class BFS(autograder.assignment.Assignment):
    def __init__(self,  **kwargs):
        input_dir = kwargs.get('input_dir', '.')
        super().__init__(
            questions = [
                TC1(1, 'cycle'),
            ],
            additional_data = {"is_explain": True, "input_dir": input_dir},
            **kwargs)

class TC1(autograder.question.Question):
    def score_question(self, submission, is_explain, input_dir):
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

        if (submission.__all__.Queue.nodes_explored == 4  and student_path == ["root", "child_1", "grand_child", "goal"]):
            self.full_credit()
        else:
            feedback = ""
            if (is_explain):
                feedback += cafe.explainer.generate_feedback(input_dir, BFS, self, "solution_profile.json")
            self.fail(feedback)

def main():
    return autograder.cmd.gradeassignment.main()

if (__name__ == '__main__'):
    sys.exit(main())
