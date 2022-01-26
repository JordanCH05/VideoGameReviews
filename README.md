# Royal Robot Reviews

This website has been created for users to write reviews for a selection of games and compare their scores.

The live site can be found [here](https://royal-robot-reviews.herokuapp.com/)

![Responsive Mockup of site](static/images/mockup.png)

## Table of Contents

* [User Experience](#user-experience)

    * [User stories](#user-stories)
    * [Admin Stories](#admin-stories)

* [Planning](#planning)

* [Features](#features)

* [Future Features](#future-features)

* [Django apps and models](#django-apps-and-models)

* [Testing](#testing)

* [Languages and Programs Used](#languages-and-programs-used)

    * [Languages](#languages)

    * [Libraries and Frameworks](#libraries-and-frameworks)

    * [Development tools](#development-tools)

    * [Required modules](#required-modules)

* [Credits](#credits)

## User Experience

### User stories

As a user I would like to be able to...

* View the list of Video Games so that I can select one to review
* View a paginated list of videogames so that I can easily select a videogame to view
* Click on a game so that I can read the full details and reviews of the game and I can review it
* View a list of reviews so that I can select one to read
* Register an account so that I can review, comment, and like
* Leave a review for a game so that my opinion is heard and I can be involved in rating the game
* Edit or delete my review in order to show my change of opinion or remove mistakes

### Admin Stories

As an admin I would like to be able to...

* Create draft games so that I can finish writing the content later
* Create, read, update and delete games so that I can manage the site content
* Create, read, update and delete reviews so that I can manage the site content
* Approve or disapprove reviews so that I can filter out objectionable content

## Planning

* Colour Scheme
    * Simple black and yellow colours for most of site and purple for logo to represent royalty
    * contrsating colours for easy legiblity and style

    ![Colour scheme #000000 #F1B814 #490B3D](static/images/colourscheme.png)

* Font taken from [Google Fonts](https://fonts.google.com/)

    ![Romanesco Font](static/images/romanescofont.PNG)

* Pages were planned out on [Figma](https://www.figma.com) using wireframes

## Features

* Logo
    * The logo was made using [Canva](canva.com)
    * Used as link to return to the home page
    * Logo uses purple to represent royalty

![Logo](static/images/logo.png)

* Base Template

    * Header with navigation bar

    ![Header with navigation](static/images/header.png)

    * Footer with social media links

    ![Footer with social media links](static/images/footer.png)

* Index Page
    * Introduction telling you about the site and what to do

    ![Introduction](static/images/intro.png)

    * List of Games to choose
    * Games ordered by average review scores
    * Images, titles, scores and developer shown on each game card

    ![List of games](static/images/gamelist.png)

    * Paginated if above 6 games

    ![Paginate Next Button](static/images/pagination.png)


* Game Detail Page

    * Game detail with average review score and description

    ![Game image, title, reating and description](static/images/gamedetail.png)

    * Game reviews with the ability for user's to edit and delete their own reviews

    ![Reviews of the game](static/images/reviews.png)

    * Review Form with stars that reflect the users rating

    ![Review form](static/images/review-form.png)

* Edit Review Page

    * Will fill the inputs with the review of that instance to be edited
    * Submits an updated review to be approved again

    ![Edit Review Page](static/images/edit-review.png)

* Delete Modal

    * An 'are you sure?' modal to prevent users from accidentaly deleting

    ![Delete Modal](static/images/delete-modal.png)

* Messages

    * Review submission, sign in and out message confirmation
    * Times out after 2.5 seconds

* Account pages

    * Login logout and signup pages connected with allauth

### Future Features

* Users can add games
* Add a spoiler-free tag on reviews

## Testing

### HTML

* Tested using the official [W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Froyal-robot-reviews.herokuapp.com%2F)

### CSS

* Tested using the official [Jigsaw W3C Validator](https://jigsaw.w3.org/css-validator/validator)

### JavaScript

* Tested using [JSHint JavaScript Validator](https://jshint.com/)

### Browsers

* Tested on Google Chrome, Internet Explorer, Microsoft Edge and even the Samsung Internet App on Mobile and Tablet

### Responsiveness

* Tested responsiveness on a Samsung A21 Phone, Samsung Galaxy Tablet and Desktop
* Tested with Google Chrome Development tools for different screen sizes

### Accessibility

* Tested using a web accessibility evaluation tool called [Wave](https://wave.webaim.org/)
* Semantic HTML is used
* Headers are in order and not skipped (h1, h2, h3)

## Bugs and Solutions

* The starRating function would produce undefined sometimes, so an if statement was used to filter them out to avoid errors
* The fixed bottom footer would overlap onto the main content, so using flexbox and a mininum height of 100vh for the body element fixed this instead of fixing it to the bottom
* The game list contents overflowed out of their cards, boostrap classes was used to change the size of the cards accordingly while keeping them all the same height
* The edit review page wouldn't fill the inputs with the rewview data, so redefining the review instance tended to fix this

## Languages and Programs Used

### Languages

* HTML5 for site structure
* CSS3 for styling
* JavaScript for star ratings and message timeouts
* Python 3.0 for Django

### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)'s model view template structure was used to create apps and run them
* [Boostrap4](https://getbootstrap.com/docs/4.5/getting-started/introduction/) framework used for responsive styling and templates

### Development tools
* Git for version control
* VS Code as IDE (integrated development environment)
* PIP to install packages
* Postgresql for the database to create content and manage data
* Heroku used for deployment

### Required modules

All modules required are located in the [requirements.txt](requirements.txt) file.

## Credits

* JavaScript code for star ratings is based on code from [Brad Traversy](https://codepen.io/bradtraversy/pen/GQLRZv)
* [Bootstrap cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/) helped by listing boostrap classes in an easy to find manner
* [Boostrap Templates and Examples](https://getbootstrap.com/docs/5.1/examples/) used as a basis for some features
* [Font Awesome](https://fontawesome.com/) used for the stars
* [W3Schools](https://www.w3schools.com/) used for reference in using coding [languages](#languages)
* [Stack Overflow](https://stackoverflow.com/) was used to find solution to some coding issues
* The [Code Institute](https://codeinstitute.net/) study material was used
* [Wikipedia](https://www.wikipedia.org/) used for descriptions of the games