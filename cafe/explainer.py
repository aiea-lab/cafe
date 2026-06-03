import argparse
import os

import cafe.profiler

import edq.util.dirent
import edq.util.json

NUM_TO_DISPLAY = 10

def generate_feedback(
        submission_dir,
        assignment_obj,
        question_object,
        path_solution_profile,
        path_student_profile = None,
        max_numer_display = NUM_TO_DISPLAY,
        ):
    if (not edq.util.dirent.exists(path_solution_profile)):
        raise ValueError("Solution profile JSON deosn't exist.")

    solution_profile_json = edq.util.json.load_path(path_solution_profile)

    if (path_student_profile is None):
        student_profile_json = cafe.profiler.profile_submission(submission_dir, assignment_obj, question_object)
    else:
        student_profile_json = edq.util.json.load_path(path_student_profile)

    feedback = ""

    question_name = question_object.__class__.__name__
    student_question_profile = student_profile_json[question_name]
    solution_question_profile = solution_profile_json[question_name]

    union_functions_called = set()
    for function in solution_question_profile:
        if (cafe.profiler.GRADING_DIR in function):
            union_functions_called.add(function)

    for function in student_question_profile:
        if (cafe.profiler.GRADING_DIR in function):
            union_functions_called.add(function)
    delta_dict = {}
    feedback += f"| {'Function':<70} | {'Expected':<10} | {'Your Code':<10} | {'Delta':<10} |\n"
    for function in union_functions_called:
        solution_call_num = solution_question_profile.get(function, 0)
        student_call_num = student_question_profile.get(function, 0)
        delta = solution_call_num - student_call_num

        if (delta != 0):
            delta_dict[function] = (solution_call_num, student_call_num, delta)

    sorted_delta_dict = sorted(delta_dict.items(), key=lambda item: abs(item[1][2]), reverse=True)

    for i in range(min(len(sorted_delta_dict), max_numer_display)):
        (key, value) = sorted_delta_dict[i]
        (solution, student, delta) = value
        feedback += f"| {key:<70} | {solution:<10} | {student:<10} | {delta:<10} |\n"

    return feedback

