#!/usr/bin/env python3

import sys
import traceback

import graph
import explainer

import autograder.assignment
import autograder.question
import autograder.cmd.gradeassignment

class BFS(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(
            questions = [
                TC1(1, 'loop'),
            ], **kwargs)

class TC1(autograder.question.Question):
    def score_question(self, submission):
        student_bfs = submission.__all__.BFS

        root = graph.Node("root")
        child_1 = graph.Node("child_1")
        child_2 = graph.Node("child_2")
        goal = graph.Node("goal")

        root.neighbors.append(child_1)
        child_1.neighbors.append(root)

        root.neighbors.append(child_2)
        child_2.neighbors.append(root)

        child_1.neighbors.append(goal)
        goal.neighbors.append(child_1)

        child_2.neighbors.append(goal)
        goal.neighbors.append(child_2)

        frontier = graph.Queue()
        try:
            student_path = student_bfs(root, goal, frontier)
        except NotImplementedError:
            self.fail('NotImplementedError')

        if (frontier._num_pop == 2 and student_path == ["root", "child_1", "goal"]):
            self.full_credit()
        else:
            feedback = explainer.generate_feedback(self)
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
