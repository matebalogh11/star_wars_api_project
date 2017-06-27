app = app || {};

app.logic = {
    checkButton: function() {
        $(".btn").click(function() {
        var name = $(this).data("name");
        $("#p, #n").prop("disabled", false);
        if(name === "next") {
            var direction = app.data.commonData.response.next;
        } else {
            var direction = app.data.commonData.response.previous;
        }

        if(direction != null) {
            app.data.commonData.apiURL = direction;
            $("#header, .trInBody").remove();
            app.data.fetchPlanetData(app.data.commonData.apiURL);
        } else {
            $(this).prop("disabled", true);
        }
        });
    }
}



