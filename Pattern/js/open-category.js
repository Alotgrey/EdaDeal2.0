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
    const categories = {
        meat: document.querySelectorAll('.meat-category'),
        milk: document.querySelectorAll('.milk-category'),
        sweets: document.querySelectorAll('.sweets-category')
    };

    for (const categoryType in categories) {
        if (categoryType !== categoryId) {
            categories[categoryType].forEach(function(category) {
                category.classList.remove('open');
            });
        }
    }

    categories[categoryId].forEach(function(category) {
        category.classList.toggle('open');
    });
}
document.getElementById('milk-category').addEventListener('mouseover', function() {
    toggleCategoryVisibility('milk');
});

document.getElementById('meat-category').addEventListener('mouseover', function() {
    toggleCategoryVisibility('meat');
});

document.getElementById('sweets-category').addEventListener('mouseover', function() {
    toggleCategoryVisibility('sweets');
});