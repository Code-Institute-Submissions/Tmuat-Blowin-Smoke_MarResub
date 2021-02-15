// Code taken and adapted from https://jsfiddle.net/jnwrc5ay/592/
$(document).ready(function () {
    $('.add-ing').on('click', add);
    $('.remove-ing').on('click', remove);

    function add() {
        var new_input_no = parseInt($('#total_ing_input').val()) + 1;
        var new_input = '<div id="ingridients_div' + new_input_no + '" class="col-12 col-md-6 mb-2"><input id="ingridients' + new_input_no + '" name="ingridients' + new_input_no + '" type="text" placeholder="Ingridient (E.g. Beef - 500g)" class="form-control custom-input valid-border" autocomplete="nope"></div>';

        $('#new_ing_input').append(new_input);

        $('#total_ing_input').val(new_input_no);
    }

    function remove() {
        var last_input_no = $('#total_ing_input').val();

        if (last_input_no > 2) {
            $('#ingridients_div' + last_input_no).remove();
            $('#total_ing_input').val(last_input_no - 1);
        }
    }
    
    $('.add-steps').on('click', addSteps);
    $('.remove-steps').on('click', removeSteps);

    function addSteps() {
        var new_input_no_steps = parseInt($('#total_steps_input').val()) + 1;
        var new_input_steps = '<div id="step_div' + new_input_no_steps + '" class="col-12 col-md-6 mb-2"><textarea id="steps' + new_input_no_steps + '" name="steps' + new_input_no_steps + '" type="text" placeholder="Cooking Steps" class="form-control custom-input valid-border" autocomplete="nope" required></textarea></div>';

        $('#new_steps_input').append(new_input_steps);

        $('#total_steps_input').val(new_input_no_steps);
    }

    function removeSteps() {
        var last_input_no_steps = $('#total_steps_input').val();

        if (last_input_no_steps > 2) {
            $('#step_div' + last_input_no_steps).remove();
            $('#total_steps_input').val(last_input_no_steps - 1);
        }
    }
});
