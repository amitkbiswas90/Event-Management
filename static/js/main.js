
document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if(menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('indicators-carousel');
    if(carousel) {
        new Flowbite.Carousel(carousel, {
            interval: 3000 
        });
    }
});