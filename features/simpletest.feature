Feature: Purchase product on DemoBlaze
  As a user, I want to purchase a product from DemoBlaze
  So that I can complete my order

  Scenario: Successfully purchase a Samsung Galaxy S6
    Given I am on the DemoBlaze homepage
    When I select the "Samsung galaxy s6"
    And I add the product to the cart
    And I proceed to the cart
    And I place an order
    And I fill in the order form with Name "Test", Country "Ukraine", City "Kyiv", Credit Card "4111111111111111", Month "2", Year "2029"
    And I confirm the purchase
    Then I should see the confirmation of the purchase