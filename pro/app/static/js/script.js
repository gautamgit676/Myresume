
const titles = [
    "Python Backend Developer",
    "Django Developer",
    "FastAPI Developer",
    "AI Engineer",
    "AWS Cloud Enthusiast"
];

const heroTitle = document.querySelector(".hero h3");

let titleIndex = 0;
let charIndex = 0;
let deleting = false;

function typeEffect() {

    if (!heroTitle) return;

    const current = titles[titleIndex];

    if (!deleting) {

        heroTitle.textContent = current.substring(0, charIndex++);

        if (charIndex > current.length) {
            deleting = true;
            setTimeout(typeEffect, 1500);
            return;
        }

    } else {

        heroTitle.textContent = current.substring(0, charIndex--);

        if (charIndex < 0) {
            deleting = false;
            titleIndex++;

            if (titleIndex >= titles.length)
                titleIndex = 0;
        }
    }

    setTimeout(typeEffect, deleting ? 50 : 100);
}

typeEffect();


// ===============================
// Navbar Background
// ===============================

const nav = document.querySelector("nav");

window.addEventListener("scroll", () => {

    if (window.scrollY > 40) {

        nav.style.background = "rgba(5,8,22,.95)";
        nav.style.boxShadow = "0 5px 25px rgba(0,0,0,.4)";

    } else {

        nav.style.background = "rgba(5,8,22,.7)";
        nav.style.boxShadow = "none";
    }

});


// ===============================
// Active Navigation
// ===============================

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll("nav ul li a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 150;

        if (pageYOffset >= sectionTop)
            current = section.getAttribute("id");

    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        if (link.getAttribute("href") === "#" + current) {
            link.classList.add("active");
        }

    });

});


// ===============================
// Fade Animation on Scroll
// ===============================

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
        }

    });

}, {
    threshold: .2
});

document.querySelectorAll(".card,.item,.about-card,.skills span").forEach(el => {

    el.style.opacity = "0";
    el.style.transform = "translateY(40px)";
    el.style.transition = ".8s";

    observer.observe(el);

});


// ===============================
// Skill Hover Animation
// ===============================

document.querySelectorAll(".skills span").forEach(skill => {

    skill.addEventListener("mouseenter", () => {

        skill.style.transform = "translateY(-8px) scale(1.1)";
        skill.style.boxShadow = "0 0 20px #00d4ff";

    });

    skill.addEventListener("mouseleave", () => {

        skill.style.transform = "";
        skill.style.boxShadow = "";

    });

});


// ===============================
// Project Card Tilt
// ===============================

document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("mousemove", e => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const rotateY = (x - rect.width / 2) / 20;
        const rotateX = -(y - rect.height / 2) / 20;

        card.style.transform =
            `perspective(1000px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            scale(1.03)`;

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform =
            "perspective(1000px) rotateX(0) rotateY(0)";

    });

});


// ===============================
// Counter Animation
// ===============================

const counters = document.querySelectorAll(".counter");

const counterObserver = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if (!entry.isIntersecting)
            return;

        const counter = entry.target;

        const target = +counter.dataset.target;

        let value = 0;

        const speed = target / 80;

        function update() {

            if (value < target) {

                value += speed;

                counter.innerText = Math.ceil(value);

                requestAnimationFrame(update);

            } else {

                counter.innerText = target;
            }

        }

        update();

    });

});

counters.forEach(counter => {

    counterObserver.observe(counter);

});


// ===============================
// Scroll To Top Button
// ===============================

const topBtn = document.createElement("button");

topBtn.innerHTML = "↑";

document.body.appendChild(topBtn);

topBtn.style.position = "fixed";
topBtn.style.right = "25px";
topBtn.style.bottom = "25px";
topBtn.style.width = "50px";
topBtn.style.height = "50px";
topBtn.style.border = "none";
topBtn.style.borderRadius = "50%";
topBtn.style.background = "#00d4ff";
topBtn.style.color = "#000";
topBtn.style.cursor = "pointer";
topBtn.style.fontSize = "22px";
topBtn.style.display = "none";
topBtn.style.zIndex = "9999";
topBtn.style.transition = ".4s";

window.addEventListener("scroll", () => {

    if (window.scrollY > 300)
        topBtn.style.display = "block";
    else
        topBtn.style.display = "none";

});

topBtn.onclick = () => {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

};


// ===============================
// Smooth Fade On Load
// ===============================

window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});