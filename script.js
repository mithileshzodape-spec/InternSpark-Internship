// Simple event handler for contact form
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for reaching out, Mithilesh will get back to you soon!');
            contactForm.reset();
        });
    }
});