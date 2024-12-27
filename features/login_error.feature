Feature: User Login
  Scenario: login with invalid credentials
    Given the user navigates to login page
    When the user enters invalid password with email "nohey11845@pofmagic.com" and password "123456"
    Then the user should get valid error message
