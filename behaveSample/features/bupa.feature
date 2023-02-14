Feature: Sample tests on Bupa site

  @sample
  Scenario: Verify the site navigation
    Given I open our bupa link
    Then  I verify the page title

  @dropdownTest
  Scenario Outline: Verify site services in various location
    Given I am on landing page
    When  I mouse hover on customer websites dropdown
    And   I click on customer websites link
    And   I select "<country>" from dropdown
    And   I navigate using "<button_name>" associated with country link
    Then  I verify the "<page_title>" of the country

    Examples:
      | country        | button_name          | page_title                                                            |
      | united-kingdom | Visit Bupa UK        | Private healthcare -> Bupa UK                                         |
      | australia      | Visit Bupa Australia | Bupa -> Health and care                                               |
      | brazil         | Visit Care Plus      | Care Plus -> Plano de Saúde e Dental Premium, Clínicas e Ocupacionaly |