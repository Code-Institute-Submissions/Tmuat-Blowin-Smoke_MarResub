// Code from https://www.sitepoint.com/basic-jquery-form-validation-tutorial/
$(function () {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='profile']").validate({
        // Specify validation rules
        rules: {
            // The key name on the left side is the name attribute
            // of an input field. Validation rules are defined
            // on the right side
            firstname: "required",
            lastname: "required",
            username: {
                required: true,
                minlength: 5,
                maxlength: 15
            },
            email: {
                required: true,
                // Specify that email should be validated
                // by the built-in "email" rule
                email: true
            },
        },
        // Specify validation error messages
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            username: {
                minlength: "Username > 5 characters long",
                maxlength: "Username < 15 characters long",
            },
            email: "Email not valid",
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function (form) {
            form.submit();
        }
    });
});
