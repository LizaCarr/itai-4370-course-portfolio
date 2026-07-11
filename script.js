const menuButton = document.querySelector('.menu-button');
const siteMenu = document.querySelector('.site-menu');

if (menuButton && siteMenu) {
  menuButton.addEventListener('click', () => {
    const isOpen = siteMenu.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(isOpen));
  });

  siteMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      siteMenu.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
    });
  });
}

const filterButtons = document.querySelectorAll('.filter-button');
const workCards = document.querySelectorAll('.work-card');

filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const selected = button.dataset.filter;
    filterButtons.forEach((item) => item.classList.remove('active'));
    button.classList.add('active');

    workCards.forEach((card) => {
      const categories = card.dataset.category.split(' ');
      card.hidden = selected !== 'all' && !categories.includes(selected);
    });
  });
});
