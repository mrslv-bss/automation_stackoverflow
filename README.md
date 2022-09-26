# Automation StackOverflow Environment
How to build your test suit or functions description
<hr>

> pages/default.py:
> search_specific_public_page_request
    
test_search.py test cases based on search_specific_public_page_request.
The pages where it is used are as follows:

    Companies page:
      >> open_companies_page_and_search_by_name
      >> open_companies_page_and_search_by_location
    Users page:
      >> open_users_page_and_search
    Tags page:
      >> open_tags_page_and_search
    
There is the main params pattern: (get_driver, search_input_loc, grid_result_loc, text)
  
1. where **search_input_loc** is the search field locator
  
2. where **grid_result_loc** is the locator of a single element of the search grid
  
3. and where **text** is yours search text

> pages/default.py:
> click_on_grid_element

A procedure that clicks a specific grid element

There is the main params pattern: (get_driver, elem_number, elem_type)

1. where ***elem_number*** chooses a specific element among the DOM elements
2. where ***elem_type*** is a specific search mode.
   * In order not to split the function into two due to different search pages, there was decided to add this parameter that regulates:
    
     * elem_type: **True** - grid elements in public pages (tags, users, and companies)
     * elem_type: **False** - grid elements in basic search


> libs/default.py:
> open_public_page

A function that opens one of three public pages (tags, users, and companies)
The pages where it is used is as follows: ***pages/tags.py***, ***pages/companies.py***, and ***pages/users.py***

There is the main params pattern: (get_driver, oneofthree)
* where ***oneofthree*** chooses the page to open

>libs/default.py: dual_tab_start

A function that **returns** the window handle of an opened second browser tab.

>pages/default.py: search_request

A function that **returns** the length of the search result.

<hr>

### Installation ###
    [requirements.txt]
    pytest==7.1.3
    allure-pytest==2.10.0
    selenium==4.4.3
