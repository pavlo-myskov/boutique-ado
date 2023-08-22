// Change color of country select

let countrySelected = $('#id_default_country').val();
// if country is not selected (first option has empty value), color is grey
if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
// if country is selected, color is black
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});