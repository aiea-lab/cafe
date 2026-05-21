import argparse
import os

import profiler

import edq.util.dirent
import edq.util.json

THIS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
SUBMISSION_DIR = os.path.join(THIS_DIR, "submission")

STUDENT_PROFILE_OUTPATH = os.path.join(THIS_DIR, "student_profile.json")
SOLUTION_PROFILE_OUTPATH = os.path.join(THIS_DIR, "solution_profile.json")

QUALIFIED_GRADER_PATH = "grader.profile_target_with_timeout"

NUM_TO_DISPLAY = 10

def profile_student_code(question_object):
    args = argparse.Namespace(
        build_question_scoring_map = QUALIFIED_GRADER_PATH,
        out_path = STUDENT_PROFILE_OUTPATH,
        question_object_to_profile = question_object,
        submission = SUBMISSION_DIR

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
        if (THIS_DIR in function):
            union_functions_called.add(function)

    for function in student_question_profile:
        if (THIS_DIR in function):
            union_functions_called.add(function)

    delta_dict = {}
    feedback += f"|{'Function':<70} | {'Expected':<10} | {'Your Code':<10} | {'Delta':<10} | \n"
    for function in union_functions_called:
        clean_function_name = function.replace(THIS_DIR, "")

        solution_call_num = solution_question_profile.get(function, 0)
        student_call_num = student_question_profile.get(function, 0)
        delta = student_call_num - solution_call_num

        if (solution_call_num != student_call_num):
            delta_dict[clean_function_name] = (solution_call_num, student_call_num, delta)
    sorted_delta_dict = sorted(delta_dict.items(), key=lambda item: abs(item[1][2]), reverse=True)

    for i in range(NUM_TO_DISPLAY):
        (key, value) = sorted_delta_dict[i]
        (solution, student, delta) = value
        feedback += f"|{key:<70} | {solution:<10} | {student:<10}| {delta:<10} |\n"
    return feedback
