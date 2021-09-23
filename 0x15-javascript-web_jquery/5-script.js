const $ = window.$;
$(document).ready(function () {
  $('li').click(function () {
    $('#add_item').append('<li>Item</li>');
  });
});
