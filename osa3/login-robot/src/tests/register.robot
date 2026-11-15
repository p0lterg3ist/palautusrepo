*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  matti  salasana123
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input New Command
    Input Credentials  kalle  uusi1234
    Output Should Contain  User with username kalle already exists
Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ab  salasana123
    Output Should Contain  Username must be at least 3 characters long
Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  matti1  salasana123
    Output Should Contain  Username must contain only lowercase letters a-z
Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  pekka  abc123
    Output Should Contain  Password must be at least 8 characters long
Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  ville  abcdefgh
    Output Should Contain  Password must contain at least one non-letter character