document.addEventListener("DOMContentLoaded", function () {

    const menuButton = document.querySelector(".menu-toggle");
    const navigation = document.querySelector(".main-nav");
    const menuIcon = document.querySelector(".menu-icon");


    // Check elements exist
    if (!menuButton || !navigation || !menuIcon) {
        return;
    }


    // Open / close mobile menu
    menuButton.addEventListener("click", function () {

        const isOpen = navigation.classList.toggle("active");


        // Update accessibility attribute
        menuButton.setAttribute(
            "aria-expanded",
            isOpen
        );


        // Update button label
        menuButton.setAttribute(
            "aria-label",
            isOpen
                ? "Close navigation menu"
                : "Open navigation menu"
        );


        // Change icon
        menuIcon.textContent = isOpen ? "✕" : "☰";

    });


    // Close menu when navigation link is clicked
    const navigationLinks =
        navigation.querySelectorAll("a");


    navigationLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            navigation.classList.remove("active");

            menuButton.setAttribute(
                "aria-expanded",
                "false"
            );

            menuButton.setAttribute(
                "aria-label",
                "Open navigation menu"
            );

            menuIcon.textContent = "☰";

        });

    });


    // Close menu when clicking outside
    document.addEventListener("click", function (event) {

        const clickedInsideNavigation =
            navigation.contains(event.target);

        const clickedMenuButton =
            menuButton.contains(event.target);


        if (
            !clickedInsideNavigation &&
            !clickedMenuButton
        ) {

            navigation.classList.remove("active");

            menuButton.setAttribute(
                "aria-expanded",
                "false"
            );

            menuButton.setAttribute(
                "aria-label",
                "Open navigation menu"
            );

            menuIcon.textContent = "☰";

        }

    });


    // Close menu when switching back to desktop
    window.addEventListener("resize", function () {

        if (window.innerWidth > 768) {

            navigation.classList.remove("active");

            menuButton.setAttribute(
                "aria-expanded",
                "false"
            );

            menuButton.setAttribute(
                "aria-label",
                "Open navigation menu"
            );

            menuIcon.textContent = "☰";

        }

    });

});


    /* =========================================
       SCROLL REVEAL
    ========================================= */

    const revealElements =
        document.querySelectorAll(".reveal");

    const revealObserver =
        new IntersectionObserver(
            function (entries, observer) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("active");

                        observer.unobserve(entry.target);

                    }

                });

            },
            {
                threshold: 0.15
            }
        );


    revealElements.forEach(function (element) {

        revealObserver.observe(element);

    });