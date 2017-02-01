window.onload = function () {
    
    var contactForm = document.getElementById('contactForm'); 
    $('#popupBtn').on('click', function () {

        $('input.contact-input[name="firstName"]').val('');
        $('input.contact-input[name="lastName"]').val('');
        $('input.contact-input[name="email"]').val('');
        $('input.contact-input[name="company"]').val('');
        $('input.contact-input[name="phone"]').val('');
        $('textarea[name="comment"]').val(''); 

        $('.popupBlock').fadeOut(500); 

    })

    if (contactForm) {

        contactForm.onsubmit = function (e) {
            e.preventDefault();

            var data = {
                first_name: document.querySelector('input.contact-input[name="firstName"]').value,
                last_name: document.querySelector('input.contact-input[name="lastName"]').value,
                email: document.querySelector('input.contact-input[name="email"]').value,
                company: document.querySelector('input.contact-input[name="company"]').value,
                phone: document.querySelector('input.contact-input[name="phone"]').value,
                comment: document.querySelector('textarea[name="comment"]').value
            }

            var json_data = JSON.stringify(data);

            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/send_form/');
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(json_data);

            xhr.onload = function () {
                $('.popupBlock').fadeIn(500); 
            }
        }
    } 
}