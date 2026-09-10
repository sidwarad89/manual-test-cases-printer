*** Settings ***
Resource    ../resources/common_keywords.robot
Test Setup    Open Browser To Application
Test Teardown    Close All Browsers
Variables    ../data/testdata.csv

*** Test Cases ***
User Can Register New Account
    [Documentation]    Verify that a new user can register using valid data.
    ${first_name}=    Get From Dictionary    ${USER_DATA}    first_name
    ${last_name}=     Get From Dictionary    ${USER_DATA}    last_name
    ${email}=         Get From Dictionary    ${USER_DATA}    email
    ${password}=      Get From Dictionary    ${USER_DATA}    password
    Register New User    ${first_name}    ${last_name}    ${email}    ${password}
    Page Should Contain    Registration Successful