document.addEventListener('DOMContentLoaded', function() {
    const categoryListItems = document.querySelectorAll('.category-list li');
    const subcategoryList = document.getElementById('subcategory-list');

    categoryListItems.forEach(item => {
        item.addEventListener('mouseover', function() {
            const subcategories = JSON.parse(this.getAttribute('data-subcategories'));
            subcategoryList.innerHTML = ''; 
            subcategories.forEach(subcategory => {

                const link = document.createElement('a');
                link.href = '#'; 
                link.textContent = subcategory;
                link.style.textDecoration = 'none';
                link.style.width = 'auto';
                link.style.fontSize = '30px';
                link.style.color = 'black';
                link.style.transition = 'color 0.3s ease-in-out';


                const listItem = document.createElement('li');
                listItem.appendChild(link); 
                subcategoryList.appendChild(listItem); 
            });
        });
    });
});