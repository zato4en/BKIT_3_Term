from pytest_bdd import scenario, given, when, then

from main import squared_cont


@scenario("C:/Users/1/PycharmProjects/BKIT5/squared_cont.feature",'New array will contain modified numbers from users interval')
def testing_squared_cont():
    pass

@given('Having interval 2-4',target_fixture='parameters')
def parameters():
    return 2,4

@when('Array got created with func squared_cont',target_fixture='resarray')
def resarray():
    return squared_cont(2,4)

@then('Result should be an array with numbers (i + i**2) for each i in given interval')
def resarray(resarray):
    assert resarray == [6,12,20]
