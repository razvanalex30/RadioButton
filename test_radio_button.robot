*** Settings ***
Library     SeleniumLibrary
Library    check_radiobutton.SelectRadioButton
Library    BuiltIn
*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

*** Variables ***
${url}    https://demoqa.com/radio-button
${chosen_value}    Yes
${browser}    chrome

*** Test Cases ***
TestCheckbox
    Open Browser Page
    Retrieve RadioButtons
    Select Button    ${chosen_value}
    Sleep   3
    Close Browser