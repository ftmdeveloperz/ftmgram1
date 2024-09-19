// Form Validation for login and registration
document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('#login-form');
    const registerForm = document.querySelector('#register-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            const email = document.querySelector('#login-email').value;
            const password = document.querySelector('#login-password').value;
            
            if (!email || !password) {
                e.preventDefault();
                alert('Please fill out all fields.');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', function (e) {
            const email = document.querySelector('#register-email').value;
            const password = document.querySelector('#register-password').value;
            const confirmPassword = document.querySelector('#confirm-password').value;
            
            if (!email || !password || !confirmPassword) {
                e.preventDefault();
                alert('Please fill out all fields.');
            } else if (password !== confirmPassword) {
                e.preventDefault();
                alert('Passwords do not match.');
            }
        });
    }
});

// Dynamic Content Loading Example
function loadPosts() {
    fetch('/posts')
        .then(response => response.json())
        .then(data => {
            const postsContainer = document.querySelector('#posts-container');
            postsContainer.innerHTML = '';
            
            data.posts.forEach(post => {
                const postElement = document.createElement('div');
                postElement.className = 'post';
                postElement.innerHTML = `
                    <img src="${post.imageUrl}" alt="${post.title}">
                    <h3>${post.title}</h3>
                    <p>${post.description}</p>
                `;
                postsContainer.appendChild(postElement);
            });
        });
}

// Call the function to load posts on page load
document.addEventListener('DOMContentLoaded', function () {
    loadPosts();
});