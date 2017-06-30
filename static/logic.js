app = app || {};

app.logic = {
    checkButton: function() {
        $("#p, #n").click(function() {
        var name = $(this).data("name");
        $("#p, #n").prop("disabled", false);
        if(name === "next") {
            var direction = app.data.commonData.response.next;
        } else {
            var direction = app.data.commonData.response.previous;
        }

        if(direction != null) {
            app.data.commonData.apiURL = direction;
            $(".trInBody").remove();
            app.data.fetchPlanetData(app.data.commonData.apiURL);
        } else {
            $(this).prop("disabled", true);
        }
        });
    },
    modalButt: function() {
        $(".planetBody").on("click", ".activator", function() {
            var index = $(this).data("planet");
            var residents = app.data.commonData.response.results[index].residents;
            var header = ["Name", "Height", "Mass", "Hair Color", "Skin Color", "Eye Color", "Birth Year", "Gender"];
            $(".modal-title").html("Residents of " + app.data.commonData.response.results[index].name)
            $("#modalHead").append(`<tr id="modalHeader"></tr>`);
            for(let j = 0; j < header.length; j++) {
                $("#modalHeader").append(`<th>${header[j]}</th>`)
            }
            for(let i = 0; i < residents.length; i++) {
                $.ajax({
                    dataType: "json",
                    url: residents[i],
                    success: function(response) {
                        var attr = [response.name, response.height, response.mass, response.skin_color, response.hair_color, response.eye_color,
                                    response.birth_year,response.gender];
                        var mID = i.toString();
                        $("#modalBody").append(`<tr class="modalRow" id=${mID}></tr>`);
                        for(let h = 0; h < attr.length; h++) {
                            $("#" + mID).append(`<td>${attr[h]}</td>`);
                        }
                    }
                });
            }
        });
    },
    closeModal: function() {
        $("#modalCloser, #modalCloser2").click(function() {
            $("#modalHeader, .modalRow, .modalHead, .modalVote").remove();
        });
    },
    planetVotes: function() {
        $(".planetBody").on("click", ".voteBtn", function() {
            var obj = {
                planet: $(this).data("planet"),
                id: $(this).data("id")
            }
            $.ajax({
                url: "http://127.0.0.1:5000/votes",
                type: "post",
                dataType: "json",
                contentType: "application/json",
                data: myJSON,
                success: function(response) {
                    $.gritter.add({
                        title: "You voted successfully on " + obj.planet
                    });
                }
            });
        });
    },
    showVoteStat: function() {
        $(".voteStat").click(function() {
            $.ajax({
                url:"http://127.0.0.1:5000/votestat",
                dataType: "json",
                contentType: "application/json",
                success: function(response) {
                    console.log(response);
                    $(".modal-title").html("Planet voting statistics");
                    $("#modalHead").append(`<tr class="modalHead"></tr>`);
                    for(let i = 0; i < response.length; i++) {
                        $(".modalHead").append(`<th>${response[i][0]}</th>`);
                    }
                    $("#modalBody").append(`<tr class="modalVote"></tr>`);
                    for(let i = 0; i < response.length; i++) {
                        $(".modalVote").append(`<td>${response[i][1]}</td>`);
                    }
                }
            })
        });
    }
}



