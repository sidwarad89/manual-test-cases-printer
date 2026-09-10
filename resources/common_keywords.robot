*** Settings ***
Library    SeleniumLibrary
Library    Collections

Suite Setup    Open Browser To Application
Suite Teardown    Close All Browsers

*** Variables ***
${BASE_URL}    https://example-app.com
${BROWSER}    chrome

*** Keywords ***
Open Browser To Application
    [Documentation]    Opens the browser to the base URL.
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.2s

Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Text    id:username    ${username}
    Input Text    id:password    ${password}
    Click Button    css:button[type=submit]
    Wait Until Page Contains    Dashboard

Register New User
    [Arguments]    ${first_name}    ${last_name}    ${email}    ${password}
    Click Link    Register
    Input Text    id:firstName    ${first_name}
    Input Text    id:lastName     ${last_name}
    Input Text    id:email        ${email}
    Input Text    id:password     ${password}
    Click Button    css:button[type=submit]
    Wait Until Page Contains    Registration Successful

Search For Item
    [Arguments]    ${item_name}
    Input Text    id:searchBox    ${item_name}
    Click Button    css:button[type=search]
    Wait Until Page Contains    ${item_name}

Add Item To Cart
    [Arguments]    ${item_name}
    ${item}=    Get Text    xpath://*[@class='product-title' and text()='${item_name}']
    Click Element    xpath://*[@class='product-title' and text()='${item_name}']/../..//button[text()='Add to Cart']
    Wait Until Page Contains    Item added to your cart

Proceed To Checkout
    Click Link    Cart
    Click Button    css:button.checkout
    Wait Until Page Contains    Checkout