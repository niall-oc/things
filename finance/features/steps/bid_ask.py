from behave import given, when, then

@given(u'I have approximately {number_of_bids} bids')
def step_impl(context, number_of_bids):
    raise NotImplementedError(u'STEP: Given I have approximately 100 bids')

@given(u'I have approximately {number_of_asks} asks')
def step_impl(context, number_of_asks):
    raise NotImplementedError(u'STEP: Given I have approximately 100 asks')

@when(u'I match orders')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I match orders')

@then(u'I see that more than half of the orders are matched')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see that more than half of the orders are matched')
