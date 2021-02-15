# Milestone Project 3 - Blow'n Smoke

![Desktop Demo](https://github.com/Tmuat/blowin-smoke/blob/master/assets/readme_images/mockup.gif "Desktop Demo")

View live project [here](http://blowin-smoke.herokuapp.com/).
---
## Description

BBQ isn't just for summer!! 

For those new to BBQ & smoking, through to seasoned pros; Blow'n Smoke allows everyone to find recipes to wow friends and family with. 

Blow'n Smoke is a recipe website for people who love to BBQ & smoke. The site allows users to search for recipes and also share their own masterful creations. The site also features products to buy to improve their cooking.

If the user has an account, he/she can add, edit and delete their recipes.

If the user is an admin, he/she can add, edit and delete their recipes; along with the ability to add, edit and delete categories and products.

---

## Contents

- [UX](#ux)
    - [Purpose](#purpose)
    - [User Stories](#user-stories)
        - [First Time User](#first-time-user)
        - [Registered User](#registered-user)
        - [Landing Imagery](#landing-imagery)
        - [Admin User](#admin-user)
    - [Design](#design)
        - [Colour Scheme](#colour-scheme)
        - [Fonts](#fonts)
        - [Information Architecture](#information-architecture)
    - [Wireframes](#wireframes)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks and External Resources](#frameworks-and-externalresources)
- [Testing](#testing)
    - [WC3 Validation](#wc3-validation)
    - [Lighthouse Accessibility](#lighthouse-accessibility)
    - [JSHint](#jshint)
    - [Google Dev Tools](#google-dev-tools)
    - [Responsivley](#responsivley)
    - [Manual Testing](#manual-testing)
    - [User Story Testing](#user-story-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Known Bugs](#known-bugs)
- [Deployment](#deployment)
    - [Github Deployment](#github-deployment)
    - [Clone](#clone)
- [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
        - [Misc](#misc)
        - [Content](#content)
        - [Images](#images)
    - [Acknowledgements](#acknowledgements)
    - [Disclaimer](#disclaimer)

---

## UX

### Purpose

- The purpose of this site was to create a full-stack responsive site that allows all users to access and manage a dataset stored in a database.
- Create a site using HTML, CSS, Javascript, Python (Flask) and MongoDB working together.
- Create a site that allows users to find recipes and share their own (READ).
- Create a responsive site that is easy to navigate
- Allow registered users to fulfill the other 3 variables of CRUD (CREATE, UPDATE & DELETE) for their own recipes.
- Allow the admin/owner to list products for potential purchase by site users.
- Limit access to CUD (CREATE, UPDATE & DELETE) of categories and products to admin only.

---

### User Stories

---

#### First Time User:
- As a **first time visitor**, I want to visit a responsive site
- As a **first time visitor**, I want to understand the main purpose of the site
- As a **first time visitor**, I want to be able to easily navigate through the site
- As a **first time visitor**, I want to be able to find recipes to cook for myself
- As a **first time visitor**, I want to be able to filter to only see recipes of particular meats
- As a **first time visitor**, I want to be able to search to find particular recipes
- As a **first time visitor**, I want to be able to register with the site
- As a **first time visitor**, I want to be able to view featured products which I may like to purchase
- As a **first time visitor**, I want to be able to filter to only see products of certain categories

---

#### Registered User:
**The goals of the first time visitor apply to the registered user with the exception of being able to register.**
- As a **registered user**, I want to be able to login and logout with ease
- As a **registered user**, I want to be able to view my profile information
- As a **registered user**, I want to update my profile information
- As a **registered user**, I want to be able to add my own recipes for all to see
- As a **registered user**, I want to be able to update my recipes that I have already added
- As a **registered user**, I want to be able to delete my recipes if I no longer want to share them

---

#### Admin User:
**The goals of the previous two user's apply to the admin user with the exception of being able to register.**
- As a **admin user**, I want to be able to add categories for recipes to aid with filtering and searching
- As a **admin user**, I want to be manage recipe categories, should I want to update or delete them
- As a **admin user**, I want to be able to add products for users to potentially buy
- As a **admin user**, I want to be able to add categories for products to aid with filtering
- As a **admin user**, I want to be able to update or delete product categories
- As a **admin user**, I want to be able to update or delete products

---

### Design

---

#### Colour Scheme

The site predominantly has a black and white theme, owing to the overall site aim being about 
smoking and the black & white nature of smoke. To add an element of colour and draw the users eye 
to key features a off coloured orange was used.

The hex codes for the main colours used are:

- Black #070707
- White #FFFFFF
- Off-white #D8CFCB
- Orange #D95E16

---

#### Fonts

Their are two main fonts which have been incorporated into the site. A title font of 
['Lily Script One'](https://fonts.google.com/specimen/Lily+Script+One?query=lily&preview.text_type=custom) from google 
fonts and then a secondary font of ['Raleway'](https://fonts.google.com/specimen/Raleway?query=rale&preview.text_type=custom).

The fonts were listed as popular pairing on google fonts.

---

#### Landing Imagery

In keeping with the theme of the site, a billowing smoke video was used as the landing image of the site.

---
#### Information Architecture

The MongoDB database consists of 6 collections within one database. Below is the structure of all 6 collections.

![Information Architecture](https://github.com/Tmuat/blowin-smoke/blob/master/assets/readme_images/information.png "Information Architecture")

---

### Wireframes

The wireframes for phone, tablet and desktop can be found by clicking [here](https://github.com/Tmuat/blowin-smoke/tree/master/assets/wireframes).

[Desktop](https://github.com/Tmuat/blowin-smoke/blob/master/assets/wireframes/Desktop.pdf)

[Tablet](https://github.com/Tmuat/blowin-smoke/blob/master/assets/wireframes/Tablet.pdf)

[Mobile](https://github.com/Tmuat/blowin-smoke/blob/master/assets/wireframes/Mobile.pdf)

[Return to Contents](#contents)

---

## Features

### Existing Features

---

#### Design

- Favicon
    - The favicon matches the colour scheme and text used on the site.

- Navbar 
    - The site features a consistent navbar across all pages. It includes the site title along with links to pages; the links update with the active class and also if the user is logged in.
        The navbar collapses into a hamburger icon on smaller screens to maximise screen space.
    - The navbar is stuck to the top of the screen, meaning however far down the page the user scrolls they can always access the sites navigation links.
    - The navbar is given a background on page scroll.

- Footer
    - The site features a consistent footer across all screen sizes; it includes links the main pages along with a small description of the website. 
    - The footer also has 3 social media links styled as the respective sites logo.
    - The footer lastly highlights the developer.

- Interaction
    - Flask flashes have been used to show toasts to inform the user of site events such as login/logout, add/update/deletion of objects. 
    - The toasts have different styles dependent on 'error' or 'success' categories.

- Overall Design
    - The site features a consistent colour scheme and styling across all pages; offering the user simple yet attractive layout.
    - The user can quickly find either products or recipes to buy or try.
    - The site is responsive on all devices with a mobile-first design using the recognised Bootstrap framework

#### Users
- User functionality
    - The site allows users to register, login and logout in clear fashions as the menu's change dependent on user authentication
    - The site allows the user to access their profile and update certain criteria

#### Recipes
- Recipe Overview
    - Visitors to the site can search, filter and view all recipes (READ). They can then follow the instructions to cook the recipe themselves.
    - Recipes can be created, updated and deleted (the remaining three from CRUD) but only users can perform actions on their recipes. 
    - Recipes can be sorted by categories with pagination.
    - Visitors can also search for recipes and view results with pagination. 
    - When users access their profile they can view a list of all recipes they have created.

---

### Features Left to Implement

- Quote Change
    - At the moment the landing page quotes are set in the database. It would be nice for the admin to be able to CRUD the quotes database.

- Rating
    - It would be nice for users to be able to rate the recipes, thus allowing other users to search based on a 1/5 or star rating and view the
        most popular recipes.

- Comments
    - Much like the rating, it would be nice for users to be able to comment on recipes. As recipes can only be updated by the recipe owner, if someone
        had an improvement they cannot add it.
    
- Favorites
    - Allow the user to create their own list of favourite recipes to quickly access.

- Contact Page
    - Currently visitors to the site cannot contact the sites owners. This is a must for the site going forward.

- Ingridient Calculation
    - The ability to update the ingredients amounts based on the number of people you wish to cook for.

- Recipe & Card Image
    - Currently the only way to add images for recipes or products is to add an external url. It would be nice in the future to have an upload option.

- User Deletion
    - Allow the user to delete their profile should they not wish to be a part of the website anymore.

- Custom Error Pages
    - At the moment I do not have custom error pages, with this site specifically a 403, 404 and 500 error pages would be essential. It would also be good to
        add some logging to be able to identify any errors that come up.

- Password Change 
    - Currently there isn't a process to change passwords. Also passwords should be verified by an email.

---

[Return to Contents](#contents)

---

## Technologies Used

### Languages

---

Across the site 4 languages were used:

- HTML5
    - This was used to form the structure of each page
- CSS3
    - This was used to add syling to all html elements
- JavaScript
    - This was was to add classes and validate forms.
- Python 3.8.7
    - Python provided the backend language of the project.


---

### Frameworks and External Resources

---

A number of external frameworks, code libraries and programs were incorportated into the Visit Kingston site. These are listed below with code attribution within each segment of the live site and in the credits section towards the end of this README.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask was the python framework used to build the application

- [Bootstrap 4.5.3](https://getbootstrap.com/)
    - Bootstrap formed the skeleton of the website; the bootstrap grid system and classes formed the underlying structure of the site

- [Font Awesome 5.15.1](https://fontawesome.com/)
    - Font Awesome was used to add icons across the site for a more intuitive user experience

- [JQuery 3.5.1](https://jquery.com/)
    - JQuery was used across the different pages of the site to create interactive elements without the need for huge volumes of Javascript coding

- [Popper.js 1.16.1](https://popper.js.org/)
    - Popper was used with Bootstrap to create a responsive navbar element

- [Animate On Scroll 2.3.1](https://michalsnik.github.io/aos/)
    - Animate on scroll was used on the 'About Kingston' page to add affects to titles and dividers

- [Gitpod](https://gitpod.io/)
    - Gitpod was the development environment used to code this site, gitpods terminal was used to synchronise with Github

- [Github](https://github.com/)
    - Github was used to store all components of this site during and after the build

- [Git](https://git-scm.com/)
    - Git was the version control system utilised for the build of this project

- [Figma](https://www.figma.com/)
    - Figma was used to create the wireframes prior to the build commencing

- [Google Fonts](https://fonts.google.com/)
    - Google Fonts was used to find and import the selected font for the site

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Was used as the templating language to pass variables from python to html

- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - Was used within Flask to hash passwords for entry into the database

- [MongoDB](https://www.mongodb.com/)
    - MongoDB was used as the database for the project.

- [Heroku](https://www.heroku.com)
    - Heroku was used to host the website online.

- WC3 [HTML](https://validator.w3.org/) & [CSS](https://jigsaw.w3.org/css-validator/) Validator
    - Both the CSS & HTML validators were used to check code for compliance with recognised standards

- [Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools)
    - Was used to check the accessibility of the site

- [JSHint](https://jshint.com/)
    - Was used to validate all Javascript codes

- [Pep8Online](http://pep8online.com/checkresult)
    - Along with the fact that Pep8 compliance is built into the coding environment, this external site was also used to
        check the python code

- [Responsivley](https://responsively.app/)
    - Responsivley was used to check the responsiveness of the site (see testing below)


[Return to Contents](#contents)

---

## Testing

### WC3 Validation

---

In order to check that all the HTML & CSS were in compliance of the recognised standards, all code was passed through the [W3C](https://www.w3.org/) validators. Specifically the [HTML validator](https://validator.w3.org/) and the [CSS validator](https://jigsaw.w3.org/css-validator/validator.html.en). The results of the css is below:

- [CSS](https://github.com/Tmuat/blowin-smoke/blob/master/assets/readme_images/css.png "CSS Output")

The HTML was checked but failed with some flask specific contents such as "Bad value {{ url_for('products') }} for attribute href on element a: Illegal character in path segment: { is not allowed."

The validator outputs were gone through to check for normal HTML errors.

---

### Lighthouse Accessibility

---

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) testing was used to ensure the Blow'n Smoke was accessible for all users. The scores for the home page can be seen below with the results linked beneath that:

![lighthouse desktop](https://github.com/Tmuat/blowin-smoke/blob/master/assets/readme_images/desktop/desktop%20overview.png "Desktop Overview")

![lighthouse mobile](https://github.com/Tmuat/blowin-smoke/blob/master/assets/readme_images/mobile/mobile%20overview.png "Desktop Mobile")

[lighthouse Desktop](https://github.com/Tmuat/blowin-smoke/tree/master/assets/readme_images/desktop)

[lighthouse Mobile](https://github.com/Tmuat/blowin-smoke/tree/master/assets/readme_images/mobile)

---

### JSHint

---

All Javascript codes were passed through the [JSHint](https://jshint.com/) validator with all corrections made.

---

### Google Dev Tools

---

Chrome DevTools was used from start to finish when building and testing this site. Throughout the build it served several purposes:

- Throughout the build it was used to quickly test responsiveness for all elements and design

- When constructing pages and elements, it was used to quickly and visually check for any padding and margin issues. Unicorn Revealer also provided a lot of help with this.

- Dev tools was used to identify and errors and warnings; I was reminded to utilise a favicon. Once created a link tag was added into the head of the base template.

- It was used vigorously to adjust css for hover, focus and active classes. 

---

### Responsivley

---

[Responsivley](https://responsively.app/) was used used to check the responsiveness of the site across multiple devices at the same time.

![responsiveness testing](https://github.com/Tmuat/blowin-smoke/blob/master/assets/readme_images/responsively.gif "responsiveness testing")

---

### Manual Testing

Along with the automated testing, the site was put through a whole selection of manual user testing. A brief summary of this manual testing can be found below:

- Each page has been tested individually to check that:
    - Images load properly and are the correct sizes
    - Navigation buttons work and also link to the correct pages on the site
    - Any external links on the site (footer & products page) are set to target="_blank" to open on a new page
    - On top of this testing, with the number of forms on the site they were also checked for:
        - Client side & server side validation works
        - Any errors or successes coming from the server side flashes appear in toasts with appropriate messages:
    - Checked the navbar is visible on all pages. 
        - On the recipe page the navbar was given a background on page load to make it visible
---

### User Story Testing

---

Testing the user stories from the [UX Section](#ux).

#### First Time User:
- As a **first time visitor**, I want to visit a responsive site
    - The site works on all screen sizes having followed a mobile first design and build process
- As a **first time visitor**, I want to understand the main purpose of the site
    - At the bottom of the landing video, is a short description regarding looking for recipes. Also, on every page is a short description of the site in the footer.
- As a **first time visitor**, I want to be able to easily navigate through the site
    - The site features a navbar fixed on every page, with links updating dependent on user authentication
- As a **first time visitor**, I want to be able to find recipes to cook for myself
    - On the home page is a random sample of 6 recipes and links in the nav bar and below the sample take the user to the recipe page. Here they are able to filter and search for different recipes.
- As a **first time visitor**, I want to be able to filter to only see recipes of particular meats
    - Above the recipe cards on the recipes page is a filter section visible on all screen sizes. Here you can text search or select a meat filter.
- As a **first time visitor**, I want to be able to search to find particular recipes
    - As stated above, there is a text search field to search, name, category and description for searched words/
- As a **first time visitor**, I want to be able to register with the site
    - The site features a register link in the navbar taking the user to a form for site registration.
- As a **first time visitor**, I want to be able to view featured products which I may like to purchase
    - As with recipes, a sample of 6 products are displayed on the home screen with a link to an all products page. On this page the user is presented with a paginated section of all products in the database.
- As a **first time visitor**, I want to be able to filter to only see products of certain categories
    - On the product page there is a filter section underneath the landing image which is visible on all screen sizes. This allows the user to filter to product types.

#### Registered User:
**The goals of the first time visitor apply to the registered user with the exception of being able to register.**
- As a **registered user**, I want to be able to login and logout with ease
    - In both the navbar and footer are links to the login page and once logged in these change to logout.
- As a **registered user**, I want to be able to view my profile information
    - Once logged in, the user has a link in the navbar to their profile. Within it they can view any recipes they have added as well as their user information.
- As a **registered user**, I want to update my profile information
    - From the profile page, the user can click a link to edit their profile. This loads a modal with options to edit their first name, last name and email. 
- As a **registered user**, I want to be able to add my own recipes for all to see
    - Once logged in, users have the option of adding a recipe in the navbar. From this page the user can add a recipe with a dynamic amount of ingridients and steps.
- As a **registered user**, I want to be able to update my recipes that I have already added
    - From the users profile page they can see a list of all their recipes, displayed next to the recipe is a link to 'edit' their recipe. They can fill out the form and the recipe will be updated.
- As a **registered user**, I want to be able to delete my recipes if I no longer want to share them
    - From the same profile page, next to the edit button, the user has the ability to delete any recipes they no longer want.
---

### Fixed Bugs

---

- Index Out of Range
    - Fixed the error on the home page whereby if there was less than 6 products or recipes it caused the index to be out of range and throw
        a server error.

- Category/Page
    - With pagination I fixed an error whereby if a user directly changed the url they could search for categories or pages that don't exist. 
        Server side, the request arguement is checked first with redirects and toasts should an error occur.

- Fixed slow loading error of landing video
    - The landing video was slow to load due to it's size. I was able to compress and shorten it to allow for quicker loading. There is tradeoff as the smaller
        it becomes it also loses quality.

- Div error for dynamically adding and deleting forms fields
    - Due to a html error when writing the code, the html fields weren't being added or removed correctly. This was also causing the inputs to not be correctly identified.

---

### Known Bugs

---

- Pagination
    - Currently the way the pagination works it queries for a full queryset(qs) before using a limit and offset to trim the qs to the objects needed
        for that page. This currently defeats the object of pagination as the page is still querying a full dataset. Whilst not a problem now with the
        current size of the data, this will present a problem as the dataset grows.

- Categories
    - Currently you can remove a product or recipe category, even if there are products or recipes in the database with that specific category. If deleted, 
        it doesn't effect the recipes or products but does mean a filter is not displayed. This could be addressed with a relational database model.

- Delete
    - Whilst not specifically a bug in the code, at the moment there is no submission check when deleting an item (be it product, recipe or category). This
        may lead to items being accidently deleted.

- Lighthouse Scores
    - At the moment the site doesn't have great lighthouse scores, improving these is a must.

[Return to Contents](#contents)

---

## Deployment

### Local Deployment

---

To run your own version of this project, it can be cloned or downloaded from Github

To clone this project:

1. At the top the repository, click the green code button at the top of the screen.
2. Click the clipboard icon to copy the URL.
3. Open a new terminal window in your IDE of choice, and make sure the current working directory is the location where you want your cloned directory.
4. In the command line, you need to paste the copied link mentioned above after 'git clone', to create your own local repository of the 'Blow'n Smoke' repository.
```
git clone https://github.com/Tmuat/blowin-smoke.git
```
5. This project uses [MongoDB](https://www.mongodb.com/), you will need to create a database that you will use for this project - you will also need to add the relevant collections later on.
6. In the terminal window, install the required dependencies needed to successfully run the app. This can be done with:
```
pip3 install -r requirements.txt
```
7. At the root level of your application, create a file called env.py to contain your environmental variables. They are as follows:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "**User Inputted Secret Key**")
os.environ.setdefault("MONGO_URI", "**Specific Link To MongoDB The User Has Created**")
os.environ.setdefault("MONGO_DBNAME", "**Your MongoDB Name**")

```

You will need to change the **MONGO_URI** and **MONGO_DBNAME** fields to those provided by your own version of the MongoDB database created. You must remeber to replace the necessary fields of 'username', 'password', 'cluste_name' and 'database_name' in the URI.
You will also need to update the **SECRET_KEY**. The secret key can be of your own creation; you can generate one with [Random Keygen](https://randomkeygen.com/).

8. You can now run the application locally, by typing in the terminal window: 
```
python3 app.py
```

***

### Deploying to Heroku

---

If you would like to deploy this site to Heroku, there are some additional steps that need to be taken:

1. Sign in or create a [Heroku](https://www.heroku.com) account and create a new app (choosing a unique name). Ensure the region selected is the one closet to you.
2. Once created, navigate to the 'Settings' tab, and click the 'Reveal Config Vars' button.
3. Here you need to enter the **exact** same variables created in your env.py file:
```
IP = 0.0.0.0
PORT = 5000
SECRET_KEY = SECRET_KEY
MONGO_URI = MONGO_URI
MONGO_DBNAME = MONGO_DBNAME
```
4. In your local repository, create the requirements.txt if not already created. Heroku will use this to create the same environment as your IDE on heroku:
```
pip3 freeze > requirements.txt
```
5. Then create a Procfile, including the content in the creation:
```
echo web: python app.py > Procfile
```
6. Within the Heroku app you have made, navigate to the 'Deploy' tab, and under the 'Deployment method' section, select 'Connect to Github'.
7. You may be required to link your Github but once it is done you can search for the repository you are storing this site in.
8. Make sure to select the correct repository and click 'connect'.
9. Now you should be able to deploy from the master branch. You have the option of setting automatic deploys, so that if you update any code it is automatically pushed to Heroku.
10. Heroku will now start building the app, you can see the app being built. It will let you know when the build is complete. 
11. When the build is complete, you should see that 'Your app was successfully deployed'. Click the 'View' button to to launch the app.

[Return to Contents](#contents)

---

## Credits

### Code

---

- Code for the navbar on the site came from [Bootstrap](https://getbootstrap.com/docs/4.5/components/navbar/).
- Code for the footer on the site came from [Bootstrap](https://mdbootstrap.com/docs/standard/navigation/footer/).
- Code for the Landing Video came from [Web Dev Simplified](https://codepen.io/WebDevSimplified/pen/oaxjQb).
- Code for the tiny sliders used for recipes and products came from [Tiny Slider](https://github.com/ganlanyuan/tiny-slider).
- Code for the toasts came from [Bootstrap](https://getbootstrap.com/docs/4.5/components/toasts/).
- Code for the form label float came from [Online Tutorials](https://www.youtube.com/watch?v=PTGnpXbMU1U).
- Code for the index.html card animation came from [Animate On Scroll](https://michalsnik.github.io/aos/).
- Code for the JQuery validate came from [JQuery Validate](https://www.sitepoint.com/basic-jquery-form-validation-tutorial/).
- Code for the JQuery to allow users to manipulate the amount of fields on the recipe form came from [JSFiddle](https://jsfiddle.net/jnwrc5ay/592/).
- Code for the Facebook social media icon came from [Font Awesome](https://fontawesome.com/icons/facebook-square?style=brands).
- Code for the Youtube social media icon came from [Font Awesome](https://fontawesome.com/icons/youtube-square?style=brands).
- Code for the Twitter social media icon came from [Font Awesome](https://fontawesome.com/icons/twitter-square?style=brands).
- Code for the left and right arrows for the card carousel came from [Font Awesome](https://fontawesome.com/icons/caret-left?style=solid) and [Font Awesome](https://fontawesome.com/icons/caret-right?style=solid).
- Code for the HTML pagination came from [Bootstrap](https://getbootstrap.com/docs/4.5/components/pagination/).
- Code for the python pagination came from [Pretty Printed](https://www.youtube.com/watch?v=Lnt6JqtzM7I).
- Code for the modal form on the profile page came from [Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/).
- Code for the python decorators came from [Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/).
- Code for the python random choices/samples came from [W3Schools](https://www.w3schools.com/python/ref_random_choices.asp).
- Code for interacting with MongoDB came from [Code Institute](https://codeinstitute.net/).
- Code for the context processors came from [Flask](https://flask.palletsprojects.com/en/1.1.x/templating/#context-processors).


---

### Media

---

- #### Misc
    - The favicon was produced using favicon.io](https://favicon.io/favicon-generator/), it incorporates the main colours of the site with the sites initials.
    - The mockup at the start of the README.md was created using [Am I Responsive](http://ami.responsivedesign.is/) - I then created the gif myself.
---

- #### Content
    - The current recipes on the site have come from a mix of [Pitboss](https://pitboss-grills.com/recipes/beef/) and [Hot Smoked](https://hotsmoked.co.uk/hot-smoking-recipes-and-tips).
    - All other content was the work of the developer.

---

- #### Images & Video
  The main images used as headers came from [unspash](https://unsplash.com/), whilst recipe and product
  images are allowed from user input so come from a variety of sources.
  
    - Landing video (billowing smoke) came from [Motion Array](https://motionarray.com/); 
        I have a subscription and am therefore allowed to use the video for my own projects
        per their [license](https://github.com/Tmuat/blowin-smoke/blob/master/assets/licenses/motion-array.txt).
    - The 3 main images used on the site come from [unspash](https://unsplash.com/). The images are for the 
        recipe page, products page and then the smokey background for most other pages.
        - [Smoke](https://unsplash.com/@honeyyanibel)
        - [Recipe](https://unsplash.com/@emersonvieira)
        - [Products](https://unsplash.com/@zgrillsaustralia)
        - [Default Recipe](https://unsplash.com/@markusspiske)
    - Most of the card & recipe images were sourced from google images.

---

### Acknowledgements

---

I would like to thank my mentor Oluwafemi Medale for his help keeping me on the 
right lines and being there to help me with my pagination woes. I would like to thank 
all the people that kindly sat and reviewed my site through production.

---

### Disclaimer

---

This project was created for educational use only.

[Return to Contents](#contents)
