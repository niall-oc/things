Feature: Sell 90% of Stock on IPO
    As a Market Maker
    I want to sell 90% of the Stock
    Because I have been contracted to

    Scenario: Sell over 40 unit of stocks over a 1 hour interval
        Given I have approximately 100 bids
        and I have approximately 100 asks
        When I match orders
        Then I see that more than half of the orders are matched

