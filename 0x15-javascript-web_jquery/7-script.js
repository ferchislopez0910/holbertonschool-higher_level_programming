var url = "https://swapi-api.hbtn.io/api/people/10/?format=json";
$.ajax({
    type: "GET",
    url: url,
    success: function( response) {
        $("#character").append(response.name)
    }
});
