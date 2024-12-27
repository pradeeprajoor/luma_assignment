Feature: User Login

  Scenario: Successful login with valid credentials
    Given the user navigates to the login page
    When the user enters valid credentials with email "nohey11845@pofmagic.com" and password "password@123"
    Then the user should be logged in successfully
