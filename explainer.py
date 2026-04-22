import argparse
import os

import profiler

import edq.util.dirent
import edq.util.json

THIS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

STUDENT_PROFILE_OUTPATH = os.path.join(THIS_DIR, "student_profile.json")
SOLUTION_PROFILE_OUTPATH = os.path.join(THIS_DIR, "solution_profile.json")

QUALIFIED_GRADER_PATH = "work.grader.profile_target_without_timeout"

def profile_student_code(question_object):
    args = argparse.Namespace(
        build_question_scoring_map = QUALIFIED_GRADER_PATH,
        out_path = STUDENT_PROFILE_OUTPATH,
        question_object_to_profile = question_object

    )
    profiler.run(args)

def generate_feedback(question_object):
    profile_student_code(question_object)

    feedback = ""

    student_assignment_profile = edq.util.json.load_path(STUDENT_PROFILE_OUTPATH)
    student_question_profile = student_assignment_profile[question_object.name]

    solution_assignment_profile = edq.util.json.load_path(SOLUTION_PROFILE_OUTPATH)
    solution_question_profile = solution_assignment_profile[question_object.name]

    union_functions_called = set()
    for function in solution_question_profile:
        if ("pacai" in function):
            union_functions_called.add(function)

    for function in student_question_profile:
        if ("pacai" in function):
            union_functions_called.add(function)

    for function in union_functions_called:
        if (solution_question_profile[function] != student_question_profile[function]):
            feedback += f"{function}, #-calls-solution : {solution_question_profile[function]} vs #-calls-student : {student_question_profile[function]}\n"

    return feedback
