import cProfile
import os
import pstats

import edq.util.json
import edq.util.pyimport

GRADING_DIR = '<grading-dir>'
def profile_submission(submission_dir, assignment_obj, question_obj = None):

    if (not submission_dir.endswith(os.sep)):
       submission_dir =  submission_dir + os.sep

    question_name_to_scoring_function_dict = _create_profile_target(assignment_obj, submission_dir)

    assignment_profile_json = {}
    for question_name in question_name_to_scoring_function_dict:
        if (question_obj is not None and question_name != type(question_obj).__name__):
            continue

        question_function = question_name_to_scoring_function_dict[question_name]

        profile = cProfile.Profile()
        profile.enable()
        question_function()
        profile.disable()

        stats = pstats.Stats(profile)
        question_profile_json = {}
        for func, (_, number_of_calls, _, _, _) in stats.stats.items():
            file_path, _, func_name = func
            file_path = file_path.replace(submission_dir, GRADING_DIR + os.sep)
            question_profile_json[f'{file_path}:{func_name}'] = number_of_calls

        assignment_profile_json[question_name] = question_profile_json

    return assignment_profile_json

def _create_profile_target(assignment_class, submission_dir):
    profiler_target = {}
    num_questions = len(assignment_class()._questions)
    for i in range(num_questions):
        assignment = assignment_class(input_dir = submission_dir)
        assignment._additional_data = {"is_explain": False, "input_dir": submission_dir}
        question = assignment._questions[i]
        question._timeout = None

        assignment.questions = [question]
        profiler_target[type(assignment._questions[0]).__name__] = assignment.grade

    return profiler_target
