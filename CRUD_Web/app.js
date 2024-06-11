document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('userForm');
    const nameInput = document.getElementById('name');
    const surnameInput = document.getElementById('surname');
    const usersDiv = document.getElementById('users');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const name = nameInput.value;
        const surname = surnameInput.value;
        createUser(name, surname);
    });

    getUsers();

    function getUsers() {
        fetch('/api/users')
            .then(response => response.json())
            .then(users => {
                usersDiv.innerHTML = '';
                users.forEach(user => {
                    const userDiv = document.createElement('div');
                    userDiv.textContent = `${user.name} ${user.surname}`;
                    usersDiv.appendChild(userDiv);
                });
            });
    }

    function createUser(name, surname) {
        fetch('/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, surname })
        })
        .then(response => {
            if (response.ok) {
                nameInput.value = '';
                surnameInput.value = '';
                getUsers();
            } else {
                console.error('Failed to create user');
            }
        });
    }
});
