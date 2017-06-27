var app = app || {};

$(document).ready(function(){
    console.log("ready!");
    // $('#myModal').modal('toggle');
});

app.init = function() {
    app.data.createPlanetHeader();
    app.data.fetchPlanetData(app.data.commonData.apiURL);
    app.logic.checkButton();
    app.logic.modalButt();
    app.logic.closeModal();
}

app.init()