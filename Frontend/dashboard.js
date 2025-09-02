// Dashboard functionality
document.addEventListener('DOMContentLoaded', function() {
    initializeTheme();
    setupEventListeners();
});

function setupEventListeners() {
    // Navigation tabs
    const navTabs = document.querySelectorAll('.nav-tab');
    navTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            navTabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Add Income/Expense buttons
    const addIncomeBtn = document.querySelector('.btn-primary');
    const addExpenseBtn = document.querySelector('.btn-secondary');
    
    if (addIncomeBtn) {
        addIncomeBtn.addEventListener('click', function() {
            // TODO: Implement add income functionality
            console.log('Add Income clicked');
        });
    }
    
    if (addExpenseBtn) {
        addExpenseBtn.addEventListener('click', function() {
            // TODO: Implement add expense functionality
            console.log('Add Expense clicked');
        });
    }

    // View Subscriptions button
    const viewSubsBtn = document.querySelector('.subscriptions-card .btn-outline');
    if (viewSubsBtn) {
        viewSubsBtn.addEventListener('click', function() {
            // TODO: Implement view subscriptions functionality
            console.log('View Subscriptions clicked');
        });
    }

    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
}

function initializeTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}


// Utility functions for future Flask integration
function fetchDashboardData() {
    // TODO: Implement API calls to Flask backend
    return {
        balance: 4247.89,
        monthlyChange: 234.54,
        expenses: [],
        budget: [],
        subscriptions: [],
        analytics: []
    };
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-GB', {
        style: 'currency',
        currency: 'GBP'
    }).format(amount);
}

function updateBalanceCard(balance, change) {
    const balanceElement = document.querySelector('.balance-amount');
    const changeElement = document.querySelector('.balance-change');
    
    if (balanceElement) {
        balanceElement.textContent = formatCurrency(balance);
    }
    
    if (changeElement) {
        changeElement.textContent = `${change >= 0 ? '+' : ''}${formatCurrency(change)} this month`;
        changeElement.className = `balance-change ${change >= 0 ? 'positive' : 'negative'}`;
    }
}