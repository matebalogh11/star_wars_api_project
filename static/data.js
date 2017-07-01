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
        return false
    },
    addThousandSeparator : function(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    createPlanetTable: function(response) {
        for(var j = 0; j < response.results.length; j++) {
            var strNum = j.toString();
            var diameterT = app.data.addThousandSeparator(response.results[j].diameter + " km");
            var thousandS = app.data.addThousandSeparator(response.results[j].population);

            var planetAttr = [response.results[j].name, diameterT, response.results[j].climate,
                              response.results[j].terrain, response.results[j].surface_water, thousandS,
                              response.results[j].residents.length, "Vote"]
            $(".planetBody").append(`<tr class="trInBody"  id=${strNum}></tr>`);

            for(var i = 0; i < planetAttr.length; i++) {
                if(i === 4) {
                    if(response.results[j].surface_water == "unknown") {
                        $("#" + strNum).append(`<td>${response.results[j].surface_water}</td>`);
                    } else {
                        $("#" + strNum).append(`<td>${response.results[j].surface_water} %</td>`);
                    }
                } else if(i === 5) {
                    if(planetAttr[i] === "unknown") {
                        $("#" + strNum).append(`<td>${thousandS}</td>`);
                    } else {
                        $("#" + strNum).append(`<td>${thousandS} people</td>`);
                    }
                } else if(i === 6) {
                    if(planetAttr[i] !== 0) {
                        $("#" + strNum).append(`<td><button class="activator btn" data-planet=${j} data-toggle="modal" data-target="#myModal">${planetAttr[i]} resident(s)</button></td>`); 
                    } else {
                        $("#" + strNum).append(`<td>No known<br>residents</td>`);
                    }    
                } else if(i === 7) {
                    var check = $(".loggedIn").text()
                    if(check) {
                        var idArray = response.results[j].url.split("/");
                        var id = Number(idArray[idArray.length - 2]);
                        $("#" + strNum).append(`<td><button class="voteBtn btn" data-planet=${planetAttr[0]} data-id=${id}>${planetAttr[i]}</button></td>`);
                    }
                } else {
                    $("#" + strNum).append(`<td>${planetAttr[i]}</td>`);
                }
            }
        }
    },
    createPlanetHeader: function() {
        var header = ["Name", "Diameter", "Climate", "Terrain", "Surface Water Percentage", "Population", "Residents"];
        $(".planetHead").append(`<tr  id="header"></tr>`);
        for(let h = 0; h < header.length; h++) {
            $("#header").append(`<th>${header[h]}</th>`);
        }
    },
    commonData: {
        response: null,
        apiURL: "https://swapi.co/api/planets/"
    }
}
