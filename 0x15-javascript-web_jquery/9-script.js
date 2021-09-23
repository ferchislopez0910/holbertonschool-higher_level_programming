const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.ajax({
  type: 'GET',
  url: url,
  success: function (response) {
    $('#hello').append(response.hello);
  }
});
