## Flask Application Design

### HTML Files
- `index.html`:
    - This will be the main HTML file providing the interface for the application.
    - It will contain a form to capture the user's cibil score.
- `results.html`:
    - This HTML file will display the best loan options available for the user's cibil score.
    - It will provide details such as interest rates, loan amounts, repayment tenures, and eligibility criteria.

### Routes
- `/`:
    - This route corresponds to the `index.html` file.
    - It handles the GET request for the main page and displays the form for capturing the user's cibil score.
- `/submit`:
    - This route corresponds to the form submission.
    - It retrieves the user's cibil score from the request object and uses it to fetch the best loan options from the database or external API.
    - Once the results are obtained, it redirects to the `/results` route, passing the loan options as part of the query parameters.
- `/results`:
    - This route corresponds to the `results.html` file.
    - It retrieves the loan options from the query parameters and populates the HTML file with the loan details.
    - It displays the customized results page to the user, showcasing the best available loans based on their cibil score.