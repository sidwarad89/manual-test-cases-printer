*** Settings ***
Resource    ../resources/common_keywords.robot
Test Setup    Open Browser To Application
Test Teardown    Close All Browsers
Variables    ../data/testdata.csv

*** Test Cases ***
Valid Login Redirects To Dashboard
    [Documentation]    Verify that a valid user can log in and sees the dashboard.
    ${username}=    Get From Dictionary    ${USER_DATA}    username
    ${password}=    Get From Dictionary    ${USER_DATA}    password
    Login With Credentials    ${username}    ${password}
    Page Should Contain    Dashboard