var app = app || {};

$(document).ready(function(){
    console.log("ready!");
});

app.init = function() {
    app.data.fetchPlanetData(app.data.commonData.apiURL);
    app.logic.checkButton();
}

app.init()