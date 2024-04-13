document.addEventListener('DOMContentLoaded', function() {
    const categoryListItems = document.querySelectorAll('.category-list li');
    const subcategoryList = document.getElementById('subcategory-list');

    categoryListItems.forEach(item => {
        item.addEventListener('mouseover', function() {
            const subcategories = JSON.parse(this.getAttribute('data-subcategories'));
            subcategoryList.innerHTML = ''; // Очищаем список подкатегорий перед добавлением новых
            subcategories.forEach(subcategory => {
                // Создаем элемент <a> вместо <li>
                const link = document.createElement('a');
                link.href = '#'; // Устанавливаем href, если это необходимо
                link.textContent = subcategory;
                link.style.textDecoration = 'none'; // Устанавливаем стили, как указано в CSS
                link.style.width = 'auto';
                link.style.fontSize = '30px';
                link.style.color = 'black';
                link.style.transition = 'color 0.3s ease-in-out';

                // Создаем элемент <li> для обертывания ссылки
                const listItem = document.createElement('li');
                listItem.appendChild(link); // Добавляем ссылку в элемент <li>
                subcategoryList.appendChild(listItem); // Добавляем элемент <li> в список подкатегорий
            });
        });
    });
});