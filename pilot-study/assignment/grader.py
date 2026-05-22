#!/usr/bin/env python3

import sys
import traceback

import util
import explainer

import autograder.assignment
import autograder.question
import autograder.cmd.gradeassignment

class BFS(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(
            questions = [
                TC1(1, 'cycle'),
            ],
            additional_data = {"is_explain": True},
            **kwargs)


class TC1(autograder.question.Question):
    def score_question(self, submission, is_explain):
        student_bfs = submission.__all__.BFS

        root = util.Node("root")
        child_1 = util.Node("child_1")
        child_2 = util.Node("child_2")
        grand_child = util.Node("grand_child")
        goal = util.Node("goal")

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
            util._expanded_node_count = 0
            student_path = student_bfs(root, goal)
        except NotImplementedError:
            self.fail('NotImplementedError')

        if (util._explored_node_count == 4  and student_path == ["root", "child_1", "grand_child", "goal"]):
            self.full_credit()
        else:
            feedback = ""
            if (is_explain):
                feedback += explainer.generate_feedback(self)
            self.fail(feedback)

def profile_target_with_timeout(input_dir):
    return _create_profile_target(BFS, input_dir, True)

def profile_target_without_timeout(input_dir):
    return _create_profile_target(BFS, input_dir, False)

def _create_profile_target(assignment_class, input_dir, use_timeout):
    profiler_target = {}
    num_questions = len(assignment_class()._questions)
    for i in range(num_questions):
        assignment = assignment_class(input_dir = input_dir)
        assignment._additional_data = {"is_explain": False}
        question = assignment._questions[i]

        if (not use_timeout):
            question._timeout = None

        assignment.questions = [question]
        profiler_target[assignment._questions[0].name] = assignment.grade

    return profiler_target

def main():
    return autograder.cmd.gradeassignment.main()

if (__name__ == '__main__'):
    sys.exit(main())
