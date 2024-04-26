document.querySelectorAll('.category-li').forEach(elem => {
    elem.addEventListener('mouseover', function (event) {
        toggleCategoryVisibility(event.target.id);
    })
})

document.getElementById("open-category-popup-btn").addEventListener("click",function(){
    document.getElementById("category-popup-id").classList.toggle("open")
}) 

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("category-popup-id").classList.remove("open")
    }
});

document.querySelector("#category-popup-id .category-box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});


document.getElementById("category-popup-id").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});


function toggleCategoryVisibility(categoryId) {
    let blocks = Array.from(document.getElementsByClassName("subcategory-elem"));
    blocks.forEach(function (category) {
        if (!category.classList.contains(categoryId)){
            console.log(category);
            category.classList.remove('open');
        }
    });
    Array.from(document.getElementsByClassName(categoryId)).forEach(function(category) {
        category.classList.add('open');
        console.log(category);
    });
}



// document.getElementById('milk-category').addEventListener('mouseover', function() {
//     toggleCategoryVisibility('milk');
// });
//
// document.getElementById('meat-category').addEventListener('mouseover', function() {
//     toggleCategoryVisibility('meat');
// });
//
// document.getElementById('sweets-category').addEventListener('mouseover', function() {
//     toggleCategoryVisibility('sweets');
// });
