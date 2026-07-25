// Toggle FAQ Answers
function toggleFaq(element) {
    const isActive = element.classList.contains('active');
    
    // Close all other FAQs
    const allFaqs = document.querySelectorAll('.faq-item');
    allFaqs.forEach(item => {
        item.classList.remove('active');
    });

    // Toggle current FAQ
    if (!isActive) {
        element.classList.add('active');
    }
}

// Simple email validation handler
function handleGetStarted() {
    const emailInput = document.getElementById('emailInput').value.trim();

    if (emailInput === '') {
        alert('Please enter your email address to get started.');
    } else if (!emailInput.includes('@') || !emailInput.includes('.')) {
        alert('Please enter a valid email address.');
    } else {
        alert('Welcome! Email registered successfully: ' + emailInput);
    }
}