
    // Upload validation
    document.querySelector("form").addEventListener("submit", function (e) {

        const file = document.getElementById("image").files[0];

        if (file && file.size > 5 * 1024 * 1024) {

            alert("Image must be smaller than 5 MB");

            e.preventDefault();
        }

    });


    // Hide success message after 3 seconds
    setTimeout(function () {

        document.querySelectorAll(".message").forEach(function (msg) {

            msg.style.display = "none";

        });

    }, 3000);


    // Open image in modal
    function openImage(url, title) {

        document.getElementById("imageModal").style.display = "block";

        document.getElementById("modalImage").src = url;

        document.getElementById("caption").innerHTML = title;

    }


    // Close modal
    function closeImage() {

        document.getElementById("imageModal").style.display = "none";

    }


    // Close when clicking outside the image
    window.onclick = function (event) {

        const modal = document.getElementById("imageModal");

        if (event.target == modal) {

            closeImage();

        }

    }


    // Close when pressing ESC
    document.addEventListener("keydown", function (e) {

        if (e.key === "Escape") {

            closeImage();

        }

    });

