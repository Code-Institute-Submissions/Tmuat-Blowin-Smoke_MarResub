
// JS for Tiny-Slider Carousel in recipe section - from https://github.com/ganlanyuan/tiny-slider
$(document).ready(function () {
    var slider = tns({
        container: '.recipe-slider',
        slideBy: 'page',
        loop: true,
        speed: 1000,
        items: 1,
        nav: false,
        mouseDrag: true,
        gutter: 50,
        controlsContainer: "#custom-controls",
        responsive: {
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3,
            }
        }

    });
    var slider = tns({
        container: '.product-slider',
        slideBy: 'page',
        loop: true,
        speed: 1000,
        items: 1,
        nav: false,
        mouseDrag: true,
        gutter: 50,
        controlsContainer: "#custom-controls2",
        responsive: {
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3,
            }
        }

    });
});

// Script to start the AOS library from https://michalsnik.github.io/aos/

// Starts the animation on scroll library 
AOS.init({
    // Sets the duration of the animations
    duration: 1000,
});
