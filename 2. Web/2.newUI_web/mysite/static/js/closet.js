'use strict';

window.addEventListener('load', () => {
  console.log('load');
  const closetSection = document.querySelector('.add-clothing-box-title');
  closetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
});
