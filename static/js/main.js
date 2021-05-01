// const btns = document.querySelectorAll(".head__link")
//
// for (btn of btns) {
//     btn.addEventListener('click', (e) => {
//         const attr = e.toElement.attributes.href.nodeValue
//         const destionation = attr.offset().top;
//     })
// }


$(".head__link").click(function () {
    elementClick = $(this).attr("href");
    destination = $(elementClick).offset().top;
    $("body,html").animate({scrollTop: destination }, 800);
});