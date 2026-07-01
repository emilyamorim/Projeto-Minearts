const hamburger = document.getElementById("hamburger");
const navbar = document.getElementById("navbar");

// Abre e fecha o menu ao clicar no botão do hambúrguer
if (hamburger && navbar) {
  hamburger.addEventListener("click", () => {
    const aberto = navbar.classList.toggle("navbar-aberta");
    hamburger.classList.toggle("hamburger-ativo", aberto);
    hamburger.setAttribute("aria-expanded", aberto);
  });

  // Fecha o menu ao clicar em qualquer link
  navbar.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navbar.classList.remove("navbar-aberta");
      hamburger.classList.remove("hamburger-ativo");
      hamburger.setAttribute("aria-expanded", false);
    });
  });
}
