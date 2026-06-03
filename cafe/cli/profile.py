import argparse
import sys

import autograder.question
import cafe.profiler
import edq.util.pyimport
import edq.util.dirent

def run(args):
    assignment_obj = edq.util.pyimport.fetch(args.assignment_to_profile)

    question_obj = None
    if (args.question_to_profile is not None):
        question_obj = edq.util.pyimport.fetch(args.question_to_profile)

    profile_json = cafe.profiler.profile_submission(args.submission, assignment_obj, question_obj)

    if (args.out_path is not None):
        edq.util.json.dump_path(profile_json, args.out_path, indent = 4)
    else:
        print(edq.util.json.dumps(profile_json, indent = 4))

    return 0

def _get_parser():
    parser = argparse.ArgumentParser(
        description = 'Profile a submission against an assignment and output function call counts as JSON.'
    )

    parser.add_argument('assignment_to_profile',
        metavar = 'ASSIGNMENT_QUALIFIED_REF', action = 'store', type = str,
        help = (
            'Fully qualified reference to the assignment object to profile (e.g. module.submodule.class-name).'
        )
    )

    parser.add_argument('question_to_profile',
        metavar = 'QUESTION_QUALIFIED_REF', action = 'store',
        nargs = '?', type = str, default = None,
        help = (
            'Fully qualified reference to the question object to profile (e.g. module.submodule.class-name).'
        )
    )

    parser.add_argument('-s', '--submission',
        action = 'store', type = str, required = True,
        help = 'The path to a submission directory to use for profiling.')

    parser.add_argument('-o', '--out-path', dest = 'out_path',
        action = 'store', type = str, required = False, default = None,
        help = 'The path to output the JSON result.')

    return parser


def main():
    return run(_get_parser().parse_args())


if (__name__ == '__main__'):
    sys.exit(main())
