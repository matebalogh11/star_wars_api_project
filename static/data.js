var app = app || {};


app.data = {
    fetchPlanetData: function(apiURL) {
        $.ajax({
            dataType: "json",
            url: apiURL,
            success: function(response) {
                app.data.commonData.response = response;
                app.data.createPlanetTable(response);
            }
        });
    },
    addThousandSeparator : function(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    createPlanetTable: function(response) {
        var header = ["Name", "Diameter", "Climate", "Terrain", "Surface Water Percentage", "Population"];
        $("thead").append(`<tr  id="header"></tr>`);
        for(let h = 0; h < header.length; h++) {
            $("#header").append(`<th>${header[h]}</th>`);
        }

        for(var j = 0; j < response.results.length; j++) {
            var strNum = j.toString();
            var planetAttr = [response.results[j].name, response.results[j].diameter/1000, response.results[j].climate,
                                response.results[j].terrain, response.results[j].surface_water, response.results[j].population]
            $("tbody").append(`<tr class="trInBody"  id=${strNum}></tr>`);

            for(var i = 0; i < planetAttr.length; i++) {
                if(i === 4) {
                    if(response.results[j].surface_water == "unknown") {
                        $("#" + strNum).append(`<td>${response.results[j].surface_water}</td>`);
                    } else {
                        $("#" + strNum).append(`<td>${response.results[j].surface_water + "%"}</td>`);
                    }
                } else if(i === 5) {
                    var thousandS = app.data.addThousandSeparator(planetAttr[i]);
                    if(planetAttr[i] === "unknown") {
                        $("#" + strNum).append(`<td>${thousandS}</td>`);
                    } else {
                        $("#" + strNum).append(`<td>${thousandS} people</td>`);
                    }
                } else {
                    $("#" + strNum).append(`<td>${planetAttr[i]}</td>`);
                }
            }
        }
    },
    commonData: {
        response: null,
        apiURL: "http://swapi.co/api/planets"
    }
}
