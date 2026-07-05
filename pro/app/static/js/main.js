
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



// camera functionality
const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const preview = document.getElementById("preview");

const openBtn = document.getElementById("openCamera");
const switchBtn = document.getElementById("switchCamera");
const captureBtn = document.getElementById("capture");
const imageInput = document.getElementById("image");

let stream = null;

// Start with back camera
let facingMode = "environment";

async function startCamera(){

    try{

        if(stream){

            stream.getTracks().forEach(track=>track.stop());

        }

        stream = await navigator.mediaDevices.getUserMedia({

            video:{
                facingMode:facingMode
            }

        });

        video.srcObject = stream;

        video.style.display = "block";

        captureBtn.style.display = "inline-block";

        switchBtn.style.display = "inline-block";

    }

    catch(err){

        alert(err.message);

        console.log(err);

    }

}

openBtn.onclick = startCamera;


// Switch Camera
switchBtn.onclick = async function(){

    if(facingMode==="environment"){

        facingMode="user";

    }else{

        facingMode="environment";

    }

    startCamera();

};


// Capture
captureBtn.onclick=function(){

    canvas.width = video.videoWidth;

    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");

    ctx.drawImage(video,0,0);

    canvas.toBlob(function(blob){

        const file = new File(
            [blob],
            "camera.png",
            {
                type:"image/png"
            }
        );

        const dt = new DataTransfer();

        dt.items.add(file);

        imageInput.files = dt.files;

        preview.src = URL.createObjectURL(blob);

        preview.style.display = "block";

    });

};
