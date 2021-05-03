const markItems = document.querySelectorAll('.mark__item'),
      addBtn = document.getElementById('addcomment'),
      commentSection = document.getElementById('comment')

for (let mark of markItems) {
    mark.addEventListener('click', e => {
        markItems.forEach( item => {
            item.classList.remove('active')
            item.removeAttribute('name')
        })
        e.target.classList.add('active')
        e.target.setAttribute('name', 'active')
    })
}

addBtn.addEventListener('click', () => {
    commentSection.setAttribute('style', 'display: block; margin-bottom: 60px')
    addBtn.setAttribute('style', 'display: none')
})

$(".head__link").click(function () {
    elementClick = $(this).attr("href");
    destination = $(elementClick).offset().top;
    $("body,html").animate({scrollTop: destination }, 800);
});

