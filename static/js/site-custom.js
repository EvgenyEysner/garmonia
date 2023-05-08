$(window).load(function () {

    'use strict';
    $("#pageloader").delay(1200).fadeOut("slow");
    $(".loader-item").delay(700).fadeOut();

    smoothScroll.init();

});


/* ==============================================
Custom Javascript
=============================================== */
$(document).ready(function () {

    'use strict';

    if ($(window).width() > 767) {

        function autosize_homepage_image() {
            var height = jQuery(window).height();
            jQuery('#home .home-header').css('height', height + 'px');
        }

        jQuery(function () {
            autosize_homepage_image();
            jQuery(window).resize(function () {
                autosize_homepage_image();
            })
        });


        $(function () {
            var header = $(".navbar"),
                yOffset = 0,
                triggerPoint = 150;
            $(window).scroll(function () {
                yOffset = $(window).scrollTop();

                if (yOffset >= triggerPoint) {
                    header.addClass("fixed-top animated fadeInDown");
                } else {
                    header.removeClass("fixed-top animated fadeInDown");
                }

            });
        });
    } else {
        jQuery(window).resize(function () {
            autosize_homepage_image();
        })
    }


    $('body').scrollspy({
        target: '.navbar',
        offest: 0
    });

    $('body').scrollspy({target: '#navbarSupportedContent'})

    // Bootstrap Tooltip
    $('.social-icons a').tooltip({
        placement: 'bottom',
    });

    //Mobile Nav
    $('#navbar').on('click', function (e) {
        $('.navbar-collapse').removeClass('show').addClass("collapse");
    });


    //Shrink Header
    var shrinkHeader = 130;
    $(window).scroll(function () {
        var scroll = getCurrentScroll();
        if (scroll >= shrinkHeader) {
            $('header').addClass('colored');
        } else {
            $('header').removeClass('colored');
        }
    });

    function getCurrentScroll() {
        return window.pageYOffset || document.documentElement.scrollTop;
    }

    // Portfolio Single Slider
    $("#home-servies").owlCarousel({
        items: 4,
        margin: 30,
        loop: true,
        nav: true,
        slideBy: 1,
        dots: false,
        center: false,
        autoplay: false,
        autoheight: true,
        navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
        responsive: {
            320: {
                items: 1,
            },
            480: {
                items: 1,
            },
            600: {
                items: 2,
            },
            1000: {
                items: 3,
                loop: true,
            },
            1200: {
                items: 4,
                loop: true,
            }
        }
    });

    $("#home-package").owlCarousel({
        items: 4,
        margin: 30,
        loop: true,
        nav: true,
        slideBy: 1,
        dots: false,
        center: false,
        autoplay: false,
        autoheight: true,
        navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
        responsive: {
            320: {
                items: 1,
            },
            480: {
                items: 1,
            },
            600: {
                items: 2,
            },
            1000: {
                items: 4,
                loop: true,
            },
            1200: {
                items: 4,
                loop: true,
            }
        }
    });

    $("#home-testimonial").owlCarousel({
        items: 1,
        margin: 0,
        loop: true,
        nav: true,
        slideBy: 1,
        dots: false,
        center: false,
        autoplay: false,
        autoheight: true,
        navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
    });

    $("#home-clients").owlCarousel({
        items: 1,
        margin: 30,
        loop: true,
        nav: false,
        slideBy: 1,
        dots: true,
        center: false,
        autoplay: false,
        autoheight: true,
        navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
        responsive: {
            320: {
                items: 2,
            },
            480: {
                items: 2,
            },
            600: {
                items: 3,
            },
            1000: {
                items: 5,
                loop: true,
            },
            1200: {
                items: 6,
                loop: true,
            }
        }
    });

    // Google Map
    $("#map_extended").gMap({
        markers: [{
            address: "",
            html: '<h4>Office</h4>' +
                '<address>' +
                '<div>' +
                '<div><b>Address:</b></div>' +
                '<div>Envato Pty Ltd, 13/2<br> Elizabeth St Melbourne VIC 3000,<br> Australia</div>' +
                '</div>' +
                '<div>' +
                '<div><b>Phone:</b></div>' +
                '<div>+1 (408) 786 - 5117</div>' +
                '</div>' +
                '<div>' +
                '<div><b>Fax:</b></div>' +
                '<div>+1 (408) 786 - 5227</div>' +
                '</div>' +
                '<div>' +
                '<div><b>Email:</b></div>' +
                '<div><a href="mailto:info@well&spa.com">info@well&spa.com</a></div>' +
                '</div>' +
                '</address>',
            latitude: -33.87695388579145,
            longitude: 151.22183918952942,
            icon: {
                image: "images/pin.png",
                iconsize: [35, 48],
                iconanchor: [17, 48]
            }
        },],
        icon: {
            image: "images/pin.png",
            iconsize: [35, 48],
            iconanchor: [17, 48]
        },
        latitude: -33.87695388579145,
        longitude: 151.22183918952942,
        zoom: 16
    });

    // Contact Form
    jQuery("#contact_form").validate({
        meta: "validate",
        /* */
        rules: {
            name: "required",
            // simple rule, converted to {required:true}
            email: { // compound rule
                required: true,
                email: true
            },
            package: {
                required: true,
            },
            phone: {
                required: true
            }
        },
        messages: {
            name: "Bitte geben Sie Ihr Name ein.",
            email: {
                required: "Bitte E-Mail eingeben",
                email: "Bitte E-Mail eingeben"
            },
            phone: "Bitte geben Sie eine Rufnummer an.",
        },
    });

    // Contact Form
    jQuery("form[name='contact']").validate({
        meta: "validate",
        /* */
        rules: {
            first_name: "required",
            last_name: "required",
            // simple rule, converted to {required:true}
            email: { // compound rule
                required: true,
                email: true
            },
            message: {
                required: true
            },
            subject: {
                required: true
            }
        },
        messages: {
            first_name: "Bitte geben Sie Ihr Name ein.",
            last_name: "Bitte geben Sie Ihr Vorname ein.",
            email: {
                required: "Bitte E-Mail eingeben",
                email: "Bitte E-Mail eingeben"
            },
            subject: "Bitte geben Sie einen Betreff ein.",
            message: "Bitte eine Nachricht eingeben"
        },
    });

    /* hide #back-top first */
    $("#back-top").hide();
    // fade in #back-top
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#back-top').fadeIn();
        } else {
            $('#back-top').fadeOut();
        }
    });
    // scroll body to 0px on click
    $('#back-top a').on('click', function (e) {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });

});