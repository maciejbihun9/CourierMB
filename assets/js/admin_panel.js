


function run_algorithm(){
    $_admin_panel_price_for_tour = $('#admin_panel_price_for_tour');
    $_admin_panel_total_earnings = $('#admin_panel_total_earnings');
    // use ajax to run algorithm
    var url = '/courierMB/actions/run_computations';
    /*$.ajax({
        url: url,
        type: 'GET',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: true,
        success:function(data) {
            console.log("success: " + data.value);
            $_admin_panel_price_for_tour.text(data.value + " " + "€");
            $_admin_panel_total_earnings.text(data.total_earnings + " " + "€");

        },
        error: function(error){
            console.log("something went wrong with response algorithm result processing!");
            console.log("error: " + error);
        }
    });*/
    request("GET", url, null, set_panel_price_and_earnings);
    console.log("Run computations has been called")
}

//init database with random packages
function init_database(){
    var init_database_url = '/courierMB/actions/init_database/';
    request("GET", init_database_url);
}

function set_panel_price_and_earnings(data){
    $_admin_panel_price_for_tour.text(data.value + " " + "€");
    $_admin_panel_total_earnings.text(data.total_earnings + " " + "€");
}




