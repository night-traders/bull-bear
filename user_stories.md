## User Stories

#### PREVIEW:

- __*“As a User, I would like to view relevant articles / visual depictions about select securities (e.g., major indices) to gain a sense of what this application offers.”*__

    - __FEATURE TASKS:__
    * Provide for display of articles related to major security indexes.
    * Display API feed of related article headlines and intro blurbs for User to select for further reading (on new tabs).

    - __ACCEPTANCE TESTS:__


#### MARKETING:

- __*“As a Developer, I want to offer Visitors a sense of the purpose and full functionality of this site, so that they might choose to register and use the site.”*__

    - __FEATURE TASKS:__
    * Provide static examples of functionality offered live to registered Users.
    * Provide a description of the additional functionality offered exclusively to registered Users.

    - __ACCEPTANCE TESTS:__


#### REGISTRATION:

- __*“As a Developer, I want to offer multiple Users the opportunity to register / Login to gain full site functionality.”*__

    - __FEATURE TASKS:__
    * Provide for secure registration of new Users.
    * Provide for Login authentication for existing Users

    - __ACCEPTANCE TESTS:__


#### LOGOUT:

- __*“As a Developer, I want to provide a User with the means to Logout / auto-Logout when leaving the site.”*__

    - __FEATURE TASKS:__
    * Provide for manual Logout by a User.
    * Provide a means for auto-Logout for Users leaving the site without manually logging out first.

    - __ACCEPTANCE TESTS:__


#### WATCH LIST:

- __*“As a User, I want to create a watch list of stocks I am interested in tracking, so that I don’t have to select those stocks each time I login.”*__

    - __FEATURE TASKS:__
    * Create user input of a security-of-interest then provide the corresponding stock symbol for that Security.
    * Create an alternate user input of the stock symbol for a security-of-interest then provide the corresponding for the Security name.
    * Provide for User selection of the security for addition to that User’s Watch List.
    * Store the Watch Listed securities-of-interest in a database (by stock symbol) linked to that User.

    - __ACCEPTANCE TESTS:__


#### TREND PREDICTION:

- __*“As a User, I want to see the trend predicted for each stock on my watch list, so that I can see where my selected stocks are likely to move in the near future.”*__

    - __FEATURE TASKS:__
    * Upon assignment of a security to the User’s Watch List, display the current trend prediction for that security.
    * Upon subsequent User login, update the performance data for all stocks on the User’s Watch List (stored in the database) and recalculate the trend.
    * Display trend predictions for next day, 3-days-forward and 7-days-forward.

    - __ACCEPTANCE TESTS:__


#### TARGETED ARTICLES:

- __*“As a User, I would like to view relevant articles about the stocks on my watch list, so that I can gather intelligence on what might affect the stock price and make more informed decisions.”*__

    - __FEATURE TASKS:__
    * Provide for User selection to view articles related to a security from their Watch List.
    * Display API feed of related article headlines and intro blurbs for User to select for further reading.

    - __ACCEPTANCE TESTS:__


#### DEREGISTERING:

- __*“As a Developer, I want to offer departing members a means of deregistering (i.e., closing their account) to reduce site overhead.”*__

    - __FEATURE TASKS:__
    * Provide for secure deregistration of departing Users.
    * Provide for retention of select information regarding deregistered Users so to prevent account duplication.

    - __ACCEPTANCE TESTS:__

---
