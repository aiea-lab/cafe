#!/usr/bin/env python3

import argparse
import cProfile
import os
import pstats
import sys

import autograder.question
import edq.util.json
import pacai.util.reflection

THIS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

def run(args):
    build_question_scoring_map = pacai.util.reflection.fetch(args.build_question_scoring_map)
    question_name_to_question_fuction_dict = build_question_scoring_map()

    assignment_profile_json = {}
    for question_name in question_name_to_question_fuction_dict:

        if ((args.question_object_to_profile is not None) and (question_name != args.question_object_to_profile.name)):
            continue

        question_function = question_name_to_question_fuction_dict[question_name]

        profile = cProfile.Profile()
        profile.enable()
        question_function()
        profile.disable()

        stats = pstats.Stats(profile)

        question_profile_json = {}
        for func, (_, number_of_calls, _, _, _) in stats.stats.items():
            file_path, _, func_name = func

            clean_file_path = file_path.replace(THIS_DIR, "")
            question_profile_json[f'{clean_file_path}:{func_name}'] = number_of_calls

        assignment_profile_json[question_name] = question_profile_json


    if args.out_path is None:
        print(edq.util.json.dumps(assignment_profile_json, indent = 4))
    else:
        edq.util.json.dump_path(assignment_profile_json, args.out_path, indent = 4)

    return 0

def _get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('build_question_scoring_map',
        metavar = 'QUESTION_SCORING_MAP_FACTORY', action = 'store', type = str,
        help = (
            'Fully qualified function name (e.g. module.submodule.function) '
            'that returns a dictionary mapping question names to their '
            'corresponding scoring function.'
        )
    )

    parser.add_argument('question_object_to_profile',
        metavar = 'QUESTION_OBJECT_TO_PROFILE', action = 'store',
        nargs = '?', type = autograder.question.Question, default = None,
        help = (
            'Question (object) that will get profiled. '
            'If nothing is provided the propfiler will profile the every question in the assignment.'
        )
    )

    parser.add_argument('-o', '--out-path', dest = 'out_path',
        action = 'store', type = str, required = False, default = None,
        help = 'The path to a output the JSON result.'
    )

    return parser

def main():
    return run(_get_parser().parse_args())

if (__name__ == '__main__'):
    sys.exit(main())
