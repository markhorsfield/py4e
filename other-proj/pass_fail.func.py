#!/usr/bin/python3

def normalize_to_100(score, out_of) :
    """
    score: numerator
    out_of: denominator
    Returns normalized score out of 100
    """

    return score*100/out_of

def pass_or_fail(score, out_of) :
    """
    score: numerator
    out_of: denominator
    Returns "pass" or "fail", depending on normalized score
    """
    if normalize_to_100(score, out_of) > 59 :
        return "pass"
    else :
        return "fail"

def grade(student_scores, out_of, f) :
    """
    student_scores: tuple of students, where each student is represented
                    by another tuple (name, score)
    out_of: integer enumerating total possible score
    f: which function to apply to the student scores
    Applies f to the student scores and prints out the information
    """

    for i in student_scores :
        print(i[0], ":", f(i[1], out_of))

scores = (("Alice", 7.5), ("Bob", 8), ("Carrie", 4.8))
# return scores
#grade(scores, 10, normalize_to_100)

# return pass or fail
grade(scores, 10, pass_or_fail)
