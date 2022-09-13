# Automation Stackoverflow Environment
How to build your own test plan / Functions description

    Pages/default.py:
    > search_specific_public_page_request
    Companies page:
      >> open_companies_page_and_search_by_name
      >> open_companies_page_and_search_by_location
    Users page:
      >> open_users_page_and_search
    Tags page:
      >> open_tags_page_and_search
    
There is the main params pattern: (get_driver, validate_new_result_loc, search_input_loc, grid_result_loc, text)

  1. where **validate_new_result_loc** is the locator for the changeable value depends on to search request. 
  * Use case: you send in a search field some text and only after the 1 second the page shows you a result, there is over time for testcase validation we save the initial pre-search value and compare it with the final search after the search request, testcase validation caught the right one
  
  2. where **search_input_loc** is the search field locator
  
  3. where **grid_result_loc** is the locator of a single element of the search grid
  
  4. and where **text** is yours search text
