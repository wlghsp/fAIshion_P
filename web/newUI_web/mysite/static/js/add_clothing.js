'use strict';

window.addEventListener('load', () => {
  const addClothingSection = document.querySelector('.add-clothing-upload-title');
  addClothingSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
});

// jquery event -->> javascript로 변경하는거 꼭 해보기.
$(document).ready(function () {
  const fileTarget = $('.file-box .cloth-input-file-hidden');
  let filename = '';
  fileTarget.on('change', function () {
    // 값이 변경되면
    if (window.FileReader) {
      // modern browser
      filename = $(this)[0].files[0].name;
    } else {
      // old IE
      filename = $(this).val().split('/').pop().split('\\').pop(); // 파일명만 추출
    } // 추출한 파일명 삽입
    $(this).siblings('.cloth-upload-name').val(filename);
  });
});
