from pytest_bdd import scenario, given, when, then

from main import gen_random


@scenario("C:/Users/1/PycharmProjects/BKIT5/gen_random.feature",'New array will contain random numbers from users interval')
def testing_gen_random():
    pass

@given('Having numbers 20, 2, 4',target_fixture='parameters')
def parameters():
    return 20,2,4

@when('Array got created with func gen_random',target_fixture='resarray')
def resarray():
    return list(set(gen_random(20,2,4)))

@then('Result should be an array with random numbers which set will be [2,3,4] (not 100% chance)')
def resarray(resarray):
    assert resarray == [2,3,4]


