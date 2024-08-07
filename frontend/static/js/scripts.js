function showLogin(type) {
    const loginContainer = document.getElementById('login-container');
    const loginForm = document.getElementById('login-form');
    const loginTitle = document.getElementById('login-title');
    const loginBtn = document.getElementById('login-btn');
    const toggleText = document.getElementById('toggle-text');

    loginContainer.style.display = 'block';
    if (type === 'resident') {
        loginTitle.textContent = 'Resident Login';
        loginForm.action = '/residents/login/';
        loginBtn.textContent = 'Login as Resident';
        toggleText.textContent = 'Don\'t have an account? Sign up here';
        toggleText.onclick = () => showSignup('resident');
    } else if (type === 'security') {
        loginTitle.textContent = 'Security Login';
        loginForm.action = '/security/login/';
        loginBtn.textContent = 'Login as Security';
        toggleText.textContent = 'Don\'t have an account? Sign up here';
        toggleText.onclick = () => showSignup('security');
    }
}

function showSignup(type) {
    const loginTitle = document.getElementById('login-title');
    const loginForm = document.getElementById('login-form');
    const loginBtn = document.getElementById('login-btn');
    const toggleText = document.getElementById('toggle-text');

    if (type === 'resident') {
        loginTitle.textContent = 'Resident Signup';
        loginForm.action = '/residents/signup/';
        loginBtn.textContent = 'Signup as Resident';
        toggleText.textContent = 'Already have an account? Login here';
        toggleText.onclick = () => showLogin('resident');
    } else if (type === 'security') {
        loginTitle.textContent = 'Security Signup';
        loginForm.action = '/security/signup/';
        loginBtn.textContent = 'Signup as Security';
        toggleText.textContent = 'Already have an account? Login here';
        toggleText.onclick = () => showLogin('security');
    }
}
