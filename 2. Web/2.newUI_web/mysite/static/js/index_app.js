'use strict';

// // 옷장 이미지 slide 구현
// const slideList = document.querySelector('.slide-list');
// const slideContents = document.querySelectorAll('.slide-content');
// const slideButtonNext = document.querySelector('.slide-button-next');
// const slideButtonPrev = document.querySelector('.slide-button-prev');
// const slideLength = slideContents.length;
// const slideSpeed = 300;
// const startNum = 0;
// let slideWidth = 0;
// setInterval(() => {
//   if (screen.width >= 768) {
//     slideWidth = 330;
//   } else {
//     slideWidth = 220;
//   }
// }, 100);
//
// // slideList.style.width = slideWidth * slideLength + 'px';
//
// let firstChild = slideList.firstElementChild;
// let lastChild = slideList.lastElementChild;
// let clonedFirst = firstChild.cloneNode(true);
// let clonedLast = lastChild.cloneNode(true);
//
// slideList.appendChild(clonedFirst);
// slideList.insertBefore(clonedLast, slideList.firstElementChild);
//
// slideList.style.transform =
//   'translate3d(-' + slideWidth * (startNum + 1) + 'px,0px,0px)';
//
// let currentIndex = startNum;
// let currentSlide = slideContents[currentIndex];
//
// slideButtonNext.addEventListener('click', () => {
//   if (currentIndex <= slideLength - 1) {
//     slideList.style.transition = slideSpeed + 'ms';
//     slideList.style.transform =
//       'translate3d(-' + slideWidth * (currentIndex + 2) + 'px, 0px, 0px)';
//   }
//   if (currentIndex === slideLength - 1) {
//     setTimeout(() => {
//       slideList.style.transition = '0ms';
//       slideList.style.transform =
//         'translate3d(-' + slideWidth + 'px, 0px, 0px)';
//     }, slideSpeed);
//     currentIndex = -1;
//   }
//   currentSlide = ++currentIndex;
// });
//
// slideButtonPrev.addEventListener('click', () => {
//   if (currentIndex >= 0) {
//     slideList.style.transition = slideSpeed + 'ms';
//     slideList.style.transform =
//       'translate3d(-' + slideWidth * currentIndex + 'px, 0px, 0px)';
//   }
//   if (currentIndex === 0) {
//     setTimeout(() => {
//       slideList.style.transition = '0ms';
//       slideList.style.transform =
//         'translate3d(-' + slideWidth * slideLength + 'px,0px,0px)';
//     }, slideSpeed);
//     currentIndex = slideLength;
//   }
//   currentSlide = --currentIndex;
// });

// button click시 해당 위치로 scroll
const headerButton = document.querySelector('.header-button');

// headerButton.addEventListener('click', (event) => {
//   event.preventDefault();
//   document.querySelector('.add-clothing-upload-title').scrollIntoView(true);
// });

const addClothingBoxButton = document.querySelector('.add-clothing-box-button');

// addClothingBoxButton.addEventListener('click', (event) => {
//   event.preventDefault();
//   document.querySelector('.recommand-section-title').scrollIntoView(true);
// });

// modal click event function
function modalControl(button, modal) {
  if (button.active) {
    modal.classList.remove('active');
  } else {
    modal.classList.add('active');
  }
  button.active = !button.active;
}

// sign-in, sign-up click event
const signUpButton = document.querySelector('.signUp-button');
const signUpAside = document.querySelector('.sign-up-aside');
signUpButton.addEventListener('click', () => {
  modalControl(signUpButton, signUpAside);
});
signUpButton.active = false;

const signInButton = document.querySelector('.signIn-button');
const signInAside = document.querySelector('.sign-in-aside');
signInButton.addEventListener('click', () => {
  modalControl(signInButton, signInAside);
});

signInButton.active = false;

// exitbutton click event
const signUpExitButton = document.querySelector('.sign-up-exit-button');
const signInExitButton = document.querySelector('.sign-in-exit-button');

signUpExitButton.addEventListener('click', () => {
  modalControl(signUpExitButton, signUpAside);
});

signUpExitButton.active = false;

signInExitButton.addEventListener('click', () => {
  modalControl(signInExitButton, signInAside);
});

signInExitButton.active = false;
