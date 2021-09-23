const $ = window.$;
$('#toggle_header').click(function () {
  $('header').toggleClass('green').toggleClass('red');
});
