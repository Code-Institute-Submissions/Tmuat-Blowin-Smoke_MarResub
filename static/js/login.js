// Code from https://www.sitepoint.com/basic-jquery-form-validation-tutorial/
$(function () {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='login']").validate({
        // Specify validation rules
        rules: {
            // The key name on the left side is the name attribute
            // of an input field. Validation rules are defined
            // on the right side
            username: {
                required: true,
            },
            password: {
                required: true,
            },
        },
        // Specify validation error messages
        messages: {
            username: {
                required: "Please provide a username",
            },
            password: {
                required: "Please provide a password",
            },
        },
        // Make sure the form is submitted to the destination defined
        // in the "action" attribute of the form when valid
        submitHandler: function (form) {
            form.submit();
        }
    });
});
