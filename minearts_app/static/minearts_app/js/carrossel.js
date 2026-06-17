new Swiper('.cards', {
  loop: true,
  spaceBetween: 30,
  speed: 1000,

  // Autoplay
   autoplay: {
    delay: 1000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true
   },

  // Marcadores de paginção
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    dynamicBullets: true
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  // Responsividade breakpoints
  breakpoints: {
    0: {
        slidesPerView: 1
    },
    500: {
        slidesPerView: 2
    },
    1024: {
        slidesPerView: 4
    }
  }
});