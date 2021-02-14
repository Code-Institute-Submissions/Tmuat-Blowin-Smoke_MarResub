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
        - [Registered Time User](#registered-time-user)
        - [Admin Time User](#admin-time-user)
    - [Design](#design)
        - [Colour Scheme](#colour-scheme)
        - [Fonts](#fonts)
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

---

#### Fonts

The main font used on the site is ************. It was chosen after experimenting with a number of fonts on [google fonts](fonts.google.com).

---

#### Landing Imagery

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

---

### Features Left to Implement

---

[Return to Contents](#contents)

---

## Technologies Used

### Languages

---

Across the site 3 languages were used:

- HTML5
    - This was used to form the structure of each page
- CSS3
    - This was used to add syling to all html elements
- JavaScript
    - This was was to make pages interactive (e.g. google maps)

---

### Frameworks and External Resources

---

A number of external frameworks, code libraries and programs were incorportated into the Visit Kingston site. These are listed below with code attribution within each segment of the live site and in the credits section towards the end of this README.

- [Bootstrap 4.5.2](https://getbootstrap.com/)
    - Bootstrap formed the skeleton of the website; the bootstrap grid system and classes formed the underlying structure of the site

- [Font Awesome 4.7.0](https://fontawesome.com/)
    - Font Awesome was used to add icons across the site for a more intuitive user experience

- [JQuery 3.5.1](https://jquery.com/)
    - JQuery was used across the different pages of the site to create interactive elements without the need for huge volumes of Javascript coding

- [Popper.js 1.16.1](https://popper.js.org/)
    - Popper was used with Bootstrap to create a responsive navbar element

- [Google Maps API](https://developers.google.com/maps/documentation/)
    - The Google Maps API was used to create a map with markers of places to eat & drink, stay overnight and attractions to see

- [Animate On Scroll 2.3.1](https://michalsnik.github.io/aos/)
    - Animate on scroll was used on the 'About Kingston' page to add affects to titles and dividers

- [EmailJS](https://www.emailjs.com/)
    - EmailJS was used to automate the sending of emails in the contact section

- [Hover.css](https://ianlunn.github.io/Hover/)
    - Hover.css was used to create hover affects for the menu items in the navbar. The license can be found [here](https://github.com/Tmuat/milestone-project-2/blob/master/assets/licenses/hover-css.txt)

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

- WC3 [HTML](https://validator.w3.org/) & [CSS](https://jigsaw.w3.org/css-validator/) Validator
    - Both the CSS & HTML validators were used to check code for compliance with recognised standards

- [Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools)
    - Was used to check the accessibility of the site

- [JSHint](https://jshint.com/)
    - Was used to validate all Javascript codes

- [Responsivley](https://responsively.app/)
    - Responsivley was used to check the responsiveness of the site (see testing below)


[Return to Contents](#contents)

---

## Testing

### WC3 Validation

---

In order to check that all the HTML & CSS were in compliance of the recognised standards, all code was passed through the [W3C](https://www.w3.org/) validators. Specifically the [HTML validator](https://validator.w3.org/) and the [CSS validator](https://jigsaw.w3.org/css-validator/validator.html.en). The results of these tests can be found in the links below:

---

### Lighthouse Accessibility

---

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools)

---

### JSHint

---

JSHint](https://jshint.com/)

---

### Responsivley

---

---

### Manual Testing

Along with the automated testing, the site was put through a whole selection of manual user testing. A brief summary of this manual testing can be found below:

- Blank
    - Blank
        - Blank
---

### User Story Testing

---

Testing the user stories from the [UX Section](#ux).

- Blank
    - Blank

---

### Fixed Bugs

---

- Blank
    - Blank

---

### Known Bugs

---

- Blank

[Return to Contents](#contents)

---

## Deployment


---

### Github Deployment

---

To deploy this site to Github pages, the following steps were taken.

1. Blank

---

### Clone

---

Should you wish to fork the project, please follow the below steps.

1. Blank

[Return to Contents](#contents)

---

## Credits

### Code

---

- Blank

---

### Media

---

- #### Misc
    - Blank

---

- #### Content
    - Blank

---

- #### Images
  The images used on this site came from a vaiety of sources.
  
    - Blank

---

### Acknowledgements

---


---

### Disclaimer

---

This project was created for educational use only.

[Return to Contents](#contents)
