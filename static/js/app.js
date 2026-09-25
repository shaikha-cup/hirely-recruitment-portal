document.addEventListener("DOMContentLoaded", () => {

    /* =====================================================
       MOBILE MENU
       ===================================================== */

    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const mobileMenu = document.getElementById("mobileMenu");

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener("click", () => {
            mobileMenu.classList.toggle("active");

            const icon = mobileMenuBtn.querySelector("i");

            if (mobileMenu.classList.contains("active")) {
                icon.classList.remove("bi-list");
                icon.classList.add("bi-x-lg");
            } else {
                icon.classList.remove("bi-x-lg");
                icon.classList.add("bi-list");
            }
        });

        mobileMenu.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                mobileMenu.classList.remove("active");

                const icon = mobileMenuBtn.querySelector("i");
                icon.classList.remove("bi-x-lg");
                icon.classList.add("bi-list");
            });
        });
    }


    /* =====================================================
       SCROLL REVEAL
       ===================================================== */

    const revealElements = document.querySelectorAll(".reveal");

    if (revealElements.length) {
        const revealObserver = new IntersectionObserver(
            (entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            {
                threshold: 0.12
            }
        );

        revealElements.forEach(element => {
            revealObserver.observe(element);
        });
    }


    /* =====================================================
       TOAST NOTIFICATION
       ===================================================== */

    window.showToast = function(message, type = "success") {
        const container = document.getElementById("toastContainer");

        if (!container) return;

        const toast = document.createElement("div");
        toast.className = "toast";

        let icon = "bi-check-circle-fill";

        if (type === "error") {
            icon = "bi-exclamation-circle-fill";
        }

        if (type === "info") {
            icon = "bi-info-circle-fill";
        }

        toast.innerHTML = `
            <i class="bi ${icon}"></i>
            <div>${message}</div>
        `;

        container.appendChild(toast);

        setTimeout(() => {
            toast.classList.add("hide");

            setTimeout(() => {
                toast.remove();
            }, 300);

        }, 3500);
    };


    /* =====================================================
       BUTTON MICRO-INTERACTION
       ===================================================== */

    document.querySelectorAll(".btn").forEach(button => {

        button.addEventListener("click", function() {

            this.style.transform = "scale(0.97)";

            setTimeout(() => {
                this.style.transform = "";
            }, 120);

        });

    });


    /* =====================================================
       ACTIVE NAV LINK
       ===================================================== */

    const currentPath = window.location.pathname;

    document.querySelectorAll(".nav-link").forEach(link => {

        const href = link.getAttribute("href");

        if (href && href !== "/" && currentPath.includes(href)) {
            link.classList.add("active");
        }

    });


    /* =====================================================
       SMOOTH INTERNAL LINKS
       ===================================================== */

    document.querySelectorAll('a[href^="#"]').forEach(link => {

        link.addEventListener("click", event => {

            const targetId = link.getAttribute("href");

            if (!targetId || targetId === "#") return;

            const target = document.querySelector(targetId);

            if (target) {
                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }

        });

    });

});