@priority_high
Feature: User Registration

  Scenario: Successful registration with valid details
    Given the user navigates to the sign-up page
    When the user enters registration details with first name "John", last name "Doe", email "nohey11845@pofmagic.com", password "password@123", and confirm password "password@123"
    Then the user should be registered successfully
