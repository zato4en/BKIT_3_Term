from pytest_bdd import scenario, given, when, then

from main import sort


@scenario("C:/Users/1/PycharmProjects/BKIT5/sort.feature",'Array will be sorted by abs')
def testing_sort():
    pass

@given('Some array',target_fixture='array')
def array():
    return [2,1,-20,56]

@when('Array get sorted with sort',target_fixture='sorting')
def sorting(array):
    return sort(array)

@then('Array is sorted')
def sorting(sorting):
    assert sorting == [1,2,-20,56]


