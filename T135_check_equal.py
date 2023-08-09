# ECOR 1042 Group Project Milestone2 Lab1 P3 Testing check equal function 
#Ali Abdollahian 101229396
#Daniele Caruso 101220647
#Yancheng Ding 101223452
#Keegan Kilfoil 101220476
#2022-04-11
#Version 1.0

def check_equal(description: str, outcome, expected, tests_passed_failed:list) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """

    tests_passed = tests_passed_failed[0]
    tests_failed = tests_passed_failed[1]
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.

        tests_failed += 1
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        print ("Tests Passed:", tests_passed)
        print ("Tests Failed:", tests_failed)
    elif outcome != expected:
        tests_failed += 1
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        print ("Tests Passed:", tests_passed)
        print ("Tests Failed:", tests_failed)
    else:
        tests_passed += 1
        print("{0} PASSED".format(description))
    print("------")
    print ("Tests Passed:", tests_passed)
    print ("Tests Failed:", tests_failed)
    return [tests_passed, tests_failed]
    
    